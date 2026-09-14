import asyncio
import json
import os
import hashlib
import secrets
import time
import aiofiles
import psutil
import re
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from urllib.parse import quote
from collections import deque, defaultdict
from pathlib import Path
import socket
import base64

from fastapi import FastAPI, Request, HTTPException, Depends, WebSocket, WebSocketDisconnect
from fastapi.responses import Response, HTMLResponse, JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import httpx
import logging

# ─── تنظیمات ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("Persepolis-Gateway")

IRAN_TZ = ZoneInfo("Asia/Tehran")

# ─── کانفیگ ──────────────────────────────────────────────────────────────────
CONFIG = {
    "port": int(os.environ.get("PORT", 8000)),
    "secret": os.environ.get("SECRET_KEY", secrets.token_urlsafe(32)),
    "host": os.environ.get("RAILWAY_PUBLIC_DOMAIN", os.environ.get("RENDER_EXTERNAL_URL", "localhost")),
}

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "P443"
DEFAULT_ADMIN_PASSWORD = "P443"  # رمز پیش‌فرض نصب — بعد از تغییر رمز، راهنمای آبی از صفحه لاگین حذف می‌شود
PANEL_VERSION = "v10.4"  # همگام با پنل کلادفلری

# ─── App ──────────────────────────────────────────────────────────────────────
app = FastAPI(title="🏛️ Persepolis Gateway v14", docs_url=None, redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── State ────────────────────────────────────────────────────────────────────
DATA_DIR = Path(os.environ.get("DATA_DIR", "/data"))
DATA_FILE = DATA_DIR / "persepolis_state.json"
SAVE_LOCK = asyncio.Lock()

# ─── In-Memory State ─────────────────────────────────────────────────────────
LINKS: dict = {}
LINKS_LOCK = asyncio.Lock()
SUBS: dict = {}
SUBS_LOCK = asyncio.Lock()
connections: dict = {}
stats = {
    "total_bytes": 0,
    "total_requests": 0,
    "total_errors": 0,
    "start_time": time.time(),
}
error_logs: deque = deque(maxlen=50)
activity_logs: deque = deque(maxlen=200)
hourly_traffic: dict = defaultdict(int)
hourly_traffic_history: dict = defaultdict(lambda: defaultdict(int))
device_connections: dict = {}
DEVICE_CONNECTIONS_LOCK = asyncio.Lock()
http_client: httpx.AsyncClient | None = None
_tg_sess: dict = {}  # جلسات گفتگوی ربات تلگرام

# ─── Auth ──────────────────────────────────────────────────────────────────────
SESSION_COOKIE = "persepolis_session"
SESSION_TTL = 60 * 60 * 24 * 7
SESSIONS: dict = {}
SESSIONS_LOCK = asyncio.Lock()

# ─── Settings ──────────────────────────────────────────────────────────────────
SETTINGS: dict = {
    "rgb_mode": False,
    "default_protocol": "vless-ws",
    "language": "fa",
    "theme": "dark",
}

# ─── پروتکل‌های پشتیبانی شده ──────────────────────────────────────────────────
PROTOCOLS = {
    "vless-ws": {"name": "VLESS-WS", "icon": "🚀", "type": "ws", "alpn": "h2,http/1.1"},
    "vless-grpc": {"name": "VLESS-gRPC", "icon": "⚡", "type": "grpc", "alpn": "h2"},
    "vless-xhttp": {"name": "VLESS-XHTTP", "icon": "🛡️", "type": "xhttp", "alpn": "h2,http/1.1"},
    "vless-http2": {"name": "VLESS-HTTP/2", "icon": "📶", "type": "tcp", "alpn": "h2"},
    "trojan-ws": {"name": "Trojan-WS", "icon": "🔒", "type": "ws", "alpn": "h2,http/1.1"},
    "shadowsocks": {"name": "Shadowsocks", "icon": "🌊", "type": "tcp", "alpn": ""},
}

DEFAULT_PROTOCOL = "vless-ws"
DEFAULT_PORT = 443

# ─── HTTP نسخه‌ها ────────────────────────────────────────────────────────────
HTTP_VERSIONS = {
    "h1": {"name": "HTTP/1.1", "alpn": "http/1.1"},
    "h2": {"name": "HTTP/2", "alpn": "h2"},
    "h3": {"name": "HTTP/3 (QUIC)", "alpn": "h3"},
    "auto": {"name": "Auto", "alpn": "h2,http/1.1"},
}

# ─── انگشت‌نگاری ──────────────────────────────────────────────────────────────
FINGERPRINTS = {
    "chrome": "🌐 Chrome",
    "firefox": "🦊 Firefox",
    "safari": "🧭 Safari",
    "edge": "🌊 Edge",
    "ios": "📱 iOS",
    "android": "🤖 Android",
    "safari_ios": "🍏 Safari iOS",
    "random": "🎲 Random",
    "none": "🚫 None"
}

# ─── Functions ─────────────────────────────────────────────────────────────────

def now_ir() -> datetime:
    return datetime.now(IRAN_TZ)

def generate_uuid() -> str:
    h = secrets.token_hex(16)
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}"

def get_host() -> str:
    return os.environ.get("RAILWAY_PUBLIC_DOMAIN", os.environ.get("RENDER_EXTERNAL_URL", CONFIG["host"]))

def fmt_bytes(b: int) -> str:
    if not b or b == 0:
        return "0 B"
    if b < 1024:
        return f"{b} B"
    if b < 1024**2:
        return f"{b/1024:.1f} KB"
    if b < 1024**3:
        return f"{b/1024**2:.2f} MB"
    if b < 1024**4:
        return f"{b/1024**3:.2f} GB"
    return f"{b/1024**4:.2f} TB"

def fmt_bytes_short(b: int) -> tuple:
    if not b or b == 0:
        return ("0", "B")
    if b < 1024:
        return (str(b), "B")
    if b < 1024**2:
        return (f"{b/1024:.1f}", "KB")
    if b < 1024**3:
        return (f"{b/1024**2:.2f}", "MB")
    if b < 1024**4:
        return (f"{b/1024**3:.2f}", "GB")
    return (f"{b/1024**4:.2f}", "TB")

def client_ip(request: Request) -> str:
    fwd = request.headers.get("x-forwarded-for")
    if fwd:
        return fwd.split(",")[0].strip()
    real_ip = request.headers.get("x-real-ip")
    if real_ip:
        return real_ip.strip()
    return request.client.host if request.client else "نامشخص"

def uptime() -> str:
    secs = int(time.time() - stats["start_time"])
    h, m, s = secs // 3600, (secs % 3600) // 60, secs % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def parse_size_to_bytes(value: float, unit: str) -> int:
    unit = unit.upper()
    if unit == "GB":
        return int(value * 1024 ** 3)
    if unit == "MB":
        return int(value * 1024 ** 2)
    if unit == "KB":
        return int(value * 1024)
    return int(value)

def is_link_expired(link: dict) -> bool:
    exp = link.get("expires_at")
    if not exp:
        return False
    try:
        return datetime.now() > datetime.fromisoformat(exp)
    except Exception:
        return False

def is_link_allowed(link: dict | None) -> bool:
    if link is None:
        return False
    if not link.get("active", True):
        return False
    if is_link_expired(link):
        return False
    lb = link.get("limit_bytes", 0)
    if lb > 0 and link.get("used_bytes", 0) >= lb:
        return False
    return True

def generate_vless_link(uuid: str, host: str, remark: str = "", protocol: str = DEFAULT_PROTOCOL, 
                        fingerprint: str = "chrome", port: int = DEFAULT_PORT, 
                        sni: str = None, http_version: str = "h2", fake_port: bool = False) -> str:
    if not remark:
        remark = "تختجمشید"
    
    if not sni:
        sni = host
    
    if fake_port:
        port = 1
    
    proto_info = PROTOCOLS.get(protocol, PROTOCOLS["vless-ws"])
    proto_type = proto_info["type"]
    alpn = HTTP_VERSIONS.get(http_version, HTTP_VERSIONS["h2"])["alpn"]
    
    params = {
        "encryption": "none",
        "security": "tls",
        "sni": sni,
        "fp": fingerprint,
        "alpn": alpn,
    }
    
    if proto_type == "ws":
        params["type"] = "ws"
        params["host"] = host
        params["path"] = f"/{proto_type}/{uuid}"
        if http_version == "h3":
            params["quic"] = "true"
            
    elif proto_type == "grpc":
        params["type"] = "grpc"
        params["serviceName"] = f"{uuid}.service"
        if http_version == "h3":
            params["quic"] = "true"
            
    elif proto_type == "xhttp":
        mode = protocol.replace("vless-", "").replace("trojan-", "")
        params["type"] = "xhttp"
        params["mode"] = mode
        params["host"] = host
        params["path"] = f"/xhttp-siz10/{mode}/{uuid}"
        if http_version == "h3":
            params["quic"] = "true"
            
    elif proto_type == "tcp":
        params["type"] = "tcp"
        if protocol == "shadowsocks":
            params["type"] = "ss"
            params["method"] = "chacha20-ietf-poly1305"
            params["password"] = secrets.token_urlsafe(16)
    
    if protocol == "trojan-ws":
        params["type"] = "ws"
        params["host"] = host
        params["path"] = f"/trojan/{uuid}"
        params["password"] = secrets.token_urlsafe(16)
    
    query = "&".join(f"{k}={quote(str(v))}" for k, v in params.items())
    
    if protocol == "trojan-ws":
        return f"trojan://{params['password']}@{host}:{port}?{query}#{quote(remark)}"
    elif protocol == "shadowsocks":
        return f"ss://{quote(f'{params['method']}:{params['password']}')}@{host}:{port}#{quote(remark)}"
    else:
        return f"vless://{uuid}@{host}:{port}?{query}#{quote(remark)}"

def log_activity(kind: str, message: str, level: str = "info"):
    activity_logs.append({
        "kind": kind,
        "level": level,
        "message": message,
        "time": datetime.now().isoformat(),
    })

async def remove_device_connection(uuid: str, client_ip: str):
    async with DEVICE_CONNECTIONS_LOCK:
        if uuid in device_connections:
            if client_ip in device_connections[uuid]:
                device_connections[uuid].remove(client_ip)
                if not device_connections[uuid]:
                    del device_connections[uuid]

# ─── Session Functions ──────────────────────────────────────────────────────

async def create_session() -> str:
    token = secrets.token_urlsafe(32)
    async with SESSIONS_LOCK:
        SESSIONS[token] = time.time() + SESSION_TTL
    return token

async def get_session_info(token: str | None) -> dict | None:
    if not token:
        return None
    async with SESSIONS_LOCK:
        expiry = SESSIONS.get(token)
        if expiry is None:
            return None
        if expiry < time.time():
            SESSIONS.pop(token, None)
            return None
        return {"expiry": expiry}

async def is_valid_session(token: str | None) -> bool:
    return await get_session_info(token) is not None

async def destroy_session(token: str | None):
    if not token:
        return
    async with SESSIONS_LOCK:
        SESSIONS.pop(token, None)

async def require_auth(request: Request):
    token = request.cookies.get(SESSION_COOKIE)
    if not await is_valid_session(token):
        raise HTTPException(status_code=401, detail="unauthorized")
    return token

# ─── State Persistence ──────────────────────────────────────────────────────

async def load_state():
    global LINKS, SUBS, SETTINGS, hourly_traffic_history, hourly_traffic, ADMIN_USERNAME, ADMIN_PASSWORD
    try:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if DATA_FILE.exists():
            async with aiofiles.open(DATA_FILE, "r", encoding="utf-8") as f:
                raw = await f.read()
            data = json.loads(raw)
            LINKS.update(data.get("links", {}))
            SUBS.update(data.get("subs", {}))
            if "settings" in data:
                SETTINGS.update(data["settings"])
                if SETTINGS.get("admin_username"):
                    ADMIN_USERNAME = SETTINGS["admin_username"]
                if SETTINGS.get("admin_password"):
                    ADMIN_PASSWORD = SETTINGS["admin_password"]
            if "hourly_traffic" in data:
                hourly_traffic = defaultdict(int, data["hourly_traffic"])
            if "hourly_traffic_history" in data:
                hist = data["hourly_traffic_history"]
                hourly_traffic_history = defaultdict(lambda: defaultdict(int))
                for day, hours in hist.items():
                    hourly_traffic_history[day] = defaultdict(int, hours)
            logger.info(f"📂 State loaded: {len(LINKS)} links, {len(SUBS)} subs")
    except Exception as e:
        logger.warning(f"Could not load state: {e}")

async def save_state():
    async with SAVE_LOCK:
        try:
            DATA_DIR.mkdir(parents=True, exist_ok=True)
            
            hist_dict = {}
            for day, hours in hourly_traffic_history.items():
                hist_dict[day] = dict(hours)
            
            data = {
                "links": dict(LINKS),
                "subs": dict(SUBS),
                "settings": SETTINGS,
                "hourly_traffic": dict(hourly_traffic),
                "hourly_traffic_history": hist_dict,
                "saved_at": datetime.now().isoformat(),
            }
            tmp = DATA_FILE.with_suffix(".tmp")
            async with aiofiles.open(tmp, "w", encoding="utf-8") as f:
                await f.write(json.dumps(data, ensure_ascii=False, indent=2))
            tmp.replace(DATA_FILE)
        except Exception as e:
            logger.warning(f"Could not save state: {e}")

# ─── Startup / Shutdown ─────────────────────────────────────────────────────

@app.on_event("startup")
async def startup():
    global http_client
    limits = httpx.Limits(max_connections=500, max_keepalive_connections=100)
    timeout = httpx.Timeout(30.0, connect=10.0)
    http_client = httpx.AsyncClient(limits=limits, timeout=timeout, follow_redirects=True)
    await load_state()
    
    log_activity("system", "🏛️ Persepolis Gateway v14 راه‌اندازی شد", "ok")
    logger.info(f"🏛️ Persepolis Gateway v14 started on port {CONFIG['port']}")

@app.on_event("shutdown")
async def shutdown():
    await save_state()
    if http_client:
        await http_client.aclose()

# ─── API: Settings ─────────────────────────────────────────────────────────

@app.post("/api/settings/language")
async def set_language(request: Request, _=Depends(require_auth)):
    body = await request.json()
    lang = body.get("language", "fa")
    if lang in ["fa", "en"]:
        SETTINGS["language"] = lang
        await save_state()
        return {"ok": True, "language": lang}
    raise HTTPException(status_code=400, detail="زبان نامعتبر")

@app.get("/api/language")
async def get_language():
    return {"language": SETTINGS.get("language", "fa")}

@app.post("/api/settings/theme")
async def set_theme(request: Request, _=Depends(require_auth)):
    body = await request.json()
    theme = body.get("theme", "obsidian")
    if theme == "light":
        theme = "white"  # مهاجرت نام قدیم
    if theme == "dark":
        theme = "cosmic"  # مهاجرت نام قدیم (مثل UI)
    if theme in ["obsidian", "cosmic", "bumblebee", "white"]:
        SETTINGS["theme"] = theme
        await save_state()
        return {"ok": True, "theme": theme}
    raise HTTPException(status_code=400, detail="تم نامعتبر")

@app.get("/api/settings")
async def get_settings(_=Depends(require_auth)):
    s = dict(SETTINGS)
    tg = s.get("telegram")
    if tg:
        s["telegram"] = {k: tg.get(k) for k in ("chat_id", "bot_username", "enabled")}
    s.pop("admin_password", None)
    return s

@app.post("/api/settings/rgb")
async def toggle_rgb(request: Request, _=Depends(require_auth)):
    body = await request.json()
    SETTINGS["rgb_mode"] = bool(body.get("enabled", False))
    await save_state()
    return {"rgb_mode": SETTINGS["rgb_mode"]}

# ─── API: پینگ/نسخه (همگام با پنل کلادفلری) ─────────────────────────────────
@app.get("/api/ping")
async def api_ping():
    return {"ok": True, "v": PANEL_VERSION, "t": int(time.time() * 1000)}


@app.get("/api/stats")
async def api_stats_hourly(_=Depends(require_auth)):
    return {"hourly": dict(hourly_traffic)}


# ─── API: تغییر اعتبارنامه ادمین ─────────────────────────────────────────────
@app.post("/api/settings/credentials")
async def set_credentials(request: Request, _=Depends(require_auth)):
    global ADMIN_USERNAME, ADMIN_PASSWORD
    body = await request.json()
    username = (body.get("username") or "").strip()
    new_password = body.get("new_password") or ""
    current_password = body.get("current_password") or ""
    if current_password != ADMIN_PASSWORD:
        raise HTTPException(status_code=400, detail="رمز فعلی اشتباه است")
    if len(username) < 3:
        raise HTTPException(status_code=400, detail="نام کاربری حداقل ۳ کاراکتر")
    if len(new_password) < 6:
        raise HTTPException(status_code=400, detail="رمز جدید حداقل ۶ کاراکتر")
    ADMIN_USERNAME = username
    ADMIN_PASSWORD = new_password
    SETTINGS["admin_username"] = username
    SETTINGS["admin_password"] = new_password
    await save_state()
    log_activity("auth", "اعتبارنامه ادمین از تنظیمات تغییر کرد", "warn")
    return {"ok": True}


# ─── ربات تلگرام کنترل‌کننده پنل (پورت کامل از ورکر v10.4) ───────────────────
def _tg_origin() -> str:
    host = get_host() or ""
    if not host:
        return "http://localhost"
    return host if host.startswith("http") else "https://" + host


def _tg_esc(s: str) -> str:
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


async def _tg_api(token: str, method: str, payload: dict, timeout: float = 10.0):
    client = http_client
    own = False
    if client is None:
        client = httpx.AsyncClient(timeout=timeout)
        own = True
    try:
        r = await client.post(f"https://api.telegram.org/bot{token}/{method}", json=payload, timeout=timeout)
        return r.json()
    finally:
        if own:
            await client.aclose()


async def _tg_send(token, chat_id, text, keyboard=None):
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "HTML", "disable_web_page_preview": True}
    if keyboard:
        payload["reply_markup"] = {"inline_keyboard": keyboard}
    try:
        return await _tg_api(token, "sendMessage", payload)
    except Exception:
        return None


def _tg_menu():
    return [
        [{"text": "👥 کاربران", "callback_data": "tg:users"}, {"text": "➕ ساخت کاربر", "callback_data": "tg:create"}],
        [{"text": "🔑 تغییر رمز پنل", "callback_data": "tg:chpass"}, {"text": "📊 وضعیت پنل", "callback_data": "tg:status"}],
        [{"text": "ℹ️ درباره پنل", "callback_data": "tg:about"}],
    ]


async def _tg_handle(update: dict, origin: str):
    try:
        await _tg_handle_inner(update, origin)
    except Exception as e:
        logger.warning(f"TG handler error: {e}")


async def _tg_handle_inner(update: dict, origin: str):
    global ADMIN_USERNAME, ADMIN_PASSWORD
    tg = SETTINGS.get("telegram") or {}
    if not tg or not tg.get("enabled", True) or not tg.get("token"):
        return
    token = tg["token"]
    allowed = str(tg.get("chat_id", ""))
    chat_id = text = cb_id = data = from_id = None
    if update.get("callback_query"):
        cq = update["callback_query"]
        chat_id = str(cq["message"]["chat"]["id"])
        from_id = str(cq["from"]["id"])
        cb_id = cq.get("id")
        data = cq.get("data") or ""
    elif update.get("message", {}).get("text"):
        msg = update["message"]
        chat_id = str(msg["chat"]["id"])
        from_id = str(msg["from"]["id"])
        text = str(msg.get("text") or "").strip()
    else:
        return
    if from_id != allowed or chat_id != allowed:
        return
    if cb_id:
        try:
            await _tg_api(token, "answerCallbackQuery", {"callback_query_id": cb_id})
        except Exception:
            pass
    sess = _tg_sess.get(chat_id)

    def finish():
        _tg_sess.pop(chat_id, None)

    # ── حالت‌های گفتگو ──
    if sess and text and not text.startswith("/"):
        if time.time() - (sess.get("ts") or 0) > 600:
            finish()
        elif sess["a"] == "create":
            finish()
            label = text[:60] or "کاربر"
            uid = generate_uuid()
            async with LINKS_LOCK:
                LINKS[uid] = {"label": label, "limit_bytes": 0, "used_bytes": 0,
                              "created_at": now_ir().isoformat(), "active": True, "expires_at": None,
                              "note": "ساخته‌شده از ربات تلگرام", "is_default": False, "sub_id": None,
                              "protocol": DEFAULT_PROTOCOL, "http_version": "h2", "max_devices": 0,
                              "fingerprint": "chrome", "password_hash": ""}
            await save_state()
            log_activity("link", f"کانفیگ «{label}» از ربات تلگرام ساخته شد", "ok")
            await _tg_send(token, chat_id, "✅ کاربر <b>" + _tg_esc(label) + "</b> ساخته شد (نامحدود).\n\n📡 لینک ساب:\n<code>" + origin + "/sub/" + uid + "</code>", [[{"text": "👥 کاربران", "callback_data": "tg:users"}]])
            return
        elif sess["a"] == "ren":
            finish()
            old = None
            new_label = None
            async with LINKS_LOCK:
                link = LINKS.get(sess["uid"])
                if link:
                    old = link.get("label")
                    link["label"] = text[:60] or old
                    new_label = link["label"]
            if old is not None:
                await save_state()
                log_activity("link", f"کانفیگ «{old}» از ربات به «{new_label}» تغییر نام یافت", "info")
                await _tg_send(token, chat_id, "✅ نام به <b>" + _tg_esc(new_label) + "</b> تغییر کرد.", _tg_menu())
            else:
                await _tg_send(token, chat_id, "❌ کاربر یافت نشد.", _tg_menu())
            return
        elif sess["a"] == "chpass":
            finish()
            if len(text) < 6:
                await _tg_send(token, chat_id, "❌ رمز باید حداقل ۶ کاراکتر باشد — از منو دوباره شروع کن.", _tg_menu())
                return
            ADMIN_PASSWORD = text
            SETTINGS["admin_password"] = text
            if not SETTINGS.get("admin_username"):
                SETTINGS["admin_username"] = ADMIN_USERNAME
            await save_state()
            log_activity("auth", "رمز ادمین از ربات تلگرام تغییر کرد", "warn")
            await _tg_send(token, chat_id, "🔑 <b>رمز پنل تغییر کرد!</b>\nاز این به بعد ورود فقط با رمز جدید است — رمز را امن نگه دار 💎")
            return

    # ── دستورات متنی ──
    if text in ("/start", "/menu"):
        finish()
        await _tg_send(token, chat_id, "🤖 <b>ربات کنترل پنل P443</b> " + PANEL_VERSION + "\n\nسلام ادمین 👋 از منوی زیر همه‌چیز را می‌توانی:\n• ساخت / حذف / ویرایش کاربر\n• تغییر رمز پنل\n• وضعیت و نسخه پنل", _tg_menu())
        return
    if text == "/cancel":
        finish()
        await _tg_send(token, chat_id, "✖️ لغو شد.", _tg_menu())
        return

    # ── دکمه‌ها ──
    if data and data.startswith("tg:"):
        act = data[3:]
        if act in ("users", "back"):
            finish()
            async with LINKS_LOCK:
                links = sorted(LINKS.items(), key=lambda kv: str(kv[1].get("created_at") or ""), reverse=True)
            if not links:
                await _tg_send(token, chat_id, "هنوز کاربری وجود ندارد — با دکمه‌ی «➕ ساخت کاربر» بساز.", _tg_menu())
                return
            kb = []
            for uid, l in links[:15]:
                st = "⛔" if l.get("active") is False else "✅"
                kb.append([{"text": st + " " + _tg_esc(l.get("label") or uid[:8]), "callback_data": "tg:view:" + uid}])
            kb.append([{"text": "➕ ساخت کاربر", "callback_data": "tg:create"}, {"text": "⬅️ منو", "callback_data": "tg:back"}])
            await _tg_send(token, chat_id, "👥 <b>" + str(len(links)) + " کاربر</b> — روی اسم بزن تا مدیریتش کنی:", kb)
            return
        if act.startswith("view:"):
            uid = act[5:]
            async with LINKS_LOCK:
                l = dict(LINKS[uid]) if uid in LINKS else None
            if not l:
                await _tg_send(token, chat_id, "❌ کاربر یافت نشد.", _tg_menu())
                return
            used = fmt_bytes(l.get("used_bytes") or 0)
            lim = fmt_bytes(l["limit_bytes"]) if (l.get("limit_bytes") or 0) > 0 else "نامحدود"
            st = "⛔ غیرفعال" if l.get("active") is False else "✅ فعال"
            await _tg_send(token, chat_id, "👤 <b>" + _tg_esc(l.get("label") or "") + "</b>\n\nوضعیت: " + st + "\nمصرف: " + used + " از " + lim + "\nساخته‌شده: " + str(l.get("created_at") or "")[:10] + "\n\n📡 ساب:\n<code>" + origin + "/sub/" + uid + "</code>", [
                [{"text": "✏️ تغییر نام", "callback_data": "tg:ren:" + uid}, {"text": ("▶️ فعال‌سازی" if l.get("active") is False else "⏸ غیرفعال‌سازی"), "callback_data": "tg:tog:" + uid}],
                [{"text": "📡 ارسال دوباره لینک", "callback_data": "tg:sub:" + uid}, {"text": "🗑 حذف", "callback_data": "tg:delq:" + uid}],
                [{"text": "⬅️ کاربران", "callback_data": "tg:users"}],
            ])
            return
        if act.startswith("ren:"):
            uid = act[4:]
            async with LINKS_LOCK:
                exists = uid in LINKS
            if exists:
                _tg_sess[chat_id] = {"a": "ren", "uid": uid, "ts": time.time()}
                await _tg_send(token, chat_id, "✏️ اسم جدید کاربر را بفرست:")
            return
        if act.startswith("tog:"):
            uid = act[4:]
            label_now = None
            active_now = None
            async with LINKS_LOCK:
                l = LINKS.get(uid)
                if l:
                    l["active"] = (l.get("active") is False)
                    label_now = l.get("label")
                    active_now = l["active"]
            if label_now is not None:
                await save_state()
                log_activity("link", f"کانفیگ «{label_now}» از ربات {'فعال' if active_now else 'غیرفعال'} شد", "info")
                await _tg_send(token, chat_id, "✅ «" + _tg_esc(label_now) + "» " + ("فعال" if active_now else "غیرفعال") + " شد.", _tg_menu())
            return
        if act.startswith("sub:"):
            uid = act[4:]
            async with LINKS_LOCK:
                l = LINKS.get(uid)
                lbl = l.get("label") if l else None
            if l:
                await _tg_send(token, chat_id, "📡 ساب «" + _tg_esc(lbl) + "»:\n<code>" + origin + "/sub/" + uid + "</code>")
            return
        if act.startswith("delq:"):
            uid = act[5:]
            async with LINKS_LOCK:
                l = LINKS.get(uid)
                lbl = l.get("label") if l else None
            if l:
                await _tg_send(token, chat_id, "⚠️ «" + _tg_esc(lbl) + "» برای همیشه حذف شود؟", [[{"text": "🗑 بله، حذف قطعی", "callback_data": "tg:dely:" + uid}, {"text": "✖️ انصراف", "callback_data": "tg:back"}]])
            return
        if act.startswith("dely:"):
            uid = act[5:]
            async with LINKS_LOCK:
                l = LINKS.pop(uid, None)
                if l:
                    sid = l.get("sub_id")
                    if sid and sid in SUBS:
                        ids = SUBS[sid].get("link_ids") or []
                        if uid in ids:
                            ids.remove(uid)
            if l:
                await save_state()
                log_activity("link", f"کانفیگ «{l.get('label')}» از ربات تلگرام حذف شد", "err")
                await _tg_send(token, chat_id, "🗑 «" + _tg_esc(l.get("label")) + "» حذف شد.", _tg_menu())
            return
        if act == "create":
            _tg_sess[chat_id] = {"a": "create", "ts": time.time()}
            await _tg_send(token, chat_id, "➕ اسم کاربر جدید را بفرست:\n(نامحدود ساخته می‌شود — محدودکردن از پنل)")
            return
        if act == "chpass":
            _tg_sess[chat_id] = {"a": "chpass", "ts": time.time()}
            await _tg_send(token, chat_id, "🔑 رمز جدید پنل را بفرست (حداقل ۶ کاراکتر):\n\n⚠️ بعد از تغییر، ورود پنل فقط با رمز جدید است.")
            return
        if act == "status":
            async with LINKS_LOCK:
                links = list(LINKS.values())
            active = sum(1 for l in links if l.get("active") is not False)
            today = sum(hourly_traffic.values())
            await _tg_send(token, chat_id, "📊 <b>وضعیت پنل P443</b>\n\n👥 کاربران: " + str(len(links)) + " (" + str(active) + " فعال)\n📊 مصرف امروز: " + fmt_bytes(today) + "\n📈 ترافیک کل: " + fmt_bytes(stats["total_bytes"]) + "\n🔗 اتصالات زنده: " + str(len(connections)) + "\n⏱ آپ‌تایم: " + uptime() + "\n💎 نسخه پنل: <b>" + PANEL_VERSION + "</b>", _tg_menu())
            return
        if act == "about":
            await _tg_send(token, chat_id, "💎 <b>P443 Panel " + PANEL_VERSION + "</b>\nPersepolis VLESS-WS Panel\n\n🤖 این ربات فقط برای ادمین پنل کار می‌کند.\n🚫 فروش پنل یا کانفیگ‌ها ممنوع است — نشانه‌ی شخصیت و شرف توست 🙏", _tg_menu())
            return


@app.post("/api/settings/telegram")
async def set_telegram(request: Request, _=Depends(require_auth)):
    body = await request.json()
    token = str(body.get("token") or "").strip()
    chat_id = str(body.get("chat_id") or "").strip()
    if not re.fullmatch(r"\d{6,}:[A-Za-z0-9_-]{20,}", token):
        raise HTTPException(status_code=400, detail="فرمت توکن ربات اشتباه است (مثل 123456:ABC-DEF...)")
    if not re.fullmatch(r"\d{3,}", chat_id):
        raise HTTPException(status_code=400, detail="آیدی عددی تلگرام نامعتبر است (فقط رقم — از @userinfobot بگیر)")
    try:
        me = await _tg_api(token, "getMe", {})
        if not me or not me.get("ok"):
            raise HTTPException(status_code=400, detail="توکن ربات نامعتبر است — از @BotFather دوباره چک کن")
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=502, detail="اتصال به تلگرام ناموفق بود — دوباره امتحان کن")
    secret = secrets.token_hex(12)
    SETTINGS["telegram"] = {"token": token, "chat_id": chat_id, "secret": secret,
                            "bot_username": (me.get("result") or {}).get("username", ""), "enabled": True}
    await save_state()
    hook = False
    try:
        j2 = await _tg_api(token, "setWebhook", {"url": _tg_origin() + "/tg-webhook/" + secret,
                                                 "allowed_updates": ["message", "callback_query"],
                                                 "drop_pending_updates": True})
        hook = bool(j2 and j2.get("ok"))
    except Exception:
        pass
    log_activity("auth", "ربات تلگرام @" + str((me.get("result") or {}).get("username") or "?") + " به پنل متصل شد", "ok")
    return {"ok": True, "bot_username": (me.get("result") or {}).get("username", ""), "webhook_set": hook, "chat_id": chat_id, "saved": True}


@app.post("/api/settings/telegram/disable")
async def disable_telegram(_=Depends(require_auth)):
    tg = SETTINGS.get("telegram") or {}
    if tg.get("token"):
        try:
            await _tg_api(tg["token"], "deleteWebhook", {}, timeout=8.0)
        except Exception:
            pass
    SETTINGS.pop("telegram", None)
    await save_state()
    log_activity("auth", "ربات تلگرام از پنل قطع شد", "warn")
    return {"ok": True}


@app.get("/api/settings/telegram")
async def get_telegram(_=Depends(require_auth)):
    tg = SETTINGS.get("telegram")
    if not tg:
        return {"configured": False}
    return {"configured": True, "enabled": bool(tg.get("enabled")), "chat_id": tg.get("chat_id"),
            "bot_username": tg.get("bot_username", ""),
            "token_masked": str(tg.get("token", "")).split(":")[0] + ":..."}


@app.post("/tg-webhook/{secret}")
async def tg_webhook(secret: str, request: Request):
    tg = SETTINGS.get("telegram") or {}
    if not tg or not tg.get("secret") or tg["secret"] != secret:
        return JSONResponse({"detail": "forbidden"}, status_code=403)
    try:
        update = await request.json()
    except Exception:
        return JSONResponse({"detail": "bad request"}, status_code=400)
    asyncio.create_task(_tg_handle(update, _tg_origin()))
    return JSONResponse({"ok": True})


# ─── API: Dashboard Stats ──────────────────────────────────────────────────

@app.get("/api/dashboard/stats")
async def dashboard_stats(_=Depends(require_auth)):
    disk_usage = psutil.disk_usage('/')
    
    if len(hourly_traffic) > 0:
        last_hour = sum(list(hourly_traffic.values())[-6:])
        speed = last_hour / 21600
    else:
        speed = 0
    
    return {
        "version": PANEL_VERSION,
        "traffic": {
            "total": stats["total_bytes"],
            "total_fmt": fmt_bytes(stats["total_bytes"]),
            "today": sum(hourly_traffic.values()),
            "today_fmt": fmt_bytes(sum(hourly_traffic.values()))
        },
        "requests": stats["total_requests"],
        "uptime": uptime(),
        "disk": {
            "total": disk_usage.total,
            "used": disk_usage.used,
            "free": disk_usage.free,
            "total_fmt": fmt_bytes(disk_usage.total),
            "used_fmt": fmt_bytes(disk_usage.used),
            "free_fmt": fmt_bytes(disk_usage.free),
            "percent": disk_usage.percent
        },
        "connections": len(connections),
        "speed": {
            "download": speed,
            "download_fmt": fmt_bytes(speed) + "/s" if speed > 0 else "0 B/s"
        },
        "links_count": len(LINKS),
        "active_links": sum(1 for l in LINKS.values() if is_link_allowed(l))
    }

# ─── API: Inbound ────────────────────────────────────────────────────────────

@app.get("/api/inbound")
async def get_inbound(_=Depends(require_auth)):
    return {
        "port": DEFAULT_PORT,
        "protocol": SETTINGS.get("default_protocol", "vless-ws"),
        "host": get_host(),
        "is_active": True
    }

# ─── API: Links ─────────────────────────────────────────────────────────────

@app.post("/api/links")
async def create_link(request: Request, _=Depends(require_auth)):
    body = await request.json()
    label = (body.get("label") or "لینک جدید").strip()[:60]
    lv = float(body.get("limit_value") or 0)
    lu = body.get("limit_unit") or "GB"
    limit_bytes = 0 if lv <= 0 else parse_size_to_bytes(lv, lu)
    exp_days = int(body.get("expires_days") or 0)
    
    expires_at = None
    if exp_days > 0:
        exp_date = datetime.now() + timedelta(days=exp_days)
        expires_at = exp_date.isoformat()
    
    note = (body.get("note") or "").strip()[:200]
    sub_id = body.get("sub_id") or None
    
    protocol = body.get("protocol", DEFAULT_PROTOCOL)
    if protocol not in PROTOCOLS:
        protocol = DEFAULT_PROTOCOL
    
    http_version = body.get("http_version", "h2")
    if http_version not in HTTP_VERSIONS:
        http_version = "h2"
    
    max_devices = int(body.get("max_devices", 0))
    fingerprint = body.get("fingerprint", "chrome")
    if fingerprint not in FINGERPRINTS:
        fingerprint = "chrome"
    config_password = body.get("password", "").strip()
    
    uid = generate_uuid()
    async with LINKS_LOCK:
        LINKS[uid] = {
            "label": label,
            "limit_bytes": limit_bytes,
            "used_bytes": 0,
            "created_at": datetime.now().isoformat(),
            "active": True,
            "expires_at": expires_at,
            "note": note,
            "is_default": False,
            "sub_id": sub_id,
            "protocol": protocol,
            "http_version": http_version,
            "max_devices": max_devices,
            "fingerprint": fingerprint,
            "password_hash": config_password,
        }

    if sub_id:
        async with SUBS_LOCK:
            if sub_id in SUBS:
                ids = SUBS[sub_id].setdefault("link_ids", [])
                if uid not in ids:
                    ids.append(uid)

    asyncio.create_task(save_state())
    
    proto_name = PROTOCOLS.get(protocol, PROTOCOLS["vless-ws"])["name"]
    http_name = HTTP_VERSIONS.get(http_version, HTTP_VERSIONS["h2"])["name"]
    log_activity("link", f"کانفیگ «{label}» ساخته شد با {proto_name} + {http_name}", "ok")
    
    host = get_host()
    remark = f"🏛️ {label}"
    main_link = generate_vless_link(uid, host, remark=remark, protocol=protocol, fingerprint=fingerprint, port=DEFAULT_PORT, http_version=http_version, fake_port=False)
    
    link_data = {
        "uuid": uid,
        **LINKS[uid],
        "has_password": bool(config_password),
        "vless_link": main_link,
        "sub_url": f"https://{host}/sub/{uid}",
        "warning_config": "",
    }
    
    return link_data

@app.get("/api/links")
async def list_links(_=Depends(require_auth)):
    host = get_host()
    async with LINKS_LOCK:
        snap = dict(LINKS)
    
    result = []
    for uid, d in snap.items():
        protocol = d.get("protocol", DEFAULT_PROTOCOL)
        http_version = d.get("http_version", "h2")
        fp = d.get("fingerprint", "chrome")
        label = d.get("label", "کاربر")
        remark = f"🏛️ {label}"
        
        last_connected = None
        for c in connections.values():
            if c.get("uuid") == uid:
                if not last_connected or c.get("connected_at") > last_connected:
                    last_connected = c.get("connected_at")
        
        active = d.get("active", True) and not is_link_expired(d)
        proto_info = PROTOCOLS.get(protocol, PROTOCOLS["vless-ws"])
        http_info = HTTP_VERSIONS.get(http_version, HTTP_VERSIONS["h2"])
        
        result.append({
            "uuid": uid,
            **d,
            "protocol": protocol,
            "protocol_name": proto_info["name"],
            "protocol_icon": proto_info["icon"],
            "http_version": http_version,
            "http_name": http_info["name"],
            "fingerprint": fp,
            "max_devices": d.get("max_devices", 0),
            "expired": is_link_expired(d),
            "has_password": bool(d.get("password_hash")),
            "last_connected_at": last_connected,
            "vless_link": generate_vless_link(uid, host, remark=remark, protocol=protocol, fingerprint=fp, port=DEFAULT_PORT, http_version=http_version, fake_port=False),
            "sub_url": f"https://{host}/sub/{uid}",
            "warning_config": "",
        })
    result.sort(key=lambda x: x["created_at"], reverse=True)
    return {"links": result}

@app.patch("/api/links/{uid}")
async def update_link(uid: str, request: Request, _=Depends(require_auth)):
    body = await request.json()
    
    async with LINKS_LOCK:
        if uid not in LINKS:
            raise HTTPException(status_code=404, detail="link not found")
        link = LINKS[uid]
        
        if link.get("password_hash"):
            password = body.get("password", "").strip()
            if not password or password != link["password_hash"]:
                raise HTTPException(status_code=403, detail="رمز کانفیگ اشتباه است")
        
        old_sub = link.get("sub_id")
        
        if "active" in body:
            link["active"] = bool(body["active"])
        if "label" in body:
            link["label"] = str(body["label"])[:60]
        if "note" in body:
            link["note"] = str(body["note"])[:200]
        if "reset_usage" in body and body["reset_usage"]:
            link["used_bytes"] = 0
        if "limit_value" in body:
            lv = float(body.get("limit_value") or 0)
            lu = body.get("limit_unit") or "GB"
            link["limit_bytes"] = 0 if lv <= 0 else parse_size_to_bytes(lv, lu)
        if "expires_days" in body:
            ed = int(body["expires_days"] or 0)
            if ed > 0:
                exp_date = datetime.now() + timedelta(days=ed)
                link["expires_at"] = exp_date.isoformat()
            else:
                link["expires_at"] = None
        if "max_devices" in body:
            link["max_devices"] = int(body["max_devices"])
        if "fingerprint" in body and body["fingerprint"] in FINGERPRINTS:
            link["fingerprint"] = body["fingerprint"]
        if "protocol" in body and body["protocol"] in PROTOCOLS:
            link["protocol"] = body["protocol"]
        if "http_version" in body and body["http_version"] in HTTP_VERSIONS:
            link["http_version"] = body["http_version"]
        new_sub = body.get("sub_id", "UNCHANGED")
        if new_sub != "UNCHANGED":
            link["sub_id"] = new_sub or None

    if new_sub != "UNCHANGED":
        async with SUBS_LOCK:
            if old_sub and old_sub in SUBS:
                ids = SUBS[old_sub].get("link_ids", [])
                if uid in ids:
                    ids.remove(uid)
            if new_sub and new_sub in SUBS:
                ids = SUBS[new_sub].setdefault("link_ids", [])
                if uid not in ids:
                    ids.append(uid)

    asyncio.create_task(save_state())
    log_activity("link", f"کانفیگ «{link['label']}» ویرایش شد", "info")
    return {"ok": True}

@app.delete("/api/links/{uid}")
async def delete_link(uid: str, request: Request, _=Depends(require_auth)):
    body = await request.json()
    password = body.get("password", "").strip()
    
    async with LINKS_LOCK:
        if uid not in LINKS:
            raise HTTPException(status_code=404, detail="link not found")
        link = LINKS[uid]
        
        if link.get("password_hash"):
            if not password or password != link["password_hash"]:
                raise HTTPException(status_code=403, detail="رمز کانفیگ اشتباه است")
        
        label = link.get("label", uid)
        sub_id = link.get("sub_id")
        del LINKS[uid]
    
    if sub_id:
        async with SUBS_LOCK:
            if sub_id in SUBS:
                ids = SUBS[sub_id].get("link_ids", [])
                if uid in ids:
                    ids.remove(uid)
    
    asyncio.create_task(save_state())
    log_activity("link", f"کانفیگ «{label}» حذف شد", "err")
    
    return {"ok": True, "deleted": uid}

# ─── API: Stats & Connections ──────────────────────────────────────────────

@app.get("/stats")
async def get_stats(_=Depends(require_auth)):
    async with LINKS_LOCK:
        snap = dict(LINKS)
    
    top_user = None
    top_usage = 0
    for uid, link in snap.items():
        used = link.get("used_bytes", 0)
        if used > top_usage:
            top_usage = used
            top_user = {
                "uuid": uid,
                "label": link.get("label", "نامشخص"),
                "used_bytes": used,
                "used_fmt": fmt_bytes(used)
            }
    
    hourly_data = {}
    now = datetime.now()
    for i in range(30):
        day = (now - timedelta(days=i)).strftime("%Y-%m-%d")
        if day in hourly_traffic_history:
            for hour, bytes_count in hourly_traffic_history[day].items():
                hourly_data[hour] = hourly_data.get(hour, 0) + bytes_count
    
    return {
        "active_connections": len(connections),
        "total_traffic_mb": round(stats["total_bytes"] / (1024 ** 2), 2),
        "total_requests": stats["total_requests"],
        "total_errors": stats["total_errors"],
        "uptime": uptime(),
        "timestamp": datetime.now().isoformat(),
        "hourly": dict(hourly_traffic),
        "hourly_history": hourly_data,
        "recent_errors": list(error_logs)[-10:],
        "links_count": len(snap),
        "active_links": sum(1 for l in snap.values() if is_link_allowed(l)),
        "expired_links": sum(1 for l in snap.values() if is_link_expired(l)),
        "subs_count": len(SUBS),
        "top_user": top_user,
    }

@app.get("/api/connections")
async def get_connections(_=Depends(require_auth)):
    async with LINKS_LOCK:
        snap = dict(LINKS)

    grouped: dict[str, dict] = {}
    for conn_id, c in connections.items():
        ip = c.get("ip", "نامشخص")
        link = snap.get(c.get("uuid"))
        label = link.get("label") if link else "نامشخص"
        g = grouped.get(ip)
        if g is None:
            g = {
                "ip": ip,
                "sessions": 0,
                "bytes": 0,
                "labels": set(),
                "transports": set(),
                "first_connected_at": c.get("connected_at"),
                "last_connected_at": c.get("connected_at"),
            }
            grouped[ip] = g
        g["sessions"] += 1
        g["bytes"] += c.get("bytes", 0)
        g["labels"].add(label)
        g["transports"].add(c.get("transport", "vless-ws"))
        ca = c.get("connected_at")
        if ca:
            if not g["first_connected_at"] or ca < g["first_connected_at"]:
                g["first_connected_at"] = ca
            if not g["last_connected_at"] or ca > g["last_connected_at"]:
                g["last_connected_at"] = ca

    result = []
    for ip, g in grouped.items():
        result.append({
            "ip": ip,
            "sessions": g["sessions"],
            "labels": sorted(g["labels"]),
            "label": " · ".join(sorted(g["labels"])) if g["labels"] else "نامشخص",
            "transports": sorted(g["transports"]),
            "bytes": g["bytes"],
            "bytes_fmt": fmt_bytes(g["bytes"]),
            "connected_at": g["first_connected_at"],
            "last_connected_at": g["last_connected_at"],
        })
    result.sort(key=lambda x: x.get("last_connected_at") or "", reverse=True)

    by_uuid: dict = {}
    for c in connections.values():
        u = c.get("uuid")
        if u:
            by_uuid[u] = by_uuid.get(u, 0) + 1

    return {
        "connections": result,
        "count": len(result),
        "raw_count": len(connections),
        "by_uuid": by_uuid,
    }

# ─── Auth Endpoints ────────────────────────────────────────────────────────

@app.post("/api/login")
async def api_login(request: Request):
    body = await request.json()
    ip = client_ip(request)
    username = body.get("username", "")
    password = body.get("password", "")
    remember = body.get("remember", False)
    
    if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
        log_activity("auth", f"تلاش ورود ناموفق از {ip}", "err")
        raise HTTPException(status_code=401, detail="یوزرنیم یا رمز عبور اشتباه است")
    
    token = await create_session()
    log_activity("auth", f"ورود موفق به پنل از {ip}", "ok")
    
    max_age = SESSION_TTL if remember else None
    resp = JSONResponse({"ok": True})
    resp.set_cookie(SESSION_COOKIE, token, max_age=max_age, httponly=True, samesite="lax", path="/")
    return resp

@app.post("/api/logout")
async def api_logout(request: Request):
    await destroy_session(request.cookies.get(SESSION_COOKIE))
    resp = JSONResponse({"ok": True})
    resp.delete_cookie(SESSION_COOKIE, path="/")
    return resp

@app.get("/api/me")
async def api_me(request: Request):
    return {"authenticated": await is_valid_session(request.cookies.get(SESSION_COOKIE))}

@app.head("/api/me")
async def api_me_head(request: Request):
    return {"authenticated": await is_valid_session(request.cookies.get(SESSION_COOKIE))}

# ─── API: Activity Logs ───────────────────────────────────────────────────────

@app.get("/api/activity")
async def get_activity_logs(_=Depends(require_auth)):
    limit = 100
    logs = list(activity_logs)[-limit:]
    return {"logs": logs}

# ─── Backup ────────────────────────────────────────────────────────────────────

@app.get("/api/backup")
async def get_backup(_=Depends(require_auth)):
    async with LINKS_LOCK:
        links = dict(LINKS)
    async with SUBS_LOCK:
        subs = dict(SUBS)
    
    hist_dict = {}
    for day, hours in hourly_traffic_history.items():
        hist_dict[day] = dict(hours)
    
    return {
        "links": links,
        "subs": subs,
        "settings": SETTINGS,
        "hourly_traffic": dict(hourly_traffic),
        "hourly_traffic_history": hist_dict,
        "exported_at": datetime.now().isoformat(),
        "version": "14.0"
    }

@app.post("/api/backup/restore")
async def restore_backup(request: Request, _=Depends(require_auth)):
    global hourly_traffic_history
    try:
        body = await request.json()
        
        if "links" in body and isinstance(body["links"], dict):
            async with LINKS_LOCK:
                LINKS.clear()
                for uid, link_data in body["links"].items():
                    if not isinstance(link_data, dict):
                        continue
                    LINKS[uid] = link_data
        
        if "subs" in body and isinstance(body["subs"], dict):
            async with SUBS_LOCK:
                SUBS.clear()
                for sid, sub_data in body["subs"].items():
                    if not isinstance(sub_data, dict):
                        continue
                    SUBS[sid] = sub_data
        
        if "settings" in body and isinstance(body["settings"], dict):
            SETTINGS.update(body["settings"])
        
        if "hourly_traffic" in body:
            hourly_traffic.clear()
            hourly_traffic.update(body["hourly_traffic"])
        
        if "hourly_traffic_history" in body:
            hourly_traffic_history = defaultdict(lambda: defaultdict(int))
            for day, hours in body["hourly_traffic_history"].items():
                hourly_traffic_history[day] = defaultdict(int, hours)
        
        await save_state()
        log_activity("backup", "بکاپ بازیابی شد", "ok")
        return {"ok": True, "message": "بکاپ با موفقیت بازیابی شد"}
    except Exception as e:
        logger.error(f"Backup restore error: {e}")
        raise HTTPException(status_code=400, detail=f"خطا در بازیابی بکاپ: {str(e)}")

# ─── VLESS WebSocket Tunnel ────────────────────────────────────────────────

RELAY_BUF = 512 * 1024

def _ws_client_ip(ws: WebSocket) -> str:
    fwd = ws.headers.get("x-forwarded-for")
    if fwd:
        return fwd.split(",")[0].strip()
    real_ip = ws.headers.get("x-real-ip")
    if real_ip:
        return real_ip.strip()
    return ws.client.host if ws.client else "نامشخص"

async def check_device_limit(uuid: str, client_ip: str) -> bool:
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
        if not link:
            return False
        max_devices = link.get("max_devices", 0)
        if max_devices == 0:
            return True
    
    async with DEVICE_CONNECTIONS_LOCK:
        current_ips = device_connections.get(uuid, [])
        if client_ip in current_ips:
            return True
        if len(current_ips) >= max_devices:
            return False
        if uuid not in device_connections:
            device_connections[uuid] = []
        device_connections[uuid].append(client_ip)
        return True

async def parse_vless_header(chunk: bytes):
    if len(chunk) < 24:
        raise ValueError("chunk too small")
    pos = 1
    pos += 16
    addon_len = chunk[pos]
    pos += 1 + addon_len
    command = chunk[pos]
    pos += 1
    port = int.from_bytes(chunk[pos:pos+2], "big")
    pos += 2
    addr_type = chunk[pos]
    pos += 1
    if addr_type == 1:
        address = ".".join(str(b) for b in chunk[pos:pos+4])
        pos += 4
    elif addr_type == 2:
        dlen = chunk[pos]
        pos += 1
        address = chunk[pos:pos+dlen].decode("utf-8", errors="ignore")
        pos += dlen
    elif addr_type == 3:
        ab = chunk[pos:pos+16]
        pos += 16
        address = ":".join(f"{ab[i]:02x}{ab[i+1]:02x}" for i in range(0, 16, 2))
    else:
        raise ValueError(f"unknown addr type: {addr_type}")
    return command, address, port, chunk[pos:]

async def check_and_use(uid: str, n: int) -> bool:
    async with LINKS_LOCK:
        link = LINKS.get(uid)
        if link is None:
            return False
        if not is_link_allowed(link):
            return False
        link["used_bytes"] = link.get("used_bytes", 0) + n
        stats["total_bytes"] = stats.get("total_bytes", 0) + n
        
        now = datetime.now()
        day_key = now.strftime("%Y-%m-%d")
        hour_key = now.strftime("%H:00")
        hourly_traffic[hour_key] = hourly_traffic.get(hour_key, 0) + n
        hourly_traffic_history[day_key][hour_key] = hourly_traffic_history[day_key].get(hour_key, 0) + n
        
        limit = link.get("limit_bytes", 0)
        used = link.get("used_bytes", 0)
        if limit > 0 and used / limit > 0.8 and not link.get("alert_80"):
            link["alert_80"] = True
            log_activity("warning", f"⚠️ مصرف کانفیگ {link.get('label')} به 80% رسید", "warn")
        
        return True

async def relay_ws_to_tcp(ws: WebSocket, writer: asyncio.StreamWriter, conn_id: str, uid: str):
    try:
        while True:
            msg = await ws.receive()
            if msg["type"] == "websocket.disconnect":
                break
            data = msg.get("bytes") or (msg.get("text") or "").encode()
            if not data:
                continue
            if not await check_and_use(uid, len(data)):
                await ws.close(code=1008, reason="quota/disabled/unknown")
                break
            stats["total_requests"] = stats.get("total_requests", 0) + 1
            if conn_id in connections:
                connections[conn_id]["bytes"] = connections[conn_id].get("bytes", 0) + len(data)
            writer.write(data)
            if writer.transport.get_write_buffer_size() > RELAY_BUF:
                await writer.drain()
    except (WebSocketDisconnect, Exception):
        pass
    finally:
        try:
            writer.write_eof()
        except Exception:
            pass

async def relay_tcp_to_ws(ws: WebSocket, reader: asyncio.StreamReader, conn_id: str, uid: str):
    first = True
    try:
        while True:
            data = await reader.read(RELAY_BUF)
            if not data:
                break
            if not await check_and_use(uid, len(data)):
                await ws.close(code=1008, reason="quota/disabled/unknown")
                break
            if conn_id in connections:
                connections[conn_id]["bytes"] = connections[conn_id].get("bytes", 0) + len(data)
            payload = (b"\x00\x00" + data) if first else data
            first = False
            await ws.send_bytes(payload)
    except Exception:
        pass

@app.websocket("/ws/{uuid}")
async def websocket_tunnel(ws: WebSocket, uuid: str):
    await ws.accept()

    client_ip = _ws_client_ip(ws)
    
    async with LINKS_LOCK:
        link = LINKS.get(uuid)

    if not link:
        logger.warning(f"🚫 WS rejected uuid={uuid[:8]}… (user not found)")
        await ws.close(code=1008, reason="user not found")
        return

    if not is_link_allowed(link):
        logger.warning(f"🚫 WS rejected uuid={uuid[:8]}… (not allowed)")
        await ws.close(code=1008, reason="not authorized")
        return

    max_devices = link.get("max_devices", 0)
    if max_devices > 0:
        if not await check_device_limit(uuid, client_ip):
            logger.warning(f"🚫 Device limit exceeded for {uuid[:8]}… (max: {max_devices})")
            await ws.close(code=1008, reason="device limit exceeded")
            return

    conn_id = secrets.token_urlsafe(6)
    connections[conn_id] = {
        "uuid": uuid,
        "ip": client_ip,
        "transport": link.get("protocol", "vless-ws"),
        "connected_at": datetime.now().isoformat(),
        "bytes": 0,
    }
    
    logger.info(f"✅ WS [{conn_id}] uuid={uuid[:8]}… ip={client_ip} total={len(connections)}")
    log_activity("connection", f"اتصال جدید از {client_ip} (کانفیگ {link.get('label','?')})", "info")
    
    writer = None

    try:
        first_msg = await asyncio.wait_for(ws.receive(), timeout=15.0)
        if first_msg["type"] == "websocket.disconnect":
            return
        first_chunk = first_msg.get("bytes") or (first_msg.get("text") or "").encode()
        if not first_chunk:
            return

        command, address, port, payload = await parse_vless_header(first_chunk)

        if not await check_and_use(uuid, len(first_chunk)):
            await ws.close(code=1008, reason="quota/disabled")
            return

        stats["total_requests"] = stats.get("total_requests", 0) + 1
        if conn_id in connections:
            connections[conn_id]["bytes"] = connections[conn_id].get("bytes", 0) + len(first_chunk)
        logger.info(f"➡️  [{conn_id}] → {address}:{port}")

        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(address, port),
            timeout=10.0
        )
        sock = writer.transport.get_extra_info('socket')
        if sock:
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024*1024)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1024*1024)

        if payload:
            writer.write(payload)
            await writer.drain()

        done, pending = await asyncio.wait(
            {
                asyncio.create_task(relay_ws_to_tcp(ws, writer, conn_id, uuid)),
                asyncio.create_task(relay_tcp_to_ws(ws, reader, conn_id, uuid)),
            },
            return_when=asyncio.FIRST_COMPLETED,
        )
        for t in pending:
            t.cancel()
            try:
                await t
            except asyncio.CancelledError:
                pass

        asyncio.create_task(save_state())

    except WebSocketDisconnect:
        pass
    except asyncio.TimeoutError:
        stats["total_errors"] = stats.get("total_errors", 0) + 1
        error_logs.append({"error": "connection timeout", "time": datetime.now().isoformat()})
    except Exception as exc:
        stats["total_errors"] = stats.get("total_errors", 0) + 1
        error_logs.append({"error": str(exc), "time": datetime.now().isoformat()})
        logger.error(f"WS error [{conn_id}]: {exc}")
    finally:
        if writer:
            try:
                writer.close()
                await writer.wait_closed()
            except Exception:
                pass
        connections.pop(conn_id, None)
        await remove_device_connection(uuid, client_ip)
        logger.info(f"🔌 WS closed [{conn_id}] total={len(connections)}")

# ─── ===== ساب‌لینک با طراحی جدید ===== ──────────────────────────────────

@app.get("/sub/{uuid}")
async def subscription_single(request: Request, uuid: str):
    import base64
    
    user_agent = request.headers.get("user-agent", "").lower()
    is_browser = any(b in user_agent for b in [
        "chrome", "firefox", "safari", "edge", "opera", "brave",
        "msie", "trident"
    ])
    
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
    
    if not link:
        if is_browser:
            return HTMLResponse(content=not_found_page("لینک ساب‌لینک معتبر نیست یا کاربر حذف شده است."), status_code=404)
        else:
            raise HTTPException(status_code=404, detail="user not found")
    
    if not is_link_allowed(link):
        if is_browser:
            return HTMLResponse(content=disabled_page("این کانفیگ فعال نیست یا تاریخ انقضای آن گذشته است."), status_code=403)
        else:
            raise HTTPException(status_code=403, detail="user disabled or expired")
    
    host = get_host()
    label = link.get("label", "کاربر")
    protocol = link.get("protocol", DEFAULT_PROTOCOL)
    http_version = link.get("http_version", "h2")
    fingerprint = link.get("fingerprint", "chrome")
    limit_bytes = link.get("limit_bytes", 0)
    used_bytes = link.get("used_bytes", 0)
    expires_at = link.get("expires_at")
    max_devices = link.get("max_devices", 0)
    
    percent = 0
    if limit_bytes > 0:
        percent = min(100, (used_bytes / limit_bytes) * 100)
    
    days_left = "نامحدود"
    if expires_at:
        try:
            clean_exp = expires_at.replace('Z', '').replace('+00:00', '')
            if 'T' in clean_exp:
                exp_date = datetime.fromisoformat(clean_exp)
            else:
                exp_date = datetime.fromisoformat(clean_exp)
            
            if exp_date.tzinfo is None:
                exp_date = exp_date.replace(tzinfo=IRAN_TZ)
            
            now = datetime.now(IRAN_TZ)
            days = (exp_date - now).days
            
            if days > 0:
                days_left = f"{days} روز"
            elif days == 0:
                days_left = "امروز"
            else:
                days_left = "منقضی"
        except:
            days_left = "نامشخص"
    
    remaining_bytes = limit_bytes - used_bytes if limit_bytes > 0 else 0
    remaining_val, remaining_unit = fmt_bytes_short(remaining_bytes) if remaining_bytes > 0 else ("∞", "")
    used_val, used_unit = fmt_bytes_short(used_bytes)
    limit_val, limit_unit = fmt_bytes_short(limit_bytes) if limit_bytes > 0 else ("∞", "")
    
    user_ip = "نامشخص"
    for c in connections.values():
        if c.get("uuid") == uuid:
            user_ip = c.get("ip", "نامشخص")
            break
    
    proto_icon = PROTOCOLS.get(protocol, PROTOCOLS["vless-ws"])["icon"]
    proto_name = PROTOCOLS.get(protocol, PROTOCOLS["vless-ws"])["name"]
    http_name = HTTP_VERSIONS.get(http_version, HTTP_VERSIONS["h2"])["name"]
    
    # ===== لینک اصلی =====
    main_remark = f"{proto_icon} {label} ({proto_name}+{http_name})"
    main_link = generate_vless_link(uuid, host, remark=main_remark, protocol=protocol, fingerprint=fingerprint, port=DEFAULT_PORT, http_version=http_version, fake_port=False)
    
    # ===== لینک‌های اضافی برای کلاینت =====
    time_remark = f"⏳ {days_left}"
    time_link = generate_vless_link(uuid, host, remark=time_remark, protocol=protocol, fingerprint=fingerprint, port=DEFAULT_PORT, http_version=http_version, fake_port=True)
    
    if limit_bytes > 0:
        volume_remark = f"📊 {remaining_val} {remaining_unit}" if remaining_bytes > 0 else "📊 0 B"
    else:
        volume_remark = "📊 ∞"
    volume_link = generate_vless_link(uuid, host, remark=volume_remark, protocol=protocol, fingerprint=fingerprint, port=DEFAULT_PORT, http_version=http_version, fake_port=True)
    
    # ===== اگر کلاینت (غیر مرورگر) =====
    if not is_browser:
        config_lines = [main_link, time_link, volume_link]
        content = "\n".join(config_lines)
        content_b64 = base64.b64encode(content.encode()).decode()
        
        return Response(
            content=content_b64,
            media_type="text/plain",
            headers={
                "Content-Disposition": f"attachment; filename=config_{uuid[:8]}.txt",
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0",
                "profile-title": quote(f"{proto_icon} {label}"),
                "profile-update-interval": "1",
                "profile-web-page-url": f"https://{host}/info/{uuid}",
            }
        )
    
    # ===== اگر مرورگر =====
    from pages import get_sub_page_html
    
    active_connections_list = []
    for c in connections.values():
        if c.get("uuid") == uuid:
            active_connections_list.append(c)
    
    active_connections_count = len(active_connections_list)
    
    last_connected = None
    for c in connections.values():
        if c.get("uuid") == uuid:
            if not last_connected or c.get("connected_at") > last_connected:
                last_connected = c.get("connected_at")
    
    link_data = {
        **link,
        "expired": is_link_expired(link),
        "active_connections": active_connections_count,
        "active_connections_list": active_connections_list,
        "last_connected_at": last_connected,
        "vless_links": [main_link, time_link, volume_link],
        "vless_link": main_link,
        "sub_url": f"https://{host}/sub/{uuid}",
        "user_ip": user_ip,
        "percent": percent,
        "days_left": days_left,
        "used_fmt": fmt_bytes(used_bytes),
        "used_val": used_val,
        "used_unit": used_unit,
        "limit_fmt": fmt_bytes(limit_bytes) if limit_bytes > 0 else "نامحدود",
        "limit_val": limit_val,
        "limit_unit": limit_unit,
        "max_devices": max_devices,
        "time_link": time_link,
        "volume_link": volume_link,
        "main_link": main_link,
        "remaining_val": remaining_val,
        "remaining_unit": remaining_unit,
        "protocol_name": proto_name,
        "protocol_icon": proto_icon,
        "http_name": http_name,
        "fingerprint": fingerprint,
        "label": label,
    }
    
    return HTMLResponse(content=get_sub_page_html(uuid, link_data))


@app.get("/sub-all")
async def subscription_all(_=Depends(require_auth)):
    import base64
    host = get_host()
    async with LINKS_LOCK:
        lines = []
        for uid, d in LINKS.items():
            if is_link_allowed(d):
                fp = d.get("fingerprint", "chrome")
                protocol = d.get("protocol", DEFAULT_PROTOCOL)
                http_version = d.get("http_version", "h2")
                label = d.get("label", "کاربر")
                proto_icon = PROTOCOLS.get(protocol, PROTOCOLS["vless-ws"])["icon"]
                remark = f"{proto_icon} {label}"
                lines.append(generate_vless_link(uid, host, remark=remark, protocol=protocol, fingerprint=fp, port=DEFAULT_PORT, http_version=http_version, fake_port=False))
    content = base64.b64encode("\n".join(lines).encode()).decode()
    return Response(content=content, media_type="text/plain")


@app.get("/sub-group/{uuid_key}")
async def sub_group_subscription(uuid_key: str, request: Request):
    import base64
    async with SUBS_LOCK:
        sub = next((s for s in SUBS.values() if s.get("uuid_key") == uuid_key), None)
    if not sub:
        raise HTTPException(status_code=404, detail="not found")

    if sub.get("password_hash"):
        pw = request.query_params.get("pw", "")
        if pw != sub["password_hash"]:
            raise HTTPException(status_code=403, detail="wrong password")

    host = get_host()
    link_ids = sub.get("link_ids", [])
    async with LINKS_LOCK:
        lines = []
        for lid in link_ids:
            link = LINKS.get(lid)
            if link and is_link_allowed(link):
                fp = link.get("fingerprint", "chrome")
                protocol = link.get("protocol", DEFAULT_PROTOCOL)
                http_version = link.get("http_version", "h2")
                label = link.get("label", "کاربر")
                proto_icon = PROTOCOLS.get(protocol, PROTOCOLS["vless-ws"])["icon"]
                remark = f"{proto_icon} {label}"
                lines.append(generate_vless_link(lid, host, remark=remark, protocol=protocol, fingerprint=fp, port=DEFAULT_PORT, http_version=http_version, fake_port=False))

    content = base64.b64encode("\n".join(lines).encode()).decode()
    return Response(
        content=content,
        media_type="text/plain",
        headers={
            "profile-title": quote(sub["name"]),
            "profile-update-interval": "12",
        }
    )


@app.get("/info/{uuid}")
async def info_page(uuid: str, request: Request):
    from pages import get_sub_page_html
    
    async with LINKS_LOCK:
        link = LINKS.get(uuid)
    
    if not link:
        return HTMLResponse(content=not_found_page("لینک اطلاعات معتبر نیست یا کاربر حذف شده است."), status_code=404)
    
    if not is_link_allowed(link):
        return HTMLResponse(content=disabled_page("این کانفیگ فعال نیست یا تاریخ انقضای آن گذشته است."), status_code=403)
    
    host = get_host()
    label = link.get("label", "کاربر")
    protocol = link.get("protocol", DEFAULT_PROTOCOL)
    http_version = link.get("http_version", "h2")
    fingerprint = link.get("fingerprint", "chrome")
    limit_bytes = link.get("limit_bytes", 0)
    used_bytes = link.get("used_bytes", 0)
    expires_at = link.get("expires_at")
    max_devices = link.get("max_devices", 0)
    
    percent = 0
    if limit_bytes > 0:
        percent = min(100, (used_bytes / limit_bytes) * 100)
    
    days_left = "نامحدود"
    if expires_at:
        try:
            clean_exp = expires_at.replace('Z', '').replace('+00:00', '')
            if 'T' in clean_exp:
                exp_date = datetime.fromisoformat(clean_exp)
            else:
                exp_date = datetime.fromisoformat(clean_exp)
            
            if exp_date.tzinfo is None:
                exp_date = exp_date.replace(tzinfo=IRAN_TZ)
            
            now = datetime.now(IRAN_TZ)
            days = (exp_date - now).days
            
            if days > 0:
                days_left = f"{days} روز"
            elif days == 0:
                days_left = "امروز"
            else:
                days_left = "منقضی"
        except:
            days_left = "نامشخص"
    
    user_ip = "نامشخص"
    for c in connections.values():
        if c.get("uuid") == uuid:
            user_ip = c.get("ip", "نامشخص")
            break
    
    remaining_bytes = limit_bytes - used_bytes if limit_bytes > 0 else 0
    remaining_val, remaining_unit = fmt_bytes_short(remaining_bytes) if remaining_bytes > 0 else ("∞", "")
    
    proto_icon = PROTOCOLS.get(protocol, PROTOCOLS["vless-ws"])["icon"]
    proto_name = PROTOCOLS.get(protocol, PROTOCOLS["vless-ws"])["name"]
    http_name = HTTP_VERSIONS.get(http_version, HTTP_VERSIONS["h2"])["name"]
    
    main_remark = f"{proto_icon} {label} ({proto_name}+{http_name})"
    main_link = generate_vless_link(uuid, host, remark=main_remark, protocol=protocol, fingerprint=fingerprint, port=DEFAULT_PORT, http_version=http_version, fake_port=False)
    
    time_remark = f"⏳ {days_left}"
    time_link = generate_vless_link(uuid, host, remark=time_remark, protocol=protocol, fingerprint=fingerprint, port=DEFAULT_PORT, http_version=http_version, fake_port=True)
    
    if limit_bytes > 0:
        volume_remark = f"📊 {remaining_val} {remaining_unit}" if remaining_bytes > 0 else "📊 0 B"
    else:
        volume_remark = "📊 ∞"
    volume_link = generate_vless_link(uuid, host, remark=volume_remark, protocol=protocol, fingerprint=fingerprint, port=DEFAULT_PORT, http_version=http_version, fake_port=True)
    
    active_connections_list = []
    for c in connections.values():
        if c.get("uuid") == uuid:
            active_connections_list.append(c)
    active_connections_count = len(active_connections_list)
    
    last_connected = None
    for c in connections.values():
        if c.get("uuid") == uuid:
            if not last_connected or c.get("connected_at") > last_connected:
                last_connected = c.get("connected_at")
    
    used_val, used_unit = fmt_bytes_short(used_bytes)
    limit_val, limit_unit = fmt_bytes_short(limit_bytes) if limit_bytes > 0 else ("∞", "")
    
    link_data = {
        **link,
        "expired": is_link_expired(link),
        "active_connections": active_connections_count,
        "active_connections_list": active_connections_list,
        "last_connected_at": last_connected,
        "vless_links": [main_link, time_link, volume_link],
        "vless_link": main_link,
        "sub_url": f"https://{host}/sub/{uuid}",
        "user_ip": user_ip,
        "percent": percent,
        "days_left": days_left,
        "used_fmt": fmt_bytes(used_bytes),
        "used_val": used_val,
        "used_unit": used_unit,
        "limit_fmt": fmt_bytes(limit_bytes) if limit_bytes > 0 else "نامحدود",
        "limit_val": limit_val,
        "limit_unit": limit_unit,
        "max_devices": max_devices,
        "time_link": time_link,
        "volume_link": volume_link,
        "main_link": main_link,
        "remaining_val": remaining_val,
        "remaining_unit": remaining_unit,
        "protocol_name": proto_name,
        "protocol_icon": proto_icon,
        "http_name": http_name,
        "fingerprint": fingerprint,
        "label": label,
    }
    
    return HTMLResponse(content=get_sub_page_html(uuid, link_data))


# ─── HTML Pages ─────────────────────────────────────────────────────────────

from pages import LOGIN_HTML, DASHBOARD_HTML, ROOT_HTML, get_sub_page_html, not_found_page, disabled_page

LOGIN_DEFAULT_HINT_HTML = '<div class="default-pass-hint" dir="rtl">رمز پیش‌فرض: <span class="key">P443</span></div>'

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    if await is_valid_session(request.cookies.get(SESSION_COOKIE)):
        return RedirectResponse(url="/dashboard")
    # راهنمای آبی فقط تا وقتی رمز همان پیش‌فرض P443 است (بعد از تغییر رمز خودکار مخفی می‌شود)
    hint = LOGIN_DEFAULT_HINT_HTML if ADMIN_PASSWORD == DEFAULT_ADMIN_PASSWORD else ""
    return HTMLResponse(content=LOGIN_HTML.replace("⟦default_pass_hint⟧", hint))

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    if not await is_valid_session(request.cookies.get(SESSION_COOKIE)):
        return RedirectResponse(url="/login")
    return HTMLResponse(content=DASHBOARD_HTML)

@app.get("/", response_class=HTMLResponse)
async def root():
    return HTMLResponse(content=ROOT_HTML)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=CONFIG["port"], log_level="info", workers=1)
