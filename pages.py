# pages.py — UI پنل P443 (همگام کامل با پنل کلادفلری v10.4)
# LOGIN/DASHBOARD/ROOT/SUB از سورس رسمی ورکر استخراج و پورت شده است
# رندر ساب: جایگذاری توکن‌های ⟦x⟧ مثل renderSubPage ورکر

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>✦ PERSEPOLIS · ورود به کیهان</title>
<link rel="icon" type="image/jpeg" href="data:image/jpeg;base64,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">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg-deep:#030418;
  --bg-mid:#0a0e2a;
  --bg-surface:rgba(10,14,35,0.55);
  --bg-surface-2:rgba(15,20,45,0.75);
  --border-subtle:rgba(100,200,255,0.08);
  --border-glow:rgba(0,240,255,0.35);
  --border-glow-strong:rgba(0,240,255,0.6);
  --cyan:#00f0ff;
  --cyan-soft:rgba(0,240,255,0.15);
  --magenta:#ff2e9a;
  --magenta-soft:rgba(255,46,154,0.15);
  --purple:#7b2ff7;
  --purple-soft:rgba(123,47,247,0.15);
  --gold:#D4A843;
  --gold2:#F5D060;
  --t1:#e8efff;
  --t2:#94a3b8;
  --t3:#64748b;
  --success:#10ffa0;
  --danger:#ff4d6d;
  --glow-cyan:0 0 30px rgba(0,240,255,0.25),0 0 60px rgba(0,240,255,0.12);
  --glow-magenta:0 0 30px rgba(255,46,154,0.25),0 0 60px rgba(255,46,154,0.12);
  --shadow-deep:0 25px 80px rgba(0,0,0,0.6),0 0 120px rgba(0,240,255,0.04);
  --transition:cubic-bezier(0.34,1.56,0.64,1)
}
html,body{height:100%}
body{
  font-family:'Vazirmatn',sans-serif;
  min-height:100vh;
  display:flex;align-items:center;justify-content:center;
  background:radial-gradient(ellipse at top,#0a0e2a 0%,#030418 50%,#000 100%);
  padding:20px;color:var(--t1);position:relative;overflow:hidden;
}

/* === ✦ تم‌های پنل: کیهانی / اوبسیدین (مشکی) / زنبوری (زرد-مشکی) === */
body[data-theme="obsidian"]{--bg-deep:#050507;--bg-mid:#0b0b10;--bg-surface:rgba(14,14,18,0.66);--bg-surface-2:rgba(18,18,23,0.85);--border-subtle:rgba(255,255,255,0.08);--border-glow:rgba(159,176,255,0.3);--border-glow-strong:rgba(159,176,255,0.55);--cyan:#9fb0ff;--cyan-soft:rgba(159,176,255,0.12);--magenta:#f0abfc;--magenta-soft:rgba(240,171,252,0.1);--purple:#c4b5fd;--purple-soft:rgba(196,181,253,0.1);--t1:#f2f4ff;--glow-cyan:0 0 24px rgba(159,176,255,0.16);--glow-magenta:0 0 24px rgba(240,171,252,0.14);--shadow-deep:0 25px 80px rgba(0,0,0,0.75);background:radial-gradient(ellipse at top,#0b0b10 0%,#050507 55%,#000 100%)!important}
body[data-theme="obsidian"] .grid-lines{background-image:linear-gradient(rgba(159,176,255,0.25) 1px,transparent 1px),linear-gradient(90deg,rgba(159,176,255,0.25) 1px,transparent 1px);opacity:.08}
body[data-theme="bumblebee"]{--bg-deep:#0a0803;--bg-mid:#141004;--bg-surface:rgba(26,21,8,0.66);--bg-surface-2:rgba(30,24,9,0.85);--border-subtle:rgba(255,214,10,0.12);--border-glow:rgba(255,214,10,0.3);--border-glow-strong:rgba(255,214,10,0.55);--cyan:#ffd60a;--cyan-soft:rgba(255,214,10,0.12);--magenta:#ffea00;--magenta-soft:rgba(255,234,0,0.08);--purple:#ffc300;--purple-soft:rgba(255,195,0,0.1);--t1:#fff9e0;--glow-cyan:0 0 24px rgba(255,214,10,0.16);--glow-magenta:0 0 24px rgba(255,234,0,0.12);--shadow-deep:0 25px 80px rgba(0,0,0,0.7);background:radial-gradient(ellipse at top,#141004 0%,#0a0803 55%,#050401 100%)!important}
body[data-theme="bumblebee"] .grid-lines{background-image:linear-gradient(rgba(255,214,10,0.3) 1px,transparent 1px),linear-gradient(90deg,rgba(255,214,10,0.3) 1px,transparent 1px);opacity:.08}
body[data-theme="white"]{--bg-deep:#e9edf5;--bg-mid:#f2f5fa;--bg-surface:rgba(255,255,255,0.82);--bg-surface-2:rgba(255,255,255,0.94);--border-subtle:rgba(15,30,70,0.12);--border-glow:rgba(11,108,224,0.3);--border-glow-strong:rgba(11,108,224,0.5);--cyan:#0b6ce0;--cyan-soft:rgba(11,108,224,0.1);--magenta:#d6336c;--magenta-soft:rgba(214,51,108,0.08);--purple:#7048e8;--purple-soft:rgba(112,72,232,0.08);--t1:#131a2b;--t2:#43506b;--t3:#7c89a3;--glow-cyan:none;--glow-magenta:none;--shadow-deep:0 20px 60px rgba(30,50,100,0.15);background:linear-gradient(160deg,#f6f8fc 0%,#e9eef7 55%,#dfe7f3 100%)!important}
body[data-theme="white"] .grid-lines{background-image:linear-gradient(rgba(20,50,120,0.16) 1px,transparent 1px),linear-gradient(90deg,rgba(20,50,120,0.16) 1px,transparent 1px);opacity:.25}

/* === ستاره‌های متحرک === */
#starfield{position:fixed;inset:0;z-index:0;pointer-events:none}
.star{position:absolute;border-radius:50%;background:#fff;animation:twinkle 3s ease-in-out infinite}
@keyframes twinkle{0%,100%{opacity:0.15;transform:scale(0.6)}50%{opacity:1;transform:scale(1.4)}}

/* === سحابی‌های شناور === */
.nebula{position:fixed;border-radius:50%;filter:blur(120px);z-index:0;pointer-events:none;animation:nebulaFloat 14s ease-in-out infinite}
.nebula-1{width:600px;height:600px;background:radial-gradient(circle,rgba(0,240,255,0.18),transparent 70%);top:-200px;right:-150px}
.nebula-2{width:500px;height:500px;background:radial-gradient(circle,rgba(255,46,154,0.15),transparent 70%);bottom:-150px;left:-100px;animation-delay:-7s}
.nebula-3{width:400px;height:400px;background:radial-gradient(circle,rgba(123,47,247,0.12),transparent 70%);top:40%;left:30%;animation-delay:-3s}
@keyframes nebulaFloat{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(40px,-30px) scale(1.08)}66%{transform:translate(-30px,40px) scale(0.95)}}

/* === خطوط هولوگرافیک متحرک === */
.grid-lines{position:fixed;inset:0;z-index:0;pointer-events:none;opacity:0.15;background-image:linear-gradient(rgba(0,240,255,0.3) 1px,transparent 1px),linear-gradient(90deg,rgba(0,240,255,0.3) 1px,transparent 1px);background-size:50px 50px;mask-image:radial-gradient(ellipse at center,#000 0%,transparent 70%);animation:gridShift 20s linear infinite}
@keyframes gridShift{0%{background-position:0 0}100%{background-position:50px 50px}}

/* === زبانه زبان === */
.lang-toggle{position:fixed;top:24px;left:24px;z-index:50;display:flex;gap:4px;background:var(--bg-surface);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:14px;padding:4px;box-shadow:0 8px 30px rgba(0,0,0,0.3)}
.lang-toggle button{background:none;border:none;color:var(--t3);font-family:inherit;font-size:11px;font-weight:700;padding:6px 12px;border-radius:10px;cursor:pointer;transition:all .3s var(--transition)}
.lang-toggle button.active{background:linear-gradient(135deg,var(--cyan),var(--purple));color:#000;box-shadow:var(--glow-cyan)}
.lang-toggle button:hover:not(.active){color:var(--t1);background:rgba(0,240,255,0.05)}

/* === کارت ورود === */
.container{position:relative;z-index:10;display:grid;grid-template-columns:1fr 1fr;max-width:1140px;width:100%;background:var(--bg-surface);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border-radius:28px;border:1px solid var(--border-subtle);overflow:hidden;box-shadow:var(--shadow-deep);animation:cardRise .8s var(--transition)}
@keyframes cardRise{from{opacity:0;transform:translateY(40px) scale(0.95)}to{opacity:1;transform:translateY(0) scale(1)}}
.container::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(0,240,255,0.04),transparent 50%,rgba(255,46,154,0.03));pointer-events:none;z-index:0}
.container::after{content:'';position:absolute;inset:-2px;border-radius:28px;padding:2px;background:linear-gradient(135deg,rgba(0,240,255,0.5),transparent 30%,transparent 70%,rgba(255,46,154,0.5));-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;opacity:0.4;pointer-events:none;animation:borderGlow 6s ease-in-out infinite}
@keyframes borderGlow{0%,100%{opacity:0.3}50%{opacity:0.7}}

.login-section{position:relative;z-index:1;padding:52px 44px}
.brand{display:flex;align-items:center;gap:14px;margin-bottom:36px}
.brand-icon{width:52px;height:52px;border-radius:14px;background:linear-gradient(135deg,var(--cyan),var(--purple),var(--magenta));display:flex;align-items:center;justify-content:center;font-size:26px;box-shadow:var(--glow-cyan);animation:iconPulse 4s ease-in-out infinite;position:relative}
.brand-icon::before{content:'';position:absolute;inset:-3px;border-radius:16px;background:linear-gradient(135deg,var(--cyan),var(--magenta));z-index:-1;filter:blur(10px);opacity:0.6;animation:iconPulse 4s ease-in-out infinite}
@keyframes iconPulse{0%,100%{box-shadow:0 0 30px rgba(0,240,255,0.4)}50%{box-shadow:0 0 50px rgba(255,46,154,0.5)}}
.brand-icon img.logo-img{width:100%;height:100%;object-fit:cover;border-radius:inherit;display:block;position:relative;z-index:1}.info-logo-wrap{display:flex;justify-content:center;margin-bottom:20px}.info-logo{width:clamp(110px,26vw,150px);height:clamp(110px,26vw,150px);border-radius:24px;object-fit:cover;border:1px solid var(--border-glow);box-shadow:var(--glow-cyan),0 12px 50px rgba(255,46,154,0.18);animation:iconPulse 4s ease-in-out infinite}.brand-text{font-size:18px;font-weight:900;background:linear-gradient(135deg,#fff,var(--cyan),var(--magenta));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;letter-spacing:0.5px}
.brand-sub{font-size:10px;color:var(--t3);letter-spacing:1.2px;text-transform:uppercase;margin-top:2px}

.welcome{font-size:26px;font-weight:800;color:var(--t1);margin-bottom:6px;background:linear-gradient(135deg,#fff,rgba(255,255,255,0.7));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.sub-text{font-size:13px;color:var(--t3);margin-bottom:30px}

.field{margin-bottom:18px;position:relative}
.field label{display:block;font-size:10px;font-weight:700;color:var(--t2);margin-bottom:6px;letter-spacing:0.5px;text-transform:uppercase}
.field input{width:100%;padding:14px 16px 14px 42px;border-radius:12px;border:1px solid var(--border-subtle);background:rgba(0,0,15,0.4);color:var(--t1);font-family:inherit;font-size:14px;outline:none;transition:all .3s var(--transition)}
.field input:focus{border-color:var(--cyan);box-shadow:0 0 0 4px rgba(0,240,255,0.08),0 0 30px rgba(0,240,255,0.15);background:rgba(0,240,255,0.03)}
.field input::placeholder{color:var(--t3)}
.field .input-icon{position:absolute;left:14px;top:36px;color:var(--t3);font-size:16px;transition:color .3s}
.field input:focus + .input-icon,.field:focus-within .input-icon{color:var(--cyan)}

.options{display:flex;justify-content:space-between;align-items:center;margin:16px 0 22px;font-size:12px}
.options label{display:flex;align-items:center;gap:8px;color:var(--t2);cursor:pointer}
.options label input[type="checkbox"]{accent-color:var(--cyan);width:16px;height:16px;cursor:pointer}

.btn-login{width:100%;padding:14px;border-radius:12px;border:none;cursor:pointer;background:linear-gradient(135deg,var(--cyan),var(--purple),var(--magenta));background-size:200% 200%;animation:gradientFlow 5s ease infinite;color:#000;font-family:inherit;font-size:15px;font-weight:800;transition:all .3s var(--transition);box-shadow:0 4px 30px rgba(0,240,255,0.3);position:relative;overflow:hidden}
.btn-login::before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.4),transparent);transform:translateX(-100%);transition:transform .6s}
.btn-login:hover{transform:translateY(-2px);box-shadow:0 8px 40px rgba(0,240,255,0.5),0 0 60px rgba(255,46,154,0.3)}
.btn-login:hover::before{transform:translateX(100%)}
.btn-login:disabled{opacity:.5;cursor:not-allowed;transform:none}
.default-pass-hint{margin-top:16px;text-align:center;font-size:13.5px;font-weight:800;color:#4d9fff;letter-spacing:.3px;text-shadow:0 0 18px rgba(77,159,255,.35)}
.default-pass-hint .key{direction:ltr;display:inline-block;padding:2px 12px;border:1px solid rgba(77,159,255,.4);border-radius:9px;background:rgba(77,159,255,.1);color:#8cc4ff;font-family:ui-monospace,Consolas,monospace;font-size:13.5px;box-shadow:0 0 16px rgba(77,159,255,.18)}
@keyframes gradientFlow{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}

.or-divider{display:flex;align-items:center;gap:14px;margin:22px 0;color:var(--t3);font-size:11px;letter-spacing:1px;text-transform:uppercase}
.or-divider::before,.or-divider::after{content:'';flex:1;height:1px;background:linear-gradient(90deg,transparent,var(--border-subtle),transparent)}

.connect-btn{width:100%;padding:12px;border-radius:12px;border:1px solid var(--border-subtle);background:rgba(255,255,255,0.02);color:var(--t1);font-family:inherit;font-size:13px;font-weight:700;cursor:pointer;transition:all .3s var(--transition);display:flex;align-items:center;justify-content:center;gap:8px}
.connect-btn:hover{background:rgba(0,240,255,0.06);border-color:var(--cyan);box-shadow:var(--glow-cyan)}

.error-box{display:none;background:rgba(255,77,109,0.08);border:1px solid rgba(255,77,109,0.25);border-radius:10px;padding:10px 14px;margin-bottom:14px;font-size:12px;color:var(--danger);align-items:center;gap:8px;animation:shake .4s}
.error-box.show{display:flex}
@keyframes shake{0%,100%{transform:translateX(0)}25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}

/* === پنل راست (اطلاعات) === */
.info-section{position:relative;background:linear-gradient(135deg,rgba(0,240,255,0.04),rgba(123,47,247,0.04),rgba(255,46,154,0.06));padding:52px 40px;display:flex;flex-direction:column;justify-content:center;border-right:1px solid var(--border-subtle);overflow:hidden}
.info-section::before{content:'';position:absolute;top:50%;left:50%;width:400px;height:400px;background:radial-gradient(circle,rgba(0,240,255,0.08),transparent 70%);transform:translate(-50%,-50%);animation:orbPulse 6s ease-in-out infinite;pointer-events:none}
@keyframes orbPulse{0%,100%{transform:translate(-50%,-50%) scale(1);opacity:0.6}50%{transform:translate(-50%,-50%) scale(1.2);opacity:0.9}}
.info-title{font-size:24px;font-weight:900;color:var(--t1);margin-bottom:8px;position:relative;z-index:1;background:linear-gradient(135deg,#fff,var(--cyan));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.info-sub{font-size:13px;color:var(--t2);margin-bottom:28px;position:relative;z-index:1;letter-spacing:0.5px}
.features{display:grid;grid-template-columns:1fr 1fr;gap:14px;position:relative;z-index:1}
.feature{background:rgba(255,255,255,0.03);backdrop-filter:blur(10px);border-radius:14px;padding:18px 14px;text-align:center;border:1px solid var(--border-subtle);transition:all .3s var(--transition);cursor:default}
.feature:hover{background:rgba(0,240,255,0.05);border-color:var(--cyan);transform:translateY(-3px);box-shadow:var(--glow-cyan)}
.feature .icon{font-size:32px;display:block;margin-bottom:8px;filter:drop-shadow(0 0 10px rgba(0,240,255,0.4))}
.feature .name{font-size:12px;font-weight:700;color:var(--t1);letter-spacing:0.3px}
.feature .desc{font-size:9px;color:var(--t3);margin-top:4px;letter-spacing:0.5px}

@media(max-width:900px){.container{grid-template-columns:1fr}.info-section{display:none}.login-section{padding:36px 28px}}
@media(max-width:480px){.login-section{padding:28px 20px}.welcome{font-size:21px}.brand-icon{width:46px;height:46px;font-size:22px}}

/* === ✦ ULTRA COSMIC: شفق قطبی === */
.aurora{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden;opacity:.9}
.aurora i{position:absolute;display:block;border-radius:50%;filter:blur(110px);mix-blend-mode:screen;will-change:transform,opacity}
.aurora .a1{width:900px;height:340px;top:-120px;right:-10%;background:linear-gradient(100deg,transparent,rgba(16,255,160,0.16),rgba(0,240,255,0.22),transparent);transform:rotate(-14deg);animation:auroraSweep 16s ease-in-out infinite}
.aurora .a2{width:800px;height:300px;top:6%;left:-15%;background:linear-gradient(80deg,transparent,rgba(123,47,247,0.2),rgba(0,240,255,0.14),transparent);transform:rotate(10deg);animation:auroraSweep 21s ease-in-out infinite reverse;animation-delay:-6s}
.aurora .a3{width:700px;height:260px;bottom:-80px;right:8%;background:linear-gradient(90deg,transparent,rgba(255,46,154,0.15),rgba(123,47,247,0.12),transparent);transform:rotate(-6deg);animation:auroraSweep 26s ease-in-out infinite;animation-delay:-12s}
@keyframes auroraSweep{0%,100%{transform:translateX(0) rotate(-12deg) scaleY(1);opacity:.55}33%{transform:translateX(-70px) rotate(-7deg) scaleY(1.35);opacity:.9}66%{transform:translateX(60px) rotate(-16deg) scaleY(.8);opacity:.45}}

/* === ✦ ULTRA COSMIC: لوگوی متحرک تخت جمشید === */
.brand-icon{overflow:visible}
.brand-icon svg{width:60%;height:60%;filter:drop-shadow(0 0 8px rgba(0,240,255,0.7))}
.brand-icon .pp-col{animation:ppColWave 2.6s ease-in-out infinite}
.brand-icon .pp-col.c2{animation-delay:.25s}
.brand-icon .pp-col.c3{animation-delay:.5s}
.brand-icon .pp-roof{animation:ppRoofGlow 3.2s ease-in-out infinite}
@keyframes ppColWave{0%,100%{opacity:.65;transform:translateY(0)}50%{opacity:1;transform:translateY(-1.5px)}}
@keyframes ppRoofGlow{0%,100%{filter:drop-shadow(0 0 3px rgba(0,240,255,0.6))}50%{filter:drop-shadow(0 0 10px rgba(255,46,154,0.9))}}

/* === ✦ مدال چرخان دور لوگو === */
.orbit-ring{position:absolute;inset:-8px;border-radius:18px;border:1px dashed rgba(0,240,255,0.35);animation:spinOrbit 14s linear infinite;pointer-events:none}
@keyframes spinOrbit{to{transform:rotate(360deg)}}
</style>
<style id="eagle-glass">
/* ═══ 🪄 EAGLE MINIMAL v3 — مینیمال، تم‌پذیر و سبک برای موبایل ═══ */
:root{--glass-brd:var(--border-subtle);--glass-hi:rgba(255,255,255,.06);--glass-bg:rgba(255,255,255,.035)}
/* 🎯 دکمه‌های مینیمال — هم‌راستا با هر تم */
.btn,.btn-login,.connect-btn,.app-btn{
  position:relative;overflow:hidden;
  background:rgba(255,255,255,.045)!important;
  backdrop-filter:blur(10px) saturate(140%)!important;-webkit-backdrop-filter:blur(10px) saturate(140%)!important;
  border:1px solid var(--border-strong)!important;border-radius:10px!important;color:var(--t1)!important;
  box-shadow:0 2px 10px rgba(0,0,0,.25)!important;
  transition:background .25s ease,border-color .25s ease,box-shadow .25s ease,filter .2s ease!important;
  font-weight:700;
}
.btn-p{background:linear-gradient(135deg,var(--cyan),var(--purple))!important;color:#0a0a12!important;border-color:transparent!important}
.btn-o{background:transparent!important}
.btn-pur{background:var(--cyan-soft)!important;border-color:var(--border-strong)!important;color:var(--cyan)!important}
.btn-d{background:var(--red-bg)!important;border-color:rgba(255,77,109,.35)!important;color:var(--red-t)!important}
.btn-amber{background:var(--amber-bg)!important;border-color:rgba(255,184,0,.35)!important;color:var(--amber-t)!important}
.btn:hover{filter:brightness(1.12);box-shadow:0 4px 16px rgba(0,0,0,.3)!important}
.btn:active{transform:scale(.97)}
.btn::after{display:none}
/* 🧊 کارت‌ها — تم‌پذیر و سبک */
.stat-card,.settings-card,.chart-section,.stat-info-card,.feature,.clock-widget,.srv-chip{
  background:var(--bg-card)!important;
  backdrop-filter:blur(12px) saturate(140%)!important;-webkit-backdrop-filter:blur(12px) saturate(140%)!important;
  border:1px solid var(--border-subtle)!important;border-radius:14px!important;
  box-shadow:0 4px 18px rgba(0,0,0,.3)!important;
}
.stat-card{transition:border-color .25s ease,box-shadow .25s ease!important}
.stat-card:hover{border-color:var(--border-glow)!important}
.stat-card .icon{display:inline-block;animation:emojiFloat 4.5s ease-in-out infinite}
@keyframes emojiFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-2.5px)}}
/* ⌨️ ورودی‌ها */
input,select,textarea{transition:border-color .25s,box-shadow .25s!important}
input:focus,select:focus,textarea:focus{border-color:var(--cyan)!important;box-shadow:0 0 0 3px var(--cyan-soft)!important}
/* 😀 ایموجی منوها */
.nav-it[data-pg="dashboard"] span::before{content:'🏠 '}
.nav-it[data-pg="users"] span::before{content:'👥 '}
.nav-it[data-pg="quota"] span::before{content:'📶 '}
.nav-it[data-pg="connections"] span::before{content:'🌐 '}
.nav-it[data-pg="settings"] span::before{content:'⚙️ '}
.nav-it[data-pg="logs"] span::before{content:'📜 '}
.nav-it[data-pg="backup"] span::before{content:'🗄️ '}
.bottom-nav .nav-item[data-pg="dashboard"] span::before{content:'🏠 '}
.bottom-nav .nav-item[data-pg="users"] span::before{content:'👥 '}
.bottom-nav .nav-item[data-pg="quota"] span::before{content:'📶 '}
.bottom-nav .nav-item[data-pg="settings"] span::before{content:'⚙️ '}
.tb-title::before{content:'✦ '}
/* 🌈 اسکرول‌بار */
::-webkit-scrollbar{width:8px;height:8px}
::-webkit-scrollbar-thumb{background:var(--border-strong);border-radius:8px}
::-webkit-scrollbar-track{background:rgba(255,255,255,.03)}
/* 🪟 مودال‌ها */
.modal{border:1px solid var(--border-strong)!important;box-shadow:0 30px 100px rgba(0,0,0,.65)!important}
/* 🟢 بج کاربر آنلاین */
.online-badge{display:inline-flex;align-items:center;gap:4px;font-size:9px;font-weight:800;padding:2px 7px;border-radius:20px;margin-right:6px;vertical-align:middle}
.online-badge.on{background:rgba(16,255,160,.12);color:var(--green-t);border:1px solid rgba(16,255,160,.3)}
.online-badge.off{background:rgba(255,255,255,.04);color:var(--t3);border:1px solid var(--border-subtle)}
.online-badge .odot{width:5px;height:5px;border-radius:50%;background:currentColor}
.online-badge.on .odot{animation:dotPulse 1.6s ease-in-out infinite}
/* 📊 نوارهای پیشرفت کوچک (مصرف امروز / ریکوئست CF) */
.mini-bar{height:5px;border-radius:4px;background:rgba(255,255,255,.06);overflow:hidden;margin-top:7px;border:1px solid var(--border-subtle)}
.mini-bar>div{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--cyan),var(--purple));transition:width .8s cubic-bezier(.34,1.56,.64,1)}
.mini-bar.warn>div{background:linear-gradient(90deg,#ffb800,#ff8800)}
.mini-bar.alert>div{background:linear-gradient(90deg,#ff4d6d,#ff2e2e)}
/* ⚠️ بنر هشدار تمام‌عرض */
.alert-banner{display:none;align-items:center;gap:10px;padding:12px 16px;border-radius:12px;margin-bottom:12px;font-size:12px;font-weight:800;animation:pulseAnim 2s infinite}
.alert-banner.show{display:flex}
.alert-banner.red{background:rgba(255,77,109,.12);border:1px solid rgba(255,77,109,.4);color:var(--red-t)}
.alert-banner.yellow{background:rgba(255,184,0,.1);border:1px solid rgba(255,184,0,.4);color:var(--amber-t)}
/* 📱 بهینه‌سازی موبایل: بدون لگ — افکت‌های سنگین خاموش */
@media(max-width:768px){
  #starfield-bg,#particle-canvas,.nebula-bg,.aurora,.grid-lines{display:none!important}
  .btn,.btn-login,.connect-btn,.app-btn{backdrop-filter:none!important;-webkit-backdrop-filter:none!important}
  .stat-card,.settings-card,.chart-section,.stat-info-card,.feature,.clock-widget,.srv-chip,.modal,.sidebar,.cmdk-box{
    backdrop-filter:none!important;-webkit-backdrop-filter:none!important;
    background:var(--bg-surface-2)!important;
  }
  .stat-card:hover,.btn:hover{transform:none!important}
  .stat-card .icon{animation:none!important}
  input,select,textarea{font-size:16px!important}
  .world-map-card,.speed-gauge-card{display:none!important}
}
@media(prefers-reduced-motion:reduce){
  *{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}
}
</style></head>
<body>
<canvas id="starfield"></canvas>
<div class="aurora"><i class="a1"></i><i class="a2"></i><i class="a3"></i></div>
<div class="nebula nebula-1"></div><div class="nebula nebula-2"></div><div class="nebula nebula-3"></div>
<div class="grid-lines"></div>

<div class="lang-toggle">
    <button class="active" onclick="setLang('fa')">🇮🇷 فارسی</button>
    <button onclick="setLang('en')">🇬🇧 English</button>
</div>

<div class="container">
    <div class="login-section">
        <div class="brand">
            <div class="brand-icon"><img class="logo-img" src="data:image/jpeg;base64,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" alt="P443"></div>
            <div>
                <div class="brand-text">PERSEPOLIS</div>
                <div class="brand-sub">COSMIC PANEL · v3.0 ULTRA</div>
            </div>
        </div>
        <div class="welcome" id="welcome-text">خوش آمدید</div>
        <div class="sub-text" id="sub-text">وارد پنل مدیریت شوید</div>
        <div class="error-box" id="error-box"><i class="ti ti-alert-circle"></i><span id="error-text"></span></div>
        <form id="login-form" onsubmit="handleLogin(event)">
            <div class="field">
                <label id="label-username">نام کاربری</label>
                <input type="text" id="username" placeholder="admin" value="admin" dir="ltr">
                <i class="ti ti-user input-icon"></i>
            </div>
            <div class="field">
                <label id="label-password">رمز عبور</label>
                <input type="password" id="password" placeholder="••••••••" dir="ltr">
                <i class="ti ti-lock input-icon"></i>
            </div>
            <div class="options"><label><input type="checkbox" id="remember"> <span id="remember-text">مرا به خاطر بسپار</span></label></div>
            <button class="btn-login" type="submit" id="login-btn"><i class="ti ti-login-2"></i> <span id="login-text">ورود</span></button>
        </form>
        ⟦default_pass_hint⟧
    </div>
    <div class="info-section">
        <div class="info-logo-wrap"><img class="info-logo" src="data:image/jpeg;base64,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P19iMlvVLZnR5yzRlFVz/wCVDtxBXVMOBKOvrPXjR85LR9I31LtCdGOrgjO58BBGiYnoDs+s9SxOiZ7EsaZYjr/6RTSW3pl9ZDp554GWx2PnLcMuHgJ3m+pl9qI51/8AgW8s6jOolvL/APb/AP/aAAwDAQACAAMAAAAQ88888888488888888888888884zEiIk3qw08888888882/SpmDVYCl7y8888888uH+1CGRg0m6OiT888884Zw2rqQkvfsnkHde8888jzNbDFKyZn9gvQOZ088wyPF80v1RpFfrOHuy288ZcQdSB/eaiM8Hy8fiS84UTDxPaEon/1NmAqwPg0of1P4RkreeIKLYMxlj88s3hMlGG/HRrLlAK5OLVc4YOCo/BoBMCSZDmHRnLU8j5AgoKM/pdCce4o89c88wBN5q9wMNOEglSp0zu88oazwQaPjshmY6prE08888oQsJs1gJSK6XZT0u888888BuU0dqQiem6f288888888BiQNxAd1V/M8888888888sm5929mEc8888888888888888888888888/8QAKREBAAICAQEHBAMBAAAAAAAAAQARITFBECBRYXGBkdEwobHwQOHxwf/aAAgBAwEBPxD+VcQbnghfdK6Kfq72X4f5+JRKcy5fQZDkxFGfpMvP+IOT/cK4h9qfKpxQhV/8/wAjczWQZWwsorts99+JoZbCAJCZZXvhRgGy8TRQSosllrUSAe+Fkc9qp4znbjEZ2eYGgjLkuKQzIm5a4dRjsNzzCG6rcNM7gMxqCnsm3u/f31gLuGiqmuSriS5RAmzUJhzGoLlcpDO4ZYh2xF4m/J2FRcqhby1W15kp2PeXNA+sxBL1MPEqPhAlI4iSxdRwICww5msdXohqUvg1ErlWbal+f9QcRTjEUtjft+1BxbLdRjKQMQQoYjZCCwqlLk9pbBqNkm19XNOij1EuAwZ+IUZZZnGT5/1LV5x6H79o6olZBQRf/wBEQPc+JWptgWhEWrJVhLzcdHXT0sIXKVZ+CAqK4u2CAB0EUYIryz1+A2VEqtszBxKdxNMsmZdLJWOrKrQqXmGATkqVFpQQQbGWu7lWbiMEKMczmQqtZmpLODvsKSUA6GEaisvuSot3zUKZSUSiUiOB2ny+kd1xFfYu2zQwGXK3UG4AtYghVzmoIljGmJhCGXlBGITa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" alt="P443"></div>
        <div class="info-title" id="info-title">✦ Persepolis</div>
        <div class="info-sub" id="info-sub">سریع‌ترین و امن‌ترین اتصال کیهانی</div>
        <div class="features">
            <div class="feature"><span class="icon">🛡️</span><div class="name" id="f-secure">امن</div><div class="desc" id="f-secure-d">حریم خصوصی شما</div></div>
            <div class="feature"><span class="icon">⚡</span><div class="name" id="f-fast">سریع</div><div class="desc" id="f-fast-d">سرعت برق آسا</div></div>
            <div class="feature"><span class="icon">🌍</span><div class="name" id="f-global">جهانی</div><div class="desc" id="f-global-d">سرورهای جهانی</div></div>
            <div class="feature"><span class="icon">🛰️</span><div class="name" id="f-anon">ناشناس</div><div class="desc" id="f-anon-d">خصوصی بمانید</div></div>
        </div>
    </div>
</div>

<script>
// === ✦ ULTRA COSMIC: ستاره‌های پارالاکس + شهاب‌سنگ (Canvas) ===
const canvas = document.getElementById('starfield');
const ctx = canvas.getContext('2d');
let stars = [], meteors = [], mouse = {x: 0.5, y: 0.5};
function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    stars = [];
    const count = Math.floor((canvas.width * canvas.height) / 6000);
    for (let i = 0; i < count; i++) {
        stars.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            r: Math.random() * 1.6 + 0.3,
            o: Math.random() * 0.8 + 0.2,
            s: Math.random() * 0.05 + 0.01,
            tw: Math.random() * Math.PI * 2,
            depth: Math.random(),
            color: Math.random() > 0.85 ? '#00f0ff' : (Math.random() > 0.7 ? '#ff2e9a' : '#ffffff')
        });
    }
}
function spawnMeteor() {
    const sx = Math.random() * canvas.width * 0.8 + canvas.width * 0.1;
    meteors.push({
        x: sx, y: -30,
        vx: -(Math.random() * 6 + 4),
        vy: Math.random() * 4 + 4,
        len: Math.random() * 90 + 60,
        life: 1, hue: Math.random() > 0.5 ? '#00f0ff' : '#ff2e9a'
    });
}
function drawStars() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const px = (mouse.x - 0.5), py = (mouse.y - 0.5);
    stars.forEach(s => {
        s.tw += 0.02;
        const op = s.o * (0.5 + 0.5 * Math.sin(s.tw));
        const ox = px * 26 * s.depth, oy = py * 18 * s.depth;
        ctx.beginPath();
        ctx.arc(s.x + ox, s.y + oy, s.r, 0, Math.PI * 2);
        ctx.fillStyle = s.color;
        ctx.globalAlpha = op;
        ctx.shadowBlur = 8 + s.depth * 6;
        ctx.shadowColor = s.color;
        ctx.fill();
    });
    // شهاب‌سنگ‌ها
    if (Math.random() < 0.012 && meteors.length < 4) spawnMeteor();
    for (let i = meteors.length - 1; i >= 0; i--) {
        const m = meteors[i];
        m.x += m.vx; m.y += m.vy; m.life -= 0.008;
        if (m.life <= 0 || m.y > canvas.height + 100) { meteors.splice(i, 1); continue; }
        const grad = ctx.createLinearGradient(m.x, m.y, m.x - m.vx * (m.len / 8), m.y - m.vy * (m.len / 8));
        grad.addColorStop(0, m.hue);
        grad.addColorStop(1, 'transparent');
        ctx.strokeStyle = grad;
        ctx.lineWidth = 2.2;
        ctx.globalAlpha = Math.min(m.life, 1);
        ctx.shadowBlur = 14;
        ctx.shadowColor = m.hue;
        ctx.beginPath();
        ctx.moveTo(m.x, m.y);
        ctx.lineTo(m.x - m.vx * (m.len / 8), m.y - m.vy * (m.len / 8));
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(m.x, m.y, 2.4, 0, Math.PI * 2);
        ctx.fillStyle = '#fff';
        ctx.fill();
    }
    ctx.globalAlpha = 1;
    ctx.shadowBlur = 0;
    requestAnimationFrame(drawStars);
}
window.addEventListener('resize', resizeCanvas);
window.addEventListener('mousemove', e => { mouse.x = e.clientX / window.innerWidth; mouse.y = e.clientY / window.innerHeight; });
resizeCanvas();
drawStars();

// === ✦ ULTRA COSMIC: موتور جلوه صوتی (WebAudio — بدون فایل خارجی) ===
const SFX = {
    ac: null, enabled: localStorage.getItem('pp-sfx') !== 'off',
    ensure() {
        if (!this.ac) { try { this.ac = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) { return false; } }
        if (this.ac && this.ac.state === 'suspended') this.ac.resume();
        return !!this.ac;
    },
    tone(f1, f2, dur, type, vol, delay) {
        if (!this.enabled || !this.ensure()) return;
        const t0 = this.ac.currentTime + (delay || 0);
        const o = this.ac.createOscillator(), g = this.ac.createGain();
        o.type = type || 'sine';
        o.frequency.setValueAtTime(f1, t0);
        if (f2) o.frequency.exponentialRampToValueAtTime(f2, t0 + dur);
        g.gain.setValueAtTime(0.0001, t0);
        g.gain.exponentialRampToValueAtTime(vol || 0.06, t0 + 0.015);
        g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
        o.connect(g); g.connect(this.ac.destination);
        o.start(t0); o.stop(t0 + dur + 0.05);
    },
    click() { this.tone(520, 760, 0.08, 'triangle', 0.05); },
    success() { this.tone(523, 0, 0.1, 'sine', 0.06); this.tone(659, 0, 0.1, 'sine', 0.06, 0.09); this.tone(784, 1046, 0.18, 'sine', 0.07, 0.18); },
    error() { this.tone(220, 110, 0.25, 'sawtooth', 0.05); },
    warp() { this.tone(180, 1200, 0.5, 'sawtooth', 0.045); this.tone(90, 600, 0.55, 'sine', 0.05, 0.05); },
    pop() { this.tone(900, 1400, 0.09, 'sine', 0.05); }
};
document.addEventListener('click', e => { if (e.target.closest('button, .btn, .feature, label')) SFX.click(); }, true);

// === ترجمه‌ها ===
const translations={
fa:{
welcome:"خوش آمدید به کیهان",
sub:"وارد پنل مدیریت شوید",
username:"نام کاربری",
password:"رمز عبور",
remember:"مرا به خاطر بسپار",
login:"ورود به پنل",


secure:"امن",
secure_d:"حریم خصوصی شما",
fast:"سریع",
fast_d:"سرعت برق آسا",
global:"جهانی",
global_d:"سرورهای جهانی",
anon:"ناشناس",
anon_d:"خصوصی بمانید",
info_title:"✦ Persepolis",
info_sub:"سریع‌ترین و امن‌ترین اتصال کیهانی"
},
en:{
welcome:"Welcome to the Cosmos",
sub:"Login to the panel",
username:"Username",
password:"Password",
remember:"Remember me",
login:"Enter Panel",
or:"OR",
connect:"Quick Login",
secure:"Secure",
secure_d:"Your Privacy",
fast:"Fast",
fast_d:"Lightning Speed",
global:"Global",
global_d:"Worldwide Servers",
anon:"Anonymous",
anon_d:"Stay Private",
info_title:"✦ Persepolis",
info_sub:"Fastest & Most Secure Connection"
}};

let currentLang=localStorage.getItem('persepolis-lang')||'fa';
// ⚡ رمز/یوزرنیم ادمین دیگر در صفحه لاگین جاسوز نمی‌شود (دکمه‌ی لاگین سریع حذف شد)

function setLang(lang){
  currentLang=lang;
  localStorage.setItem('persepolis-lang',lang);
  document.querySelectorAll('.lang-toggle button').forEach(b=>b.classList.toggle('active',b.textContent.includes(lang==='fa'?'فارسی':'English')));
  updateTexts();
}
function updateTexts(){
  const t=translations[currentLang];
  document.getElementById('welcome-text').textContent=t.welcome;
  document.getElementById('sub-text').textContent=t.sub;
  document.getElementById('label-username').textContent=t.username;
  document.getElementById('label-password').textContent=t.password;
  document.getElementById('remember-text').textContent=t.remember;
  document.getElementById('login-text').textContent=t.login;
  document.getElementById('f-secure').textContent=t.secure;
  document.getElementById('f-secure-d').textContent=t.secure_d;
  document.getElementById('f-fast').textContent=t.fast;
  document.getElementById('f-fast-d').textContent=t.fast_d;
  document.getElementById('f-global').textContent=t.global;
  document.getElementById('f-global-d').textContent=t.global_d;
  document.getElementById('f-anon').textContent=t.anon;
  document.getElementById('f-anon-d').textContent=t.anon_d;
  document.getElementById('info-title').textContent=t.info_title;
  document.getElementById('info-sub').textContent=t.info_sub;
}

async function handleLogin(e){
  e.preventDefault();
  const btn=document.getElementById('login-btn');
  const err=document.getElementById('error-box');
  const errText=document.getElementById('error-text');
  err.classList.remove('show');
  btn.disabled=true;
  btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> '+ (currentLang==='fa'?'در حال ورود...':'Loading...');

  try{
    const username=document.getElementById('username').value;
    const password=document.getElementById('password').value;
    const remember=document.getElementById('remember').checked;

    const r=await fetch('/api/login',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({username,password,remember})
    });

    if(!r.ok){
      const d=await r.json().catch(()=>({}));
      errText.textContent=d.detail||(currentLang==='fa'?'یوزرنیم یا رمز عبور اشتباه است':'Wrong username or password');
      err.classList.add('show');
      btn.disabled=false;
      btn.innerHTML='<i class="ti ti-login-2"></i> '+translations[currentLang].login;
      SFX.error();
      return;
    }
    // انیمیشن خروج + صدای وارپ کیهانی
    SFX.warp();
    document.querySelector('.container').style.animation='cardOut .5s ease forwards';
    setTimeout(()=>{window.location.href='/dashboard';},400);
  }catch(e){
    errText.textContent=currentLang==='fa'?'خطا در ارتباط با سرور':'Connection error';
    err.classList.add('show');
    btn.disabled=false;
    btn.innerHTML='<i class="ti ti-login-2"></i> '+translations[currentLang].login;
    SFX.error();
  }
}

function quickConnect(){} /* removed */

document.getElementById('password').addEventListener('keydown',(e)=>{if(e.key==='Enter')document.getElementById('login-form').dispatchEvent(new Event('submit'))});
document.getElementById('username').addEventListener('keydown',(e)=>{if(e.key==='Enter')document.getElementById('login-form').dispatchEvent(new Event('submit'))});

// === افزودن استایل انیمیشن خروج ===
const styleOut=document.createElement('style');
styleOut.textContent='@keyframes cardOut{to{opacity:0;transform:scale(0.92) translateY(-20px)}}@keyframes spin{to{transform:rotate(360deg)}}';
document.head.appendChild(styleOut);

// === ✦ اعمال تم ذخیره‌شده (اوبسیدین/کیهانی/زنبوری) ===
try{const th=localStorage.getItem('persepolis-theme')||'obsidian';document.body.dataset.theme=(th==='light'?'white':th);}catch(e){}

setLang(currentLang);
</script>
</body></html>
"""

DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>✦ PERSEPOLIS · کیهان ULTRA</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/qrcodejs@1.0.0/qrcode.min.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css">
<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>
<script src="https://cdn.jsdelivr.net/npm/flatpickr/dist/plugins/rangePlugin.js"></script>
<script src="https://cdn.jsdelivr.net/npm/flatpickr@4.6.13/dist/l10n/fa.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg-deep:#030418;
  --bg-mid:#0a0e2a;
  --bg-surface:rgba(10,14,35,0.55);
  --bg-surface-2:rgba(15,20,45,0.75);
  --bg-card:rgba(10,14,35,0.6);
  --bg-card-hover:rgba(15,20,45,0.75);
  --border-subtle:rgba(100,200,255,0.08);
  --border-glow:rgba(0,240,255,0.25);
  --border-strong:rgba(0,240,255,0.4);
  --cyan:#00f0ff;
  --cyan-soft:rgba(0,240,255,0.1);
  --magenta:#ff2e9a;
  --magenta-soft:rgba(255,46,154,0.1);
  --purple:#7b2ff7;
  --purple-soft:rgba(123,47,247,0.1);
  --gold:#D4A843;
  --gold2:#F5D060;
  --green:#10ffa0;
  --green-bg:rgba(16,255,160,0.08);
  --green-t:#10ffa0;
  --red:#ff4d6d;
  --red-bg:rgba(255,77,109,0.08);
  --red-t:#ff6b8a;
  --amber:#ffb800;
  --amber-bg:rgba(255,184,0,0.08);
  --amber-t:#ffcc4d;
  --t1:#e8efff;
  --t2:#94a3b8;
  --t3:#64748b;
  --sidebar-w:200px;
  --radius:14px;
  --shadow:0 8px 32px rgba(0,0,0,0.5),0 0 60px rgba(0,240,255,0.03);
  --glow-cyan:0 0 30px rgba(0,240,255,0.2);
  --transition:cubic-bezier(0.34,1.56,0.64,1)
}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg-deep);color:var(--t1);min-height:100vh;display:flex;font-size:13px;position:relative;overflow-x:hidden;transition:background .4s,color .4s}

/* === ✦ تم‌های پنل: اوبسیدین (مشکی، پیش‌فرض) / کیهانی / زنبوری (زرد-مشکی) === */
body[data-theme="obsidian"]{
  --bg-deep:#050507;--bg-mid:#0b0b10;
  --bg-surface:rgba(13,13,17,0.72);--bg-surface-2:rgba(17,17,22,0.88);--bg-card:rgba(19,19,25,0.62);--bg-card-hover:rgba(24,24,31,0.8);
  --border-subtle:rgba(255,255,255,0.075);--border-glow:rgba(159,176,255,0.22);--border-strong:rgba(159,176,255,0.4);
  --cyan:#9fb0ff;--cyan-soft:rgba(159,176,255,0.1);
  --magenta:#f0abfc;--magenta-soft:rgba(240,171,252,0.08);
  --purple:#c4b5fd;--purple-soft:rgba(196,181,253,0.08);
  --t1:#f2f4ff;--t2:#a2a8bd;--t3:#5d6375;
  --shadow:0 8px 32px rgba(0,0,0,0.65);--glow-cyan:0 0 24px rgba(159,176,255,0.14);
  background:radial-gradient(ellipse at top,#0c0c12 0%,#050507 55%,#010102 100%);
}
body[data-theme="obsidian"] #starfield-bg{opacity:.55}
body[data-theme="obsidian"] .grid-lines{opacity:.05}
body[data-theme="bumblebee"]{
  --bg-deep:#0a0803;--bg-mid:#141004;
  --bg-surface:rgba(26,21,8,0.72);--bg-surface-2:rgba(30,24,9,0.88);--bg-card:rgba(32,26,10,0.62);--bg-card-hover:rgba(40,32,12,0.8);
  --border-subtle:rgba(255,214,10,0.11);--border-glow:rgba(255,214,10,0.25);--border-strong:rgba(255,214,10,0.42);
  --cyan:#ffd60a;--cyan-soft:rgba(255,214,10,0.1);
  --magenta:#ffea00;--magenta-soft:rgba(255,234,0,0.07);
  --purple:#ffc300;--purple-soft:rgba(255,195,0,0.08);
  --t1:#fff9e0;--t2:#c9bd96;--t3:#8a8062;
  --shadow:0 8px 32px rgba(0,0,0,0.6);--glow-cyan:0 0 24px rgba(255,214,10,0.14);
  background:radial-gradient(ellipse at top,#161104 0%,#0a0803 55%,#050401 100%);
}
body[data-theme="bumblebee"] .grid-lines{opacity:.06}
body[data-theme="white"]{--bg-surface:rgba(255,255,255,0.82);--bg-surface-2:rgba(255,255,255,0.94);--bg-card:rgba(255,255,255,0.88);--bg-card-hover:rgba(255,255,255,0.98);--border-subtle:rgba(15,30,70,0.12);--border-strong:rgba(15,30,70,0.24);--border-glow:rgba(11,108,224,0.3);--border-glow-strong:rgba(11,108,224,0.5);--cyan:#0b6ce0;--cyan-soft:rgba(11,108,224,0.1);--magenta:#d6336c;--magenta-soft:rgba(214,51,108,0.08);--purple:#7048e8;--purple-soft:rgba(112,72,232,0.08);--t1:#131a2b;--t2:#43506b;--t3:#7c89a3;--glow-cyan:none;--glow-magenta:none;--shadow-deep:0 20px 60px rgba(30,50,100,0.14);background:linear-gradient(160deg,#f6f8fc 0%,#e9eef7 55%,#dfe7f3 100%)!important}
body[data-theme="white"] .grid-lines{background-image:linear-gradient(rgba(20,50,120,0.16) 1px,transparent 1px),linear-gradient(90deg,rgba(20,50,120,0.16) 1px,transparent 1px);opacity:.25}
body[data-theme="white"] .fi,body[data-theme="white"] .settings-card .field input{background:rgba(255,255,255,0.92);border-color:rgba(15,30,70,0.16);color:#131a2b}
body[data-theme="white"] .stat-card .number,body[data-theme="white"] .logo-name{background:linear-gradient(135deg,#0f1729,#0b6ce0);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
body[data-theme="white"] #starfield-bg,body[data-theme="white"] .aurora-bg,body[data-theme="white"] .nebula-bg{opacity:.08}

/* === ستاره‌های متحرک === */
#starfield-bg{position:fixed;inset:0;z-index:0;pointer-events:none}

/* === سحابی‌ها === */
.nebula-bg{position:fixed;border-radius:50%;filter:blur(140px);z-index:0;pointer-events:none;animation:nebulaFloat 16s ease-in-out infinite}
.nebula-bg-1{width:500px;height:500px;background:radial-gradient(circle,rgba(0,240,255,0.06),transparent 70%);top:-200px;left:-150px}
.nebula-bg-2{width:400px;height:400px;background:radial-gradient(circle,rgba(255,46,154,0.05),transparent 70%);bottom:-150px;right:-100px;animation-delay:-8s}
@keyframes nebulaFloat{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(40px,-30px) scale(1.1)}}

/* === ساید بار === */
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--bg-surface);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border-left:1px solid var(--border-subtle);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .4s var(--transition),background .4s;box-shadow:var(--shadow)}
.logo{display:flex;align-items:center;gap:12px;padding:20px 16px 16px;border-bottom:1px solid var(--border-subtle);position:relative}
.logo-icon{width:42px;height:42px;border-radius:12px;background:linear-gradient(135deg,var(--cyan),var(--purple),var(--magenta));display:flex;align-items:center;justify-content:center;font-size:20px;flex-shrink:0;box-shadow:0 0 30px rgba(0,240,255,0.3);animation:logoPulse 4s ease-in-out infinite}
@keyframes logoPulse{0%,100%{box-shadow:0 0 30px rgba(0,240,255,0.3)}50%{box-shadow:0 0 50px rgba(255,46,154,0.4)}}
.logo-name{font-size:14px;font-weight:900;background:linear-gradient(135deg,#fff,var(--cyan));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;letter-spacing:0.5px}
.logo-sub{font-size:8px;color:var(--t3);letter-spacing:1.5px;text-transform:uppercase}
.nav-wrap{flex:1;overflow-y:auto;padding:10px 0;position:relative;z-index:1}
.nav-wrap::-webkit-scrollbar{width:4px}
.nav-wrap::-webkit-scrollbar-track{background:transparent}
.nav-wrap::-webkit-scrollbar-thumb{background:var(--cyan-soft);border-radius:4px}
.nav-it{display:flex;align-items:center;gap:10px;padding:10px 12px;color:var(--t3);font-size:12px;cursor:pointer;border-right:2px solid transparent;transition:all .3s var(--transition);margin:2px 6px;border-radius:10px;position:relative;overflow:hidden}
.nav-it i{font-size:16px;width:20px;text-align:center;flex-shrink:0;transition:transform .3s}
.nav-it:hover{background:rgba(0,240,255,0.04);color:var(--t1)}
.nav-it:hover i{transform:scale(1.15);color:var(--cyan)}
.nav-it.on{background:linear-gradient(90deg,rgba(0,240,255,0.12),rgba(0,240,255,0.02));color:var(--cyan);border-right-color:var(--cyan);font-weight:700;box-shadow:inset 0 0 20px rgba(0,240,255,0.05)}
.nav-it.on i{color:var(--cyan);filter:drop-shadow(0 0 8px var(--cyan))}
.nav-it.on::before{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--cyan);box-shadow:0 0 10px var(--cyan)}
.sb-foot{padding:12px 14px;border-top:1px solid var(--border-subtle)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:6px;background:var(--red-bg);color:var(--red-t);border-radius:10px;padding:8px;font-size:11px;font-weight:600;font-family:inherit;border:1px solid rgba(255,77,109,0.15);cursor:pointer;width:100%;transition:all .3s var(--transition)}
.logout-btn:hover{background:rgba(255,77,109,0.15);transform:scale(1.03);box-shadow:0 0 20px rgba(255,77,109,0.3)}

/* === موبایل تاپ === */
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:54px;background:var(--bg-surface);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border-bottom:1px solid var(--border-subtle);z-index:150;align-items:center;justify-content:space-between;padding:0 12px;transition:background .4s}
.mob-top .ml{display:flex;align-items:center;gap:8px}
.mob-logo{width:30px;height:30px;border-radius:8px;background:linear-gradient(135deg,var(--cyan),var(--purple));display:flex;align-items:center;justify-content:center;font-size:14px;box-shadow:var(--glow-cyan)}
.mob-title{color:var(--t1);font-size:12px;font-weight:800;background:linear-gradient(135deg,#fff,var(--cyan));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.menu-btn{background:rgba(0,240,255,0.05);border:1px solid var(--border-subtle);color:var(--cyan);width:34px;height:34px;border-radius:10px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .3s var(--transition)}
.menu-btn:hover{background:rgba(0,240,255,0.1);transform:scale(1.05)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.7);z-index:190;backdrop-filter:blur(8px)}
.overlay.show{display:block}

/* === بخش اصلی === */
.main{margin-right:var(--sidebar-w);flex:1;padding:20px 24px 80px;min-width:0;transition:margin .4s;position:relative;z-index:1}
.topbar{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;padding:18px 22px;background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);position:relative;overflow:hidden}
.topbar::before{content:'';position:absolute;top:-30px;right:-30px;width:200px;height:200px;background:radial-gradient(circle,rgba(0,240,255,0.05),transparent 70%);pointer-events:none}
.tb-title{font-size:16px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}
.tb-title i{color:var(--cyan);filter:drop-shadow(0 0 6px var(--cyan))}
.tb-sub{font-size:10px;color:var(--t3);margin-top:2px;letter-spacing:0.5px}
.tb-right{display:flex;align-items:center;gap:8px}

.badge{display:inline-flex;align-items:center;gap:5px;padding:5px 12px;border-radius:20px;font-size:10px;font-weight:700;letter-spacing:0.3px}
.bg-fire{background:rgba(255,46,154,0.1);border:1px solid rgba(255,46,154,0.2);color:var(--magenta);box-shadow:0 0 15px rgba(255,46,154,0.15)}
.bg-green{background:var(--green-bg);border:1px solid rgba(16,255,160,0.2);color:var(--green-t)}
.dot{width:6px;height:6px;border-radius:50%;display:inline-block}
.dg{background:var(--green);animation:dotPulse 1.5s ease-in-out infinite;box-shadow:0 0 8px var(--green)}
.dr{background:var(--red);animation:dotPulse 1.8s ease-in-out infinite;box-shadow:0 0 8px var(--red)}
.da{background:var(--amber);animation:dotPulse 2s ease-in-out infinite;box-shadow:0 0 8px var(--amber)}
.db{background:var(--cyan);animation:dotPulse 1.2s ease-in-out infinite;box-shadow:0 0 8px var(--cyan)}
@keyframes dotPulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.3;transform:scale(0.7)}}
.pulse{animation:pulseAnim 2s infinite}
@keyframes pulseAnim{0%,100%{opacity:1}50%{opacity:.25}}

/* === کارت‌های آماری === */
.stats-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-bottom:6px}
.stat-card{background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:16px 10px;transition:all .4s var(--transition);text-align:center;position:relative;overflow:hidden;cursor:default}
.stat-card::before{content:'';position:absolute;top:-50%;right:-50%;width:150px;height:150px;background:radial-gradient(circle,rgba(0,240,255,0.06),transparent 70%);pointer-events:none;transition:transform .5s}
.stat-card::after{content:'';position:absolute;inset:0;background:linear-gradient(135deg,transparent,rgba(0,240,255,0.03),transparent);opacity:0;transition:opacity .3s}
.stat-card:hover{border-color:var(--border-strong);transform:translateY(-4px) scale(1.02);box-shadow:0 8px 30px rgba(0,240,255,0.15)}
.stat-card:hover::before{transform:scale(1.5)}
.stat-card:hover::after{opacity:1}
.stat-card .icon{font-size:22px;margin-bottom:6px;display:block;filter:drop-shadow(0 0 8px rgba(0,240,255,0.4))}
.stat-card .number{font-size:20px;font-weight:900;color:var(--t1);line-height:1.2;background:linear-gradient(135deg,#fff,rgba(0,240,255,0.8));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.stat-card .number.small{font-size:14px}
.stat-card .label{font-size:10px;color:var(--t3);margin-top:4px;font-weight:600;letter-spacing:0.3px}
.stat-card .sub{font-size:8px;color:var(--t3);margin-top:2px;opacity:.7}

/* === نمودار === */
.chart-section{background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:18px;margin:14px 0;transition:all .3s;position:relative;overflow:hidden}
.chart-section::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,var(--cyan),transparent);opacity:0.5}
.chart-section .chart-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px}
.chart-section .chart-title{font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px}
.chart-section .chart-title i{color:var(--cyan);filter:drop-shadow(0 0 6px var(--cyan))}
.chart-section .chart-sub{font-size:10px;color:var(--t3);letter-spacing:0.5px}
.chart-section .chart-actions{display:flex;gap:6px;flex-wrap:wrap}

.stat-mini{background:var(--bg-card);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid var(--border-subtle);border-radius:10px;padding:10px 14px;display:flex;align-items:center;gap:10px;transition:all .3s var(--transition)}
.stat-mini:hover{transform:translateY(-2px);border-color:var(--border-strong);box-shadow:0 4px 20px rgba(0,240,255,0.1)}
.stat-mini-icon{font-size:18px;filter:drop-shadow(0 0 6px rgba(0,240,255,0.3))}
.stat-mini-num{font-size:18px;font-weight:900;color:var(--t1)}
.stat-mini-label{font-size:10px;color:var(--t3);letter-spacing:0.3px}

/* === جدول کاربران === */
.users-table{width:100%;border-collapse:collapse;font-size:12px}
.users-table thead th{padding:12px 14px;text-align:right;color:var(--cyan);font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:0.5px;border-bottom:1px solid var(--border-strong);background:rgba(0,240,255,0.03)}
.users-table tbody td{padding:10px 14px;border-bottom:1px solid var(--border-subtle);color:var(--t1);vertical-align:middle}
.users-table tbody tr{transition:all .3s var(--transition)}
.users-table tbody tr:hover{background:rgba(0,240,255,0.03)}
.users-table tbody tr:hover .user-name-cell .avatar{transform:scale(1.1) rotate(-5deg)}
.users-table .status-badge{display:inline-flex;align-items:center;gap:5px;padding:3px 12px;border-radius:14px;font-size:10px;font-weight:700}
.users-table .status-badge .status-dot{width:6px;height:6px;border-radius:50%;display:inline-block;animation:statusPulse 1.5s ease-in-out infinite}
.users-table .status-badge.active .status-dot{background:var(--green-t);box-shadow:0 0 6px var(--green-t)}
.users-table .status-badge.expired .status-dot{background:var(--red-t);box-shadow:0 0 6px var(--red-t)}
.users-table .status-badge.disabled .status-dot{background:var(--amber-t);box-shadow:0 0 6px var(--amber-t)}
@keyframes statusPulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.3;transform:scale(0.6)}}
.users-table .status-badge.active{background:var(--green-bg);color:var(--green-t);border:1px solid rgba(16,255,160,0.2)}
.users-table .status-badge.expired{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(255,77,109,0.2)}
.users-table .status-badge.disabled{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(255,184,0,0.2)}
.users-table .usage-bar{display:flex;align-items:center;gap:8px}
.users-table .usage-bar .bar{width:80px;height:4px;border-radius:4px;background:rgba(0,240,255,0.05);overflow:hidden;position:relative}
.users-table .usage-bar .bar .fill{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--cyan),var(--magenta),var(--purple));transition:width .8s var(--transition);box-shadow:0 0 8px var(--cyan)}
.users-table .usage-text{font-size:9px;color:var(--t2);white-space:nowrap;font-family:monospace}
.users-table .action-btns{display:flex;gap:4px;justify-content:center;flex-wrap:wrap}
.users-table .action-btns .btn{padding:3px 7px;font-size:9px;border-radius:6px}
.user-name-cell{display:flex;align-items:center;gap:8px}
.user-name-cell .avatar{width:28px;height:28px;border-radius:8px;background:linear-gradient(135deg,var(--cyan),var(--purple));display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:800;color:#000;flex-shrink:0;transition:transform .3s var(--transition);box-shadow:0 0 12px rgba(0,240,255,0.3)}
.user-name-cell .name{font-weight:700;color:var(--t1);font-size:12px}
.user-name-cell .uuid-short{font-size:8px;color:var(--t3);font-family:monospace;letter-spacing:0.5px}

/* === دکمه‌ها === */
.btn{font-family:inherit;font-size:11px;font-weight:700;border-radius:8px;padding:6px 12px;cursor:pointer;display:inline-flex;align-items:center;gap:4px;border:none;transition:all .3s var(--transition);white-space:nowrap;letter-spacing:0.3px}
.btn i{font-size:12px;transition:transform .3s}
.btn:hover i{transform:scale(1.15)}
.btn-p{background:linear-gradient(135deg,var(--cyan),var(--purple),var(--magenta));background-size:200% 200%;animation:btnGradient 5s ease infinite;color:#000;box-shadow:0 3px 15px rgba(0,240,255,0.25)}
@keyframes btnGradient{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.btn-p:hover{transform:translateY(-2px);box-shadow:0 6px 25px rgba(0,240,255,0.4),0 0 40px rgba(255,46,154,0.2)}
.btn-o{background:rgba(255,255,255,0.02);border:1px solid var(--border-subtle);color:var(--t2)}
.btn-o:hover{background:rgba(0,240,255,0.05);border-color:var(--cyan);color:var(--cyan);transform:translateY(-1px)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(255,77,109,.2)}
.btn-d:hover{background:rgba(255,77,109,.15);transform:translateY(-1px);box-shadow:0 4px 15px rgba(255,77,109,0.3)}
.btn-pur{background:rgba(0,240,255,0.08);color:var(--cyan);border:1px solid rgba(0,240,255,.15)}
.btn-pur:hover{background:rgba(0,240,255,.15);transform:translateY(-1px);box-shadow:var(--glow-cyan)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(255,184,0,0.15)}
.btn-amber:hover{background:rgba(255,184,0,.15);transform:translateY(-1px)}
.btn-sm{padding:3px 8px;font-size:9px;border-radius:6px}
.btn-icon{width:24px;height:24px;padding:0;justify-content:center}
.btn-generate{background:rgba(0,240,255,0.08);color:var(--cyan);border:1px solid rgba(0,240,255,0.15);padding:6px 12px;flex-shrink:0}
.btn-generate:hover{background:rgba(0,240,255,0.15);transform:scale(1.05);box-shadow:var(--glow-cyan)}

/* === مودال‌ها === */
.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.8);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
.modal-bg.open{display:flex;animation:modalFade .3s ease}
@keyframes modalFade{from{opacity:0}to{opacity:1}}
.modal{background:var(--bg-surface-2);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border:1px solid var(--border-strong);border-radius:18px;padding:24px 22px;max-width:580px;width:calc(100% - 20px);max-height:90vh;overflow-y:auto;position:relative;animation:modalIn .4s var(--transition);box-shadow:0 30px 100px rgba(0,0,0,0.6),0 0 60px rgba(0,240,255,0.15)}
.modal::before{content:'';position:absolute;top:0;left:20px;right:20px;height:2px;background:linear-gradient(90deg,transparent,var(--cyan),var(--magenta),transparent);opacity:0.7}
@keyframes modalIn{from{opacity:0;transform:scale(0.92) translateY(20px)}to{opacity:1;transform:scale(1) translateY(0)}}
.modal-close{position:absolute;top:12px;left:12px;background:rgba(255,255,255,0.05);border:1px solid var(--border-subtle);color:var(--t2);width:28px;height:28px;border-radius:8px;font-size:14px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none;transition:all .3s var(--transition)}
.modal-close:hover{background:var(--red-bg);color:var(--red-t);transform:rotate(90deg);border-color:var(--red-t)}
.modal-title{font-size:16px;font-weight:800;color:var(--t1);margin-bottom:16px;display:flex;align-items:center;gap:8px;padding-bottom:14px;border-bottom:1px solid var(--border-subtle)}
.modal-title i{color:var(--cyan);font-size:18px;filter:drop-shadow(0 0 6px var(--cyan))}
.fg{display:flex;flex-direction:column;gap:4px;margin-bottom:10px}
.fg label{font-size:10px;color:var(--cyan);font-weight:700;text-transform:uppercase;letter-spacing:0.5px;display:flex;align-items:center;gap:4px}
.fg label i{font-size:11px}
.fi{width:100%;padding:8px 12px;border-radius:8px;border:1px solid var(--border-subtle);background:rgba(0,0,15,0.4);color:var(--t1);font-family:inherit;font-size:11px;outline:none;transition:all .3s var(--transition)}
.fi:focus{border-color:var(--cyan);box-shadow:0 0 0 3px rgba(0,240,255,0.08),0 0 20px rgba(0,240,255,0.1);background:rgba(0,240,255,0.03)}
.fi::placeholder{color:var(--t3)}
select.fi{appearance:none;cursor:pointer;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='%2300f0ff' stroke-width='3'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:left 12px center;padding-left:30px}
.fi-date{color:var(--t1);background:rgba(0,0,15,0.4);border:1px solid var(--border-subtle);border-radius:8px;padding:8px 12px;width:100%;font-family:inherit;font-size:11px;outline:none;transition:all .3s var(--transition);cursor:pointer}
.fi-date:focus{border-color:var(--cyan);box-shadow:0 0 0 3px rgba(0,240,255,0.08)}
.fi-date::placeholder{color:var(--t3)}
.fg-row{display:flex;gap:8px;align-items:center}
.fg-row .fg{flex:1}

/* === اتصالات === */
.conn-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px}
.conn-card{background:var(--bg-card);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid var(--border-subtle);border-radius:12px;padding:12px 14px;transition:all .3s var(--transition);position:relative;overflow:hidden}
.conn-card::before{content:'';position:absolute;top:0;left:0;width:100%;height:1px;background:linear-gradient(90deg,transparent,var(--cyan),transparent);opacity:0.5}
.conn-card:hover{border-color:var(--border-strong);transform:translateY(-3px);box-shadow:0 8px 30px rgba(0,240,255,0.15)}
.conn-card .ip{font-family:monospace;font-size:12px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px}
.conn-card .label{font-size:9px;color:var(--t3);margin-top:4px;letter-spacing:0.3px}
.conn-card .conn-info{display:flex;justify-content:space-between;margin-top:6px;font-size:9px;color:var(--t2);gap:4px;flex-wrap:wrap}
.conn-status-dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--green-t);animation:pulseAnim 1.5s infinite;margin-left:4px;box-shadow:0 0 8px var(--green-t)}

/* === تنظیمات === */
.settings-card{background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:18px 20px;max-width:500px;margin-bottom:12px;position:relative;overflow:hidden;transition:all .3s var(--transition)}
.settings-card:hover{border-color:var(--border-strong)}
.settings-card::before{content:'';position:absolute;top:-50%;right:-50%;width:200px;height:200px;background:radial-gradient(circle,rgba(0,240,255,0.04),transparent 70%);pointer-events:none}
.settings-card .title{font-size:14px;font-weight:800;color:var(--t1);margin-bottom:12px;display:flex;align-items:center;gap:8px}
.settings-card .title i{color:var(--cyan);filter:drop-shadow(0 0 6px var(--cyan))}
.settings-card .field{margin-bottom:10px}
.settings-card .field label{font-size:10px;color:var(--t3);display:block;margin-bottom:4px;font-weight:700}
.settings-card .field input{width:100%;padding:8px 12px;border-radius:8px;border:1px solid var(--border-subtle);background:rgba(0,0,15,0.4);color:var(--t1);font-family:inherit;font-size:11px;outline:none;transition:.3s var(--transition)}
.settings-card .field input:focus{border-color:var(--cyan);box-shadow:0 0 0 3px rgba(0,240,255,0.08)}
.settings-card .btn{width:100%;justify-content:center;margin-top:6px;font-size:12px;padding:8px}
.settings-card .toggle-row{display:flex;align-items:center;justify-content:space-between;padding:10px 0;border-bottom:1px solid var(--border-subtle)}
.settings-card .toggle-row .toggle-label{font-size:12px;color:var(--t2);display:flex;align-items:center;gap:6px}
/* ⚡ v10: کارت‌های تنظیمات بغل‌هم (گرید) — نه زیرهم */
#pg-settings.on{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:12px;align-items:start}
#pg-settings .topbar{grid-column:1/-1}
#pg-settings .settings-card{max-width:none;margin-bottom:0}
/* ⚡ v10: بهینه‌سازی کامل موبایل — حذف افکت‌های سنگین = بدون لگ */
@media(max-width:768px){
  #starfield-bg,.aurora-bg,.nebula-bg{display:none!important}
  .stat-card,.settings-card,.chart-section,.stat-info-card,.feature,.clock-widget,.srv-chip,.modal-bg,.user-card,.conn-card,.info-card{backdrop-filter:none!important;-webkit-backdrop-filter:none!important}
  .user-card,.conn-card,.feature,.stat-info-card{content-visibility:auto;contain-intrinsic-size:auto 140px}
  .stat-card:hover,.settings-card:hover,.chart-section:hover{transform:none}
  *{-webkit-tap-highlight-color:transparent}
  .btn,.nav-it,.switch,.modal-close{touch-action:manipulation}
}
.switch{position:relative;width:42px;height:22px;background:var(--t3);border-radius:11px;cursor:pointer;transition:all .4s var(--transition);flex-shrink:0}
.switch.on{background:linear-gradient(135deg,var(--cyan),var(--purple));box-shadow:0 0 12px rgba(0,240,255,0.4)}
.switch .slider{position:absolute;top:2px;right:2px;width:18px;height:18px;background:#fff;border-radius:50%;transition:all .4s var(--transition);box-shadow:0 2px 6px rgba(0,0,0,0.3)}
.switch.on .slider{right:22px}

/* === Toast === */
.toast{position:fixed;bottom:80px;left:50%;transform:translateX(-50%) translateY(50px);background:var(--bg-surface-2);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border:1px solid var(--border-strong);color:var(--t1);border-radius:12px;padding:10px 18px;font-size:12px;opacity:0;transition:all .4s var(--transition);z-index:999;pointer-events:none;box-shadow:0 8px 30px rgba(0,0,0,0.5),0 0 30px rgba(0,240,255,0.1);display:flex;align-items:center;gap:6px;font-weight:600}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,255,160,.3);background:rgba(16,255,160,0.1);color:var(--green-t);box-shadow:0 8px 30px rgba(16,255,160,0.2)}
.toast.err{border-color:rgba(255,77,109,.3);background:rgba(255,77,109,0.1);color:var(--red-t);box-shadow:0 8px 30px rgba(255,77,109,0.2)}
.toast.warn{border-color:rgba(255,184,0,.3);background:rgba(255,184,0,0.1);color:var(--amber-t);box-shadow:0 8px 30px rgba(255,184,0,0.2)}

.empty{text-align:center;padding:40px 20px;color:var(--t3)}
.empty i{font-size:36px;opacity:.3;display:block;margin-bottom:10px;filter:drop-shadow(0 0 10px rgba(0,240,255,0.2))}
.empty p{font-size:11px;letter-spacing:0.3px}

/* === ناوبری پایین (موبایل) === */
.bottom-nav{display:none;position:fixed;bottom:0;right:0;left:0;background:var(--bg-surface-2);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border-top:1px solid var(--border-subtle);z-index:300;padding:6px 4px 8px;justify-content:space-around;align-items:center}
.bottom-nav .nav-item{display:flex;flex-direction:column;align-items:center;gap:2px;color:var(--t3);font-size:8px;cursor:pointer;padding:4px 8px;border-radius:10px;transition:all .3s var(--transition);border:none;background:none;font-family:inherit;min-width:44px;position:relative}
.bottom-nav .nav-item i{font-size:18px;transition:all .3s var(--transition)}
.bottom-nav .nav-item:hover{color:var(--cyan);transform:translateY(-2px)}
.bottom-nav .nav-item.active{color:var(--cyan)}
.bottom-nav .nav-item.active i{transform:scale(1.15);filter:drop-shadow(0 0 6px var(--cyan))}
.bottom-nav .nav-item .notif-dot{position:absolute;top:2px;right:6px;width:6px;height:6px;background:var(--red);border-radius:50%;animation:pulseAnim 1.5s infinite;box-shadow:0 0 6px var(--red)}

/* === صفحات === */
.pg{display:none;animation:pageIn .4s var(--transition)}
.pg.on{display:block}
@keyframes pageIn{from{opacity:0;transform:translateY(15px)}to{opacity:1;transform:translateY(0)}}

@media(max-width:768px){
  .bottom-nav{display:flex !important}
  .main{padding-bottom:70px !important;margin-right:0 !important;padding-top:64px !important}
  .sidebar{transform:translateX(100%);padding-bottom:60px}
  .sidebar.open{transform:translateX(0)}
  .mob-top{display:flex}
  .stats-grid{grid-template-columns:repeat(3,1fr)}
  .dash-grid{gap:12px;margin-top:12px}
}
@media(max-width:480px){
  .stats-grid{grid-template-columns:1fr 1fr}
  .main{padding:58px 10px 70px}
  .bottom-nav .nav-item{min-width:36px;padding:3px 6px}
  .bottom-nav .nav-item i{font-size:16px}
  .bottom-nav .nav-item span{font-size:7px}
  .users-table thead th{font-size:8px;padding:8px 6px}
  .users-table tbody td{font-size:10px;padding:8px 6px}
  .users-table .usage-bar .bar{width:40px}
  .stat-mini{padding:8px 10px}
  .stat-mini-num{font-size:14px}
  .topbar{padding:14px 16px}
  .tb-title{font-size:14px}
}
@media(min-width:769px){.bottom-nav{display:none !important}}

/* === تم روشن === */
body.light-theme{
  --bg-deep:#eef1f8;
  --bg-mid:#e1e6f0;
  --bg-surface:rgba(255,255,255,0.7);
  --bg-surface-2:rgba(255,255,255,0.85);
  --bg-card:rgba(255,255,255,0.75);
  --bg-card-hover:rgba(255,255,255,0.9);
  --border-subtle:rgba(0,100,200,0.1);
  --border-glow:rgba(0,150,255,0.3);
  --border-strong:rgba(0,150,255,0.45);
  --t1:#0f1729;
  --t2:#475569;
  --t3:#94a3b8;
  --shadow:0 8px 32px rgba(0,0,0,0.08),0 0 60px rgba(0,150,255,0.04)
}
body.light-theme .nebula-bg{display:none}
body.light-theme .stat-card .number{background:linear-gradient(135deg,#0f1729,rgba(0,150,200,0.8));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
body.light-theme .fi{background:rgba(255,255,255,0.7)}
body.light-theme .logo-name{background:linear-gradient(135deg,#0f1729,#0099cc);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
body.light-theme .nav-it.on{background:linear-gradient(90deg,rgba(0,150,255,0.12),rgba(0,150,255,0.02))}
body.light-theme .btn-p{color:#fff}

/* === RGB Mode === */
body.rgb-mode{animation:rgbShift 8s linear infinite}
@keyframes rgbShift{0%{filter:hue-rotate(0deg)}100%{filter:hue-rotate(360deg)}}

/* === شیمر برای نوار سهمیه === */
@keyframes shimmer{0%{transform:translateX(100%)}100%{transform:translateX(-200%)}}

/* ========================================
   ✦ WTF Factor #1: Command Palette (Ctrl+K) ✦
   ======================================== */
.cmdk-overlay{display:none;position:fixed;inset:0;z-index:600;background:rgba(0,0,0,0.7);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);align-items:flex-start;justify-content:center;padding-top:12vh}
.cmdk-overlay.open{display:flex;animation:cmdkFade .2s ease}
@keyframes cmdkFade{from{opacity:0}to{opacity:1}}
.cmdk-box{width:90%;max-width:640px;background:var(--bg-surface-2);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border:1px solid var(--border-strong);border-radius:16px;overflow:hidden;box-shadow:0 30px 100px rgba(0,0,0,0.6),0 0 60px rgba(0,240,255,0.15);animation:cmdkIn .35s var(--transition)}
@keyframes cmdkIn{from{opacity:0;transform:translateY(-30px) scale(0.96)}to{opacity:1;transform:translateY(0) scale(1)}}
.cmdk-input-wrap{padding:18px 20px;border-bottom:1px solid var(--border-subtle);display:flex;align-items:center;gap:12px}
.cmdk-input-wrap i{color:var(--cyan);font-size:20px;filter:drop-shadow(0 0 6px var(--cyan))}
.cmdk-input{flex:1;background:transparent;border:none;outline:none;color:var(--t1);font-family:inherit;font-size:16px;font-weight:600}
.cmdk-input::placeholder{color:var(--t3)}
.cmdk-kbd{font-size:10px;color:var(--t3);background:rgba(255,255,255,0.05);padding:3px 8px;border-radius:6px;border:1px solid var(--border-subtle);font-family:monospace}
.cmdk-list{max-height:400px;overflow-y:auto;padding:8px}
.cmdk-list::-webkit-scrollbar{width:4px}
.cmdk-list::-webkit-scrollbar-track{background:transparent}
.cmdk-list::-webkit-scrollbar-thumb{background:var(--cyan-soft);border-radius:4px}
.cmdk-category{font-size:10px;font-weight:700;color:var(--cyan);text-transform:uppercase;letter-spacing:1px;padding:8px 12px 4px;text-shadow:0 0 6px rgba(0,240,255,0.4)}
.cmdk-item{display:flex;align-items:center;gap:12px;padding:10px 12px;border-radius:10px;cursor:pointer;transition:all .15s;color:var(--t1);font-size:13px;font-weight:600}
.cmdk-item:hover,.cmdk-item.active{background:rgba(0,240,255,0.08);color:var(--cyan)}
.cmdk-item.active{box-shadow:inset 3px 0 0 var(--cyan)}
.cmdk-item .cmdk-icon{width:32px;height:32px;border-radius:8px;background:rgba(0,240,255,0.05);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0;color:var(--cyan)}
.cmdk-item .cmdk-text{flex:1;min-width:0}
.cmdk-item .cmdk-text .cmdk-title{font-size:13px;font-weight:700;color:var(--t1);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.cmdk-item .cmdk-text .cmdk-desc{font-size:10px;color:var(--t3);margin-top:1px}
.cmdk-item .cmdk-shortcut{font-size:9px;color:var(--t3);background:rgba(255,255,255,0.05);padding:3px 6px;border-radius:5px;border:1px solid var(--border-subtle);font-family:monospace}
.cmdk-empty{text-align:center;padding:30px;color:var(--t3);font-size:12px}
.cmdk-empty i{font-size:32px;opacity:0.3;display:block;margin-bottom:8px}

/* ========================================
   ✦ WTF Factor #2: Counter Up Animation ✦
   ======================================== */
.counter-num{display:inline-block;transition:color .3s}
.counter-num.counting{color:var(--cyan);text-shadow:0 0 12px rgba(0,240,255,0.6)}

/* ========================================
   ✦ WTF Factor #3: World Map with Servers ✦
   ======================================== */
.server-connection{position:absolute;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:1}
.server-connection line{stroke:url(#connGradient);stroke-width:1;opacity:0.4;stroke-dasharray:4 4;animation:dashMove 30s linear infinite}
@keyframes dashMove{to{stroke-dashoffset:-200}}

/* ========================================
   ✦ WTF Factor #4: Speedometer Gauge ✦
   ======================================== */
.activity-feed-card{background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:14px 16px;margin-top:14px;max-height:280px;overflow-y:auto}
.activity-feed-card::-webkit-scrollbar{width:4px}
.activity-feed-card::-webkit-scrollbar-track{background:transparent}
.activity-feed-card::-webkit-scrollbar-thumb{background:var(--cyan-soft);border-radius:4px}
.activity-feed-title{font-size:13px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px;margin-bottom:10px;position:sticky;top:0;background:var(--bg-card);backdrop-filter:blur(20px);padding-bottom:6px}
.activity-feed-title i{color:var(--cyan);filter:drop-shadow(0 0 6px var(--cyan))}
.activity-feed-title .live-dot{margin-right:auto;width:8px;height:8px;border-radius:50%;background:var(--green-t);box-shadow:0 0 8px var(--green-t);animation:pulseAnim 1.5s infinite}
.activity-item{display:flex;align-items:flex-start;gap:10px;padding:8px 0;border-bottom:1px solid rgba(0,240,255,0.04);font-size:11px;animation:activityIn .4s var(--transition)}
.activity-item:last-child{border-bottom:none}
@keyframes activityIn{from{opacity:0;transform:translateX(-15px)}to{opacity:1;transform:translateX(0)}}
.activity-icon{width:24px;height:24px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0;font-weight:700}
.activity-icon.info{background:rgba(0,240,255,0.08);color:var(--cyan)}
.activity-icon.success{background:var(--green-bg);color:var(--green-t)}
.activity-icon.warning{background:var(--amber-bg);color:var(--amber-t)}
.activity-icon.error{background:var(--red-bg);color:var(--red-t)}
.activity-text{flex:1;min-width:0;color:var(--t1);font-weight:600}
.activity-text .activity-user{color:var(--cyan);font-weight:700}
.activity-time{font-size:9px;color:var(--t3);margin-top:2px;font-family:monospace}

/* ========================================
   ✦ داشبورد تمام‌صفحه: گرید دو‌ستونه ✦
   ======================================== */
.dash-grid{display:grid;grid-template-columns:1fr;gap:14px;margin-top:14px}
@media(min-width:1100px){
  .dash-grid{grid-template-columns:minmax(0,7fr) minmax(0,5fr);align-items:stretch}
  .dash-grid .span-2{grid-column:1/-1}
}
@media(max-width:1099px){.dash-grid{grid-template-columns:1fr}}

/* ========================================
   ✦ WTF Factor #7: Desktop Notifications ✦
   ======================================== */
.notif-perm-card{background:rgba(0,240,255,0.04);border:1px solid var(--border-subtle);border-radius:10px;padding:10px 12px;margin-top:10px;font-size:11px;color:var(--t2);display:flex;align-items:center;gap:8px}
.notif-perm-card i{color:var(--cyan)}
.notif-perm-card button{margin-right:auto;background:rgba(0,240,255,0.08);color:var(--cyan);border:1px solid var(--cyan-soft);padding:4px 10px;border-radius:6px;cursor:pointer;font-family:inherit;font-size:10px;font-weight:700}

/* ========================================
   ✦ WTF Factor #8: Drag & Drop Reorder ✦
   ======================================== */
.users-table tbody tr.dragging{opacity:0.4;background:rgba(0,240,255,0.08) !important}
.users-table tbody tr.drag-over{border-top:2px solid var(--cyan)}
.users-table tbody tr[draggable="true"]{cursor:grab}
.users-table tbody tr[draggable="true"]:active{cursor:grabbing}

/* ========================================
   ✦ WTF Factor #9: Live Search + Filter ✦
   ======================================== */
.search-filter-bar{background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:12px 16px;margin-bottom:12px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.search-input-wrap{position:relative;flex:1;min-width:200px}
.search-input-wrap i{position:absolute;right:12px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px;pointer-events:none}
.search-input{width:100%;padding:8px 36px 8px 12px;border-radius:8px;border:1px solid var(--border-subtle);background:rgba(0,0,15,0.4);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:all .3s var(--transition)}
.search-input:focus{border-color:var(--cyan);box-shadow:0 0 0 3px rgba(0,240,255,0.08)}
.search-input::placeholder{color:var(--t3)}
.filter-chip{padding:6px 12px;border-radius:20px;font-size:10px;font-weight:700;cursor:pointer;border:1px solid var(--border-subtle);background:rgba(255,255,255,0.02);color:var(--t3);transition:all .25s var(--transition);font-family:inherit;display:inline-flex;align-items:center;gap:4px}
.filter-chip:hover{background:rgba(0,240,255,0.05);color:var(--t1);border-color:var(--cyan-soft)}
.filter-chip.active{background:linear-gradient(135deg,var(--cyan),var(--purple));color:#000;border-color:var(--cyan);box-shadow:0 0 12px rgba(0,240,255,0.3)}
.filter-chip .chip-count{font-size:9px;background:rgba(0,0,0,0.3);padding:1px 6px;border-radius:10px;font-weight:800}

/* ========================================
   ✦ WTF Factor #10: Particle Cursor Trail ✦
   ======================================== */
#particle-canvas{position:fixed;inset:0;z-index:9999;pointer-events:none}

/* ========================================
   ✦ WTF Factor #11: Player-style Bottom Bar ✦
   ======================================== */
.player-bar{position:fixed;bottom:0;right:0;left:0;z-index:250;background:var(--bg-surface-2);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border-top:1px solid var(--border-strong);padding:8px 20px;display:flex;align-items:center;justify-content:space-between;gap:14px;transform:translateY(100%);transition:transform .5s var(--transition);box-shadow:0 -8px 30px rgba(0,0,0,0.4),0 0 30px rgba(0,240,255,0.05)}
.player-bar.show{transform:translateY(0)}
.player-bar-left{display:flex;align-items:center;gap:10px;font-size:11px;font-weight:700;color:var(--t1)}
.player-bar-left .pb-logo{width:28px;height:28px;border-radius:8px;background:linear-gradient(135deg,var(--cyan),var(--purple),var(--magenta));display:flex;align-items:center;justify-content:center;font-size:14px;box-shadow:0 0 15px rgba(0,240,255,0.3);animation:logoPulse 4s ease-in-out infinite}
.player-bar-center{display:flex;align-items:center;gap:18px;font-size:11px}
.player-stat{display:flex;align-items:center;gap:6px;color:var(--t2);font-weight:600}
.player-stat i{color:var(--cyan);font-size:13px;filter:drop-shadow(0 0 4px var(--cyan))}
.player-stat .player-stat-val{color:var(--t1);font-weight:800;font-family:monospace}
.player-bar-right{display:flex;align-items:center;gap:8px}
.player-bar-right button{background:rgba(0,240,255,0.05);border:1px solid var(--border-subtle);color:var(--cyan);width:28px;height:28px;border-radius:8px;cursor:pointer;font-size:13px;display:flex;align-items:center;justify-content:center;transition:all .25s var(--transition)}
.player-bar-right button:hover{background:rgba(0,240,255,0.12);transform:translateY(-2px)}
@media(max-width:768px){.player-bar{padding:6px 12px}.player-bar-center{display:none}}
body.has-player-bar{padding-bottom:50px}
body.has-player-bar .main{padding-bottom:80px}

/* ========================================
   ✦ WTF Factor #12: Animated Theme Switcher (Circular Reveal) ✦
   ======================================== */
.theme-reveal{position:fixed;inset:0;z-index:9998;pointer-events:none;border-radius:50%;transform:scale(0);transition:transform .6s cubic-bezier(0.4,0,0.2,1)}
.theme-reveal.active{transform:scale(1)}

/* === Flatpickr === */
.flatpickr-calendar{background:var(--bg-surface-2) !important;backdrop-filter:blur(40px) !important;-webkit-backdrop-filter:blur(40px) !important;border:1px solid var(--border-strong) !important;border-radius:14px !important;box-shadow:var(--shadow) !important}
.flatpickr-calendar .flatpickr-months .flatpickr-month{color:var(--t1) !important}
.flatpickr-calendar .flatpickr-weekday{color:var(--cyan) !important;font-weight:700 !important}
.flatpickr-calendar .flatpickr-day{color:var(--t1) !important;border-radius:8px !important}
.flatpickr-calendar .flatpickr-day:hover{background:rgba(0,240,255,0.1) !important}
.flatpickr-calendar .flatpickr-day.selected{background:linear-gradient(135deg,var(--cyan),var(--purple)) !important;color:#000 !important;border-color:var(--cyan) !important;box-shadow:0 0 15px rgba(0,240,255,0.4) !important}
.flatpickr-calendar .flatpickr-day.today{border-color:var(--cyan) !important}
.flatpickr-calendar .flatpickr-day.inRange{background:rgba(0,240,255,0.08) !important}
.flatpickr-calendar .flatpickr-day.startRange,.flatpickr-calendar .flatpickr-day.endRange{background:linear-gradient(135deg,var(--cyan),var(--purple)) !important;color:#000 !important}
.flatpickr-calendar .flatpickr-day.disabled{color:var(--t3) !important}
.flatpickr-calendar .flatpickr-current-month .flatpickr-monthDropdown-months{color:var(--t1) !important;background:transparent !important}
.flatpickr-calendar .flatpickr-current-month input.cur-year{color:var(--t1) !important}
.flatpickr-calendar .flatpickr-prev-month,.flatpickr-calendar .flatpickr-next-month{color:var(--t3) !important}
.flatpickr-calendar .flatpickr-prev-month:hover,.flatpickr-calendar .flatpickr-next-month:hover{color:var(--cyan) !important}
.flatpickr-time{background:var(--bg-surface-2) !important;border-top:1px solid var(--border-subtle) !important;border-radius:0 0 14px 14px !important}
.flatpickr-time input{color:var(--t1) !important}
.flatpickr-time .flatpickr-time-separator{color:var(--t3) !important}
.flatpickr-time .numInputWrapper:hover{background:rgba(0,240,255,0.05) !important}

/* ============================================
   ✦ ULTRA COSMIC v3.0 — قابلیت‌های جدید ✦
   ============================================ */

/* === شفق قطبی متحرک === */
.aurora-bg{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden;opacity:.75;transition:opacity .5s}
body.light-theme .aurora-bg{opacity:.25}
.aurora-bg i{position:absolute;display:block;border-radius:50%;filter:blur(110px);mix-blend-mode:screen;will-change:transform,opacity}
.aurora-bg .a1{width:1000px;height:320px;top:-100px;right:-12%;background:linear-gradient(100deg,transparent,rgba(16,255,160,0.13),rgba(0,240,255,0.18),transparent);transform:rotate(-13deg);animation:auroraSweep 17s ease-in-out infinite}
.aurora-bg .a2{width:850px;height:280px;top:12%;left:-14%;background:linear-gradient(80deg,transparent,rgba(123,47,247,0.16),rgba(0,240,255,0.12),transparent);transform:rotate(9deg);animation:auroraSweep 23s ease-in-out infinite reverse;animation-delay:-7s}
.aurora-bg .a3{width:760px;height:240px;bottom:-60px;right:15%;background:linear-gradient(90deg,transparent,rgba(255,46,154,0.12),rgba(123,47,247,0.1),transparent);transform:rotate(-5deg);animation:auroraSweep 27s ease-in-out infinite;animation-delay:-14s}
@keyframes auroraSweep{0%,100%{transform:translateX(0) rotate(-11deg) scaleY(1);opacity:.5}33%{transform:translateX(-80px) rotate(-6deg) scaleY(1.4);opacity:.85}66%{transform:translateX(70px) rotate(-15deg) scaleY(.75);opacity:.4}}

/* === نوار وضعیت سرور (بالای صفحه) === */
.srv-bar{position:fixed;top:0;right:0;left:0;height:3px;z-index:1000;background:linear-gradient(90deg,var(--green),var(--cyan));box-shadow:0 0 12px rgba(16,255,160,0.6);transition:background .6s,box-shadow .6s;pointer-events:none}
.srv-bar.warn{background:linear-gradient(90deg,var(--amber),#ff9500);box-shadow:0 0 12px rgba(255,184,0,0.6)}
.srv-bar.crit{background:linear-gradient(90deg,var(--red),#ff2e9a);box-shadow:0 0 12px rgba(255,77,109,0.7)}
.srv-bar.off{background:var(--red);box-shadow:0 0 16px rgba(255,77,109,0.9);animation:srvBlink .8s ease-in-out infinite}
@keyframes srvBlink{0%,100%{opacity:1}50%{opacity:.35}}

/* === چیپ وضعیت سرور === */
.srv-chip{display:inline-flex;align-items:center;gap:7px;padding:6px 14px;border-radius:20px;font-size:10px;font-weight:800;letter-spacing:.4px;background:var(--green-bg);border:1px solid rgba(16,255,160,0.25);color:var(--green-t);transition:all .5s;cursor:default;position:relative;overflow:hidden}
.srv-chip::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.25),transparent);transform:translateX(-100%);animation:chipShine 3.5s ease infinite}
@keyframes chipShine{0%{transform:translateX(-100%)}55%,100%{transform:translateX(100%)}}
.srv-chip .dot{width:7px;height:7px;border-radius:50%;background:var(--green);box-shadow:0 0 8px var(--green);animation:dotPulse 1.4s ease-in-out infinite}
.srv-chip.warn{background:var(--amber-bg);border-color:rgba(255,184,0,0.3);color:var(--amber-t)}
.srv-chip.warn .dot{background:var(--amber);box-shadow:0 0 8px var(--amber)}
.srv-chip.crit{background:var(--red-bg);border-color:rgba(255,77,109,0.3);color:var(--red-t)}
.srv-chip.crit .dot{background:var(--red);box-shadow:0 0 8px var(--red)}
.srv-chip b{font-family:monospace;font-size:10px}

/* === ساعت و تقویم شمسی === */
.clock-widget{display:flex;align-items:center;gap:12px;padding:8px 16px;background:var(--bg-card);border:1px solid var(--border-subtle);border-radius:14px;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);position:relative;overflow:hidden;transition:all .4s}
.clock-widget:hover{border-color:var(--border-strong);box-shadow:var(--glow-cyan)}
.clock-widget::before{content:'';position:absolute;top:0;right:0;left:0;height:1px;background:linear-gradient(90deg,transparent,var(--cyan),transparent);opacity:.6}
.clock-time{font-size:19px;font-weight:900;font-family:monospace;background:linear-gradient(135deg,#fff,var(--cyan),var(--magenta));background-size:200% 200%;animation:gradientFlow 6s ease infinite;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;line-height:1.1;direction:ltr}
.clock-date{font-size:9.5px;color:var(--t2);font-weight:600;letter-spacing:.2px;line-height:1.5}
.clock-date .fa-cal{color:var(--cyan);font-size:10px}
.clock-icon{width:34px;height:34px;border-radius:10px;background:linear-gradient(135deg,rgba(0,240,255,0.12),rgba(123,47,247,0.12));display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0;animation:clockGlow 3s ease-in-out infinite}
@keyframes clockGlow{0%,100%{box-shadow:0 0 10px rgba(0,240,255,0.2)}50%{box-shadow:0 0 22px rgba(255,46,154,0.35)}}
.clock-sec{font-size:9px;color:var(--t3);font-family:monospace}

/* === دکمه صدا === */
.sfx-btn{width:36px;height:36px;border-radius:10px;border:1px solid var(--border-subtle);background:var(--bg-card);color:var(--t2);font-size:15px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .3s var(--transition);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.sfx-btn:hover{border-color:var(--cyan);color:var(--cyan);transform:scale(1.08);box-shadow:var(--glow-cyan)}
.sfx-btn.on{background:rgba(0,240,255,0.08);border-color:rgba(0,240,255,0.3);color:var(--cyan)}

/* === کارت پینگ‌سنج زنده === */
.ping-card{background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:16px 18px;margin-top:14px;position:relative;overflow:hidden;transition:all .3s}
.ping-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,var(--green),var(--cyan),transparent);opacity:.5}
.ping-card:hover{border-color:var(--border-strong)}
.ping-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;flex-wrap:wrap;gap:8px}
.ping-title{font-size:13px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:7px}
.ping-title i{color:var(--cyan);filter:drop-shadow(0 0 6px var(--cyan))}
.ping-quality{display:inline-flex;align-items:center;gap:6px;padding:4px 12px;border-radius:16px;font-size:10px;font-weight:800;transition:all .4s}
.ping-quality .dot{width:7px;height:7px;border-radius:50%;animation:dotPulse 1.3s ease-in-out infinite}
.pq-excellent{background:var(--green-bg);border:1px solid rgba(16,255,160,0.3);color:var(--green-t)}
.pq-excellent .dot{background:var(--green);box-shadow:0 0 8px var(--green)}
.pq-good{background:rgba(0,240,255,0.07);border:1px solid rgba(0,240,255,0.3);color:var(--cyan)}
.pq-good .dot{background:var(--cyan);box-shadow:0 0 8px var(--cyan)}
.pq-fair{background:var(--amber-bg);border:1px solid rgba(255,184,0,0.3);color:var(--amber-t)}
.pq-fair .dot{background:var(--amber);box-shadow:0 0 8px var(--amber)}
.pq-poor{background:var(--red-bg);border:1px solid rgba(255,77,109,0.3);color:var(--red-t)}
.pq-poor .dot{background:var(--red);box-shadow:0 0 8px var(--red)}
.ping-body{display:grid;grid-template-columns:150px 1fr;gap:16px;align-items:center}
@media(max-width:640px){.ping-body{grid-template-columns:1fr}}
.ping-big{text-align:center;padding:14px 8px;background:rgba(0,240,255,0.04);border-radius:12px;border:1px solid var(--border-subtle);position:relative}
.ping-big .num{font-size:30px;font-weight:900;font-family:monospace;color:var(--cyan);text-shadow:0 0 16px rgba(0,240,255,0.45);line-height:1.1;transition:color .4s}
.ping-big .num.ms{font-size:11px;color:var(--t3);font-weight:700;margin-top:2px}
.ping-big .lbl{font-size:9px;color:var(--t3);margin-top:4px;letter-spacing:.5px}
.ping-big .minmax{display:flex;justify-content:center;gap:10px;margin-top:6px;font-size:8.5px;color:var(--t3);font-family:monospace}
.ping-big .minmax b{color:var(--t2)}
.ping-chart-wrap{position:relative;height:86px;width:100%}
.ping-chart-wrap canvas{width:100%;height:100%;display:block}
.ping-legend{display:flex;gap:14px;margin-top:8px;font-size:8.5px;color:var(--t3);flex-wrap:wrap}
.ping-legend span{display:inline-flex;align-items:center;gap:4px}
.ping-legend .lg-dot{width:5px;height:5px;border-radius:50%}

/* === لوگوی SVG متحرک === */
.logo-icon{overflow:visible}
.logo-icon svg{width:62%;height:62%;filter:drop-shadow(0 0 8px rgba(0,240,255,0.7))}
.logo-icon .pp-col{animation:ppColWave 2.6s ease-in-out infinite}
.logo-icon .pp-col.c2{animation-delay:.25s}
.logo-icon .pp-col.c3{animation-delay:.5s}
.logo-icon .pp-roof{animation:ppRoofGlow 3.2s ease-in-out infinite}
@keyframes ppColWave{0%,100%{opacity:.65;transform:translateY(0)}50%{opacity:1;transform:translateY(-1.5px)}}
@keyframes ppRoofGlow{0%,100%{filter:drop-shadow(0 0 3px rgba(0,240,255,0.6))}50%{filter:drop-shadow(0 0 10px rgba(255,46,154,0.9))}}
.mob-logo svg{width:70%;height:70%}
.pb-logo{overflow:visible}
.pb-logo svg{width:70%;height:70%;filter:drop-shadow(0 0 6px rgba(0,240,255,0.6))}
</style>
<style id="eagle-glass">
/* ═══ 🪄 EAGLE MINIMAL v3 — مینیمال، تم‌پذیر و سبک برای موبایل ═══ */
:root{--glass-brd:var(--border-subtle);--glass-hi:rgba(255,255,255,.06);--glass-bg:rgba(255,255,255,.035)}
/* 🎯 دکمه‌های مینیمال — هم‌راستا با هر تم */
.btn,.btn-login,.connect-btn,.app-btn{
  position:relative;overflow:hidden;
  background:rgba(255,255,255,.045)!important;
  backdrop-filter:blur(10px) saturate(140%)!important;-webkit-backdrop-filter:blur(10px) saturate(140%)!important;
  border:1px solid var(--border-strong)!important;border-radius:10px!important;color:var(--t1)!important;
  box-shadow:0 2px 10px rgba(0,0,0,.25)!important;
  transition:background .25s ease,border-color .25s ease,box-shadow .25s ease,filter .2s ease!important;
  font-weight:700;
}
.btn-p{background:linear-gradient(135deg,var(--cyan),var(--purple))!important;color:#0a0a12!important;border-color:transparent!important}
.btn-o{background:transparent!important}
.btn-pur{background:var(--cyan-soft)!important;border-color:var(--border-strong)!important;color:var(--cyan)!important}
.btn-d{background:var(--red-bg)!important;border-color:rgba(255,77,109,.35)!important;color:var(--red-t)!important}
.btn-amber{background:var(--amber-bg)!important;border-color:rgba(255,184,0,.35)!important;color:var(--amber-t)!important}
.btn:hover{filter:brightness(1.12);box-shadow:0 4px 16px rgba(0,0,0,.3)!important}
.btn:active{transform:scale(.97)}
.btn::after{display:none}
/* 🧊 کارت‌ها — تم‌پذیر و سبک */
.stat-card,.settings-card,.chart-section,.stat-info-card,.feature,.clock-widget,.srv-chip{
  background:var(--bg-card)!important;
  backdrop-filter:blur(12px) saturate(140%)!important;-webkit-backdrop-filter:blur(12px) saturate(140%)!important;
  border:1px solid var(--border-subtle)!important;border-radius:14px!important;
  box-shadow:0 4px 18px rgba(0,0,0,.3)!important;
}
.stat-card{transition:border-color .25s ease,box-shadow .25s ease!important}
.stat-card:hover{border-color:var(--border-glow)!important}
.stat-card .icon{display:inline-block;animation:emojiFloat 4.5s ease-in-out infinite}
@keyframes emojiFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-2.5px)}}
/* ⌨️ ورودی‌ها */
input,select,textarea{transition:border-color .25s,box-shadow .25s!important}
input:focus,select:focus,textarea:focus{border-color:var(--cyan)!important;box-shadow:0 0 0 3px var(--cyan-soft)!important}
/* 😀 ایموجی منوها */
.nav-it[data-pg="dashboard"] span::before{content:'🏠 '}
.nav-it[data-pg="users"] span::before{content:'👥 '}
.nav-it[data-pg="quota"] span::before{content:'📶 '}
.nav-it[data-pg="connections"] span::before{content:'🌐 '}
.nav-it[data-pg="settings"] span::before{content:'⚙️ '}
.nav-it[data-pg="logs"] span::before{content:'📜 '}
.nav-it[data-pg="backup"] span::before{content:'🗄️ '}
.bottom-nav .nav-item[data-pg="dashboard"] span::before{content:'🏠 '}
.bottom-nav .nav-item[data-pg="users"] span::before{content:'👥 '}
.bottom-nav .nav-item[data-pg="quota"] span::before{content:'📶 '}
.bottom-nav .nav-item[data-pg="settings"] span::before{content:'⚙️ '}
.tb-title::before{content:'✦ '}
/* 🌈 اسکرول‌بار */
::-webkit-scrollbar{width:8px;height:8px}
::-webkit-scrollbar-thumb{background:var(--border-strong);border-radius:8px}
::-webkit-scrollbar-track{background:rgba(255,255,255,.03)}
/* 🪟 مودال‌ها */
.modal{border:1px solid var(--border-strong)!important;box-shadow:0 30px 100px rgba(0,0,0,.65)!important}
/* 🟢 بج کاربر آنلاین */
.online-badge{display:inline-flex;align-items:center;gap:4px;font-size:9px;font-weight:800;padding:2px 7px;border-radius:20px;margin-right:6px;vertical-align:middle}
.online-badge.on{background:rgba(16,255,160,.12);color:var(--green-t);border:1px solid rgba(16,255,160,.3)}
.online-badge.off{background:rgba(255,255,255,.04);color:var(--t3);border:1px solid var(--border-subtle)}
.online-badge .odot{width:5px;height:5px;border-radius:50%;background:currentColor}
.online-badge.on .odot{animation:dotPulse 1.6s ease-in-out infinite}
/* 📊 نوارهای پیشرفت کوچک (مصرف امروز / ریکوئست CF) */
.mini-bar{height:5px;border-radius:4px;background:rgba(255,255,255,.06);overflow:hidden;margin-top:7px;border:1px solid var(--border-subtle)}
.mini-bar>div{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--cyan),var(--purple));transition:width .8s cubic-bezier(.34,1.56,.64,1)}
.mini-bar.warn>div{background:linear-gradient(90deg,#ffb800,#ff8800)}
.mini-bar.alert>div{background:linear-gradient(90deg,#ff4d6d,#ff2e2e)}
/* ⚠️ بنر هشدار تمام‌عرض */
.alert-banner{display:none;align-items:center;gap:10px;padding:12px 16px;border-radius:12px;margin-bottom:12px;font-size:12px;font-weight:800;animation:pulseAnim 2s infinite}
.alert-banner.show{display:flex}
.alert-banner.red{background:rgba(255,77,109,.12);border:1px solid rgba(255,77,109,.4);color:var(--red-t)}
.alert-banner.yellow{background:rgba(255,184,0,.1);border:1px solid rgba(255,184,0,.4);color:var(--amber-t)}
/* 📱 بهینه‌سازی موبایل: بدون لگ — افکت‌های سنگین خاموش */
@media(max-width:768px){
  #starfield-bg,#particle-canvas,.nebula-bg,.aurora,.grid-lines{display:none!important}
  .btn,.btn-login,.connect-btn,.app-btn{backdrop-filter:none!important;-webkit-backdrop-filter:none!important}
  .stat-card,.settings-card,.chart-section,.stat-info-card,.feature,.clock-widget,.srv-chip,.modal,.sidebar,.cmdk-box{
    backdrop-filter:none!important;-webkit-backdrop-filter:none!important;
    background:var(--bg-surface-2)!important;
  }
  .stat-card:hover,.btn:hover{transform:none!important}
  .stat-card .icon{animation:none!important}
  input,select,textarea{font-size:16px!important}
  .world-map-card,.speed-gauge-card{display:none!important}
}
@media(prefers-reduced-motion:reduce){
  *{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}
}
</style></head>
<body>
<canvas id="starfield-bg"></canvas>
<div class="aurora-bg"><i class="a1"></i><i class="a2"></i><i class="a3"></i></div>
<div class="srv-bar" id="srvBar"></div>
<div class="nebula-bg nebula-bg-1"></div><div class="nebula-bg nebula-bg-2"></div>
<div class="toast" id="toast"></div>

<!-- Modal User -->
<div class="modal-bg" id="modal-user">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-user')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-user-plus"></i> <span id="modal-user-title">ساخت کاربر جدید</span></div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
      <div class="fg" style="grid-column:1/2;position:relative;">
        <label><i class="ti ti-tag"></i> <span id="f-label-name">نام کاربری</span></label>
        <div style="display:flex;gap:4px;">
          <input class="fi" id="user-label" placeholder="نام کاربری" style="flex:1">
          <button class="btn btn-generate" onclick="generateRandomUsername()" title="ساخت تصادفی"><i class="ti ti-dice"></i></button>
        </div>
      </div>
      <div class="fg"><label><i class="ti ti-database"></i> <span id="f-label-quota">حجم (GB)</span></label><input class="fi" id="user-quota" type="number" min="0" step="0.5" value="2"></div>
      <div class="fg"><label><i class="ti ti-calendar"></i> <span id="f-label-expiry">انقضا</span></label>
        <input class="fi-date" id="user-expiry-date" type="text" placeholder="انتخاب تاریخ">
      </div>
      <div class="fg"><label><i class="ti ti-devices"></i> <span id="f-label-devices">دستگاه</span></label><input class="fi" id="user-devices" type="number" min="0" max="10" value="1"></div>
      <div class="fg"><label><i class="ti ti-fingerprint"></i> <span id="f-label-fingerprint">انگشت‌نگاری</span></label>
        <select class="fi" id="user-fingerprint">
          <option value="chrome">🌐 Chrome</option><option value="firefox">🦊 Firefox</option>
          <option value="safari">🧭 Safari</option><option value="edge">🌊 Edge</option>
          <option value="ios">📱 iOS</option><option value="android">🤖 Android</option>
          <option value="safari_ios">🍏 Safari iOS</option><option value="random">🎲 Random</option><option value="none">🚫 None</option>
        </select>
      </div>
      <div class="fg">
        <label><i class="ti ti-cloud"></i> <span id="f-label-http">HTTP نسخه</span></label>
        <select class="fi" id="user-http">
          <option value="h2">🚀 HTTP/2</option>
          <option value="h3">⚡ HTTP/3 (QUIC)</option>
          <option value="h1">📶 HTTP/1.1</option>
          <option value="auto">🔄 Auto</option>
        </select>
      </div>
    </div>
    <div style="display:flex;gap:8px;margin-top:14px"><button class="btn btn-p" onclick="saveUser()" style="flex:2"><i class="ti ti-check"></i> <span id="btn-create-user">ساخت کاربر</span></button><button class="btn btn-o" onclick="closeModal('modal-user')" style="flex:1"><span id="btn-cancel">انصراف</span></button></div>
  </div>
</div>

<!-- Modal Edit -->
<div class="modal-bg" id="modal-edit">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> <span id="modal-edit-title">ویرایش کاربر</span></div>
    <input type="hidden" id="edit-uuid">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
      <div class="fg" style="grid-column:1/2;"><label><i class="ti ti-tag"></i> <span id="e-label-name">نام</span></label><input class="fi" id="edit-label" placeholder="نام کاربری"></div>
      <div class="fg"><label><i class="ti ti-database"></i> <span id="e-label-quota">حجم (GB)</span></label><input class="fi" id="edit-quota" type="number" min="0" step="0.5"></div>
      <div class="fg"><label><i class="ti ti-calendar"></i> <span id="e-label-expiry">انقضا</span></label>
        <input class="fi-date" id="edit-expiry-date" type="text" placeholder="انتخاب تاریخ">
      </div>
      <div class="fg"><label><i class="ti ti-devices"></i> <span id="e-label-devices">دستگاه</span></label><input class="fi" id="edit-devices" type="number" min="0" max="10"></div>
      <div class="fg"><label><i class="ti ti-toggle-left"></i> <span id="e-label-status">وضعیت</span></label><select class="fi" id="edit-status"><option value="true">✅ فعال</option><option value="false">❌ غیرفعال</option></select></div>
    </div>
    <div class="fg"><label><i class="ti ti-fingerprint"></i> <span id="e-label-fingerprint">انگشت‌نگاری</span></label>
      <select class="fi" id="edit-fingerprint">
        <option value="chrome">🌐 Chrome</option><option value="firefox">🦊 Firefox</option>
        <option value="safari">🧭 Safari</option><option value="edge">🌊 Edge</option>
        <option value="ios">📱 iOS</option><option value="android">🤖 Android</option>
        <option value="safari_ios">🍏 Safari iOS</option><option value="random">🎲 Random</option><option value="none">🚫 None</option>
      </select>
    </div>
    <div class="fg">
      <label><i class="ti ti-cloud"></i> <span id="e-label-http">HTTP نسخه</span></label>
      <select class="fi" id="edit-http">
        <option value="h2">🚀 HTTP/2</option>
        <option value="h3">⚡ HTTP/3 (QUIC)</option>
        <option value="h1">📶 HTTP/1.1</option>
        <option value="auto">🔄 Auto</option>
      </select>
    </div>
    <div style="display:flex;gap:8px;margin-top:14px"><button class="btn btn-p" onclick="saveEdit()" style="flex:2"><i class="ti ti-check"></i> <span id="btn-save">ذخیره</span></button><button class="btn btn-o" onclick="closeModal('modal-edit')" style="flex:1"><span id="btn-cancel2">انصراف</span></button></div>
  </div>
</div>

<!-- Modal Delete -->
<div class="modal-bg" id="modal-delete">
  <div class="modal" style="max-width:360px">
    <button class="modal-close" onclick="closeModal('modal-delete')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-trash"></i> <span id="modal-delete-title">حذف کاربر</span></div>
    <input type="hidden" id="delete-uuid">
    <p style="font-size:11px;color:var(--t2);margin-bottom:12px" id="delete-desc">این کاربر برای همیشه حذف می‌شود — مطمئنی؟</p>
    <div style="display:flex;gap:8px;margin-top:14px"><button class="btn btn-d" onclick="confirmDelete()" style="flex:2"><i class="ti ti-trash"></i> <span id="btn-delete">حذف</span></button><button class="btn btn-o" onclick="closeModal('modal-delete')" style="flex:1"><span id="btn-cancel3">انصراف</span></button></div>
  </div>
</div>

<!-- Modal QR Code -->
<div class="modal-bg" id="modal-qr">
  <div class="modal" style="max-width:420px;text-align:center">
    <button class="modal-close" onclick="closeModal('modal-qr')"><i class="ti ti-x"></i></button>
    <div class="modal-title" style="justify-content:center"><i class="ti ti-qrcode"></i> <span id="qr-title">QR Code</span></div>
    <div id="qrcode-container" style="display:flex;justify-content:center;padding:14px 0;"></div>
    <p style="font-size:10px;color:var(--t3);margin-top:6px" id="qr-desc">اسکن کنید تا ساب‌لینک اضافه شود</p>
    <button class="btn btn-p btn-sm" onclick="downloadQR()" style="margin-top:10px"><i class="ti ti-download"></i> <span id="qr-download">دانلود QR</span></button>
  </div>
</div>

<div class="mob-top">
  <div class="ml"><div class="mob-logo"><svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="ppGradMob" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#00f0ff"/><stop offset="0.5" stop-color="#7b2ff7"/><stop offset="1" stop-color="#ff2e9a"/></linearGradient></defs><g class="pp-roof"><rect x="6" y="8" width="52" height="6" rx="2" fill="url(#ppGradMob)"/><rect x="10" y="16" width="44" height="4" rx="2" fill="url(#ppGradMob)" opacity="0.75"/></g><rect class="pp-col c1" x="13" y="23" width="6" height="27" rx="2" fill="url(#ppGradMob)"/><rect class="pp-col c2" x="29" y="23" width="6" height="27" rx="2" fill="url(#ppGradMob)" opacity="0.85"/><rect class="pp-col c3" x="45" y="23" width="6" height="27" rx="2" fill="url(#ppGradMob)" opacity="0.7"/><rect x="7" y="52" width="50" height="5" rx="2" fill="url(#ppGradMob)"/></svg></div><span class="mob-title">PERSEPOLIS</span></div>
  <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
</div>
<div class="overlay" id="overlay"></div>

<aside class="sidebar" id="sb">
  <div class="logo"><div class="logo-icon"><svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="ppGradSb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#00f0ff"/><stop offset="0.5" stop-color="#7b2ff7"/><stop offset="1" stop-color="#ff2e9a"/></linearGradient></defs><g class="pp-roof"><rect x="6" y="8" width="52" height="6" rx="2" fill="url(#ppGradSb)"/><rect x="10" y="16" width="44" height="4" rx="2" fill="url(#ppGradSb)" opacity="0.75"/></g><rect class="pp-col c1" x="13" y="23" width="6" height="27" rx="2" fill="url(#ppGradSb)"/><rect class="pp-col c2" x="29" y="23" width="6" height="27" rx="2" fill="url(#ppGradSb)" opacity="0.85"/><rect class="pp-col c3" x="45" y="23" width="6" height="27" rx="2" fill="url(#ppGradSb)" opacity="0.7"/><rect x="7" y="52" width="50" height="5" rx="2" fill="url(#ppGradSb)"/></svg></div><div><div class="logo-name">PERSEPOLIS</div><div class="logo-sub">COSMIC · ULTRA</div></div></div>
  <div class="nav-wrap">
    <div class="nav-it on" data-pg="dashboard"><i class="ti ti-layout-dashboard"></i> <span id="nav-home">خانه</span></div>
    <div class="nav-it" data-pg="users"><i class="ti ti-users"></i> <span id="nav-users">کاربران</span></div>
    <div class="nav-it" data-pg="quota"><i class="ti ti-gauge"></i> <span id="nav-quota">مصرف مجاز</span></div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> <span id="nav-connections">اتصالات</span></div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> <span id="nav-settings">تنظیمات</span></div>
    <div class="nav-it" data-pg="logs"><i class="ti ti-notes"></i> <span id="nav-logs">لاگ‌ها</span></div>
    <div class="nav-it" data-pg="backup"><i class="ti ti-database"></i> <span id="nav-backup">بکاپ</span></div>
  </div>
  <div class="sb-foot"><button class="logout-btn" onclick="logout()"><i class="ti ti-logout"></i> <span id="nav-logout">خروج</span></button></div>
</aside>

<div class="bottom-nav" id="bottomNav">
  <button class="nav-item active" data-pg="dashboard" onclick="navTo('dashboard')"><i class="ti ti-layout-dashboard"></i><span id="b-home">خانه</span></button>
  <button class="nav-item" data-pg="users" onclick="navTo('users')"><i class="ti ti-users"></i><span id="b-users">کاربران</span></button>
  <button class="nav-item" data-pg="quota" onclick="navTo('quota')"><i class="ti ti-gauge"></i><span id="b-quota">سهمیه</span></button>
  <button class="nav-item" data-pg="settings" onclick="navTo('settings')"><i class="ti ti-settings"></i><span id="b-settings">تنظیمات</span></button>
</div>

<main class="main">
<!-- صفحه خانه -->
<section class="pg on" id="pg-dashboard">
  <div class="topbar">
    <div style="display:flex;align-items:center;gap:14px;flex-wrap:wrap">
      <div><div class="tb-title"><i class="ti ti-layout-dashboard"></i> <span id="dash-title">خانه</span></div><div class="tb-sub" id="last-update">بروزرسانی: لحظه‌ای</div></div>
      <div class="clock-widget" id="clockWidget">
        <div class="clock-icon"><i class="ti ti-clock-bolt"></i></div>
        <div>
          <div class="clock-time" id="faClockTime">--:--:--</div>
          <div class="clock-date"><i class="ti ti-calendar-star fa-cal"></i> <span id="faClockDate">—</span></div>
        </div>
      </div>
    </div>
    <div class="tb-right">
      <span class="srv-chip" id="srvChip"><span class="dot"></span> <span id="srvChipText">در حال بررسی…</span></span>
      <button class="sfx-btn" id="sfxToggle" onclick="toggleSFX()" title="جلوه صوتی"><i class="ti ti-volume-2" id="sfxIcon"></i></button>
      <span class="badge bg-fire" id="online-badge"><span class="dot dg"></span> ۰ آنلاین</span>
      <button class="btn btn-p btn-sm" onclick="openModal('modal-user')"><i class="ti ti-plus"></i> <span id="dash-add-user">کاربر</span></button>
    </div>
  </div>
  
  <div id="alert-daily" class="alert-banner red"><i class="ti ti-alert-octagon" style="font-size:20px;flex-shrink:0"></i><div><div id="alert-daily-title">⚠️ سقف مصرف روزانه ۱۰ گیگابایت پر شد</div><div style="font-size:10px;opacity:.85;margin-top:2px" id="alert-daily-desc">کانفیگ‌ها وصل‌اند؛ سهمیه ساعت ۰۳:۳۰ بامداد تهران خودکار ریست می‌شود</div></div></div>
  
  <div class="stats-grid">
    <div class="stat-card"><span class="icon">📊</span><div class="number" id="stat-traffic">۰</div><div class="label" id="s-traffic">ترافیک</div><div class="sub">MB</div></div>
    <div class="stat-card"><span class="icon">📶</span><div class="number" id="stat-ping">—</div><div class="label" id="s-ping">پینگ زنده</div><div class="sub" id="s-ping-sub">در حال اندازه‌گیری…</div></div>
    <div class="stat-card"><span class="icon">👥</span><div class="number" id="stat-users">۰</div><div class="label" id="s-users">کاربران</div><div class="sub" id="stat-users-active">۰ فعال</div></div>
    <div class="stat-card"><span class="icon">📅</span><div class="number small" id="stat-today">۰ B</div><div class="label" id="s-today">مصرف امروز</div><div class="sub" id="s-today-sub">از ۱۰ گیگ روزانه</div><div class="mini-bar" id="bar-daily"><div style="width:0%"></div></div></div>
    <div class="stat-card"><span class="icon">💎</span><div class="number small" id="stat-version">—</div><div class="label" id="s-version">نسخه پنل</div><div class="sub" id="s-version-sub">P443 Panel</div></div>
  </div>

  <div class="dash-grid">
  <div class="chart-section" style="margin:0">
    <div class="chart-header">
      <div>
        <span class="chart-title"><i class="ti ti-chart-bar"></i> <span id="chart-title-text">مصرف روزانه</span></span>
        <span class="chart-sub" id="chart-sub-text">آخرین ۷ روز</span>
      </div>
      <div class="chart-actions">
        <button class="btn btn-sm btn-pur" onclick="loadChart('7d')" id="chart-7d">۷ روز</button>
        <button class="btn btn-sm btn-o" onclick="loadChart('30d')" id="chart-30d">۳۰ روز</button>
        <button class="btn btn-sm btn-o" onclick="loadChart('90d')" id="chart-90d">۹۰ روز</button>
      </div>
    </div>
    <div style="position:relative;height:200px;width:100%">
      <canvas id="trafficChart"></canvas>
    </div>
  </div>

  <div class="recent-card" style="background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:14px 16px;transition:background .4s">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
      <span style="font-size:12px;font-weight:800;color:var(--t1)">🆕 <span id="recent-users-title">کاربران اخیر</span></span>
      <button class="btn btn-sm btn-o" onclick="loadDashboard()"><i class="ti ti-refresh"></i></button>
    </div>
    <div id="recent-users" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:6px"></div>
  </div>

  <!-- ✦ پینگ‌سنج زنده (Live Ping Monitor) -->
  <div class="ping-card" id="pingCard" style="margin-top:0">
    <div class="ping-head">
      <span class="ping-title"><i class="ti ti-wave-sine"></i> <span id="ping-title-text">پینگ‌سنج زنده</span></span>
      <span class="ping-quality pq-good" id="pingQuality"><span class="dot"></span> <span id="pingQualityText">در حال اندازه‌گیری…</span></span>
    </div>
    <div class="ping-body">
      <div class="ping-big">
        <div class="num" id="pingNum">—</div>
        <div class="num ms">ms</div>
        <div class="lbl" id="pingLbl">تاخیر لحظه‌ای به سرور</div>
        <div class="minmax"><span>↓ <b id="pingMin">—</b></span><span>↑ <b id="pingMax">—</b></span><span>∝ <b id="pingAvg">—</b></span></div>
      </div>
      <div>
        <div class="ping-chart-wrap"><canvas id="pingChart"></canvas></div>
        <div class="ping-legend">
          <span><i class="lg-dot" style="background:#10ffa0;box-shadow:0 0 6px #10ffa0"></i> عالی &lt;۱۰۰</span>
          <span><i class="lg-dot" style="background:#00f0ff;box-shadow:0 0 6px #00f0ff"></i> خوب &lt;۳۰۰</span>
          <span><i class="lg-dot" style="background:#ffb800;box-shadow:0 0 6px #ffb800"></i> متوسط &lt;۶۰۰</span>
          <span><i class="lg-dot" style="background:#ff4d6d;box-shadow:0 0 6px #ff4d6d"></i> ضعیف +۶۰۰</span>
        </div>
      </div>
    </div>
  </div>
  
  <!-- Activity Feed زنده -->
  <div class="activity-feed-card" style="margin-top:0">
    <div class="activity-feed-title">
      <i class="ti ti-activity"></i>
      <span id="activity-title">فعالیت‌های زنده</span>
      <span class="live-dot"></span>
    </div>
    <div id="activityFeed">
      <div class="empty"><i class="ti ti-loader" style="font-size:18px"></i><p style="font-size:10px">در حال بارگذاری...</p></div>
    </div>
  </div>
  </div><!-- /dash-grid -->
</section>

<!-- صفحه کاربران -->
<section class="pg" id="pg-users">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-users"></i> <span id="users-title">کاربران</span></div><div class="tb-sub" id="users-sub">لیست کانفیگ‌ها، سهمیه و انقضا</div></div><div class="tb-right"><button class="btn btn-o btn-sm" onclick="loadUsers()"><i class="ti ti-refresh"></i></button></div></div>
  
  <!-- نوار سرچ و فیلتر (WTF #9) -->
  <div class="search-filter-bar">
    <div class="search-input-wrap">
      <input type="text" class="search-input" id="userSearch" placeholder="جست‌وجوی کاربر..." oninput="applyUserFilters()">
      <i class="ti ti-search"></i>
    </div>
    <button class="filter-chip active" data-filter="all" onclick="setUserFilter('all')">همه <span class="chip-count" id="chip-all">0</span></button>
    <button class="filter-chip" data-filter="active" onclick="setUserFilter('active')">فعال <span class="chip-count" id="chip-active">0</span></button>
    <button class="filter-chip" data-filter="expired" onclick="setUserFilter('expired')">منقضی <span class="chip-count" id="chip-expired">0</span></button>
    <button class="filter-chip" data-filter="disabled" onclick="setUserFilter('disabled')">غیرفعال <span class="chip-count" id="chip-disabled">0</span></button>
    <button class="filter-chip" data-filter="high-usage" onclick="setUserFilter('high-usage')">مصرف بالا <span class="chip-count" id="chip-high">0</span></button>
  </div>
  
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:14px;">
    <div class="stat-mini"><span class="stat-mini-icon">👥</span><div><div class="stat-mini-num" id="users-total">0</div><div class="stat-mini-label" id="u-total">کل کاربران</div></div></div>
    <div class="stat-mini"><span class="stat-mini-icon">🟢</span><div><div class="stat-mini-num" id="users-active">0</div><div class="stat-mini-label" id="u-active">فعال</div></div></div>
    <div class="stat-mini"><span class="stat-mini-icon">🔴</span><div><div class="stat-mini-num" id="users-expired">0</div><div class="stat-mini-label" id="u-expired">منقضی</div></div></div>
    <div class="stat-mini"><span class="stat-mini-icon">📊</span><div><div class="stat-mini-num" id="users-traffic">0</div><div class="stat-mini-label" id="u-traffic">مصرف کل</div></div></div>
  </div>
  <div style="background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);overflow:hidden">
    <div style="overflow-x:auto;"><table class="users-table" id="users-table"><thead><tr><th id="th-name">نام</th><th id="th-account">اکانت</th><th id="th-status">وضعیت</th><th id="th-usage">مصرف دیتا</th><th id="th-duration">مدت</th><th style="text-align:center;" id="th-actions">عملیات</th></tr></thead><tbody id="users-tbody"><tr><td colspan="6" style="text-align:center;padding:30px;color:var(--t3);" id="no-users">هیچ کاربری وجود ندارد</td></tr></tbody></table></div>
    <div style="display:flex;justify-content:space-between;align-items:center;padding:12px 16px;border-top:1px solid var(--border-subtle);flex-wrap:wrap;gap:8px;"><div style="font-size:10px;color:var(--t3);"><span id="users-count-label">۰ کاربر</span></div><div style="display:flex;gap:6px;"><button class="btn btn-p btn-sm" onclick="openModal('modal-user')"><i class="ti ti-plus"></i> <span id="add-user-btn">افزودن کاربر جدید</span></button></div></div>
  </div>
</section>

<!-- صفحه مصرف مجاز -->
<section class="pg" id="pg-quota">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-gauge"></i> <span id="quota-title">مصرف مجاز</span></div><div class="tb-sub" id="quota-sub">مصرف روزانه سرور — ریست ۰۳:۳۰ بامداد تهران</div></div><div class="tb-right"><button class="btn btn-sm btn-o" onclick="loadQuota()"><i class="ti ti-refresh"></i></button></div></div>
  
  <!-- کارت اصلی سهمیه -->
  <div class="settings-card" style="max-width:none">
    <div class="title"><i class="ti ti-chart-dots"></i> <span id="quota-overview-title">نمای کلی مصرف</span></div>
    
    <!-- اعداد بزرگ -->
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:20px">
      <div style="text-align:center;padding:18px 10px;background:rgba(0,240,255,0.04);border-radius:12px;border:1px solid var(--border-subtle)">
        <div style="font-size:11px;color:var(--t3);font-weight:700;letter-spacing:0.5px;text-transform:uppercase" id="q-used-label">مصرف شده</div>
        <div style="font-size:28px;font-weight:900;color:var(--cyan);margin-top:6px;font-family:monospace;text-shadow:0 0 12px rgba(0,240,255,0.4)" id="q-used-value">0 GB</div>
      </div>
      <div style="text-align:center;padding:18px 10px;background:rgba(255,46,154,0.04);border-radius:12px;border:1px solid var(--border-subtle)">
        <div style="font-size:11px;color:var(--t3);font-weight:700;letter-spacing:0.5px;text-transform:uppercase" id="q-limit-label">سقف مجاز</div>
        <div style="font-size:28px;font-weight:900;color:var(--magenta);margin-top:6px;font-family:monospace;text-shadow:0 0 12px rgba(255,46,154,0.4)" id="q-limit-value">100 GB</div>
      </div>
      <div style="text-align:center;padding:18px 10px;background:rgba(16,255,160,0.04);border-radius:12px;border:1px solid var(--border-subtle)">
        <div style="font-size:11px;color:var(--t3);font-weight:700;letter-spacing:0.5px;text-transform:uppercase" id="q-remaining-label">باقی مانده</div>
        <div style="font-size:28px;font-weight:900;color:var(--green-t);margin-top:6px;font-family:monospace;text-shadow:0 0 12px rgba(16,255,160,0.4)" id="q-remaining-value">100 GB</div>
      </div>
    </div>
    
    <!-- نوار پیشرفت خطی اصلی -->
    <div style="margin-top:18px">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
        <span style="font-size:12px;font-weight:700;color:var(--t1)" id="q-progress-label">میزان مصرف</span>
        <span style="font-size:14px;font-weight:900;color:var(--cyan);font-family:monospace" id="q-percent">0.0%</span>
      </div>
      <div style="font-size:11px;font-weight:700;color:var(--t2);margin-bottom:8px" id="q-reset-timer">⏳ —</div>
      <div id="q-progress-bar-bg" style="height:24px;border-radius:14px;background:rgba(0,240,255,0.06);overflow:hidden;border:1px solid var(--border-subtle);position:relative">
        <div id="q-progress-fill" style="height:100%;border-radius:14px;background:linear-gradient(90deg,#00f0ff,#7b2ff7,#ff2e9a);background-size:200% 200%;animation:gradientFlow 5s ease infinite;width:0%;transition:width 1.2s cubic-bezier(0.34,1.56,0.64,1);box-shadow:0 0 15px rgba(0,240,255,0.5);position:relative">
          <div style="position:absolute;top:0;right:0;width:40px;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.4),transparent);animation:shimmer 2s linear infinite"></div>
        </div>
      </div>
      <div style="display:flex;justify-content:space-between;margin-top:6px;font-size:9px;color:var(--t3)">
        <span>0 GB</span>
        <span id="q-mid-label">50 GB</span>
        <span id="q-end-label">100 GB</span>
      </div>
    </div>
    
    <!-- هشدار تموم شدن سهمیه -->
    <div id="q-alert" style="display:none;margin-top:18px;padding:16px 18px;background:rgba(255,77,109,0.12);border:1px solid rgba(255,77,109,0.35);border-radius:12px;align-items:center;gap:10px;animation:pulseAnim 2s infinite;box-shadow:0 0 25px rgba(255,77,109,0.2)">
      <i class="ti ti-alert-octagon" style="font-size:24px;color:var(--red-t);flex-shrink:0"></i>
      <div>
        <div style="font-size:14px;font-weight:800;color:var(--red-t)" id="q-alert-title">⚠️ سقف روزانه ۱۰ گیگابایت تمام شد</div>
        <div style="font-size:10px;color:var(--t2);margin-top:3px" id="q-alert-desc">کانفیگ‌ها وصل‌اند — سهمیه ساعت ۰۳:۳۰ بامداد تهران خودکار ریست می‌شود</div>
      </div>
    </div>
  </div>
  
  <!-- توزیع مصرف بین کاربران -->
  <div style="background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:16px 18px;margin-top:14px">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px">
      <span style="font-size:13px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px"><i class="ti ti-users" style="color:var(--cyan)"></i> <span id="q-users-title">مصرف به تفکیک کاربران</span></span>
      <span style="font-size:10px;color:var(--t3)" id="q-users-sub">برترین مصرف‌کنندگان</span>
    </div>
    <div id="q-users-list" style="display:flex;flex-direction:column;gap:10px">
      <div class="empty"><i class="ti ti-users"></i><p style="font-size:10px">در حال بارگذاری...</p></div>
    </div>
  </div>
  
  <!-- نمودار مصرف تجمعی -->
  <div class="chart-section" style="margin-top:14px">
    <div class="chart-header">
      <div>
        <span class="chart-title"><i class="ti ti-chart-line"></i> <span id="q-cumulative-title">مصرف تجمعی</span></span>
        <span class="chart-sub" id="q-cumulative-sub">انباشت مصرف نسبت به سقف مجاز</span>
      </div>
    </div>
    <div style="position:relative;height:200px;width:100%">
      <canvas id="quotaChart"></canvas>
    </div>
  </div>
</section>

<!-- صفحه اتصالات -->
<section class="pg" id="pg-connections">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-plug-connected"></i> <span id="conn-title">اتصالات</span></div><div class="tb-sub" id="conn-count">۰ اتصال</div></div><div class="tb-right"><span class="badge bg-green"><span class="dot dg pulse"></span> <span id="conn-active-label">فعال</span></span><button class="btn btn-sm btn-o" onclick="loadConnections()"><i class="ti ti-refresh"></i></button></div></div>
  <div id="conns-grid" class="conn-grid"><div class="empty"><i class="ti ti-plug-off"></i><p id="no-conn">هیچ اتصالی وجود ندارد</p></div></div>
</section>

<!-- صفحه تنظیمات -->
<section class="pg" id="pg-settings">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-settings"></i> <span id="settings-title">تنظیمات</span></div><div class="tb-sub" id="settings-sub">مدیریت پنل</div></div></div>
  
  <div class="settings-card"><div class="title"><i class="ti ti-palette"></i> <span id="set-theme-title">تم پنل</span></div><div style="display:flex;gap:8px;margin-top:6px;flex-wrap:wrap"><button class="btn" onclick="setTheme('obsidian')" id="theme-obsidian-btn" style="flex:1;font-size:12px;padding:10px 14px;min-width:100px">⬛ <span id="set-obsidian">اوبسیدین (مشکی)</span></button><button class="btn" onclick="setTheme('cosmic')" id="theme-cosmic-btn" style="flex:1;font-size:12px;padding:10px 14px;min-width:100px">🌌 <span id="set-cosmic">کیهانی</span></button><button class="btn" onclick="setTheme('bumblebee')" id="theme-bumblebee-btn" style="flex:1;font-size:12px;padding:10px 14px;min-width:100px">🐝 <span id="set-bumblebee">زنبوری (زرد-مشکی)</span></button><button class="btn" onclick="setTheme('white')" id="theme-white-btn" style="flex:1;font-size:12px;padding:10px 14px;min-width:100px">⚪ <span id="set-white">سفید (روشن)</span></button></div><div style="font-size:10px;color:var(--t3);margin-top:8px;">💡 <span id="set-current-theme">تم فعلی</span>: <span id="current-theme-label">اوبسیدین</span></div></div>
  
  <div class="settings-card"><div class="title"><i class="ti ti-language"></i> <span id="set-lang-title">زبان پنل</span></div><div style="display:flex;gap:8px;margin-top:6px"><button class="btn btn-pur" onclick="setLang('fa')" style="flex:1;font-size:12px;padding:8px 14px" id="lang-fa-btn">🇮🇷 فارسی</button><button class="btn btn-o" onclick="setLang('en')" style="flex:1;font-size:12px;padding:8px 14px" id="lang-en-btn">🇬🇧 English</button></div><div style="font-size:10px;color:var(--t3);margin-top:8px">💡 <span id="set-current-lang">زبان فعلی</span>: <span id="current-lang-label">فارسی</span></div></div>
  
  <div class="settings-card"><div class="title"><i class="ti ti-shield-lock"></i> <span id="set-cred-title">تغییر اعتبارنامه ادمین</span></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:8px">
      <div class="fg"><label style="font-size:10px;color:var(--t3)" id="cred-user-label">نام کاربری جدید</label><input class="fi" id="cred-username" dir="ltr" placeholder="admin"></div>
      <div class="fg"><label style="font-size:10px;color:var(--t3)" id="cred-pass-label">رمز عبور جدید (حداقل ۶ کاراکتر)</label><input class="fi" id="cred-password" type="password" dir="ltr" placeholder="••••••••"></div>
    </div>
    <div class="fg" style="margin-top:8px"><label style="font-size:10px;color:var(--t3)" id="cred-current-label">رمز فعلی (برای تأیید)</label><input class="fi" id="cred-current" type="password" dir="ltr" placeholder="••••••••"></div>
    <div style="display:flex;gap:8px;margin-top:10px"><button class="btn btn-p" onclick="saveCredentials()" style="flex:2"><i class="ti ti-device-save"></i> <span id="cred-save-btn">ذخیره اعتبارنامه</span></button></div>
    <div style="font-size:9.5px;color:var(--t3);margin-top:8px" id="cred-hint">🔒 با تغییر رمز، ورود بعدی با اعتبارنامه‌ی جدید انجام می‌شود — رمز را جایی امن نگه دار</div></div>

  <div class="settings-card"><div class="title"><i class="ti ti-info-circle"></i> <span id="set-about-title">درباره پنل</span></div><div style="font-size:10.5px;color:var(--t2);margin-top:4px;line-height:2.1" id="about-hint">💎 <b>P443 Panel</b> — پنل VLESS ابرسرعت<br>⚡ کاملاً بهینه برای موبایل · 📶 پینگ زنده در داشبورد<br>🤖 ربات تلگرام: کنترل کامل پنل از تلگرام</div></div>
  
  <div class="settings-card"><div class="title"><i class="ti ti-brand-telegram"></i> <span id="set-tg-title">ربات تلگرام</span></div>
    <div class="fg" style="margin-top:6px"><label style="font-size:10px;color:var(--t3)" id="tg-token-label">توکن ربات (از @BotFather)</label><input class="fi" id="tg-token" dir="ltr" placeholder="123456:ABC-DEF..."></div>
    <div class="fg" style="margin-top:8px"><label style="font-size:10px;color:var(--t3)" id="tg-chat-label">آیدی عددی تلگرام شما (از @userinfobot)</label><input class="fi" id="tg-chat" dir="ltr" placeholder="مثلاً 123456789"></div>
    <div style="display:flex;gap:8px;margin-top:10px"><button class="btn btn-p" onclick="saveTelegram()" style="flex:2"><i class="ti ti-brand-telegram"></i> <span id="tg-save-btn">فعال‌سازی ربات</span></button><button class="btn btn-d" onclick="disableTelegram()" style="flex:1"><span id="tg-dis-btn">قطع اتصال</span></button></div>
    <div style="font-size:9.5px;color:var(--t3);margin-top:8px" id="tg-hint">🤖 بعد از فعال‌سازی، ربات فقط برای آیدی عددی خودت کار می‌کند: ساخت/حذف/ویرایش کاربر، تغییر رمز پنل، وضعیت — همه از داخل تلگرام. در تلگرام به ربات /start بده.</div>
    <div style="font-size:9.5px;color:var(--cyan);margin-top:4px" id="tg-status">—</div></div>

  <div class="settings-card"><div class="title"><i class="ti ti-music"></i> <span id="set-sfx-title">جلوه‌های صوتی کیهانی</span></div><div class="toggle-row"><div class="toggle-label"><i class="ti ti-volume-2" style="color:var(--cyan)"></i> صدای دکمه‌ها و اعلان‌ها</div><div class="switch" id="sfx-switch" onclick="toggleSFX()"><div class="slider"></div></div></div><div style="display:flex;gap:6px;margin-top:10px"><button class="btn btn-pur btn-sm" onclick="SFX.success()" style="flex:1"><i class="ti ti-sparkles"></i> تست موفقیت</button><button class="btn btn-o btn-sm" onclick="SFX.warp()" style="flex:1"><i class="ti ti-rocket"></i> تست وارپ</button><button class="btn btn-d btn-sm" onclick="SFX.error()" style="flex:1"><i class="ti ti-alert-triangle"></i> تست خطا</button></div><div style="font-size:9.5px;color:var(--t3);margin-top:8px">💡 صداهای فوتوریستی بدون فایل خارجی — با WebAudio ساخته می‌شوند</div></div>
  
</section>

<!-- 📜 مودال قوانین استفاده P443 -->
<style>
#rules-overlay{position:fixed;inset:0;background:rgba(5,6,15,.8);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);z-index:99999;display:flex;align-items:center;justify-content:center;padding:18px;opacity:0;pointer-events:none;transition:opacity .45s ease}
#rules-overlay.show{opacity:1;pointer-events:auto}
.rules-card{background:linear-gradient(160deg,#12142a,#0b0c1c);border:1px solid rgba(255,80,100,.35);border-radius:20px;max-width:520px;width:100%;padding:26px 24px;text-align:center;box-shadow:0 25px 80px rgba(0,0,0,.6),0 0 40px rgba(255,46,110,.15);transform:translateY(26px) scale(.92);opacity:0;transition:all .55s cubic-bezier(.18,.89,.32,1.18)}
#rules-overlay.show .rules-card{transform:translateY(0) scale(1);opacity:1}
.rules-emoji{font-size:44px;animation:pulseRule 2s ease-in-out infinite;display:inline-block}
@keyframes pulseRule{0%,100%{transform:scale(1)}50%{transform:scale(1.18)}}
.rules-title{font-size:19px;font-weight:800;color:#fff;margin:8px 0 14px}
.rules-red{color:#ff5468;font-weight:800;font-size:14.5px;line-height:2.1;background:rgba(255,60,90,.08);border:1px solid rgba(255,60,90,.3);border-radius:12px;padding:12px 14px;margin-bottom:12px}
.rules-yellow{color:#ffd94a;font-weight:700;font-size:13.5px;line-height:2.1;background:rgba(255,210,60,.07);border:1px solid rgba(255,210,60,.3);border-radius:12px;padding:12px 14px;margin-bottom:18px}
.rules-btn{background:linear-gradient(135deg,#ff2e5f,#c2185b);color:#fff;border:none;border-radius:12px;padding:12px 46px;font-size:15px;font-weight:800;cursor:pointer;transition:all .25s ease;box-shadow:0 8px 24px rgba(255,46,95,.35);font-family:inherit}
.rules-btn:hover{transform:translateY(-2px);box-shadow:0 12px 30px rgba(255,46,95,.5)}
.rules-btn:active{transform:scale(.96)}
</style>
<div id="rules-overlay">
  <div class="rules-card">
    <div class="rules-emoji">🤝</div>
    <div class="rules-title">📜 قوانین استفاده از P443</div>
    <div class="rules-red">🚫 استفاده از این پنل برای «فروش» کاملاً ممنوع است!<br>⚠️ هرگونه فروش پنل یا فروش کانفیگ‌ها ممنوع است — احترام به این قانون نشانه‌ی شخصیت و شرف توست 💎🙏</div>
    <div class="rules-yellow">✅ استفاده از کانفیگ‌های این پنل برای گرفتن ممبر و بازدید مجاز است — فقط با ذکر منبع کانفیگ (اسم پنل: P443) 📌</div>
    <button class="rules-btn" onclick="hideRulesModal()">متوجه شدم!</button>
  </div>
</div>
<script>
function showRulesModal(){ var o=document.getElementById('rules-overlay'); if(o) o.classList.add('show'); }
function hideRulesModal(){ var o=document.getElementById('rules-overlay'); if(o){ o.classList.remove('show'); setTimeout(function(){ try{o.remove();}catch(e){} }, 500); } }
</script>

<!-- صفحه لاگ‌ها -->
<section class="pg" id="pg-logs">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-notes"></i> <span id="logs-title">لاگ‌ها</span></div><div class="tb-sub" id="logs-count">۰ لاگ</div></div><div class="tb-right"><button class="btn btn-sm btn-o" onclick="loadLogs()"><i class="ti ti-refresh"></i></button></div></div>
  <div style="background:var(--bg-card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--border-subtle);border-radius:var(--radius);padding:12px 14px;max-height:450px;overflow-y:auto"><div id="logs-container" style="font-family:monospace;font-size:10px;color:var(--t2);direction:ltr;text-align:left;line-height:1.7"></div></div>
</section>

<!-- صفحه بکاپ -->
<section class="pg" id="pg-backup">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-database"></i> <span id="backup-title">بکاپ</span></div><div class="tb-sub" id="backup-sub">ذخیره و بازیابی</div></div></div>
  <div class="settings-card"><div class="title"><i class="ti ti-download"></i> <span id="backup-download-title">بکاپ‌گیری</span></div><div style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn btn-p btn-sm" onclick="createBackup()" style="flex:2"><i class="ti ti-download"></i> <span id="backup-download-btn">دانلود</span></button><button class="btn btn-o btn-sm" onclick="document.getElementById('restore-input').click()" style="flex:1"><i class="ti ti-upload"></i> <span id="backup-restore-btn">بازیابی</span></button><input type="file" id="restore-input" accept=".json" style="display:none" onchange="restoreBackup(event)"></div></div>
</section>
</main>

<!-- ==================== WTF #1: Command Palette (Ctrl+K) ==================== -->
<div class="cmdk-overlay" id="cmdkOverlay" onclick="if(event.target===this)closeCmdk()">
  <div class="cmdk-box">
    <div class="cmdk-input-wrap">
      <i class="ti ti-search"></i>
      <input type="text" class="cmdk-input" id="cmdkInput" placeholder="جست‌وجو یا دستور... (مثلاً: کاربر جدید، QR، تم)" oninput="filterCmdk()" autocomplete="off">
      <span class="cmdk-kbd">ESC</span>
    </div>
    <div class="cmdk-list" id="cmdkList"></div>
  </div>
</div>

<!-- ==================== WTF #10: Particle Canvas (Cursor Trail) ==================== -->
<canvas id="particle-canvas"></canvas>

<!-- ==================== WTF #11: Player-style Bottom Bar ==================== -->
<div class="player-bar" id="playerBar">
  <div class="player-bar-left">
    <div class="pb-logo"><svg viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="ppGradPb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#00f0ff"/><stop offset="0.5" stop-color="#7b2ff7"/><stop offset="1" stop-color="#ff2e9a"/></linearGradient></defs><rect x="6" y="8" width="52" height="6" rx="2" fill="url(#ppGradPb)"/><rect x="10" y="16" width="44" height="4" rx="2" fill="url(#ppGradPb)" opacity="0.75"/><rect x="13" y="23" width="6" height="27" rx="2" fill="url(#ppGradPb)"/><rect x="29" y="23" width="6" height="27" rx="2" fill="url(#ppGradPb)" opacity="0.85"/><rect x="45" y="23" width="6" height="27" rx="2" fill="url(#ppGradPb)" opacity="0.7"/><rect x="7" y="52" width="50" height="5" rx="2" fill="url(#ppGradPb)"/></svg></div>
    <div>
      <div style="font-size:12px;font-weight:800;color:var(--t1)">PERSEPOLIS</div>
      <div style="font-size:8px;color:var(--t3);letter-spacing:1px">COSMIC · v3.0 ULTRA</div>
    </div>
  </div>
  <div class="player-bar-center">
    <div class="player-stat"><i class="ti ti-users"></i> <span id="pb-users">0</span></div>
    <div class="player-stat"><i class="ti ti-bolt"></i> <span id="pb-online">0</span></div>
    <div class="player-stat"><i class="ti ti-activity"></i> <span id="pb-traffic">0 MB</span></div>
    <div class="player-stat"><i class="ti ti-calendar-stats"></i> <span id="pb-today">0 B</span></div>
  </div>
  <div class="player-bar-right">
    <button onclick="openCmdk()" title="Command Palette (Ctrl+K)"><i class="ti ti-command"></i></button>
    <button onclick="navTo('dashboard')" title="خانه"><i class="ti ti-home"></i></button>
    <button onclick="navTo('quota')" title="سهمیه"><i class="ti ti-gauge"></i></button>
    <button onclick="togglePlayerBar()" title="بستن نوار"><i class="ti ti-x"></i></button>
  </div>
</div>

<!-- ==================== WTF #12: Theme Reveal ==================== -->
<div class="theme-reveal" id="themeReveal"></div>

<script>
// === ✦ ULTRA COSMIC: ستاره‌های پارالاکس + شهاب‌سنگ (Canvas) ===
const canvasBg = document.getElementById('starfield-bg');
const ctxBg = canvasBg.getContext('2d');
let starsBg = [], meteorsBg = [], mouseBg = {x: 0.5, y: 0.5};
function resizeCanvasBg() {
    canvasBg.width = window.innerWidth;
    canvasBg.height = window.innerHeight;
    starsBg = [];
    const count = Math.floor((canvasBg.width * canvasBg.height) / 9000);
    for (let i = 0; i < count; i++) {
        starsBg.push({
            x: Math.random() * canvasBg.width,
            y: Math.random() * canvasBg.height,
            r: Math.random() * 1.3 + 0.2,
            o: Math.random() * 0.6 + 0.2,
            tw: Math.random() * Math.PI * 2,
            depth: Math.random(),
            color: Math.random() > 0.85 ? '#00f0ff' : (Math.random() > 0.7 ? '#ff2e9a' : '#ffffff')
        });
    }
}
function spawnMeteorBg() {
    const sx = Math.random() * canvasBg.width * 0.85 + canvasBg.width * 0.08;
    meteorsBg.push({
        x: sx, y: -30,
        vx: -(Math.random() * 6 + 4),
        vy: Math.random() * 4 + 4,
        len: Math.random() * 100 + 60,
        life: 1, hue: Math.random() > 0.5 ? '#00f0ff' : '#ff2e9a'
    });
}
function drawStarsBg() {
    ctxBg.clearRect(0, 0, canvasBg.width, canvasBg.height);
    const px = (mouseBg.x - 0.5), py = (mouseBg.y - 0.5);
    starsBg.forEach(s => {
        s.tw += 0.015;
        const op = s.o * (0.5 + 0.5 * Math.sin(s.tw));
        const ox = px * 22 * s.depth, oy = py * 15 * s.depth;
        ctxBg.beginPath();
        ctxBg.arc(s.x + ox, s.y + oy, s.r, 0, Math.PI * 2);
        ctxBg.fillStyle = s.color;
        ctxBg.globalAlpha = op;
        ctxBg.shadowBlur = 6 + s.depth * 6;
        ctxBg.shadowColor = s.color;
        ctxBg.fill();
    });
    // شهاب‌سنگ‌ها
    if (Math.random() < 0.01 && meteorsBg.length < 3) spawnMeteorBg();
    for (let i = meteorsBg.length - 1; i >= 0; i--) {
        const m = meteorsBg[i];
        m.x += m.vx; m.y += m.vy; m.life -= 0.007;
        if (m.life <= 0 || m.y > canvasBg.height + 100) { meteorsBg.splice(i, 1); continue; }
        const grad = ctxBg.createLinearGradient(m.x, m.y, m.x - m.vx * (m.len / 8), m.y - m.vy * (m.len / 8));
        grad.addColorStop(0, m.hue);
        grad.addColorStop(1, 'transparent');
        ctxBg.strokeStyle = grad;
        ctxBg.lineWidth = 2;
        ctxBg.globalAlpha = Math.min(m.life, 1);
        ctxBg.shadowBlur = 12;
        ctxBg.shadowColor = m.hue;
        ctxBg.beginPath();
        ctxBg.moveTo(m.x, m.y);
        ctxBg.lineTo(m.x - m.vx * (m.len / 8), m.y - m.vy * (m.len / 8));
        ctxBg.stroke();
        ctxBg.beginPath();
        ctxBg.arc(m.x, m.y, 2.2, 0, Math.PI * 2);
        ctxBg.fillStyle = '#fff';
        ctxBg.fill();
    }
    ctxBg.globalAlpha = 1;
    ctxBg.shadowBlur = 0;
    requestAnimationFrame(drawStarsBg);
}
window.addEventListener('resize', resizeCanvasBg);
window.addEventListener('mousemove', e => { mouseBg.x = e.clientX / window.innerWidth; mouseBg.y = e.clientY / window.innerHeight; });
resizeCanvasBg();
drawStarsBg();

// ===== ترجمه‌ها =====
const translations = {
  fa: {
    nav_home: 'خانه', nav_users: 'کاربران',
    nav_connections: 'اتصالات', nav_settings: 'تنظیمات', nav_logs: 'لاگ‌ها',
    nav_backup: 'بکاپ', nav_logout: 'خروج', nav_quota: 'مصرف مجاز',
    b_quota: 'سهمیه',
    quota_title: 'مصرف مجاز', quota_sub: 'مصرف روزانه سرور — ریست ۰۳:۳۰ بامداد تهران',
    quota_overview_title: 'نمای کلی مصرف',
    q_used_label: 'مصرف شده', q_limit_label: 'سقف مجاز', q_remaining_label: 'باقی مانده',
    q_progress_label: 'میزان مصرف',
    q_alert_title: '⚠️ سقف روزانه ۱۰ گیگابایت تمام شد',
    q_alert_desc: 'کانفیگ‌ها وصل‌اند — سهمیه ساعت ۰۳:۳۰ بامداد تهران خودکار ریست می‌شود',
    q_users_title: 'مصرف به تفکیک کاربران', q_users_sub: 'برترین مصرف‌کنندگان',
    q_cumulative_title: 'مصرف ۱۴ روز اخیر', q_cumulative_sub: 'مصرف روزانه واقعی در مقابل سقف روزانه',
    // WTF Factor translations
    cmdk_placeholder: 'جست‌وجو یا دستور... (مثلاً: کاربر جدید، QR، تم)',
    cmdk_cat_navigation: 'ناوبری',
    cmdk_cat_actions: 'عملیات',
    cmdk_cat_settings: 'تنظیمات',
    cmdk_cat_users: 'کاربران',
    cmdk_no_results: 'نتیجه‌ای یافت نشد',
    cmdk_open_user: 'ساخت کاربر جدید', cmdk_open_user_d: 'باز کردن مودال ساخت کاربر',
    cmdk_nav_dashboard: 'رفتن به خانه', cmdk_nav_dashboard_d: 'صفحه اصلی داشبورد',
    cmdk_nav_users: 'رفتن به کاربران', cmdk_nav_users_d: 'لیست کاربران',
    cmdk_nav_quota: 'رفتن به مصرف مجاز', cmdk_nav_quota_d: 'سهمیه کل سرور',
    cmdk_nav_inbound: 'رفتن به اینباند', cmdk_nav_inbound_d: 'تنظیمات ورودی', // unused
    cmdk_nav_connections: 'رفتن به اتصالات', cmdk_nav_connections_d: 'اتصالات فعال',
    cmdk_nav_settings: 'رفتن به تنظیمات', cmdk_nav_settings_d: 'تنظیمات پنل',
    cmdk_nav_logs: 'رفتن به لاگ‌ها', cmdk_nav_logs_d: 'لاگ‌های سیستم',
    cmdk_nav_backup: 'رفتن به بکاپ', cmdk_nav_backup_d: 'بکاپ‌گیری',
    cmdk_logout: 'خروج از پنل', cmdk_logout_d: 'خروج و بازگشت به صفحه ورود',
    cmdk_toggle_theme: 'تغییر تم (روشن/کیهانی)', cmdk_toggle_theme_d: 'سوییچ بین تم روشن و تاریک',
    cmdk_toggle_rgb: 'تغییر حالت RGB', cmdk_toggle_rgb_d: 'چرخش رنگ‌های RGB',
    cmdk_refresh: 'بروزرسانی داده‌ها', cmdk_refresh_d: 'بارگذاری مجدد داشبورد',
    cmdk_backup: 'بکاپ‌گیری', cmdk_backup_d: 'دانلود فایل بکاپ',
    gauge_title: 'سرعت زنده', gauge_label: 'سرعت دانلود لحظه‌ای',
    map_title: 'سرورهای جهان',
    activity_title: 'فعالیت‌های زنده',
    activity_user_created: 'کاربر {user} ساخته شد',
    activity_user_deleted: 'کاربر {user} حذف شد',
    activity_user_edited: 'کاربر {user} ویرایش شد',
    activity_quota_warning: 'سهمیه کاربر {user} نزدیک اتمام است',
    activity_quota_exhausted: 'مصرف مجاز شما تمام شد',
    activity_login: 'ورود به پنل',
    notif_enable: 'فعال‌سازی اطلاع‌رسانی دسکتاپ',
    notif_desc: 'برای رویدادهای مهم (سهمیه تمام شد، کاربر ساخته شد) مطلع شوید',
    notif_enable_btn: 'فعال‌سازی',
    search_placeholder: 'جست‌وجوی کاربر...',
    filter_all: 'همه', filter_active: 'فعال', filter_expired: 'منقضی',
    filter_disabled: 'غیرفعال', filter_high_usage: 'مصرف بالا',
    dash_title: 'خانه', dash_add_user: 'کاربر',
    s_traffic: 'ترافیک', s_ping: 'پینگ زنده', s_users: 'کاربران',
    s_today: 'مصرف امروز', s_today_sub: 'از ۱۰ گیگ روزانه',
    s_version: 'نسخه پنل', s_version_sub: 'P443 Panel',
    alert_daily_title: '⚠️ سقف مصرف روزانه ۱۰ گیگابایت پر شد',
    alert_daily_desc: 'کانفیگ‌ها وصل‌اند؛ سهمیه ساعت ۰۳:۳۰ بامداد تهران خودکار ریست می‌شود',
    chart_title: 'مصرف روزانه', chart_sub: 'آخرین ۷ روز',
    recent_users: 'کاربران اخیر',
    users_title: 'کاربران', users_sub: 'لیست کانفیگ‌ها، سهمیه و انقضا',
    u_total: 'کل کاربران', u_active: 'فعال', u_expired: 'منقضی', u_traffic: 'مصرف کل',
    th_name: 'نام', th_account: 'اکانت', th_status: 'وضعیت', th_usage: 'مصرف دیتا',
    th_duration: 'مدت', th_actions: 'عملیات',
    add_user_btn: 'افزودن کاربر جدید', no_users: 'هیچ کاربری وجود ندارد',
    conn_title: 'اتصالات', conn_active: 'فعال', no_conn: 'هیچ اتصالی وجود ندارد',
    settings_title: 'تنظیمات', settings_sub: 'مدیریت پنل',
    set_theme: 'تم پنل', set_obsidian: 'اوبسیدین (مشکی)', set_cosmic: 'کیهانی', set_bumblebee: 'زنبوری (زرد-مشکی)', set_white: 'سفید (روشن)',
    set_current_theme: 'تم فعلی', set_lang: 'زبان پنل', set_current_lang: 'زبان فعلی',
    set_sfx: 'جلوه‌های صوتی کیهانی',
    set_cred: 'تغییر اعتبارنامه ادمین', cred_user: 'نام کاربری جدید', cred_pass: 'رمز عبور جدید (حداقل ۶ کاراکتر)',
    cred_current: 'رمز فعلی (برای تأیید)', cred_save: 'ذخیره اعتبارنامه',
    cred_hint: '🔒 با تغییر رمز، ورود بعدی با اعتبارنامه‌ی جدید انجام می‌شود — رمز را جایی امن نگه دار',
    set_tg: 'ربات تلگرام', tg_token: 'توکن ربات (از @BotFather)', tg_chat: 'آیدی عددی تلگرام شما (از @userinfobot)',
    tg_save: 'فعال‌سازی ربات', tg_disable: 'قطع اتصال',
    set_about: 'درباره پنل', about_hint: '💎 <b>P443 Panel</b> — پنل VLESS ابرسرعت<br>⚡ کاملاً بهینه برای موبایل · 📶 پینگ زنده در داشبورد<br>🤖 ربات تلگرام: کنترل کامل پنل از تلگرام — ساخت/حذف/ویرایش کاربر و تغییر رمز',
    backup_title: 'بکاپ', backup_sub: 'ذخیره و بازیابی',
    backup_download: 'بکاپ‌گیری', backup_download_btn: 'دانلود', backup_restore_btn: 'بازیابی',
    logs_title: 'لاگ‌ها',
    modal_user_title: 'ساخت کاربر جدید',
    f_label_name: 'نام کاربری', f_label_quota: 'حجم (GB)',
    f_label_expiry: 'انقضا', f_label_devices: 'دستگاه',
    f_label_fingerprint: 'انگشت‌نگاری', f_label_protocol: 'پروتکل',
    f_label_http: 'HTTP نسخه',
    btn_create_user: 'ساخت کاربر', btn_cancel: 'انصراف',
    modal_edit_title: 'ویرایش کاربر',
    e_label_name: 'نام',
    e_label_quota: 'حجم (GB)', e_label_expiry: 'انقضا',
    e_label_devices: 'دستگاه', e_label_status: 'وضعیت',
    e_label_fingerprint: 'انگشت‌نگاری', e_label_protocol: 'پروتکل',
    e_label_http: 'HTTP نسخه',
    btn_save: 'ذخیره',
    modal_delete_title: 'حذف کاربر', delete_desc: 'این کاربر برای همیشه حذف می‌شود — مطمئنی؟',
    btn_delete: 'حذف',
    qr_title: 'QR Code', qr_desc: 'اسکن کنید تا ساب‌لینک اضافه شود',
    qr_download: 'دانلود QR'
  },
  en: {
    nav_home: 'Home', nav_users: 'Users', nav_inbound: 'Inbound',
    nav_connections: 'Connections', nav_settings: 'Settings', nav_logs: 'Logs',
    nav_backup: 'Backup', nav_logout: 'Logout', nav_quota: 'Quota',
    b_quota: 'Quota',
    quota_title: 'Allowed Quota', quota_sub: 'Daily server usage — resets 03:30 AM Tehran',
    quota_overview_title: 'Usage Overview',
    q_used_label: 'Used', q_limit_label: 'Allowed Limit', q_remaining_label: 'Remaining',
    q_progress_label: 'Usage Progress',
    q_alert_title: '⚠️ Daily 10GB quota exhausted',
    q_alert_desc: 'Configs stay connected — quota auto-resets at 03:30 AM Tehran time',
    q_users_title: 'Per-user usage', q_users_sub: 'Top consumers',
    q_cumulative_title: 'Last 14 days', q_cumulative_sub: 'Real daily usage vs daily limit',
    // WTF Factor translations
    cmdk_placeholder: 'Search or command... (e.g.: new user, QR, theme)',
    cmdk_cat_navigation: 'Navigation',
    cmdk_cat_actions: 'Actions',
    cmdk_cat_settings: 'Settings',
    cmdk_cat_users: 'Users',
    cmdk_no_results: 'No results found',
    cmdk_open_user: 'Create New User', cmdk_open_user_d: 'Open create user modal',
    cmdk_nav_dashboard: 'Go to Dashboard', cmdk_nav_dashboard_d: 'Main dashboard page',
    cmdk_nav_users: 'Go to Users', cmdk_nav_users_d: 'Users list',
    cmdk_nav_quota: 'Go to Quota', cmdk_nav_quota_d: 'Server total quota',
    cmdk_nav_inbound: 'Go to Inbound', cmdk_nav_inbound_d: 'Inbound settings',
    cmdk_nav_connections: 'Go to Connections', cmdk_nav_connections_d: 'Active connections',
    cmdk_nav_settings: 'Go to Settings', cmdk_nav_settings_d: 'Panel settings',
    cmdk_nav_logs: 'Go to Logs', cmdk_nav_logs_d: 'System logs',
    cmdk_nav_backup: 'Go to Backup', cmdk_nav_backup_d: 'Backup',
    cmdk_logout: 'Logout from panel', cmdk_logout_d: 'Logout and return to login page',
    cmdk_toggle_theme: 'Toggle Theme (Light/Cosmic)', cmdk_toggle_theme_d: 'Switch between light and dark themes',
    cmdk_toggle_rgb: 'Toggle RGB Mode', cmdk_toggle_rgb_d: 'Rotate RGB colors',
    cmdk_refresh: 'Refresh Data', cmdk_refresh_d: 'Reload dashboard data',
    cmdk_backup: 'Backup', cmdk_backup_d: 'Download backup file',
    gauge_title: 'Live Speed', gauge_label: 'Live download speed',
    map_title: 'World Servers',
    activity_title: 'Live Activity',
    activity_user_created: 'User {user} created',
    activity_user_deleted: 'User {user} deleted',
    activity_user_edited: 'User {user} edited',
    activity_quota_warning: 'User {user} quota near limit',
    activity_quota_exhausted: 'Your allowed quota is exhausted',
    activity_login: 'Logged in to panel',
    notif_enable: 'Enable Desktop Notifications',
    notif_desc: 'Get notified for important events (quota exhausted, user created)',
    notif_enable_btn: 'Enable',
    search_placeholder: 'Search users...',
    filter_all: 'All', filter_active: 'Active', filter_expired: 'Expired',
    filter_disabled: 'Disabled', filter_high_usage: 'High Usage',
    dash_title: 'Dashboard', dash_add_user: 'User',
    s_traffic: 'Traffic', s_ping: 'Live Ping', s_users: 'Users',
    s_today: 'Today Usage', s_today_sub: 'of 10GB daily',
    s_version: 'Panel Version', s_version_sub: 'P443 Panel',
    alert_daily_title: '⚠️ Daily 10GB quota reached',
    alert_daily_desc: 'Configs stay connected; quota auto-resets at 03:30 AM Tehran time',
    chart_title: 'Daily Usage', chart_sub: 'Last 7 days',
    recent_users: 'Recent Users',
    users_title: 'Users', users_sub: 'Link list, quota and expiry',
    u_total: 'Total Users', u_active: 'Active', u_expired: 'Expired', u_traffic: 'Total Usage',
    th_name: 'Name', th_account: 'Account', th_status: 'Status', th_usage: 'Data Usage',
    th_duration: 'Duration', th_actions: 'Actions',
    add_user_btn: 'Add New User', no_users: 'No users found',
    conn_title: 'Connections', conn_active: 'Active', no_conn: 'No active connections',
    settings_title: 'Settings', settings_sub: 'Panel Settings',
    set_theme: 'Panel Theme', set_obsidian: 'Obsidian (Black)', set_cosmic: 'Cosmic', set_bumblebee: 'Bumblebee (Yellow-Black)', set_white: 'White (Light)',
    set_current_theme: 'Current Theme', set_lang: 'Language', set_current_lang: 'Current Language',
    set_sfx: 'Cosmic Sound Effects',
    set_cred: 'Change Admin Credentials', cred_user: 'New username', cred_pass: 'New password (min 6 chars)',
    cred_current: 'Current password (to confirm)', cred_save: 'Save credentials',
    cred_hint: '🔒 After changing, sign in with the new credentials — keep the password safe',
    set_tg: 'Telegram Bot', tg_token: 'Bot token (from @BotFather)', tg_chat: 'Your numeric Telegram ID (from @userinfobot)',
    tg_save: 'Activate Bot', tg_disable: 'Disconnect',
    set_about: 'About Panel', about_hint: '💎 <b>P443 Panel</b> — HyperSpeed VLESS Panel<br>⚡ Fully mobile-optimized · 📶 Live ping on dashboard<br>🤖 Telegram bot: full panel control from Telegram',
    backup_title: 'Backup', backup_sub: 'Save & Restore',
    backup_download: 'Backup', backup_download_btn: 'Download', backup_restore_btn: 'Restore',
    logs_title: 'Logs',
    modal_user_title: 'Create New User',
    f_label_name: 'Username', f_label_quota: 'Quota (GB)',
    f_label_expiry: 'Expiry', f_label_devices: 'Devices',
    f_label_fingerprint: 'Fingerprint', f_label_protocol: 'Protocol',
    f_label_http: 'HTTP Version',
    btn_create_user: 'Create User', btn_cancel: 'Cancel',
    modal_edit_title: 'Edit User',
    e_label_name: 'Name',
    e_label_quota: 'Quota (GB)', e_label_expiry: 'Expiry',
    e_label_devices: 'Devices', e_label_status: 'Status',
    e_label_fingerprint: 'Fingerprint', e_label_protocol: 'Protocol',
    e_label_http: 'HTTP Version',
    btn_save: 'Save',
    modal_delete_title: 'Delete User', delete_desc: 'This user will be permanently deleted — sure?',
    btn_delete: 'Delete',
    qr_title: 'QR Code', qr_desc: 'Scan to add subscription',
    qr_download: 'Download QR'
  }
};

let currentLang = localStorage.getItem('persepolis-lang') || 'fa';
let currentTheme = localStorage.getItem('persepolis-theme') || 'obsidian';
let trafficChart = null;
let chartPeriod = '7d';
let qrCodeInstance = null;
let expiryPicker = null;
let editExpiryPicker = null;

// ===== تولید یوزرنیم رندوم =====
function generateRandomUsername() {
    const prefixes = ['Cyber', 'Tech', 'Shadow', 'Neon', 'Nova', 'Apex', 'Zen', 'Vex', 'Zion', 'Knight', 'Phoenix', 'Falcon', 'Titan', 'Ghost', 'Raven', 'Wolf', 'Eagle', 'Hawk', 'Storm', 'Blaze', 'Quantum', 'Echo', 'Omega', 'Alpha', 'Delta', 'Sigma', 'Cipher', 'Dragon', 'Tiger', 'Viper'];
    const suffixes = ['X', 'Z', 'Y', 'V', 'W', 'K', 'G', 'P', 'R', 'M', 'H', 'T', 'N', 'S', 'D', 'F', 'Q', 'L', 'J', 'C'];
    const middle = ['flow', 'star', 'dark', 'light', 'storm', 'fire', 'ice', 'wind', 'cloud', 'shadow', 'nova', 'neon', 'cyber', 'ghost', 'raven', 'wolf', 'titan', 'zen', 'vex', 'apex', 'surge', 'pulse', 'cipher'];
    
    let username = '';
    const useMiddle = Math.random() > 0.4;
    
    if (useMiddle) {
        username = prefixes[Math.floor(Math.random() * prefixes.length)] + 
                    middle[Math.floor(Math.random() * middle.length)] +
                    Math.floor(Math.random() * 100);
    } else {
        username = prefixes[Math.floor(Math.random() * prefixes.length)] + 
                    suffixes[Math.floor(Math.random() * suffixes.length)] +
                    Math.floor(Math.random() * 1000);
    }
    
    document.getElementById('user-label').value = username;
    toast('✅ ' + (currentLang === 'fa' ? 'نام کاربری ساخته شد' : 'Username generated'), 'ok');
}

// ===== توابع =====
function t(key) { return translations[currentLang]?.[key] || key; }

// ===== ✦ سیستم تم سه‌گانه: اوبسیدین / کیهانی / زنبوری ✦ =====
const THEME_LABELS = {
  obsidian: { fa: 'اوبسیدین (مشکی)', en: 'Obsidian (Black)' },
  cosmic:   { fa: 'کیهانی', en: 'Cosmic' },
  bumblebee:{ fa: 'زنبوری (زرد-مشکی)', en: 'Bumblebee (Yellow-Black)' },
  white:    { fa: 'سفید (روشن)', en: 'White (Light)' },
};
function normalizeTheme(t) {
  if (t === 'dark') return 'cosmic';       // مهاجرت نام قدیم
  if (t === 'light') return 'white';    // مهاجرت نام قدیم → سفید
  return THEME_LABELS[t] ? t : 'obsidian';
}
function setTheme(theme) {
  currentTheme = normalizeTheme(theme);
  localStorage.setItem('persepolis-theme', currentTheme);
  document.body.dataset.theme = currentTheme;
  document.body.classList.toggle('light-theme', currentTheme === 'white');
  const lbl = document.getElementById('current-theme-label');
  if (lbl) lbl.textContent = THEME_LABELS[currentTheme][currentLang];
  ['obsidian', 'cosmic', 'bumblebee', 'white'].forEach(tn => {
    const btn = document.getElementById('theme-' + tn + '-btn');
    if (btn) btn.className = 'btn ' + (tn === currentTheme ? 'btn-pur' : 'btn-o');
  });
  fetch('/api/settings/theme', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ theme: currentTheme })
  }).catch(() => {});
}

async function loadThemeFromServer() {
  try {
    const r = await fetch('/api/settings');
    const data = await r.json();
    if (data.theme) {
      currentTheme = normalizeTheme(data.theme);
      localStorage.setItem('persepolis-theme', currentTheme);
      setTheme(currentTheme);
    } else {
      setTheme(currentTheme);
    }
  } catch(e) { setTheme(currentTheme); }
}

function setLang(lang) {
  currentLang = lang;
  localStorage.setItem('persepolis-lang', lang);
  document.getElementById('lang-fa-btn').className = 'btn ' + (lang === 'fa' ? 'btn-pur' : 'btn-o');
  document.getElementById('lang-en-btn').className = 'btn ' + (lang === 'en' ? 'btn-pur' : 'btn-o');
  document.getElementById('current-lang-label').textContent = lang === 'fa' ? 'فارسی' : 'English';
  updateUITexts();
  fetch('/api/settings/language', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ language: lang })
  }).catch(() => {});
  
  if (expiryPicker) expiryPicker.set('locale', lang === 'fa' ? 'fa' : 'en');
  if (editExpiryPicker) editExpiryPicker.set('locale', lang === 'fa' ? 'fa' : 'en');
}

function updateUITexts() {
  const t = translations[currentLang];
  if (!t) return;
  
  document.getElementById('nav-home').textContent = t.nav_home;
  document.getElementById('nav-users').textContent = t.nav_users;
  document.getElementById('nav-connections').textContent = t.nav_connections;
  document.getElementById('nav-settings').textContent = t.nav_settings;
  document.getElementById('nav-logs').textContent = t.nav_logs;
  document.getElementById('nav-backup').textContent = t.nav_backup;
  document.getElementById('nav-logout').textContent = t.nav_logout;
  document.getElementById('nav-quota').textContent = t.nav_quota;
  
  document.getElementById('b-home').textContent = t.nav_home;
  document.getElementById('b-users').textContent = t.nav_users;
  document.getElementById('b-quota').textContent = t.b_quota;
  document.getElementById('b-settings').textContent = t.nav_settings;
  
  document.getElementById('quota-title').textContent = t.quota_title;
  document.getElementById('quota-sub').textContent = t.quota_sub;
  document.getElementById('quota-overview-title').textContent = t.quota_overview_title;
  document.getElementById('q-used-label').textContent = t.q_used_label;
  document.getElementById('q-limit-label').textContent = t.q_limit_label;
  document.getElementById('q-remaining-label').textContent = t.q_remaining_label;
  document.getElementById('q-progress-label').textContent = t.q_progress_label;
  document.getElementById('q-alert-title').textContent = t.q_alert_title;
  document.getElementById('q-alert-desc').textContent = t.q_alert_desc;
  document.getElementById('q-users-title').textContent = t.q_users_title;
  document.getElementById('q-users-sub').textContent = t.q_users_sub;
  document.getElementById('q-cumulative-title').textContent = t.q_cumulative_title;
  document.getElementById('q-cumulative-sub').textContent = t.q_cumulative_sub;
  
  // WTF Factor translations
  document.getElementById('activity-title').textContent = t.activity_title;
  const cmdkPlaceholder = document.getElementById('cmdkInput');
  if (cmdkPlaceholder) cmdkPlaceholder.placeholder = t.cmdk_placeholder;
  const searchInput = document.getElementById('userSearch');
  if (searchInput) searchInput.placeholder = t.search_placeholder;
  
  document.getElementById('dash-title').textContent = t.dash_title;
  document.getElementById('dash-add-user').textContent = t.dash_add_user;
  document.getElementById('s-traffic').textContent = t.s_traffic;
  const spg = document.getElementById('s-ping'); if (spg) spg.textContent = t.s_ping;
  document.getElementById('s-users').textContent = t.s_users;
  const psub = document.getElementById('s-ping-sub'); if (psub) psub.textContent = (currentLang === 'fa' ? 'در حال اندازه‌گیری…' : 'measuring…');
  const st = document.getElementById('s-today'); if (st) st.textContent = t.s_today;
  const sts = document.getElementById('s-today-sub'); if (sts) sts.textContent = t.s_today_sub;
  const svv = document.getElementById('s-version'); if (svv) svv.textContent = t.s_version;
  const svvs = document.getElementById('s-version-sub'); if (svvs) svvs.textContent = t.s_version_sub;
  const ad1 = document.getElementById('alert-daily-title'); if (ad1) ad1.textContent = t.alert_daily_title;
  const ad2 = document.getElementById('alert-daily-desc'); if (ad2) ad2.textContent = t.alert_daily_desc;
  document.getElementById('chart-title-text').textContent = t.chart_title;
  document.getElementById('chart-sub-text').textContent = t.chart_sub;
  document.getElementById('recent-users-title').textContent = t.recent_users;
  
  document.getElementById('users-title').textContent = t.users_title;
  document.getElementById('users-sub').textContent = t.users_sub;
  document.getElementById('u-total').textContent = t.u_total;
  document.getElementById('u-active').textContent = t.u_active;
  document.getElementById('u-expired').textContent = t.u_expired;
  document.getElementById('u-traffic').textContent = t.u_traffic;
  document.getElementById('th-name').textContent = t.th_name;
  document.getElementById('th-account').textContent = t.th_account;
  document.getElementById('th-status').textContent = t.th_status;
  document.getElementById('th-usage').textContent = t.th_usage;
  document.getElementById('th-duration').textContent = t.th_duration;
  document.getElementById('th-actions').textContent = t.th_actions;
  document.getElementById('add-user-btn').textContent = t.add_user_btn;
  document.getElementById('no-users').textContent = t.no_users;
  
  document.getElementById('conn-title').textContent = t.conn_title;
  document.getElementById('conn-active-label').textContent = t.conn_active;
  document.getElementById('no-conn').textContent = t.no_conn;
  
  document.getElementById('settings-title').textContent = t.settings_title;
  document.getElementById('settings-sub').textContent = t.settings_sub;
  document.getElementById('set-theme-title').textContent = t.set_theme;
  document.getElementById('set-obsidian').textContent = t.set_obsidian;
  document.getElementById('set-cosmic').textContent = t.set_cosmic;
  document.getElementById('set-bumblebee').textContent = t.set_bumblebee;
  const swt = document.getElementById('set-white'); if (swt) swt.textContent = t.set_white;
  document.getElementById('set-current-theme').textContent = t.set_current_theme;
  document.getElementById('current-theme-label').textContent = THEME_LABELS[currentTheme] ? THEME_LABELS[currentTheme][currentLang] : currentTheme;
  document.getElementById('set-lang-title').textContent = t.set_lang;
  document.getElementById('set-current-lang').textContent = t.set_current_lang;
  document.getElementById('set-cred-title').textContent = t.set_cred;
  document.getElementById('cred-user-label').textContent = t.cred_user;
  document.getElementById('cred-pass-label').textContent = t.cred_pass;
  document.getElementById('cred-current-label').textContent = t.cred_current;
  document.getElementById('cred-save-btn').textContent = t.cred_save;
  document.getElementById('cred-hint').textContent = t.cred_hint;
  const sabt = document.getElementById('set-about-title'); if (sabt) sabt.textContent = t.set_about;
  const sabh = document.getElementById('about-hint'); if (sabh) sabh.innerHTML = t.about_hint;
  const stgt = document.getElementById('set-tg-title'); if (stgt) stgt.textContent = t.set_tg;
  const tgtl = document.getElementById('tg-token-label'); if (tgtl) tgtl.textContent = t.tg_token;
  const tgcl = document.getElementById('tg-chat-label'); if (tgcl) tgcl.textContent = t.tg_chat;
  const tgsb = document.getElementById('tg-save-btn'); if (tgsb) tgsb.textContent = t.tg_save;
  const tgdb = document.getElementById('tg-dis-btn'); if (tgdb) tgdb.textContent = t.tg_disable;
  try { loadTelegramStatus(); } catch (e) {}
  const sfxTitle = document.getElementById('set-sfx-title'); if (sfxTitle) sfxTitle.textContent = t.set_sfx;
  const qt = document.getElementById('quota-title'); if (qt) qt.textContent = t.quota_title;
  const qs = document.getElementById('quota-sub'); if (qs) qs.textContent = t.quota_sub;
  const qct = document.getElementById('q-cumulative-title'); if (qct) qct.textContent = t.q_cumulative_title;
  const qcs = document.getElementById('q-cumulative-sub'); if (qcs) qcs.textContent = t.q_cumulative_sub;
  const qat = document.getElementById('q-alert-title'); if (qat) qat.textContent = t.q_alert_title;
  const qad = document.getElementById('q-alert-desc'); if (qad) qad.textContent = t.q_alert_desc;
  
  document.getElementById('backup-title').textContent = t.backup_title;
  document.getElementById('backup-sub').textContent = t.backup_sub;
  document.getElementById('backup-download-title').textContent = t.backup_download;
  document.getElementById('backup-download-btn').textContent = t.backup_download_btn;
  document.getElementById('backup-restore-btn').textContent = t.backup_restore_btn;
  
  document.getElementById('logs-title').textContent = t.logs_title;
  
  document.getElementById('modal-user-title').textContent = t.modal_user_title;
  document.getElementById('f-label-name').textContent = t.f_label_name;
  document.getElementById('f-label-quota').textContent = t.f_label_quota;
  document.getElementById('f-label-expiry').textContent = t.f_label_expiry;
  document.getElementById('f-label-devices').textContent = t.f_label_devices;
  document.getElementById('f-label-fingerprint').textContent = t.f_label_fingerprint;
  document.getElementById('f-label-http').textContent = t.f_label_http;
  document.getElementById('btn-create-user').textContent = t.btn_create_user;
  document.getElementById('btn-cancel').textContent = t.btn_cancel;
  
  document.getElementById('modal-edit-title').textContent = t.modal_edit_title;
  document.getElementById('e-label-name').textContent = t.e_label_name;
  document.getElementById('e-label-quota').textContent = t.e_label_quota;
  document.getElementById('e-label-expiry').textContent = t.e_label_expiry;
  document.getElementById('e-label-devices').textContent = t.e_label_devices;
  document.getElementById('e-label-status').textContent = t.e_label_status;
  document.getElementById('e-label-fingerprint').textContent = t.e_label_fingerprint;
  document.getElementById('e-label-http').textContent = t.e_label_http;
  document.getElementById('btn-save').textContent = t.btn_save;
  document.getElementById('btn-cancel2').textContent = t.btn_cancel;
  
  document.getElementById('modal-delete-title').textContent = t.modal_delete_title;
  document.getElementById('delete-desc').textContent = t.delete_desc;
  document.getElementById('btn-delete').textContent = t.btn_delete;
  document.getElementById('btn-cancel3').textContent = t.btn_cancel;
  
  document.getElementById('qr-title').textContent = t.qr_title;
  document.getElementById('qr-desc').textContent = t.qr_desc;
  document.getElementById('qr-download').textContent = t.qr_download;
  
  document.getElementById('current-lang-label').textContent = currentLang === 'fa' ? 'فارسی' : 'English';
  renderOnlineBadges();
}

// ===== توابع عمومی =====
function toast(msg, type = '', dur = 2500) {
  const tEl = document.getElementById('toast');
  tEl.textContent = msg;
  tEl.className = 'toast show' + (type ? ' ' + type : '');
  clearTimeout(tEl._timeout);
  tEl._timeout = setTimeout(() => tEl.classList.remove('show'), dur);
  // ✦ صدای همراه توست
  if (type === 'ok') SFX.success();
  else if (type === 'err') SFX.error();
  else if (type === 'warn') SFX.pop();
}

/* ============================================
   ✦ ULTRA COSMIC v3.0 — هسته قابلیت‌های جدید ✦
   ============================================ */

// ===== ✦ ۱) موتور جلوه صوتی فوتوریستی (WebAudio) =====
const SFX = {
  ac: null,
  enabled: localStorage.getItem('pp-sfx') !== 'off',
  ensure() {
    if (!this.ac) { try { this.ac = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) { return false; } }
    if (this.ac && this.ac.state === 'suspended') this.ac.resume();
    return !!this.ac;
  },
  tone(f1, f2, dur, type, vol, delay) {
    if (!this.enabled || !this.ensure()) return;
    try {
      const t0 = this.ac.currentTime + (delay || 0);
      const o = this.ac.createOscillator(), g = this.ac.createGain();
      o.type = type || 'sine';
      o.frequency.setValueAtTime(f1, t0);
      if (f2) o.frequency.exponentialRampToValueAtTime(f2, t0 + dur);
      g.gain.setValueAtTime(0.0001, t0);
      g.gain.exponentialRampToValueAtTime(vol || 0.05, t0 + 0.015);
      g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
      o.connect(g); g.connect(this.ac.destination);
      o.start(t0); o.stop(t0 + dur + 0.05);
    } catch (e) {}
  },
  click() { this.tone(520, 760, 0.08, 'triangle', 0.04); },
  success() { this.tone(523, 0, 0.1, 'sine', 0.055); this.tone(659, 0, 0.1, 'sine', 0.055, 0.09); this.tone(784, 1046, 0.18, 'sine', 0.065, 0.18); },
  error() { this.tone(220, 110, 0.25, 'sawtooth', 0.045); },
  warp() { this.tone(180, 1200, 0.5, 'sawtooth', 0.04); this.tone(90, 600, 0.55, 'sine', 0.045, 0.05); },
  pop() { this.tone(900, 1400, 0.09, 'sine', 0.045); },
  ping(good) { if (good) this.tone(700, 1000, 0.07, 'sine', 0.03); else this.tone(400, 250, 0.12, 'triangle', 0.035); }
};
function toggleSFX() {
  SFX.enabled = !SFX.enabled;
  localStorage.setItem('pp-sfx', SFX.enabled ? 'on' : 'off');
  updateSFXUI();
  if (SFX.enabled) SFX.success();
  toast(SFX.enabled ? (currentLang === 'fa' ? '🔊 جلوه صوتی روشن شد' : '🔊 Sound enabled') : (currentLang === 'fa' ? '🔇 جلوه صوتی خاموش شد' : '🔇 Sound disabled'), '');
}
function updateSFXUI() {
  const btn = document.getElementById('sfxToggle');
  const icon = document.getElementById('sfxIcon');
  const sw = document.getElementById('sfx-switch');
  if (btn) btn.classList.toggle('on', SFX.enabled);
  if (icon) icon.className = SFX.enabled ? 'ti ti-volume-2' : 'ti ti-volume-off';
  if (sw) sw.classList.toggle('on', SFX.enabled);
}
// صدای کلیک روی دکمه‌ها
document.addEventListener('click', e => {
  if (e.target.closest('.btn, button:not(#sfxToggle), .nav-it, .filter-chip, .switch')) SFX.click();
}, true);
// صدای باز شدن مودال
const _openModal = openModal;
openModal = function(id) { _openModal(id); SFX.pop(); };
// صدای تعویض تب
const _navTo = navTo;
navTo = function(name) { if (name !== (document.querySelector('.nav-it.on') || {}).dataset?.pg) SFX.tone(340, 620, 0.12, 'sine', 0.04); _navTo(name); };

// ===== ✦ ۲) پینگ‌سنج زنده =====
const pingState = { hist: [], min: null, max: null, timer: null, lastBad: false };
async function measurePing() {
  const t0 = performance.now();
  try {
    await fetch('/api/me?_p=' + Date.now(), { method: 'HEAD', cache: 'no-store' });
    return Math.round(performance.now() - t0);
  } catch (e) { return -1; }
}
function pingQualityInfo(ms) {
  if (ms < 0) return { cls: 'pq-poor', txt: currentLang === 'fa' ? '⛔ قطع ارتباط' : 'Disconnected', color: '#ff4d6d', bar: 'crit' };
  if (ms < 100) return { cls: 'pq-excellent', txt: currentLang === 'fa' ? '✦ عالی' : 'Excellent', color: '#10ffa0', bar: '' };
  if (ms < 300) return { cls: 'pq-good', txt: currentLang === 'fa' ? '✦ خوب' : 'Good', color: '#00f0ff', bar: '' };
  if (ms < 600) return { cls: 'pq-fair', txt: currentLang === 'fa' ? '✦ متوسط' : 'Fair', color: '#ffb800', bar: 'warn' };
  return { cls: 'pq-poor', txt: currentLang === 'fa' ? '✦ ضعیف' : 'Poor', color: '#ff4d6d', bar: 'crit' };
}
function updateServerStatusBar(ms) {
  const q = pingQualityInfo(ms);
  const bar = document.getElementById('srvBar');
  const chip = document.getElementById('srvChip');
  const chipTxt = document.getElementById('srvChipText');
  if (bar) { bar.className = 'srv-bar' + (q.bar ? ' ' + q.bar : ''); }
  if (chip) { chip.className = 'srv-chip' + (q.bar && q.bar !== 'crit' ? ' ' + q.bar : (q.bar === 'crit' ? ' crit' : '')); }
  if (chipTxt) {
    if (ms < 0) chipTxt.textContent = currentLang === 'fa' ? 'سرور قطع' : 'Server down';
    else chipTxt.innerHTML = (currentLang === 'fa' ? 'سرور آنلاین · ' : 'Online · ') + '<b>' + ms + 'ms</b>';
  }
}
function drawPingChart() {
  const cv = document.getElementById('pingChart');
  if (!cv) return;
  const w = cv.clientWidth || 300, h = cv.clientHeight || 86;
  if (cv.width !== w * 2) { cv.width = w * 2; cv.height = h * 2; }
  const c = cv.getContext('2d');
  c.setTransform(2, 0, 0, 2, 0, 0);
  c.clearRect(0, 0, w, h);
  const hist = pingState.hist.slice(-40);
  if (!hist.length) return;
  const maxMs = Math.max(600, ...hist.filter(v => v >= 0)) * 1.1;
  const bw = w / 40;
  // خطوط راهنما
  c.strokeStyle = 'rgba(100,200,255,0.07)';
  c.lineWidth = 1;
  [0.25, 0.5, 0.75].forEach(f => { c.beginPath(); c.moveTo(0, h * f); c.lineTo(w, h * f); c.stroke(); });
  // میله‌ها
  hist.forEach((v, i) => {
    const x = i * bw + (w - hist.length * bw) / 2;
    let bh, col;
    if (v < 0) { bh = h * 0.92; col = 'rgba(255,77,109,0.75)'; }
    else {
      bh = Math.max(4, (v / maxMs) * h * 0.9);
      col = v < 100 ? 'rgba(16,255,160,0.8)' : v < 300 ? 'rgba(0,240,255,0.8)' : v < 600 ? 'rgba(255,184,0,0.8)' : 'rgba(255,77,109,0.85)';
    }
    const g = c.createLinearGradient(0, h - bh, 0, h);
    g.addColorStop(0, col);
    g.addColorStop(1, col.replace('0.8', '0.15').replace('0.75', '0.15').replace('0.85', '0.15'));
    c.fillStyle = g;
    c.beginPath();
    const r = Math.min(2, bw / 3);
    c.roundRect ? c.roundRect(x, h - bh, bw * 0.62, bh, r) : c.rect(x, h - bh, bw * 0.62, bh);
    c.fill();
  });
  // خط میانگین
  const valid = hist.filter(v => v >= 0);
  if (valid.length) {
    const avg = valid.reduce((a, b) => a + b, 0) / valid.length;
    const ay = h - Math.max(4, (avg / maxMs) * h * 0.9);
    c.strokeStyle = 'rgba(255,46,154,0.5)';
    c.setLineDash([4, 4]);
    c.lineWidth = 1;
    c.beginPath(); c.moveTo(0, ay); c.lineTo(w, ay); c.stroke();
    c.setLineDash([]);
  }
}
async function pingLoop(first) {
  const ms = await measurePing();
  pingState.hist.push(ms);
  if (pingState.hist.length > 60) pingState.hist.shift();
  const valid = pingState.hist.filter(v => v >= 0);
  if (valid.length) {
    pingState.min = Math.min(...valid);
    pingState.max = Math.max(...valid);
  }
  const num = document.getElementById('pingNum');
  const q = pingQualityInfo(ms);
  if (num) {
    num.textContent = ms < 0 ? '✕' : ms;
    num.style.color = q.color;
    num.style.textShadow = '0 0 16px ' + q.color + '66';
  }
  const qEl = document.getElementById('pingQuality');
  if (qEl) { qEl.className = 'ping-quality ' + q.cls; document.getElementById('pingQualityText').textContent = q.txt + (ms >= 0 ? ' · ' + ms + 'ms' : ''); }
  document.getElementById('pingMin').textContent = pingState.min !== null ? pingState.min : '—';
  document.getElementById('pingMax').textContent = pingState.max !== null ? pingState.max : '—';
  document.getElementById('pingAvg').textContent = valid.length ? Math.round(valid.reduce((a, b) => a + b, 0) / valid.length) : '—';
  updateServerStatusBar(ms);
  updatePingCard(ms);
  drawPingChart();
  if (first && ms >= 0) SFX.ping(ms < 300);
}
function startPingMonitor() {
  pingLoop(true);
  // ⚡ صرفه‌جویی درخواست: پینگ هر ۲۰ ثانیه + وقتی تب مخفیه اصلاً درخواست نمی‌زنه
  // (قبلاً هر ۵ ثانیه با no-store بود = ~۱۷ هزار درخواست CF در روز فقط برای پینگ!)
  pingState.timer = setInterval(() => { if (!document.hidden) pingLoop(false); }, 20000);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) pingLoop(false); });
  window.addEventListener('resize', () => drawPingChart());
}

// ===== ✦ ۳) ساعت دیجیتال + تقویم شمسی =====
function updateFaClock() {
  const now = new Date();
  try {
    const time = now.toLocaleTimeString('fa-IR', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
    const el = document.getElementById('faClockTime');
    if (el) el.textContent = time;
    const dEl = document.getElementById('faClockDate');
    if (dEl) dEl.textContent = new Intl.DateTimeFormat('fa-IR', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }).format(now);
  } catch (e) {}
}
function startFaClock() { updateFaClock(); setInterval(updateFaClock, 1000); }

function fmtB(b) {
  if (!b || b === 0) return '0 B';
  if (b < 1024) return b + ' B';
  if (b < 1024**2) return (b/1024).toFixed(1) + ' KB';
  if (b < 1024**3) return (b/1024**2).toFixed(1) + ' MB';
  if (b < 1024**4) return (b/1024**3).toFixed(2) + ' GB';
  return (b/1024**4).toFixed(2) + ' TB';
}

function esc(s) {
  return String(s || '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}

function openModal(id) { document.getElementById(id).classList.add('open'); }
function closeModal(id) { document.getElementById(id).classList.remove('open'); }

// ===== احراز هویت =====
async function authF(url, opts = {}) {
  const r = await fetch(url, opts);
  if (r.status === 401) { location.href = '/login'; throw new Error('unauthorized'); }
  return r;
}

async function logout() {
  try { await fetch('/api/logout', { method: 'POST' }); } catch(e) {}
  location.href = '/login';
}

// ===== ناوبری =====
function navTo(name) {
  document.querySelectorAll('.nav-it').forEach(n => n.classList.toggle('on', n.dataset.pg === name));
  document.querySelectorAll('.pg').forEach(p => p.classList.toggle('on', p.id === 'pg-' + name));
  document.querySelectorAll('.bottom-nav .nav-item').forEach(n => n.classList.toggle('active', n.dataset.pg === name));
  closeSb();
  const loaders = {
    dashboard: loadDashboard,
    users: loadUsers,
    quota: loadQuota,
    connections: loadConnections,
    logs: loadLogs,
    settings: () => {}
  };
  if (loaders[name]) loaders[name]();
}

document.querySelectorAll('.nav-it, .bottom-nav .nav-item').forEach(el => {
  el.addEventListener('click', () => navTo(el.dataset.pg));
});

const sb = document.getElementById('sb'), overlay = document.getElementById('overlay');
function openSb() { sb.classList.add('open'); overlay.classList.add('show'); }
function closeSb() { sb.classList.remove('open'); overlay.classList.remove('show'); }
document.getElementById('open-sb').addEventListener('click', openSb);
overlay.addEventListener('click', closeSb);

// ===== نمودار مصرف =====
async function loadChart(period) {
  chartPeriod = period || '7d';
  document.querySelectorAll('#chart-7d, #chart-30d, #chart-90d').forEach(btn => {
    btn.className = 'btn btn-sm btn-o';
  });
  const btnMap = {'7d':'chart-7d','30d':'chart-30d','90d':'chart-90d'};
  if (btnMap[period]) {
    document.getElementById(btnMap[period]).className = 'btn btn-sm btn-pur';
  }
  
  let days = 7;
  if (period === '30d') days = 30;
  if (period === '90d') days = 90;
  
  try {
    // تلاش برای گرفتن داده‌های آماری
    let dailyData = {};
    let totalUsedBytes = 0;
    
    try {
      const r = await authF('/api/stats');
      const data = await r.json();
      const hourly = data.hourly || {};
      
      for (const [key, bytes] of Object.entries(hourly)) {
        // key می‌تونه YYYY-MM-DD:HH یا YYYY-MM-DD باشه
        const dayKey = key.split(':')[0] || key;
        if (!dailyData[dayKey]) dailyData[dayKey] = 0;
        dailyData[dayKey] += bytes || 0;
        totalUsedBytes += bytes || 0;
      }
    } catch(e) { console.warn('stats API unavailable, using fallback', e); }
    
    // اگر داده‌ای نداشتیم، از /api/links برای ساخت داده روزانه استفاده می‌کنیم
    if (Object.keys(dailyData).length === 0) {
      try {
        const r2 = await authF('/api/links');
        const usersData = await r2.json();
        const links = usersData.links || [];
        const today = new Date();
        const startDate = new Date();
        startDate.setDate(startDate.getDate() - days + 1);
        
        links.forEach(l => {
          if (l.created_at) {
            try {
              const cDate = new Date(l.created_at);
              if (cDate >= startDate) {
                const dayKey = cDate.toISOString().split('T')[0];
                if (!dailyData[dayKey]) dailyData[dayKey] = 0;
                const dailyAvg = (l.used_bytes || 0) / Math.max(1, days);
                dailyData[dayKey] += dailyAvg;
              }
            } catch(e) {}
          }
          totalUsedBytes += l.used_bytes || 0;
        });
      } catch(e) { console.warn('links API fallback failed', e); }
    }
    
    // اگر باز هم خالی بود، داده‌های ثابت نمایش بدیم
    if (Object.keys(dailyData).length === 0) {
      // داده‌های نمونه برای نمایش نمودار خالی
      for (let i = 0; i < days; i++) {
        const d = new Date();
        d.setDate(d.getDate() - (days - 1 - i));
        dailyData[d.toISOString().split('T')[0]] = 0;
      }
    }
    
    // ساخت آرایه نهایی برای روزهای اخیر
    const labels = [];
    const values = [];
    const startDate = new Date();
    startDate.setDate(startDate.getDate() - days + 1);
    startDate.setHours(0, 0, 0, 0);
    
    for (let i = 0; i < days; i++) {
      const d = new Date(startDate);
      d.setDate(d.getDate() + i);
      const key = d.toISOString().split('T')[0];
      labels.push(key);
      values.push(dailyData[key] || 0);
    }
    
    const mbValues = values.map(v => Number((v / (1024 * 1024)).toFixed(2)));
    
    const labelsFa = labels.map(d => {
      const date = new Date(d);
      return date.toLocaleDateString(currentLang === 'fa' ? 'fa-IR' : 'en-US', { weekday: 'short', day: 'numeric' });
    });
    
    if (trafficChart) { trafficChart.destroy(); }
    
    const ctx = document.getElementById('trafficChart').getContext('2d');
    const gradient = ctx.createLinearGradient(0, 0, 0, 200);
    gradient.addColorStop(0, 'rgba(0, 240, 255, 0.4)');
    gradient.addColorStop(0.5, 'rgba(123, 47, 247, 0.2)');
    gradient.addColorStop(1, 'rgba(0, 240, 255, 0.02)');
    
    const lineGradient = ctx.createLinearGradient(0, 0, ctx.canvas.width, 0);
    lineGradient.addColorStop(0, '#00f0ff');
    lineGradient.addColorStop(0.5, '#7b2ff7');
    lineGradient.addColorStop(1, '#ff2e9a');
    
    trafficChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labelsFa,
        datasets: [{
          label: currentLang === 'fa' ? 'مصرف (MB)' : 'Usage (MB)',
          data: mbValues,
          borderColor: lineGradient,
          backgroundColor: gradient,
          borderWidth: 2.5,
          fill: true,
          tension: 0.4,
          pointBackgroundColor: '#00f0ff',
          pointBorderColor: '#0a0e2a',
          pointBorderWidth: 2,
          pointRadius: 3,
          pointHoverRadius: 6,
          pointHoverBackgroundColor: '#ff2e9a',
          pointHoverBorderColor: '#fff'
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            backgroundColor: 'rgba(10, 14, 35, 0.95)',
            borderColor: '#00f0ff',
            borderWidth: 1,
            titleColor: '#00f0ff',
            bodyColor: '#e8efff',
            padding: 10,
            cornerRadius: 8,
            displayColors: false,
            callbacks: {
              label: function(context) { return context.parsed.y + ' MB'; }
            }
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            ticks: { color: '#64748b', font: { size: 9 }, callback: function(value) { return value + ' MB'; } },
            grid: { color: 'rgba(0, 240, 255, 0.05)' }
          },
          x: {
            ticks: { color: '#64748b', font: { size: 9 } },
            grid: { display: false }
          }
        },
        interaction: { intersect: false, mode: 'index' }
      }
    });
  } catch(e) { console.error('loadChart error', e); }
}

// ===== بارگذاری داشبورد =====
async function loadDashboard() {
  try {
    const r = await authF('/api/dashboard/stats');
    const data = await r.json();
    document.getElementById('stat-traffic').textContent = (data.traffic.total / (1024 * 1024)).toFixed(1);
    // ⚡ v10: کارت «نسخه پنل» + «پینگ زنده» جایگزین ریکوئست‌ها
    const vEl = document.getElementById('stat-version');
    if (vEl) vEl.textContent = data.version || WORKER_VERSION;
    const abv = document.getElementById('about-version');
    if (abv) abv.textContent = data.version || WORKER_VERSION;
    document.getElementById('stat-users').textContent = data.links_count || 0;
    document.getElementById('stat-users-active').textContent = (data.active_links || 0) + (currentLang === 'fa' ? ' فعال' : ' active');
    document.getElementById('online-badge').innerHTML = '<span class="dot dg"></span> ' + (data.connections || 0) + (currentLang === 'fa' ? ' آنلاین' : ' online');
    document.getElementById('last-update').textContent = (currentLang === 'fa' ? 'بروزرسانی: ' : 'Updated: ') + new Date().toLocaleTimeString(currentLang === 'fa' ? 'fa-IR' : 'en-US');
    
    // ⚡ مصرف امروز با سقف ۱۰ گیگ روزانه (ریست ۰۳:۳۰ تهران)
    const daily = data.daily || {};
    const todayEl = document.getElementById('stat-today');
    if (todayEl) todayEl.textContent = daily.bytes_fmt || '0 B';
    const dailyBar = document.getElementById('bar-daily');
    if (dailyBar) {
      const fill = dailyBar.querySelector('div');
      if (fill) fill.style.width = Math.min(100, daily.percent || 0) + '%';
      dailyBar.classList.toggle('warn', (daily.percent || 0) >= 80 && !daily.exhausted);
      dailyBar.classList.toggle('alert', !!daily.exhausted);
    }
    const dailyBanner = document.getElementById('alert-daily');
    if (dailyBanner) {
      const key = 'pp-daily-alert-' + (daily.day || '');
      if (daily.exhausted) {
        dailyBanner.classList.add('show');
        if (!localStorage.getItem(key)) {
          localStorage.setItem(key, '1');
          toast('⚠️ ' + (currentLang === 'fa' ? 'سقف ۱۰ گیگ امروز پر شد — ریست ۰۳:۳۰ بامداد تهران' : 'Daily 10GB quota used — resets 03:30 Tehran'), 'err');
          notifyIfAllowed(currentLang === 'fa' ? '⚠️ سقف روزانه ۱۰ گیگ پر شد' : '⚠️ Daily 10GB quota reached', currentLang === 'fa' ? 'ریست ساعت ۰۳:۳۰ بامداد تهران' : 'Resets at 03:30 AM Tehran');
        }
      } else {
        dailyBanner.classList.remove('show');
      }
    }
    
    const usersR = await authF('/api/links');
    const usersData = await usersR.json();
    const links = usersData.links || [];
    const recent = links.slice(0, 4);
    const grid = document.getElementById('recent-users');
    if (!recent.length) {
      grid.innerHTML = '<div class="empty" style="padding:14px"><i class="ti ti-users"></i><p style="font-size:10px">' + (currentLang === 'fa' ? 'هیچ کاربری وجود ندارد' : 'No users') + '</p></div>';
    } else {
      grid.innerHTML = recent.map(l => `<div style="background:rgba(255,255,255,0.03);border:1px solid var(--border-subtle);border-radius:10px;padding:8px 10px;display:flex;justify-content:space-between;align-items:center;transition:border-color .3s"><div><div style="font-size:10px;font-weight:700;color:var(--t1)">${esc(l.label)}<span data-online-uuid="${l.uuid}"></span></div><div style="font-size:8px;color:var(--t3);margin-top:2px">${l.active ? '🟢' : '🔴'} ${l.uuid.slice(0,8)}…</div></div><div style="font-size:9px;color:var(--cyan);font-family:monospace;font-weight:700">${fmtB(l.used_bytes||0)}</div></div>`).join('');
      renderOnlineBadges();
    }
    
    loadChart(chartPeriod);
  } catch(e) { console.error(e); }
}

// ===== بارگذاری مصرف مجاز (سقف روزانه ۱۰ گیگ — ریست ۰۳:۳۰ بامداد تهران) =====
let quotaChart = null;
const DAILY_QUOTA_GB = 10;

async function loadQuota() {
  try {
    const statsR = await authF('/api/dashboard/stats');
    const stats = await statsR.json();
    const daily = stats.daily || {};
    
    let linksList = [];
    try {
      const r = await authF('/api/links');
      linksList = (await r.json()).links || [];
    } catch(e) { console.warn('links API failed for quota', e); }
    
    const limitBytes = daily.limit || (DAILY_QUOTA_GB * 1024 * 1024 * 1024);
    const usedBytes = daily.bytes || 0;
    const remainingBytes = Math.max(0, limitBytes - usedBytes);
    const percent = Math.min(100, (usedBytes / limitBytes) * 100);
    const usedGB = usedBytes / (1024 * 1024 * 1024);
    const remainingGB = remainingBytes / (1024 * 1024 * 1024);
    const isExhausted = !!daily.exhausted;
    const isWarning = percent >= 80 && !isExhausted;
    
    // ⏳ زمان تا ریست (۰۳:۳۰ بامداد تهران = ۰۰:۰۰ UTC)
    let resetIn = '';
    if (daily.reset_at) {
      const ms = Math.max(0, Date.parse(daily.reset_at) - Date.now());
      const hrs = Math.floor(ms / 3600000), mins = Math.floor((ms % 3600000) / 60000);
      resetIn = hrs > 0 ? hrs + (currentLang === 'fa' ? ' ساعت و ' : 'h ') + mins + (currentLang === 'fa' ? ' دقیقه' : 'm') : mins + (currentLang === 'fa' ? ' دقیقه' : 'm');
    }
    const resetEl = document.getElementById('q-reset-timer');
    if (resetEl) resetEl.textContent = (currentLang === 'fa' ? '⏳ ریست تا ' : '⏳ Resets in ') + resetIn;
    
    // آپدیت اعداد
    document.getElementById('q-used-value').textContent = usedGB.toFixed(2) + ' GB';
    document.getElementById('q-limit-value').textContent = DAILY_QUOTA_GB + ' GB';
    document.getElementById('q-remaining-value').textContent = remainingGB.toFixed(2) + ' GB';
    document.getElementById('q-percent').textContent = percent.toFixed(1) + '%';
    document.getElementById('q-mid-label').textContent = (DAILY_QUOTA_GB / 2) + ' GB';
    document.getElementById('q-end-label').textContent = DAILY_QUOTA_GB + ' GB';
    
    // آپدیت نوار پیشرفت
    const fill = document.getElementById('q-progress-fill');
    fill.style.width = percent + '%';
    
    const barBg = document.getElementById('q-progress-bar-bg');
    const percentEl = document.getElementById('q-percent');
    const alertBox = document.getElementById('q-alert');
    const remainingEl = document.getElementById('q-remaining-value');
    
    if (isExhausted) {
      fill.style.background = 'linear-gradient(90deg,#ff4d6d,#ff2e2e,#ff4d6d)';
      fill.style.boxShadow = '0 0 25px rgba(255,77,109,0.6)';
      barBg.style.borderColor = 'rgba(255,77,109,0.5)';
      barBg.style.background = 'rgba(255,77,109,0.08)';
      percentEl.style.color = 'var(--red-t)';
      percentEl.textContent = (currentLang === 'fa' ? 'تمام شد! ' : 'Exhausted! ') + percent.toFixed(1) + '%';
      remainingEl.style.color = 'var(--red-t)';
      remainingEl.textContent = '0 GB';
      alertBox.style.display = 'flex';
    } else if (isWarning) {
      fill.style.background = 'linear-gradient(90deg,#ffb800,#ff8800,#ff2e9a)';
      fill.style.boxShadow = '0 0 20px rgba(255,184,0,0.5)';
      barBg.style.borderColor = 'rgba(255,184,0,0.4)';
      barBg.style.background = 'rgba(255,184,0,0.06)';
      percentEl.style.color = 'var(--amber-t)';
      remainingEl.style.color = 'var(--amber-t)';
      alertBox.style.display = 'none';
    } else {
      fill.style.background = 'linear-gradient(90deg,var(--cyan),var(--purple),var(--magenta))';
      fill.style.boxShadow = '0 0 15px var(--cyan-soft)';
      barBg.style.borderColor = 'var(--border-subtle)';
      barBg.style.background = 'rgba(255,255,255,0.04)';
      percentEl.style.color = 'var(--cyan)';
      remainingEl.style.color = 'var(--green-t)';
      alertBox.style.display = 'none';
    }
    
    // نمایش توزیع مصرف بین کاربران (برترین‌ها)
    const usersList = document.getElementById('q-users-list');
    if (!linksList.length) {
      usersList.innerHTML = '<div class="empty"><i class="ti ti-users"></i><p style="font-size:10px">' + (currentLang === 'fa' ? 'هیچ کاربری وجود ندارد' : 'No users') + '</p></div>';
    } else {
      const top = linksList.slice().sort((a, b) => (b.used_bytes||0) - (a.used_bytes||0)).slice(0, 5);
      usersList.innerHTML = top.map((l) => {
        const used = l.used_bytes || 0;
        const limit = l.limit_bytes || 0;
        const pct = limit > 0 ? Math.min(100, (used / limit) * 100) : 0;
        const usedFmt = fmtB(used);
        const limitFmt = limit === 0 ? '∞' : fmtB(limit);
        const avatarLetter = (l.label || 'U')[0].toUpperCase();
        const isOver = limit > 0 && used >= limit;
        const barColor = isOver ? 'linear-gradient(90deg,#ff4d6d,#ff2e2e)' : 
                         pct >= 80 ? 'linear-gradient(90deg,#ffb800,#ff8800)' :
                         'linear-gradient(90deg,var(--cyan),var(--purple))';
        return `<div style="background:rgba(255,255,255,0.03);border:1px solid var(--border-subtle);border-radius:10px;padding:10px 12px">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px">
            <div style="width:30px;height:30px;border-radius:8px;background:linear-gradient(135deg,var(--cyan),var(--purple));display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:800;color:#000;flex-shrink:0">${avatarLetter}</div>
            <div style="flex:1;min-width:0">
              <div style="font-size:11px;font-weight:700;color:var(--t1);overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${esc(l.label)}<span data-online-uuid="${l.uuid}"></span></div>
              <div style="font-size:8px;color:var(--t3);font-family:monospace;margin-top:2px">${l.uuid.slice(0,8)}…</div>
            </div>
            <div style="text-align:left;flex-shrink:0">
              <div style="font-size:11px;font-weight:800;color:${isOver?'var(--red-t)':(pct>=80?'var(--amber-t)':'var(--cyan)')};font-family:monospace">${usedFmt} / ${limitFmt}</div>
              <div style="font-size:8px;color:var(--t3);margin-top:1px">${pct.toFixed(1)}% ${isOver?(currentLang==='fa'?'تمام شد':'exhausted'):''}</div>
            </div>
          </div>
          <div style="height:5px;border-radius:3px;background:rgba(255,255,255,0.05);overflow:hidden">
            <div style="height:100%;border-radius:3px;background:${barColor};width:${pct}%;transition:width .8s ease"></div>
          </div>
        </div>`;
      }).join('');
      renderOnlineBadges();
    }
    
    // نمودار مصرف ۱۴ روز اخیر با داده‌ی واقعی سمت سرور
    drawQuotaChart(stats.history_14d || {}, limitBytes, isExhausted, isWarning);
    
  } catch(e) { console.error('loadQuota error', e); }
}

function drawQuotaChart(history14, limitBytes, isExhausted, isWarning) {
  try {
    if (quotaChart) { quotaChart.destroy(); }
    
    const ctx = document.getElementById('quotaChart').getContext('2d');
    
    const keys = Object.keys(history14).sort();
    const labels = [];
    const dailyData = [];
    const limitGB = limitBytes / (1024 ** 3);
    keys.forEach(k => {
      const d = new Date(k + 'T12:00:00Z');
      labels.push(d.toLocaleDateString(currentLang === 'fa' ? 'fa-IR' : 'en-US', { weekday: 'short', day: 'numeric' }));
      dailyData.push(Number(((history14[k] || 0) / (1024 ** 3)).toFixed(3)));
    });
    if (!labels.length) { labels.push('—'); dailyData.push(0); }
    
    const lineColor = isExhausted ? '#ff4d6d' : isWarning ? '#ffb800' : '#00f0ff';
    const fillColor = isExhausted ? 'rgba(255,77,109,0.3)' : isWarning ? 'rgba(255,184,0,0.2)' : 'rgba(0,240,255,0.2)';
    
    const gradient = ctx.createLinearGradient(0, 0, 0, 200);
    gradient.addColorStop(0, fillColor);
    gradient.addColorStop(1, 'rgba(0,0,0,0.02)');
    
    quotaChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [
          {
            label: currentLang === 'fa' ? 'مصرف روزانه (GB)' : 'Daily usage (GB)',
            data: dailyData,
            borderColor: lineColor,
            backgroundColor: gradient,
            borderWidth: 2.5,
            fill: true,
            tension: 0.4,
            pointBackgroundColor: lineColor,
            pointBorderColor: '#0a0e2a',
            pointBorderWidth: 2,
            pointRadius: 3,
            pointHoverRadius: 6
          },
          {
            label: currentLang === 'fa' ? 'سقف روزانه' : 'Daily limit',
            data: labels.map(() => limitGB),
            borderColor: isExhausted ? '#ff4d6d' : '#ff2e9a',
            borderWidth: 2,
            borderDash: [6, 4],
            fill: false,
            pointRadius: 0,
            tension: 0
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: true,
            position: 'top',
            labels: { color: '#94a3b8', font: { size: 10 }, boxWidth: 12, padding: 8 }
          },
          tooltip: {
            backgroundColor: 'rgba(10, 14, 35, 0.95)',
            borderColor: lineColor,
            borderWidth: 1,
            titleColor: lineColor,
            bodyColor: '#e8efff',
            padding: 10,
            cornerRadius: 8,
            callbacks: {
              label: function(context) { return context.dataset.label + ': ' + context.parsed.y + ' GB'; }
            }
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            suggestedMax: limitGB,
            ticks: { color: '#64748b', font: { size: 9 }, callback: function(value) { return value + ' GB'; } },
            grid: { color: 'rgba(0, 240, 255, 0.05)' }
          },
          x: {
            ticks: { color: '#64748b', font: { size: 9 } },
            grid: { display: false }
          }
        },
        interaction: { intersect: false, mode: 'index' }
      }
    });
  } catch(e) { console.error('drawQuotaChart error', e); }
}

// ===== بارگذاری کاربران =====
async function loadUsers() {
  try {
    const r = await authF('/api/links');
    const { links = [] } = await r.json();
    const tbody = document.getElementById('users-tbody');
    const total = links.length;
    const active = links.filter(l => l.active && !l.expired).length;
    const expired = links.filter(l => l.expired).length;
    const totalTraffic = links.reduce((sum, l) => sum + (l.used_bytes || 0), 0);
    
    document.getElementById('users-total').textContent = total;
    document.getElementById('users-active').textContent = active;
    document.getElementById('users-expired').textContent = expired;
    document.getElementById('users-traffic').textContent = fmtB(totalTraffic);
    document.getElementById('users-count-label').textContent = total + (currentLang === 'fa' ? ' کاربر' : ' users');
    
    if (!links.length) {
      tbody.innerHTML = '<tr><td colspan="6" style="text-align:center;padding:30px;color:var(--t3);">' + (currentLang === 'fa' ? 'هیچ کاربری وجود ندارد' : 'No users found') + '</td></tr>';
      return;
    }
    
    const fpEmoji = { chrome: '🌐', firefox: '🦊', safari: '🧭', edge: '🌊', ios: '📱', android: '🤖', safari_ios: '🍏', random: '🎲', none: '🚫' };
    const protocolIcons = { 'vless-ws':'🚀', 'vless-grpc':'⚡', 'vless-xhttp':'🛡️', 'vless-http2':'📶', 'trojan-ws':'🔒', 'shadowsocks':'🌊' };
    
    tbody.innerHTML = links.map(l => {
      const isActive = l.active && !l.expired;
      const statusClass = isActive ? 'active' : (l.expired ? 'expired' : 'disabled');
      const statusText = isActive ? (currentLang === 'fa' ? 'فعال' : 'Active') : (l.expired ? (currentLang === 'fa' ? 'منقضی' : 'Expired') : (currentLang === 'fa' ? 'غیرفعال' : 'Disabled'));
      const pct = l.limit_bytes === 0 ? 0 : Math.min(100, (l.used_bytes / l.limit_bytes) * 100);
      const usedFmt = fmtB(l.used_bytes || 0);
      const limitFmt = l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes);
      const fp = l.fingerprint || 'chrome';
      const fpName = { chrome: 'Chrome', firefox: 'Firefox', safari: 'Safari', edge: 'Edge', ios: 'iOS', android: 'Android', safari_ios: 'Safari iOS', random: 'Random', none: 'None' }[fp] || fp;
      const protocol = l.protocol || 'vless-ws';
      const protoIcon = protocolIcons[protocol] || '🚀';
      const protoName = { 'vless-ws':'VLESS-WS', 'vless-grpc':'VLESS-gRPC', 'vless-xhttp':'VLESS-XHTTP', 'vless-http2':'VLESS-HTTP/2', 'trojan-ws':'Trojan-WS', 'shadowsocks':'Shadowsocks' }[protocol] || protocol;
      const httpVer = l.http_version || 'h2';
      const httpName = { 'h1':'HTTP/1.1', 'h2':'HTTP/2', 'h3':'HTTP/3', 'auto':'Auto' }[httpVer] || httpVer;
      let duration = '∞';
      if (l.expires_at) {
        try {
          const exp = new Date(l.expires_at);
          const now = new Date();
          const days = Math.ceil((exp - now) / (1000 * 60 * 60 * 24));
          duration = days > 0 ? days + (currentLang === 'fa' ? ' روز' : ' days') : (currentLang === 'fa' ? 'منقضی' : 'Expired');
        } catch(e) { duration = '—'; }
      }
      const avatarLetter = (l.label || 'U')[0].toUpperCase();
      const cFlag = '';
      return `<tr><td><div class="user-name-cell"><div class="avatar">${avatarLetter}</div><div><div class="name">${esc(l.label)}<span data-online-uuid="${l.uuid}"></span></div><div class="uuid-short">${l.uuid.slice(0,8)}… ${protoIcon} ${protoName}${cFlag}</div></div></div></td><td style="font-size:10px;color:var(--t2);">${fpEmoji[fp] || '🌐'} ${fpName}<br><span style="font-size:8px;color:var(--t3)">${httpName}</span></td><td><span class="status-badge ${statusClass}"><span class="status-dot"></span>${statusText}</span></td><td><div class="usage-bar"><span class="usage-text">${usedFmt} / ${limitFmt}</span><div class="bar"><div class="fill" style="width:${pct}%"></div></div></div></td><td style="font-size:11px;color:var(--t2);">${duration}</td><td><div class="action-btns"><button class="btn btn-pur btn-sm" onclick="showQR('${l.sub_url}')" title="QR Code"><i class="ti ti-qrcode"></i></button><button class="btn btn-pur btn-sm" onclick="navigator.clipboard.writeText('${esc(l.sub_url)}').then(()=>toast('${currentLang === 'fa' ? '✅ کپی ساب' : '✅ Copied'}','ok'))" title="${currentLang === 'fa' ? 'کپی ساب‌لینک' : 'Copy sub'}"><i class="ti ti-link"></i></button><button class="btn btn-amber btn-sm" onclick="resetUsage('${l.uuid}')" title="${currentLang === 'fa' ? 'ریست مصرف' : 'Reset usage'}"><i class="ti ti-rotate"></i></button><button class="btn btn-pur btn-sm" onclick="openEditModal('${l.uuid}')" title="${currentLang === 'fa' ? 'ویرایش' : 'Edit'}"><i class="ti ti-edit"></i></button><button class="btn btn-d btn-sm" onclick="openDeleteModal('${l.uuid}')" title="${currentLang === 'fa' ? 'حذف' : 'Delete'}"><i class="ti ti-trash"></i></button></div></td></tr>`;
    }).join('');
  } catch(e) { console.error(e); }
}

// ===== QR Code =====
function showQR(url) {
  const container = document.getElementById('qrcode-container');
  container.innerHTML = '';
  if (qrCodeInstance) { qrCodeInstance.clear(); qrCodeInstance = null; }
  qrCodeInstance = new QRCode(container, {
    text: url,
    width: 200,
    height: 200,
    colorDark: '#00f0ff',
    colorLight: '#0a0e2a',
    correctLevel: QRCode.CorrectLevel.H
  });
  openModal('modal-qr');
  container.dataset.url = url;
}

function downloadQR() {
  const canvas = document.querySelector('#qrcode-container canvas');
  if (!canvas) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); return; }
  const link = document.createElement('a');
  link.download = 'qrcode.png';
  link.href = canvas.toDataURL('image/png');
  link.click();
  toast('✅ ' + (currentLang === 'fa' ? 'QR دانلود شد' : 'QR downloaded'), 'ok');
}

// ===== مدیریت کاربران با تقویم =====
function initDatePickers() {
  if (expiryPicker) expiryPicker.destroy();
  expiryPicker = flatpickr("#user-expiry-date", {
    locale: currentLang === 'fa' ? 'fa' : 'en',
    dateFormat: "Y-m-d",
    minDate: "today",
    disableMobile: true,
    placeholder: currentLang === 'fa' ? 'انتخاب تاریخ انقضا' : 'Select expiry date',
    allowInput: true,
    onChange: function(selectedDates, dateStr, instance) {
      if (dateStr) document.getElementById('user-expiry-date').value = dateStr;
    }
  });
  
  if (editExpiryPicker) editExpiryPicker.destroy();
  editExpiryPicker = flatpickr("#edit-expiry-date", {
    locale: currentLang === 'fa' ? 'fa' : 'en',
    dateFormat: "Y-m-d",
    minDate: "today",
    disableMobile: true,
    placeholder: currentLang === 'fa' ? 'انتخاب تاریخ انقضا' : 'Select expiry date',
    allowInput: true,
    onChange: function(selectedDates, dateStr, instance) {
      if (dateStr) document.getElementById('edit-expiry-date').value = dateStr;
    }
  });
}

async function saveUser() {
  const label = document.getElementById('user-label').value.trim() || 'کاربر';
  const quota = parseFloat(document.getElementById('user-quota').value) || 0;
  const expiryDate = document.getElementById('user-expiry-date').value;
  const devices = parseInt(document.getElementById('user-devices').value) || 0;
  const fingerprint = document.getElementById('user-fingerprint').value || 'chrome';
  // ⚡ پروتکل حذف شد — همیشه VLESS-WS (تنها پروتکلی که وصل می‌شود)
  const http_version = document.getElementById('user-http').value || 'h2';
  
  let expires_days = 0;
  if (expiryDate) {
    const exp = new Date(expiryDate);
    const now = new Date();
    expires_days = Math.ceil((exp - now) / (1000 * 60 * 60 * 24));
    if (expires_days < 0) expires_days = 0;
  }
  
  try {
    const r = await authF('/api/links', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ label, limit_value: quota, limit_unit: 'GB', expires_days, max_devices: devices, fingerprint, http_version })
    });
    if (!r.ok) throw new Error();
    const _cd = await r.json().catch(() => ({}));
    if (_cd && _cd.persisted === false) toast('⚠️ ' + (currentLang === 'fa' ? 'ساخته شد ولی ذخیره ابری ناموفق بود — سهمیه KV امروز پر است؛ بعد از ریست (۰۳:۳۰ تهران) دوباره ذخیره می‌شود یا کاربر را بسازید' : 'Created, but cloud save failed — daily KV quota exhausted; will retry after reset'), 'warn', 9000);
    document.getElementById('user-label').value = 'کاربر';
    document.getElementById('user-quota').value = '2';
    document.getElementById('user-expiry-date').value = '';
    document.getElementById('user-devices').value = '1';
    document.getElementById('user-fingerprint').value = 'chrome';
    document.getElementById('user-http').value = 'h2';
    closeModal('modal-user');
    toast('✅ ' + (currentLang === 'fa' ? 'کاربر ساخته شد' : 'User created'), 'ok');
    loadUsers();
    loadDashboard();
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

async function openEditModal(uuid) {
  try {
    const r = await authF('/api/links');
    const { links = [] } = await r.json();
    const link = links.find(l => l.uuid === uuid);
    if (!link) { toast((currentLang === 'fa' ? 'کاربر یافت نشد' : 'User not found'), 'err'); return; }
    document.getElementById('edit-uuid').value = uuid;
    document.getElementById('edit-label').value = link.label || '';
    document.getElementById('edit-quota').value = link.limit_bytes === 0 ? '' : (link.limit_bytes / (1024 ** 3)).toFixed(1);
    
    if (link.expires_at) {
      const expDate = new Date(link.expires_at);
      const dateStr = expDate.toISOString().split('T')[0];
      document.getElementById('edit-expiry-date').value = dateStr;
      if (editExpiryPicker) editExpiryPicker.setDate(dateStr);
    } else {
      document.getElementById('edit-expiry-date').value = '';
      if (editExpiryPicker) editExpiryPicker.clear();
    }
    
    document.getElementById('edit-devices').value = link.max_devices || 0;
    document.getElementById('edit-status').value = link.active ? 'true' : 'false';
    document.getElementById('edit-fingerprint').value = link.fingerprint || 'chrome';
    document.getElementById('edit-http').value = link.http_version || 'h2';
    openModal('modal-edit');
  } catch(e) { toast((currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

async function saveEdit() {
  const uuid = document.getElementById('edit-uuid').value;
  const label = document.getElementById('edit-label').value.trim() || 'کاربر';
  const quota = parseFloat(document.getElementById('edit-quota').value) || 0;
  const expiryDate = document.getElementById('edit-expiry-date').value;
  const devices = parseInt(document.getElementById('edit-devices').value) || 0;
  const active = document.getElementById('edit-status').value === 'true';
  const fingerprint = document.getElementById('edit-fingerprint').value || 'chrome';
  // ⚡ پروتکل حذف شد — همیشه VLESS-WS
  const http_version = document.getElementById('edit-http').value || 'h2';
  
  let expires_days = 0;
  if (expiryDate) {
    const exp = new Date(expiryDate);
    const now = new Date();
    expires_days = Math.ceil((exp - now) / (1000 * 60 * 60 * 24));
    if (expires_days < 0) expires_days = 0;
  }
  
  try {
    const r = await authF('/api/links/' + uuid, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ label, limit_value: quota, limit_unit: 'GB', expires_days, max_devices: devices, active, fingerprint, http_version })
    });
    if (!r.ok) { throw new Error(); }
    const _ed = await r.json().catch(() => ({}));
    if (_ed && _ed.persisted === false) toast('⚠️ ' + (currentLang === 'fa' ? 'ویرایش شد ولی روی فضای ابری ذخیره نشد — سهمیه KV امروز پر است' : 'Saved, but cloud write failed — daily KV quota exhausted'), 'warn', 9000);
    closeModal('modal-edit');
    toast('✅ ' + (currentLang === 'fa' ? 'ویرایش شد' : 'Saved'), 'ok');
    loadUsers();
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

function openDeleteModal(uuid) {
  document.getElementById('delete-uuid').value = uuid;
  openModal('modal-delete');
}

async function confirmDelete() {
  const uuid = document.getElementById('delete-uuid').value;
  try {
    const r = await authF('/api/links/' + uuid, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({})
    });
    if (!r.ok) { throw new Error(); }
    const _dd = await r.json().catch(() => ({}));
    if (_dd && _dd.persisted === false) toast('⚠️ ' + (currentLang === 'fa' ? 'حذف شد ولی روی فضای ابری ثبت نشد — ممکن است بعداً برگردد؛ سهمیه KV امروز پر است' : 'Deleted, but cloud write failed — user may reappear; daily KV quota exhausted'), 'warn', 9000);
    closeModal('modal-delete');
    toast('✅ ' + (currentLang === 'fa' ? 'حذف شد' : 'Deleted'), 'ok');
    loadUsers();
    loadDashboard();
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

async function resetUsage(uuid) {
  if (!confirm(currentLang === 'fa' ? 'ریست مصرف؟' : 'Reset usage?')) return;
  try {
    const r = await authF('/api/links/' + uuid, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ reset_usage: true })
    });
    if (!r.ok) throw new Error();
    toast('✅ ' + (currentLang === 'fa' ? 'ریست شد' : 'Reset'), 'ok');
    loadUsers();
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

// ===== بارگذاری اتصالات =====
async function loadConnections() {
  try {
    const r = await authF('/api/connections');
    const d = await r.json();
    // ⚡ شمارش زنده به تفکیک کاربر — برای بج «چند نفر وصل‌اند» کنار هر کاربر
    window._onlineByUuid = d.by_uuid || {};
    renderOnlineBadges();
    const grid = document.getElementById('conns-grid');
    const count = d.count || 0;
    document.getElementById('conn-count').textContent = count + (currentLang === 'fa' ? ' اتصال' : ' connections');
    if (!count) {
      grid.innerHTML = '<div class="empty"><i class="ti ti-plug-off"></i><p>' + (currentLang === 'fa' ? 'هیچ اتصالی وجود ندارد' : 'No connections') + '</p></div>';
      return;
    }
    grid.innerHTML = d.connections.map(c => {
      const secs = c.connected_at ? Math.max(0, Math.floor((Date.now() - new Date(c.connected_at).getTime()) / 1000)) : 0;
      const dur = secs < 60 ? secs + 's' : secs < 3600 ? Math.floor(secs / 60) + 'm' : Math.floor(secs / 3600) + 'h';
      return `<div class="conn-card"><div class="ip"><span class="conn-status-dot"></span> ${esc(c.ip)}</div><div class="label">${esc(c.label || 'نامشخص')}</div><div class="conn-info"><span>📥 ${esc(c.bytes_fmt || '0 B')}</span><span>⏱ ${dur}</span></div></div>`;
    }).join('');
  } catch(e) { console.error(e); }
}

// ===== ⚡ بج آنلاین هر کاربر: چند نفر همین حالا به کانفیگش وصل‌اند =====
function renderOnlineBadges() {
  const map = window._onlineByUuid || {};
  document.querySelectorAll('[data-online-uuid]').forEach(el => {
    const uid = el.getAttribute('data-online-uuid');
    const info = map[uid];
    const sessions = info ? info.sessions : 0;
    const ips = info ? info.ip_count : 0;
    if (sessions > 0) {
      el.className = 'online-badge on';
      el.title = (currentLang === 'fa' ? 'اتصال فعال' : 'active sessions') + ': ' + sessions + (ips > 1 ? ' · ' + (currentLang === 'fa' ? 'آی‌پی' : 'IPs') + ': ' + ips : '');
      el.innerHTML = '<span class="odot"></span>' + sessions;
    } else {
      el.className = 'online-badge off';
      el.title = currentLang === 'fa' ? 'آفلاین' : 'offline';
      el.innerHTML = '<span class="odot"></span>0';
    }
  });
}

// ===== ⚡ v10 پینگ زنده + نسخه پنل — جایگزین کامل شمارش ریکوئست =====
const WORKER_VERSION = 'v10.4';
function updatePingCard(ms) {
  const fa = currentLang === 'fa';
  const q = pingQualityInfo(ms);
  const el = document.getElementById('stat-ping');
  if (el) { el.textContent = ms < 0 ? '✕' : ms; el.style.color = q.color; el.style.textShadow = '0 0 14px ' + q.color + '55'; }
  const sub = document.getElementById('s-ping-sub');
  if (sub) sub.textContent = ms < 0 ? (fa ? '⛔ قطع' : 'down') : (q.txt.replace('✦ ', '') + ' · ' + ms + 'ms');
}

// ===== ⚡ v10 ربات تلگرام — اتصال از تنظیمات =====
async function saveTelegram() {
  const token = document.getElementById('tg-token').value.trim();
  const chat_id = document.getElementById('tg-chat').value.trim();
  if (!token || !chat_id) { toast('❌ ' + (currentLang === 'fa' ? 'توکن و آیدی عددی را وارد کن' : 'Enter bot token & numeric ID'), 'err'); return; }
  toast('⏳ ' + (currentLang === 'fa' ? 'در حال اتصال به تلگرام…' : 'Connecting to Telegram…'), 'ok');
  try {
    const r = await authF('/api/settings/telegram', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ token, chat_id }) });
    const d = await r.json();
    if (!r.ok) { toast('❌ ' + (d.detail || 'Error'), 'err'); return; }
    if (d.saved === false) { toast('⚠️ ' + (currentLang === 'fa' ? 'اتصال شد ولی ذخیره‌سازی پنل موقتاً در دسترس نیست — چند دقیقه بعد دوباره «فعال‌سازی» را بزن' : 'Connected but not saved - try again soon'), 'err'); return; }
    document.getElementById('tg-token').value = '';
    document.getElementById('tg-chat').value = '';
    toast('✅ ' + (currentLang === 'fa' ? 'ربات فعال شد! حالا در تلگرام به ربات /start بده' : 'Bot activated! Now send /start to your bot'), 'ok');
    loadTelegramStatus();
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}
async function disableTelegram() {
  try { await authF('/api/settings/telegram/disable', { method: 'POST' }); toast('✅ ' + (currentLang === 'fa' ? 'ربات قطع شد' : 'Bot disconnected'), 'ok'); loadTelegramStatus(); } catch(e) {}
}
async function loadTelegramStatus() {
  const el = document.getElementById('tg-status');
  if (!el) return;
  try {
    const r = await authF('/api/settings/telegram');
    const d = await r.json();
    if (d && d.configured) el.innerHTML = (currentLang === 'fa' ? '🟢 متصل به @' : '🟢 Connected to @') + (d.bot_username || '?') + ' · ID: ' + d.chat_id;
    else el.textContent = (currentLang === 'fa' ? '⚪ غیرفعال — توکن و آیدی را وارد کن' : '⚪ Not configured — enter token & ID');
  } catch(e) { el.textContent = '—'; }
}

function notifyIfAllowed(title, body) {
  try {
    if ('Notification' in window && Notification.permission === 'granted') {
      new Notification(title, { body });
    }
  } catch(e) {}
}

// ===== ⚡ تغییر اعتبارنامه ادمین از تنظیمات =====
async function saveCredentials() {
  const username = document.getElementById('cred-username').value.trim();
  const new_password = document.getElementById('cred-password').value;
  const current_password = document.getElementById('cred-current').value;
  if (!current_password) { toast('❌ ' + (currentLang === 'fa' ? 'رمز فعلی را وارد کن' : 'Enter current password'), 'err'); return; }
  if (username.length < 3) { toast('❌ ' + (currentLang === 'fa' ? 'نام کاربری حداقل ۳ کاراکتر' : 'Username min 3 chars'), 'err'); return; }
  if (new_password.length < 6) { toast('❌ ' + (currentLang === 'fa' ? 'رمز جدید حداقل ۶ کاراکتر' : 'Password min 6 chars'), 'err'); return; }
  try {
    const r = await authF('/api/settings/credentials', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, new_password, current_password })
    });
    const d = await r.json();
    if (!r.ok) { toast('❌ ' + (d.detail || (currentLang === 'fa' ? 'خطا' : 'Error')), 'err'); return; }
    document.getElementById('cred-password').value = '';
    document.getElementById('cred-current').value = '';
    toast('✅ ' + (currentLang === 'fa' ? 'اعتبارنامه تغییر کرد — از این به بعد با همان وارد شو' : 'Credentials updated'), 'ok');
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

// ===== بارگذاری لاگ‌ها =====
async function loadLogs() {
  try {
    const r = await authF('/api/activity');
    const data = await r.json();
    const logs = data.logs || [];
    document.getElementById('logs-count').textContent = logs.length + (currentLang === 'fa' ? ' لاگ' : ' logs');
    const container = document.getElementById('logs-container');
    if (!logs.length) {
      container.innerHTML = '<div class="empty"><i class="ti ti-notes"></i><p>' + (currentLang === 'fa' ? 'هیچ لاگی وجود ندارد' : 'No logs') + '</p></div>';
      return;
    }
    container.innerHTML = logs.map(log => {
      const time = log.time ? new Date(log.time).toLocaleString(currentLang === 'fa' ? 'fa-IR' : 'en-US') : '—';
      const color = log.level === 'err' ? 'var(--red-t)' : log.level === 'warn' ? 'var(--amber-t)' : 'var(--cyan)';
      return `<div style="padding:4px 0;border-bottom:1px solid rgba(0,240,255,0.04);display:flex;gap:8px;flex-wrap:wrap"><span style="color:${color};font-weight:700;text-shadow:0 0 6px ${color}">[${(log.level || 'info').toUpperCase()}]</span><span style="color:var(--t3)">${time}</span><span style="color:var(--t1)">${esc(log.message)}</span></div>`;
    }).join('');
  } catch(e) { console.error(e); }
}

// ===== بکاپ ===== (RGB حذف شد — تم‌های سه‌گانه جایگزین)
async function createBackup() {
  try {
    const r = await authF('/api/backup');
    const data = await r.json();
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `persepolis_backup_${new Date().toISOString().slice(0,10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
    toast('✅ ' + (currentLang === 'fa' ? 'بکاپ دانلود شد' : 'Backup downloaded'), 'ok');
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); }
}

async function restoreBackup(event) {
  const file = event.target.files[0];
  if (!file) return;
  try {
    const text = await file.text();
    const data = JSON.parse(text);
    const r = await authF('/api/backup/restore', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    if (!r.ok) { toast('❌ ' + (currentLang === 'fa' ? 'خطا' : 'Error'), 'err'); return; }
    toast('✅ ' + (currentLang === 'fa' ? 'بکاپ بازیابی شد' : 'Backup restored'), 'ok');
    setTimeout(() => location.reload(), 1000);
  } catch(e) { toast('❌ ' + (currentLang === 'fa' ? 'خطا: ' : 'Error: ') + e.message, 'err'); }
  event.target.value = '';
}

// ========================================
// ✦ WTF Factor #1: Command Palette ✦
// ========================================
let cmdkItems = [];
let cmdkActiveIdx = 0;
let cmdkFiltered = [];

function buildCmdkItems() {
  const t = translations[currentLang];
  cmdkItems = [
    {cat: 'actions', icon: 'ti-user-plus', title: t.cmdk_open_user, desc: t.cmdk_open_user_d, shortcut: 'N', action: () => openModal('modal-user')},
    {cat: 'navigation', icon: 'ti-layout-dashboard', title: t.cmdk_nav_dashboard, desc: t.cmdk_nav_dashboard_d, shortcut: 'G H', action: () => navTo('dashboard')},
    {cat: 'navigation', icon: 'ti-users', title: t.cmdk_nav_users, desc: t.cmdk_nav_users_d, shortcut: 'G U', action: () => navTo('users')},
    {cat: 'navigation', icon: 'ti-gauge', title: t.cmdk_nav_quota, desc: t.cmdk_nav_quota_d, shortcut: 'G Q', action: () => navTo('quota')},
    {cat: 'navigation', icon: 'ti-plug-connected', title: t.cmdk_nav_connections, desc: t.cmdk_nav_connections_d, shortcut: 'G C', action: () => navTo('connections')},
    {cat: 'navigation', icon: 'ti-settings', title: t.cmdk_nav_settings, desc: t.cmdk_nav_settings_d, shortcut: 'G S', action: () => navTo('settings')},
    {cat: 'navigation', icon: 'ti-notes', title: t.cmdk_nav_logs, desc: t.cmdk_nav_logs_d, shortcut: 'G L', action: () => navTo('logs')},
    {cat: 'navigation', icon: 'ti-database', title: t.cmdk_nav_backup, desc: t.cmdk_nav_backup_d, shortcut: 'G B', action: () => navTo('backup')},
    {cat: 'settings', icon: 'ti-color-swatch', title: t.cmdk_toggle_theme, desc: t.cmdk_toggle_theme_d, shortcut: 'T', action: () => setTheme(currentTheme === 'obsidian' ? 'cosmic' : currentTheme === 'cosmic' ? 'bumblebee' : currentTheme === 'bumblebee' ? 'white' : 'obsidian')},
    {cat: 'settings', icon: 'ti-logout', title: t.cmdk_logout, desc: t.cmdk_logout_d, shortcut: 'L', action: () => logout()},
    {cat: 'actions', icon: 'ti-refresh', title: t.cmdk_refresh, desc: t.cmdk_refresh_d, shortcut: 'F5', action: () => { loadDashboard(); loadUsers(); loadQuota(); }},
    {cat: 'actions', icon: 'ti-download', title: t.cmdk_backup, desc: t.cmdk_backup_d, shortcut: 'B', action: () => createBackup()}
  ];
}

function initCmdk() {
  buildCmdkItems();
  filterCmdk();
  document.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      openCmdk();
    }
    if (e.key === 'Escape') closeCmdk();
  });
}

function openCmdk() {
  document.getElementById('cmdkOverlay').classList.add('open');
  const inp = document.getElementById('cmdkInput');
  inp.value = '';
  inp.focus();
  filterCmdk();
}

function closeCmdk() {
  document.getElementById('cmdkOverlay').classList.remove('open');
}

function filterCmdk() {
  const q = (document.getElementById('cmdkInput').value || '').trim().toLowerCase();
  cmdkFiltered = q ? cmdkItems.filter(it => it.title.toLowerCase().includes(q) || it.desc.toLowerCase().includes(q) || it.cat.includes(q)) : cmdkItems;
  cmdkActiveIdx = 0;
  renderCmdk();
}

function renderCmdk() {
  const t = translations[currentLang];
  const list = document.getElementById('cmdkList');
  if (!cmdkFiltered.length) {
    list.innerHTML = '<div class="cmdk-empty"><i class="ti ti-mood-empty"></i>' + t.cmdk_no_results + '</div>';
    return;
  }
  let html = '';
  let lastCat = '';
  cmdkFiltered.forEach((it, idx) => {
    if (it.cat !== lastCat) {
      const catName = t['cmdk_cat_' + it.cat] || it.cat;
      html += '<div class="cmdk-category">' + catName + '</div>';
      lastCat = it.cat;
    }
    const cls = idx === cmdkActiveIdx ? 'cmdk-item active' : 'cmdk-item';
    html += '<div class="' + cls + '" onclick="execCmdk(' + idx + ')" onmouseenter="setCmdkActive(' + idx + ')"><div class="cmdk-icon"><i class="ti ' + it.icon + '"></i></div><div class="cmdk-text"><div class="cmdk-title">' + it.title + '</div><div class="cmdk-desc">' + it.desc + '</div></div><span class="cmdk-shortcut">' + it.shortcut + '</span></div>';
  });
  list.innerHTML = html;
}

function setCmdkActive(idx) {
  cmdkActiveIdx = idx;
  renderCmdk();
}

function execCmdk(idx) {
  if (!cmdkFiltered[idx]) return;
  closeCmdk();
  setTimeout(() => cmdkFiltered[idx].action(), 150);
}

// ========== keyboard navigation in command palette ==========
document.addEventListener('keydown', (e) => {
  const overlay = document.getElementById('cmdkOverlay');
  if (!overlay.classList.contains('open')) return;
  if (e.key === 'ArrowDown') {
    e.preventDefault();
    cmdkActiveIdx = Math.min(cmdkFiltered.length - 1, cmdkActiveIdx + 1);
    renderCmdk();
  } else if (e.key === 'ArrowUp') {
    e.preventDefault();
    cmdkActiveIdx = Math.max(0, cmdkActiveIdx - 1);
    renderCmdk();
  } else if (e.key === 'Enter') {
    e.preventDefault();
    execCmdk(cmdkActiveIdx);
  }
});

// ========================================
// ✦ WTF Factor #2: Counter Up Animation ✦
// ========================================
function animateCounter(el, target, duration = 1000, suffix = '') {
  const start = parseFloat(el.dataset.currentValue || '0') || 0;
  const startTime = performance.now();
  el.classList.add('counting');
  
  function step(now) {
    const elapsed = now - startTime;
    const progress = Math.min(1, elapsed / duration);
    const eased = 1 - Math.pow(1 - progress, 3);
    const value = start + (target - start) * eased;
    let display = Number.isInteger(target) ? Math.round(value) : value.toFixed(1);
    el.textContent = display + suffix;
    el.dataset.currentValue = value;
    if (progress < 1) {
      requestAnimationFrame(step);
    } else {
      el.classList.remove('counting');
    }
  }
  requestAnimationFrame(step);
}

// ========================================
// ✦ WTF Factor #5: Real-time Activity Feed ✦
// ========================================
let activityLog = [];

function addActivity(type, text, user) {
  const now = new Date();
  const timeStr = now.toLocaleTimeString(currentLang === 'fa' ? 'fa-IR' : 'en-US');
  activityLog.unshift({type, text, user, time: timeStr});
  if (activityLog.length > 30) activityLog.pop();
  renderActivityFeed();
  // اگه notification permission داشتیم، نشون بده
  if (type === 'error' || type === 'warning') {
    showDesktopNotification(type === 'error' ? '⚠️' : '💡', text);
  }
}

function renderActivityFeed() {
  const feedEl = document.getElementById('activityFeed');
  if (!feedEl) return;
  if (!activityLog.length) {
    feedEl.innerHTML = '<div class="empty"><i class="ti ti-activity"></i><p style="font-size:10px">هنوز فعالیتی ثبت نشده</p></div>';
    return;
  }
  const iconMap = {info: 'ti-info-circle', success: 'ti-check', warning: 'ti-alert-triangle', error: 'ti-alert-octagon'};
  feedEl.innerHTML = activityLog.map(a => {
    const userText = a.user ? '<span class="activity-user">' + esc(a.user) + '</span> · ' : '';
    return '<div class="activity-item"><div class="activity-icon ' + a.type + '"><i class="ti ' + (iconMap[a.type] || 'ti-info-circle') + '"></i></div><div class="activity-text">' + userText + a.text + '<div class="activity-time">' + a.time + '</div></div></div>';
  }).join('');
}

async function loadActivityFeed() {
  try {
    const r = await authF('/api/activity');
    const data = await r.json();
    const logs = (data.logs || []).slice(0, 15).reverse();
    activityLog = logs.map(l => {
      const type = l.level === 'err' ? 'error' : l.level === 'warn' ? 'warning' : 'info';
      return {type, text: l.message || l.text || '', user: l.user || '', time: l.time ? new Date(l.time).toLocaleTimeString(currentLang === 'fa' ? 'fa-IR' : 'en-US') : ''};
    });
    activityLog.reverse();
    // اضافه کردن ورود به پنل به‌عنوان اولین فعالیت
    activityLog.unshift({type: 'success', text: translations[currentLang].activity_login, user: '', time: new Date().toLocaleTimeString(currentLang === 'fa' ? 'fa-IR' : 'en-US')});
    renderActivityFeed();
  } catch(e) {
    activityLog = [{type: 'success', text: translations[currentLang].activity_login, user: '', time: new Date().toLocaleTimeString(currentLang === 'fa' ? 'fa-IR' : 'en-US')}];
    renderActivityFeed();
  }
}


// ========================================
// ✦ WTF Factor #7: Desktop Notifications ✦
// ========================================
function showDesktopNotification(emoji, body) {
  if (!('Notification' in window)) return;
  if (Notification.permission !== 'granted') return;
  try {
    new Notification('✦ PERSEPOLIS', {
      body: emoji + ' ' + body,
      icon: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><text y="80" font-size="80">🏛️</text></svg>',
      badge: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" fill="%2300f0ff"/></svg>',
      tag: 'persepolis-' + Date.now()
    });
  } catch(e) { console.warn('Notification error', e); }
}

function addNotifPermissionCard() {
  const settingsSection = document.getElementById('pg-settings');
  if (!settingsSection) return;
  if (!('Notification' in window)) return;
  if (Notification.permission === 'granted') return;
  
  const t = translations[currentLang];
  const card = document.createElement('div');
  card.className = 'notif-perm-card';
  card.innerHTML = '<i class="ti ti-bell"></i><div style="flex:1"><div style="font-weight:700;color:var(--t1)">' + t.notif_enable + '</div><div>' + t.notif_desc + '</div></div><button onclick="requestNotifPermission()">' + t.notif_enable_btn + '</button>';
  settingsSection.appendChild(card);
}

function requestNotifPermission() {
  Notification.requestPermission().then(p => {
    if (p === 'granted') {
      toast('✅ ' + (currentLang === 'fa' ? 'اطلاع‌رسانی فعال شد' : 'Notifications enabled'), 'ok');
      showDesktopNotification('🎉', currentLang === 'fa' ? 'اطلاع‌رسانی دسکتاپ فعال شد' : 'Desktop notifications enabled');
      document.querySelectorAll('.notif-perm-card').forEach(c => c.remove());
    }
  });
}

// ========================================
// ✦ WTF Factor #8: Drag & Drop Reorder ✦
// ========================================
function initDragAndDrop() {
  const tbody = document.getElementById('users-tbody');
  if (!tbody) return;
  let draggedRow = null;
  
  tbody.addEventListener('dragstart', (e) => {
    if (!e.target.closest('tr[data-uuid]')) return;
    draggedRow = e.target.closest('tr[data-uuid]');
    draggedRow.classList.add('dragging');
    e.dataTransfer.effectAllowed = 'move';
  });
  
  tbody.addEventListener('dragend', (e) => {
    if (draggedRow) draggedRow.classList.remove('dragging');
    document.querySelectorAll('.drag-over').forEach(r => r.classList.remove('drag-over'));
    draggedRow = null;
  });
  
  tbody.addEventListener('dragover', (e) => {
    e.preventDefault();
    const target = e.target.closest('tr[data-uuid]');
    if (target && target !== draggedRow) {
      document.querySelectorAll('.drag-over').forEach(r => r.classList.remove('drag-over'));
      target.classList.add('drag-over');
    }
  });
  
  tbody.addEventListener('drop', (e) => {
    e.preventDefault();
    const target = e.target.closest('tr[data-uuid]');
    if (target && draggedRow && target !== draggedRow) {
      const rows = Array.from(tbody.querySelectorAll('tr[data-uuid]'));
      const fromIdx = rows.indexOf(draggedRow);
      const toIdx = rows.indexOf(target);
      if (fromIdx < toIdx) {
        target.parentNode.insertBefore(draggedRow, target.nextSibling);
      } else {
        target.parentNode.insertBefore(draggedRow, target);
      }
      saveUserOrder();
    }
  });
}

function saveUserOrder() {
  const order = Array.from(document.querySelectorAll('#users-tbody tr[data-uuid]')).map(tr => tr.dataset.uuid);
  try { localStorage.setItem('persepolis-user-order', JSON.stringify(order)); } catch(e) {}
}

// ========================================
// ✦ WTF Factor #9: Live Search + Filter ✦
// ========================================
let userFilter = 'all';
let allUsersCache = [];

function setUserFilter(filter) {
  userFilter = filter;
  document.querySelectorAll('.filter-chip').forEach(c => c.classList.toggle('active', c.dataset.filter === filter));
  applyUserFilters();
}

function applyUserFilters() {
  const q = (document.getElementById('userSearch').value || '').toLowerCase().trim();
  const tbody = document.getElementById('users-tbody');
  if (!tbody || !allUsersCache.length) return;
  
  const filtered = allUsersCache.filter(l => {
    const isActive = l.active && !l.expired;
    // filter chips
    if (userFilter === 'active' && !isActive) return false;
    if (userFilter === 'expired' && !l.expired) return false;
    if (userFilter === 'disabled' && (l.active || l.expired)) return false;
    if (userFilter === 'high-usage') {
      const pct = l.limit_bytes > 0 ? (l.used_bytes / l.limit_bytes) * 100 : 0;
      if (pct < 80) return false;
    }
    // text search
    if (q) {
      const text = (l.label + ' ' + l.uuid + ' ' + (l.protocol || '')).toLowerCase();
      if (!text.includes(q)) return false;
    }
    return true;
  });
  
  if (!filtered.length) {
    tbody.innerHTML = '<tr><td colspan="6" style="text-align:center;padding:30px;color:var(--t3);">' + (currentLang === 'fa' ? 'هیچ کاربری یافت نشد' : 'No users found') + '</td></tr>';
    return;
  }
  
  tbody.innerHTML = filtered.map(l => {
    const isActive = l.active && !l.expired;
    const statusClass = isActive ? 'active' : (l.expired ? 'expired' : 'disabled');
    const statusText = isActive ? (currentLang === 'fa' ? 'فعال' : 'Active') : (l.expired ? (currentLang === 'fa' ? 'منقضی' : 'Expired') : (currentLang === 'fa' ? 'غیرفعال' : 'Disabled'));
    const pct = l.limit_bytes === 0 ? 0 : Math.min(100, (l.used_bytes / l.limit_bytes) * 100);
    const usedFmt = fmtB(l.used_bytes || 0);
    const limitFmt = l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes);
    const fp = l.fingerprint || 'chrome';
    const fpEmoji = { chrome: '🌐', firefox: '🦊', safari: '🧭', edge: '🌊', ios: '📱', android: '🤖', safari_ios: '🍏', random: '🎲', none: '🚫' };
    const fpName = { chrome: 'Chrome', firefox: 'Firefox', safari: 'Safari', edge: 'Edge', ios: 'iOS', android: 'Android', safari_ios: 'Safari iOS', random: 'Random', none: 'None' }[fp] || fp;
    const protocol = l.protocol || 'vless-ws';
    const protoIcon = { 'vless-ws':'🚀', 'vless-grpc':'⚡', 'vless-xhttp':'🛡️', 'vless-http2':'📶', 'trojan-ws':'🔒', 'shadowsocks':'🌊' }[protocol] || '🚀';
    const protoName = { 'vless-ws':'VLESS-WS', 'vless-grpc':'VLESS-gRPC', 'vless-xhttp':'VLESS-XHTTP', 'vless-http2':'VLESS-HTTP/2', 'trojan-ws':'Trojan-WS', 'shadowsocks':'Shadowsocks' }[protocol] || protocol;
    const httpVer = l.http_version || 'h2';
    const httpName = { 'h1':'HTTP/1.1', 'h2':'HTTP/2', 'h3':'HTTP/3', 'auto':'Auto' }[httpVer] || httpVer;
    let duration = '∞';
    if (l.expires_at) {
      try {
        const exp = new Date(l.expires_at);
        const now = new Date();
        const days = Math.ceil((exp - now) / (1000 * 60 * 60 * 24));
        duration = days > 0 ? days + (currentLang === 'fa' ? ' روز' : ' days') : (currentLang === 'fa' ? 'منقضی' : 'Expired');
      } catch(e) { duration = '—'; }
    }
    const avatarLetter = (l.label || 'U')[0].toUpperCase();
    return '<tr data-uuid="' + l.uuid + '" draggable="true"><td><div class="user-name-cell"><div class="avatar">' + avatarLetter + '</div><div><div class="name">' + esc(l.label) + '<span data-online-uuid="' + l.uuid + '"></span></div><div class="uuid-short">' + l.uuid.slice(0,8) + '… ' + protoIcon + ' ' + protoName + '</div></div></div></td><td style="font-size:10px;color:var(--t2);">' + (fpEmoji[fp] || '🌐') + ' ' + fpName + '<br><span style="font-size:8px;color:var(--t3)">' + httpName + '</span></td><td><span class="status-badge ' + statusClass + '"><span class="status-dot"></span>' + statusText + '</span></td><td><div class="usage-bar"><span class="usage-text">' + usedFmt + ' / ' + limitFmt + '</span><div class="bar"><div class="fill" style="width:' + pct + '%"></div></div></div></td><td style="font-size:11px;color:var(--t2);">' + duration + '</td><td><div class="action-btns"><button class="btn btn-pur btn-sm" onclick="showQR(\'' + l.sub_url + '\')" title="QR Code"><i class="ti ti-qrcode"></i></button><button class="btn btn-pur btn-sm" onclick="navigator.clipboard.writeText(\'' + esc(l.sub_url) + '\').then(()=>toast(\'' + (currentLang === 'fa' ? '✅ کپی ساب' : '✅ Copied') + '\',\'ok\'))" title="' + (currentLang === 'fa' ? 'کپی ساب‌لینک' : 'Copy sub') + '"><i class="ti ti-link"></i></button><button class="btn btn-amber btn-sm" onclick="resetUsage(\'' + l.uuid + '\')" title="' + (currentLang === 'fa' ? 'ریست مصرف' : 'Reset usage') + '"><i class="ti ti-rotate"></i></button><button class="btn btn-pur btn-sm" onclick="openEditModal(\'' + l.uuid + '\')" title="' + (currentLang === 'fa' ? 'ویرایش' : 'Edit') + '"><i class="ti ti-edit"></i></button><button class="btn btn-d btn-sm" onclick="openDeleteModal(\'' + l.uuid + '\')" title="' + (currentLang === 'fa' ? 'حذف' : 'Delete') + '"><i class="ti ti-trash"></i></button></div></td></tr>';
  }).join('');
  
  // آپدیت chip counts
  const counts = {
    all: allUsersCache.length,
    active: allUsersCache.filter(l => l.active && !l.expired).length,
    expired: allUsersCache.filter(l => l.expired).length,
    disabled: allUsersCache.filter(l => !l.active && !l.expired).length,
    'high-usage': allUsersCache.filter(l => l.limit_bytes > 0 && (l.used_bytes / l.limit_bytes) >= 0.8).length
  };
  document.getElementById('chip-all').textContent = counts.all;
  document.getElementById('chip-active').textContent = counts.active;
  document.getElementById('chip-expired').textContent = counts.expired;
  document.getElementById('chip-disabled').textContent = counts.disabled;
  document.getElementById('chip-high').textContent = counts['high-usage'];
}

// ========================================
// ✦ WTF Factor #10: Particle Cursor Trail ✦
// ========================================
function initParticleCursor() {
  const canvas = document.getElementById('particle-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let particles = [];
  let lastMouse = {x: 0, y: 0};
  
  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);
  
  document.addEventListener('mousemove', (e) => {
    const dx = e.clientX - lastMouse.x;
    const dy = e.clientY - lastMouse.y;
    const speed = Math.sqrt(dx*dx + dy*dy);
    if (speed > 2) {
      const count = Math.min(3, Math.floor(speed / 5));
      for (let i = 0; i < count; i++) {
        particles.push({
          x: e.clientX + (Math.random() - 0.5) * 6,
          y: e.clientY + (Math.random() - 0.5) * 6,
          vx: (Math.random() - 0.5) * 1.5,
          vy: (Math.random() - 0.5) * 1.5 - 0.5,
          life: 1,
          size: Math.random() * 2 + 1,
          color: Math.random() > 0.5 ? '#00f0ff' : (Math.random() > 0.5 ? '#ff2e9a' : '#7b2ff7')
        });
      }
    }
    lastMouse = {x: e.clientX, y: e.clientY};
  });
  
  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles = particles.filter(p => p.life > 0);
    particles.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;
      p.vy += 0.02;
      p.life -= 0.025;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.size * p.life, 0, Math.PI * 2);
      ctx.fillStyle = p.color;
      ctx.globalAlpha = p.life;
      ctx.shadowBlur = 8;
      ctx.shadowColor = p.color;
      ctx.fill();
    });
    ctx.globalAlpha = 1;
    ctx.shadowBlur = 0;
    requestAnimationFrame(animate);
  }
  animate();
}

// ========================================
// ✦ WTF Factor #11: Player-style Bottom Bar ✦
// ========================================
let playerBarVisible = true;

function initPlayerBar() {
  const bar = document.getElementById('playerBar');
  if (!bar) return;
  setTimeout(() => {
    bar.classList.add('show');
    document.body.classList.add('has-player-bar');
  }, 800);
  updatePlayerBar();
}

function togglePlayerBar() {
  playerBarVisible = !playerBarVisible;
  const bar = document.getElementById('playerBar');
  if (playerBarVisible) {
    bar.classList.add('show');
    document.body.classList.add('has-player-bar');
  } else {
    bar.classList.remove('show');
    document.body.classList.remove('has-player-bar');
  }
}

function updatePlayerBar() {
  try {
    const users = document.getElementById('stat-users')?.textContent || '0';
    const online = document.getElementById('online-badge')?.textContent || '0';
    const traffic = document.getElementById('stat-traffic')?.textContent || '0';
    const today = document.getElementById('stat-today')?.textContent || '0 B';
    const pbUsers = document.getElementById('pb-users');
    const pbOnline = document.getElementById('pb-online');
    const pbTraffic = document.getElementById('pb-traffic');
    const pbToday = document.getElementById('pb-today');
    if (pbUsers) pbUsers.textContent = users + (currentLang === 'fa' ? ' کاربر' : ' users');
    if (pbOnline) pbOnline.textContent = online;
    if (pbTraffic) pbTraffic.textContent = traffic + ' MB';
    if (pbToday) pbToday.textContent = today;
  } catch(e) {}
}

// ========================================
// ✦ WTF Factor #12: Animated Theme Switcher (Circular Reveal) ✦
// ========================================
function animatedThemeSwitch(newTheme, x, y) {
  const reveal = document.getElementById('themeReveal');
  if (!reveal) { setTheme(newTheme); return; }
  if (x === undefined) x = window.innerWidth / 2;
  if (y === undefined) y = window.innerHeight / 2;
  const maxR = Math.hypot(Math.max(x, window.innerWidth - x), Math.max(y, window.innerHeight - y));
  reveal.style.left = (x - maxR) + 'px';
  reveal.style.top = (y - maxR) + 'px';
  reveal.style.width = (maxR * 2) + 'px';
  reveal.style.height = (maxR * 2) + 'px';
  reveal.style.background = currentTheme === 'white' ? '#eef1f7' : currentTheme === 'bumblebee' ? '#141004' : currentTheme === 'cosmic' ? '#030418' : '#050507';
  reveal.classList.remove('active');
  void reveal.offsetWidth; // trigger reflow
  reveal.classList.add('active');
  setTimeout(() => { setTheme(newTheme); }, 300);
  setTimeout(() => { reveal.classList.remove('active'); }, 800);
}

// Override theme button clicks to use animated switcher
document.addEventListener('click', (e) => {
  const btn = e.target.closest('[onclick*="setTheme"]');
  if (!btn) return;
  e.preventDefault();
  const match = btn.getAttribute('onclick').match(/setTheme\('(\w+)'\)/);
  if (match) {
    const newTheme = match[1];
    if (newTheme !== currentTheme) animatedThemeSwitch(newTheme, e.clientX, e.clientY);
  }
});

// ========================================
// ✦ Keyboard Shortcuts (Ctrl+K already handled) ✦
// ========================================
function initKeyboardShortcuts() {
  document.addEventListener('keydown', (e) => {
    // Alt+1 to Alt+7 برای ناوبری سریع
    if (e.altKey && e.key >= '1' && e.key <= '7') {
      e.preventDefault();
      const pages = ['dashboard', 'users', 'quota', 'connections', 'settings', 'logs'];
      navTo(pages[parseInt(e.key) - 1]);
    }
    // Ctrl+/ برای toggle player bar
    if ((e.ctrlKey || e.metaKey) && e.key === '/') {
      e.preventDefault();
      togglePlayerBar();
    }
  });
}

// ===== راه‌اندازی اولیه =====
document.addEventListener('DOMContentLoaded', async () => {
  try {
    const r = await fetch('/api/me');
    const d = await r.json();
    if (!d.authenticated) location.href = '/login';
  } catch(e) { location.href = '/login'; }
  
  await loadThemeFromServer();
  try { setLang(currentLang); } catch(e) { console.warn('setLang:', e); }
  initDatePickers();
  
  loadDashboard();
  loadUsers();
  loadConnections();
  loadLogs();
  loadQuota();
  setTimeout(showRulesModal, 5000);
  
  // === WTF Factors initialization ===
  initCmdk();
  initParticleCursor();
  initPlayerBar();
  initDragAndDrop();
  loadActivityFeed();
  initKeyboardShortcuts();
  
  // === ✦ ULTRA COSMIC v3.0 initialization ===
  updateSFXUI();
  startPingMonitor();
  startFaClock();
  
  // اضافه کردن کارت درخواست notification به تنظیمات
  addNotifPermissionCard();
  
  // رفع placeholder cmdk
  const cmdkInput = document.getElementById('cmdkInput');
  if (cmdkInput) cmdkInput.placeholder = (currentLang === 'fa' ? 'جست‌وجو یا دستور... (مثلاً: کاربر جدید، QR، تم)' : 'Search or command...');
  
  // ⚡ صرفه‌جویی درخواست: هر ۶۰ ثانیه (هر poll خودش ریکوئست مصرف می‌کند) + وقتی تب مخفیه skip می‌شه
  setInterval(() => {
    if (document.hidden) return;
    if (document.getElementById('pg-dashboard').classList.contains('on')) loadDashboard();
    if (document.getElementById('pg-connections').classList.contains('on')) loadConnections();
    if (document.getElementById('pg-users').classList.contains('on')) loadUsers();
    if (document.getElementById('pg-quota').classList.contains('on')) loadQuota();
    updatePlayerBar();
  }, 60000);
});
</script>
</body></html>
"""


ROOT_HTML = r"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>🏛️ Persepolis Gateway v14</title>
<style>
body{font-family:sans-serif;background:#0a0a1a;color:#F5ECD7;display:flex;align-items:center;justify-content:center;height:100vh;margin:0}
.card{text-align:center;padding:40px;background:rgba(20,15,10,0.7);border-radius:20px;border:1px solid rgba(212,175,55,0.2)}
h1{font-size:48px;margin:0}
.sub{color:#8A7A4A}
a{color:#D4A843;text-decoration:none;font-weight:bold}
</style>
</head>
<body>
<div class="card">
    <h1>🏛️</h1>
    <h2>Persepolis Gateway v14</h2>
    <p class="sub">پنل مدیریت فیلترشکن</p>
    <a href="/login">ورود به پنل →</a>
</div>
</body>
</html>
"""


SUB_PAGE_ALLOWED = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>✦ ⟦label⟧ · Persepolis</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#030418;--card:rgba(10,14,35,0.55);--card-border:rgba(0,240,255,0.12);
  --text:#e8efff;--text2:#94a3b8;--text3:#64748b;
  --accent:#00f0ff;--accent2:#7b2ff7;--accent3:#ff2e9a;
  --green:#10ffa0;--green-bg:rgba(16,255,160,0.08);--green-text:#10ffa0;
  --red:#ff4d6d;--red-bg:rgba(255,77,109,0.08);--red-text:#ff6b8a;
  --shadow:0 25px 80px rgba(0,0,0,0.6),0 0 120px rgba(0,240,255,0.04);
  --transition:all 0.4s cubic-bezier(0.34,1.56,0.64,1);--radius:18px
}
[data-theme="cosmic_neon"]{--bg:#030418;--card:rgba(10,14,35,0.55);--card-border:rgba(0,240,255,0.12);--accent:#00f0ff;--accent2:#7b2ff7;--accent3:#ff2e9a;--text:#e8efff;--text2:#94a3b8;--text3:#64748b}
[data-theme="cosmic_aurora"]{--bg:#020815;--card:rgba(8,15,30,0.6);--card-border:rgba(16,255,160,0.12);--accent:#10ffa0;--accent2:#00f0ff;--accent3:#7b2ff7;--text:#d4ffe8;--text2:#7eb8a0;--text3:#4a7868}
[data-theme="cosmic_void"]{--bg:#000005;--card:rgba(15,15,25,0.7);--card-border:rgba(100,100,200,0.1);--accent:#8a8aff;--accent2:#aaaaff;--accent3:#cc66ff;--text:#e0e0ff;--text2:#9090c0;--text3:#505078}
[data-theme="cosmic_purple"]{--bg:#08051a;--card:rgba(20,10,40,0.6);--card-border:rgba(123,47,247,0.15);--accent:#7b2ff7;--accent2:#ff2e9a;--accent3:#00f0ff;--text:#f0e8ff;--text2:#a890c0;--text3:#685088}
[data-theme="cosmic_sunset"]{--bg:#1a0810;--card:rgba(40,15,25,0.6);--card-border:rgba(255,46,154,0.12);--accent:#ff2e9a;--accent2:#ffb800;--accent3:#7b2ff7;--text:#ffe8e8;--text2:#c0a090;--text3:#806058}
[data-theme="cosmic_ocean"]{--bg:#001525;--card:rgba(8,25,50,0.6);--card-border:rgba(0,150,255,0.15);--accent:#00f0ff;--accent2:#0066ff;--accent3:#10ffa0;--text:#e0f0ff;--text2:#80b0d0;--text3:#5080a0}
[data-theme="cosmic_gold"]{--bg:#0a0805;--card:rgba(25,20,8,0.6);--card-border:rgba(212,168,67,0.12);--accent:#D4A843;--accent2:#F5D060;--accent3:#B8922E;--text:#F5ECD7;--text2:#C4A35A;--text3:#8A7A4A}
[data-theme="cosmic_mint"]{--bg:#001510;--card:rgba(8,30,20,0.6);--card-border:rgba(16,255,160,0.12);--accent:#10ffa0;--accent2:#00f0ff;--accent3:#7b2ff7;--text:#d0ffe8;--text2:#80c0a0;--text3:#508070}
[data-theme="cosmic_rose"]{--bg:#1a0515;--card:rgba(40,15,30,0.6);--card-border:rgba(255,46,154,0.12);--accent:#ff2e9a;--accent2:#ffb6c1;--accent3:#7b2ff7;--text:#ffe8f0;--text2:#c090a0;--text3:#806070}
[data-theme="cosmic_matrix"]{--bg:#000a00;--card:rgba(0,20,0,0.65);--card-border:rgba(0,255,0,0.15);--accent:#00ff00;--accent2:#00cc00;--accent3:#008800;--text:#c0ffc0;--text2:#80a080;--text3:#506050}

@keyframes twinkle{0%,100%{opacity:0.15}50%{opacity:0.9}}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
@keyframes cardIn{from{opacity:0;transform:translateY(40px) scale(0.92);filter:blur(10px)}to{opacity:1;transform:translateY(0) scale(1);filter:blur(0)}}
@keyframes float{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(20px,-20px) scale(1.05)}}
@keyframes shimmer{0%{background-position:-200% 0}100%{background-position:200% 0}}
@keyframes gradientFlow{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes orbit{0%{transform:rotate(0deg) translateX(120px) rotate(0deg)}100%{transform:rotate(360deg) translateX(120px) rotate(-360deg)}}

body{font-family:'Vazirmatn',sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:16px;background:radial-gradient(ellipse at top,var(--bg),#000 80%);color:var(--text);transition:var(--transition);position:relative;overflow-x:hidden}

#starfield{position:fixed;inset:0;z-index:0;pointer-events:none}
.nebula{position:fixed;border-radius:50%;filter:blur(120px);z-index:0;pointer-events:none;animation:float 12s ease-in-out infinite}
.nebula1{width:500px;height:500px;background:radial-gradient(circle,rgba(0,240,255,0.1),transparent 70%);top:-150px;right:-100px}
.nebula2{width:400px;height:400px;background:radial-gradient(circle,rgba(255,46,154,0.08),transparent 70%);bottom:-100px;left:-80px;animation-delay:-6s}
.nebula3{width:350px;height:350px;background:radial-gradient(circle,rgba(123,47,247,0.08),transparent 70%);top:40%;left:30%;animation-delay:-3s}

/* خطوط هولوگرافیک */
.grid-bg{position:fixed;inset:0;z-index:0;opacity:0.1;background-image:linear-gradient(rgba(0,240,255,0.3) 1px,transparent 1px),linear-gradient(90deg,rgba(0,240,255,0.3) 1px,transparent 1px);background-size:40px 40px;mask-image:radial-gradient(ellipse at center,#000 0%,transparent 60%);-webkit-mask-image:radial-gradient(ellipse at center,#000 0%,transparent 60%);pointer-events:none;animation:gridShift 20s linear infinite}
@keyframes gridShift{from{background-position:0 0}to{background-position:40px 40px}}

/* === دراپ‌داون تم === */
.theme-dropdown{position:fixed;top:20px;left:50%;transform:translateX(-50%);z-index:100}
.theme-dropdown .toggle-btn{background:var(--card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--card-border);border-radius:14px;padding:10px 20px;color:var(--text);font-family:'Vazirmatn',sans-serif;font-size:13px;font-weight:700;cursor:pointer;display:flex;align-items:center;gap:10px;transition:var(--transition);box-shadow:0 8px 40px rgba(0,0,0,0.3)}
.theme-dropdown .toggle-btn:hover{border-color:var(--accent);transform:scale(1.02);box-shadow:0 0 30px rgba(0,240,255,0.2)}
.theme-dropdown .toggle-btn .arrow{transition:transform .3s;font-size:12px}
.theme-dropdown .toggle-btn .arrow.open{transform:rotate(180deg)}
.theme-dropdown .menu{display:none;position:absolute;top:calc(100% + 8px);left:50%;transform:translateX(-50%);background:var(--card);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border:1px solid var(--card-border);border-radius:14px;padding:8px;min-width:220px;box-shadow:0 12px 50px rgba(0,0,0,0.5),0 0 30px rgba(0,240,255,0.1);animation:cardIn .3s ease}
.theme-dropdown .menu.open{display:block}
.theme-dropdown .menu-item{display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:10px;cursor:pointer;transition:var(--transition);color:var(--text2);font-size:13px;font-weight:600}
.theme-dropdown .menu-item:hover{background:rgba(0,240,255,0.06);color:var(--text);transform:translateX(-3px)}
.theme-dropdown .menu-item .dot{display:inline-block;width:20px;height:20px;border-radius:6px;flex-shrink:0;border:1px solid rgba(255,255,255,0.1);box-shadow:0 0 10px rgba(0,240,255,0.2)}
.theme-dropdown .menu-item .check{margin-right:auto;opacity:0;transition:opacity .2s;color:var(--accent);font-weight:900}
.theme-dropdown .menu-item.active .check{opacity:1}
.theme-dropdown .menu-item.active{background:rgba(0,240,255,0.06);color:var(--text)}

/* === کارت اصلی === */
.card{position:relative;z-index:10;background:var(--card);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border:1px solid var(--card-border);border-radius:var(--radius);padding:28px 24px 24px;max-width:520px;width:100%;box-shadow:var(--shadow);animation:cardIn 0.7s var(--transition);transition:var(--transition);margin-top:70px}
.card::before{content:'';position:absolute;inset:0;border-radius:var(--radius);padding:1px;background:linear-gradient(135deg,rgba(0,240,255,0.5),transparent 30%,transparent 70%,rgba(255,46,154,0.5));-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;opacity:0.4;pointer-events:none;animation:borderGlow 6s ease-in-out infinite}
@keyframes borderGlow{0%,100%{opacity:0.3}50%{opacity:0.7}}
.card::after{content:'';position:absolute;top:0;left:30px;right:30px;height:2px;background:linear-gradient(90deg,transparent,var(--accent),var(--accent3),transparent);opacity:0.6;pointer-events:none}

/* هدر */
.card-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px;padding-bottom:14px;border-bottom:1px solid var(--card-border);position:relative}
.brand{display:flex;align-items:center;gap:10px}
.brand-icon{width:40px;height:40px;border-radius:12px;background:linear-gradient(135deg,var(--accent),var(--accent2),var(--accent3));display:flex;align-items:center;justify-content:center;font-size:20px;box-shadow:0 0 30px rgba(0,240,255,0.3);animation:iconPulse 4s ease-in-out infinite;position:relative}
.brand-icon::before{content:'';position:absolute;inset:-3px;border-radius:14px;background:inherit;filter:blur(10px);opacity:0.5;z-index:-1}
@keyframes iconPulse{0%,100%{box-shadow:0 0 30px rgba(0,240,255,0.4);transform:scale(1)}50%{box-shadow:0 0 50px rgba(255,46,154,0.5);transform:scale(1.05)}}
.brand-text{font-size:13px;font-weight:900;background:linear-gradient(135deg,#fff,var(--accent),var(--accent3));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;letter-spacing:0.5px}
.brand-sub{font-size:7px;color:var(--text3);letter-spacing:1.5px;text-transform:uppercase;margin-top:1px}
.theme-toggle-btn{background:rgba(0,240,255,0.05);border:1px solid var(--card-border);color:var(--text2);width:34px;height:34px;border-radius:10px;cursor:pointer;font-size:16px;transition:var(--transition)}
.theme-toggle-btn:hover{background:rgba(0,240,255,0.1);transform:rotate(20deg);color:var(--accent);box-shadow:0 0 15px rgba(0,240,255,0.3)}

/* نام کاربر */
.user-name-row{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;flex-wrap:wrap;gap:8px}
.user-name{font-size:22px;font-weight:900;color:var(--text);display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.user-name .proto-badge{font-size:10px;font-weight:700;background:linear-gradient(135deg,rgba(0,240,255,0.12),rgba(255,46,154,0.08));padding:3px 12px;border-radius:14px;color:var(--accent);letter-spacing:0.3px;border:1px solid var(--card-border);box-shadow:0 0 15px rgba(0,240,255,0.1)}
.status-badge{display:inline-flex;align-items:center;gap:5px;padding:4px 14px;border-radius:14px;font-size:11px;font-weight:700;letter-spacing:0.3px}
.status-badge.active{background:var(--green-bg);color:var(--green-text);border:1px solid rgba(16,255,160,0.2);box-shadow:0 0 15px rgba(16,255,160,0.15)}
.status-badge.inactive{background:var(--red-bg);color:var(--red-text);border:1px solid rgba(255,77,109,0.2);box-shadow:0 0 15px rgba(255,77,109,0.15)}
.status-dot{width:7px;height:7px;border-radius:50%;display:inline-block;animation:pulse 1.5s infinite}
.status-dot.green{background:var(--green-text);box-shadow:0 0 8px var(--green-text)}
.status-dot.red{background:var(--red-text);box-shadow:0 0 8px var(--red-text)}

/* UUID */
.uuid-box{background:rgba(0,240,255,0.04);border:1px solid var(--card-border);border-radius:10px;padding:8px 12px;font-size:10px;font-family:monospace;color:var(--accent);word-break:break-all;cursor:pointer;transition:var(--transition);text-align:center;margin:8px 0 12px;letter-spacing:0.3px}
.uuid-box:hover{background:rgba(0,240,255,0.08);transform:scale(1.01);box-shadow:0 0 20px rgba(0,240,255,0.15)}

/* کارت‌های آمار */
.stats-card-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 0}
.stat-info-card{background:rgba(0,240,255,0.03);border:1px solid var(--card-border);border-radius:12px;padding:12px 14px;transition:var(--transition);position:relative;overflow:hidden}
.stat-info-card::before{content:'';position:absolute;top:0;left:0;width:100%;height:1px;background:linear-gradient(90deg,transparent,var(--accent),transparent);opacity:0.5}
.stat-info-card:hover{background:rgba(0,240,255,0.06);transform:translateY(-3px);box-shadow:0 8px 25px rgba(0,240,255,0.1)}
.stat-info-label{font-size:8px;color:var(--text3);font-weight:700;text-transform:uppercase;letter-spacing:0.6px}
.stat-info-value{font-size:17px;font-weight:900;color:var(--text);margin-top:3px}
.stat-info-value .unit{font-size:10px;font-weight:400;color:var(--text2)}
.stat-info-value.used{color:var(--accent);text-shadow:0 0 12px rgba(0,240,255,0.3)}
.stat-info-value.limit{color:var(--text2)}

/* نوار پیشرفت */
.progress-section{margin:10px 0}
.progress-bar{height:6px;border-radius:6px;background:rgba(0,240,255,0.05);overflow:hidden;position:relative;border:1px solid var(--card-border)}
.progress-fill{height:100%;border-radius:6px;background:linear-gradient(90deg,var(--accent),var(--accent2),var(--accent3));background-size:200% 200%;animation:gradientFlow 4s ease infinite;width:0%;transition:width 1.2s ease;box-shadow:0 0 12px rgba(0,240,255,0.5);position:relative}
.progress-fill::after{content:'';position:absolute;top:0;right:0;width:30px;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.6),transparent);animation:shimmer 2s linear infinite}
.progress-text{display:flex;justify-content:space-between;font-size:9px;color:var(--text3);margin-top:5px;letter-spacing:0.3px}
.progress-text .pct{font-weight:900;color:var(--accent);text-shadow:0 0 8px rgba(0,240,255,0.4)}

/* لینک ساب */
.sub-link-section{background:rgba(0,240,255,0.03);border:1px solid var(--card-border);border-radius:12px;padding:10px 14px;margin:10px 0;position:relative;overflow:hidden}
.sub-link-section::before{content:'';position:absolute;top:0;left:0;width:100%;height:1px;background:linear-gradient(90deg,transparent,var(--accent),transparent);opacity:0.5}
.sub-link-label{font-size:8px;font-weight:700;color:var(--text3);text-transform:uppercase;letter-spacing:0.6px;display:flex;align-items:center;gap:5px;margin-bottom:5px}
.sub-link-label i{color:var(--accent);font-size:10px;filter:drop-shadow(0 0 4px var(--accent))}
.sub-link-url{font-family:monospace;font-size:9px;color:var(--accent);word-break:break-all;line-height:1.6;background:rgba(0,0,15,0.4);padding:6px 8px;border-radius:6px;border:1px solid var(--card-border);text-shadow:0 0 8px rgba(0,240,255,0.2)}
.sub-link-actions{display:flex;gap:6px;margin-top:6px;flex-wrap:wrap}
.sub-link-actions .btn{flex:1;font-size:9px;padding:6px 10px;justify-content:center}

/* اپلیکیشن‌ها */
.apps-section{margin:12px 0}
.apps-title{font-size:10px;font-weight:700;color:var(--text3);margin-bottom:8px;display:flex;align-items:center;gap:5px;letter-spacing:0.5px;text-transform:uppercase}
.apps-title i{color:var(--accent);font-size:11px;filter:drop-shadow(0 0 4px var(--accent))}
.apps-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}
.app-btn{background:rgba(0,240,255,0.03);border:1px solid var(--card-border);border-radius:12px;padding:8px 4px;text-align:center;cursor:pointer;transition:var(--transition);text-decoration:none;color:var(--text);position:relative;overflow:hidden}
.app-btn::before{content:'';position:absolute;top:0;left:0;width:100%;height:1px;background:linear-gradient(90deg,transparent,var(--accent),transparent);opacity:0;transition:opacity .3s}
.app-btn:hover{background:rgba(0,240,255,0.08);transform:translateY(-3px);border-color:var(--accent);box-shadow:0 8px 25px rgba(0,240,255,0.15)}
.app-btn:hover::before{opacity:1}
.app-btn .app-icon{font-size:24px;display:block;margin-bottom:4px;filter:drop-shadow(0 0 6px rgba(0,240,255,0.4))}
.app-btn:hover .app-icon{transform:scale(1.15)}
.app-btn .app-name{font-size:7px;color:var(--text2);font-weight:700;display:block;letter-spacing:0.3px}
.app-btn .app-action{font-size:6px;color:var(--text3);display:block;margin-top:1px}
.app-btn .app-action.copy{color:var(--accent)}

/* کانفیگ */
.configs-section{margin:12px 0}
.config-item{display:flex;align-items:center;justify-content:space-between;background:rgba(0,240,255,0.03);border:1px solid var(--card-border);border-radius:10px;padding:8px 12px;margin-bottom:4px;transition:var(--transition)}
.config-item:hover{background:rgba(0,240,255,0.06);transform:translateX(-3px)}
.config-item .config-name{font-size:10px;font-weight:700;color:var(--text)}
.config-item .config-type{font-size:8px;color:var(--text3);background:rgba(0,240,255,0.06);padding:2px 8px;border-radius:6px;letter-spacing:0.3px}
.config-item .config-action{font-size:10px;color:var(--accent);cursor:pointer;transition:var(--transition);padding:4px 8px;border-radius:6px}
.config-item .config-action:hover{color:var(--accent2);background:rgba(0,240,255,0.08)}

/* دکمه‌ها */
.btn{font-family:inherit;font-size:10px;font-weight:700;border-radius:10px;padding:6px 12px;cursor:pointer;display:inline-flex;align-items:center;gap:4px;border:none;transition:var(--transition);white-space:nowrap;justify-content:center;letter-spacing:0.3px}
.btn i{font-size:11px}
.btn-success{background:linear-gradient(135deg,var(--green-bg),rgba(16,255,160,0.15));border:1px solid rgba(16,255,160,0.2);color:var(--green-text)}
.btn-success:hover{background:linear-gradient(135deg,rgba(16,255,160,0.15),rgba(16,255,160,0.25));transform:translateY(-2px);box-shadow:0 4px 20px rgba(16,255,160,0.3)}
.btn-success.copied{background:linear-gradient(135deg,#10ffa0,#00cc80);color:#000;transform:scale(0.95)}
.btn-secondary{background:rgba(255,255,255,0.03);border:1px solid var(--card-border);color:var(--text2)}
.btn-secondary:hover{background:rgba(0,240,255,0.06);color:var(--text);transform:translateY(-2px)}
.btn-gold{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#000;box-shadow:0 0 20px rgba(0,240,255,0.25)}
.btn-gold:hover{transform:translateY(-2px);box-shadow:0 4px 25px rgba(0,240,255,0.4)}

.footer{margin-top:14px;padding-top:12px;border-top:1px solid var(--card-border);text-align:center;font-size:7px;color:var(--text3);letter-spacing:0.5px}
.footer .brand-name{color:var(--accent);font-weight:900;text-shadow:0 0 8px rgba(0,240,255,0.4)}

.toast{position:fixed;bottom:20px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--card-border);color:var(--text);border-radius:12px;padding:8px 16px;font-size:10px;opacity:0;transition:var(--transition);z-index:999;pointer-events:none;box-shadow:var(--shadow);display:flex;align-items:center;gap:5px;font-weight:600}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,255,160,0.3);color:var(--green-text);box-shadow:0 8px 30px rgba(16,255,160,0.2)}

@media(max-width:420px){.card{padding:20px 14px;margin-top:80px}.user-name{font-size:19px}.stats-card-grid{gap:6px}.stat-info-value{font-size:15px}.apps-grid{grid-template-columns:repeat(4,1fr)}.app-btn .app-icon{font-size:20px}}

/* ============================================
   ✦ ULTRA COSMIC v3.0 — صفحه اشتراک ✦
   ============================================ */
.aurora{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden;opacity:.85}
.aurora i{position:absolute;display:block;border-radius:50%;filter:blur(100px);mix-blend-mode:screen;will-change:transform,opacity}
.aurora .a1{width:800px;height:280px;top:-90px;right:-10%;background:linear-gradient(100deg,transparent,rgba(16,255,160,0.14),rgba(0,240,255,0.2),transparent);transform:rotate(-12deg);animation:auroraSweep 17s ease-in-out infinite}
.aurora .a2{width:700px;height:240px;top:14%;left:-12%;background:linear-gradient(80deg,transparent,rgba(123,47,247,0.17),rgba(0,240,255,0.11),transparent);transform:rotate(9deg);animation:auroraSweep 22s ease-in-out infinite reverse;animation-delay:-6s}
.aurora .a3{width:600px;height:200px;bottom:-60px;right:10%;background:linear-gradient(90deg,transparent,rgba(255,46,154,0.13),rgba(123,47,247,0.1),transparent);transform:rotate(-5deg);animation:auroraSweep 26s ease-in-out infinite;animation-delay:-13s}
@keyframes auroraSweep{0%,100%{transform:translateX(0) rotate(-11deg) scaleY(1);opacity:.5}33%{transform:translateX(-60px) rotate(-6deg) scaleY(1.4);opacity:.85}66%{transform:translateX(50px) rotate(-15deg) scaleY(.8);opacity:.4}}

.brand-icon{overflow:visible}
.brand-icon svg{width:62%;height:62%;filter:drop-shadow(0 0 8px rgba(0,240,255,0.7))}
.brand-icon .pp-col{animation:ppColWave 2.6s ease-in-out infinite}
.brand-icon .pp-col.c2{animation-delay:.25s}
.brand-icon .pp-col.c3{animation-delay:.5s}
.brand-icon .pp-roof{animation:ppRoofGlow 3.2s ease-in-out infinite}
@keyframes ppColWave{0%,100%{opacity:.65;transform:translateY(0)}50%{opacity:1;transform:translateY(-1.5px)}}
@keyframes ppRoofGlow{0%,100%{filter:drop-shadow(0 0 3px rgba(0,240,255,0.6))}50%{filter:drop-shadow(0 0 10px rgba(255,46,154,0.9))}}
.orbit-ring{position:absolute;inset:-7px;border-radius:14px;border:1px dashed rgba(0,240,255,0.35);animation:spinOrbit 14s linear infinite;pointer-events:none}
@keyframes spinOrbit{to{transform:rotate(360deg)}}
</style>
</head>
<body>
<canvas id="starfield"></canvas>
<div class="aurora"><i class="a1"></i><i class="a2"></i><i class="a3"></i></div>
<div class="nebula nebula1"></div><div class="nebula nebula2"></div><div class="nebula nebula3"></div>
<div class="grid-bg"></div>
<div class="toast" id="toast"></div>

<div class="theme-dropdown">
    <button class="toggle-btn" onclick="toggleThemeMenu()">
        <span>🎨</span>
        <span id="themeDisplay">انتخاب تم کیهانی</span>
        <span class="arrow" id="themeArrow">▾</span>
    </button>
    <div class="menu" id="themeMenu">
        
        <div class="menu-item" data-theme="cosmic_neon" onclick="selectTheme('cosmic_neon')">
            <span class="dot" style="background:linear-gradient(135deg,#00f0ff,#7b2ff7)"></span>
            🌌 نئون کیهانی
            <span class="check">✓</span>
        </div>
        
        <div class="menu-item" data-theme="cosmic_aurora" onclick="selectTheme('cosmic_aurora')">
            <span class="dot" style="background:linear-gradient(135deg,#10ffa0,#00f0ff,#7b2ff7)"></span>
            ✨ شفق قطبی
            <span class="check">✓</span>
        </div>
        
        <div class="menu-item" data-theme="cosmic_void" onclick="selectTheme('cosmic_void')">
            <span class="dot" style="background:linear-gradient(135deg,#0a0a1a,#1a1a3a)"></span>
            🕳️ خلاء سیاه
            <span class="check">✓</span>
        </div>
        
        <div class="menu-item" data-theme="cosmic_purple" onclick="selectTheme('cosmic_purple')">
            <span class="dot" style="background:linear-gradient(135deg,#7b2ff7,#ff2e9a)"></span>
            🔮 بنفش کیهانی
            <span class="check">✓</span>
        </div>
        
        <div class="menu-item" data-theme="cosmic_sunset" onclick="selectTheme('cosmic_sunset')">
            <span class="dot" style="background:linear-gradient(135deg,#ff2e9a,#ffb800)"></span>
            🌅 غروب کیهانی
            <span class="check">✓</span>
        </div>
        
        <div class="menu-item" data-theme="cosmic_ocean" onclick="selectTheme('cosmic_ocean')">
            <span class="dot" style="background:linear-gradient(135deg,#0066ff,#00f0ff)"></span>
            🌊 اقیانوس عمیق
            <span class="check">✓</span>
        </div>
        
        <div class="menu-item" data-theme="cosmic_gold" onclick="selectTheme('cosmic_gold')">
            <span class="dot" style="background:linear-gradient(135deg,#D4A843,#F5D060)"></span>
            🏛️ طلایی تخت جمشید
            <span class="check">✓</span>
        </div>
        
        <div class="menu-item" data-theme="cosmic_mint" onclick="selectTheme('cosmic_mint')">
            <span class="dot" style="background:linear-gradient(135deg,#10ffa0,#00f0ff)"></span>
            🌱 سبز نعنایی
            <span class="check">✓</span>
        </div>
        
        <div class="menu-item" data-theme="cosmic_rose" onclick="selectTheme('cosmic_rose')">
            <span class="dot" style="background:linear-gradient(135deg,#ff2e9a,#ffb6c1)"></span>
            🌸 رز کیهانی
            <span class="check">✓</span>
        </div>
        
        <div class="menu-item" data-theme="cosmic_matrix" onclick="selectTheme('cosmic_matrix')">
            <span class="dot" style="background:linear-gradient(135deg,#00ff00,#008800)"></span>
            💻 ماتریکس
            <span class="check">✓</span>
        </div>
        
    </div>
</div>

<div class="card" id="mainCard">
    <div class="card-header">
        <div class="brand">
            <div class="brand-icon"><img class="logo-img" src="data:image/jpeg;base64,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" alt="P443"></div>
            <div>
                <div class="brand-text">PERSEPOLIS</div>
                <div class="brand-sub">COSMIC SUBSCRIPTION · v3.0</div>
            </div>
        </div>
        <button class="theme-toggle-btn" onclick="toggleTheme()" id="themeBtn">🌙</button>
    </div>

    <div class="user-name-row">
        <div class="user-name">
            ⟦label⟧
            <span class="proto-badge">⟦protocol_icon⟧ ⟦protocol_name⟧ · ⟦http_name⟧</span>
        </div>
        <span class="status-badge active">
            <span class="status-dot green"></span>
            فعال
        </span>
    </div>

    <div class="uuid-box" onclick="copyUUID()">🔑 ⟦uuid⟧</div>

    <div class="stats-card-grid">
        <div class="stat-info-card">
            <div class="stat-info-label">📊 مصرف</div>
            <div class="stat-info-value used">⟦used_val⟧ <span class="unit">⟦used_unit⟧</span></div>
        </div>
        <div class="stat-info-card">
            <div class="stat-info-label">📦 سهمیه</div>
            <div class="stat-info-value limit">⟦limit_val⟧ <span class="unit">⟦limit_unit⟧</span></div>
        </div>
        <div class="stat-info-card">
            <div class="stat-info-label">⏳ زمان باقی</div>
            <div class="stat-info-value">⟦days_left⟧</div>
        </div>
        <div class="stat-info-card">
            <div class="stat-info-label">📱 دستگاه‌ها</div>
            <div class="stat-info-value">⟦max_devices⟧</div>
        </div>
    </div>

    <div class="progress-section">
        <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
        <div class="progress-text">
            <span>میزان مصرف</span>
            <span class="pct">0.0%</span>
        </div>
    </div>

    <div class="sub-link-section">
        <div class="sub-link-label"><i class="ti ti-link"></i> لینک اشتراک</div>
        <div class="sub-link-url" id="subLink">⟦sub_url⟧</div>
        <div class="sub-link-actions">
            <button class="btn btn-success" onclick="copySub()" id="copySubBtn"><i class="ti ti-copy"></i> کپی لینک</button>
            <button class="btn btn-gold" onclick="window.open('⟦sub_url⟧', '_blank')"><i class="ti ti-external-link"></i> باز کردن</button>
        </div>
    </div>

    <div class="apps-section">
        <div class="apps-title"><i class="ti ti-devices"></i> نصب روی دستگاه‌ها</div>
        <div class="apps-grid">
            <div class="app-btn" onclick="openApp('hiddify')">
                <span class="app-icon">📱</span>
                <span class="app-name">Hiddify</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('v2rayng')">
                <span class="app-icon">📲</span>
                <span class="app-name">V2rayNG</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('v2box')">
                <span class="app-icon">📱</span>
                <span class="app-name">V2Box</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="copySub()">
                <span class="app-icon">📋</span>
                <span class="app-name">نکست‌وی‌پی‌ان</span>
                <span class="app-action copy">کپی لینک</span>
            </div>
            <div class="app-btn" onclick="openApp('clash')">
                <span class="app-icon">⚔️</span>
                <span class="app-name">Clash Meta</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('windows')">
                <span class="app-icon">🪟</span>
                <span class="app-name">Windows</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('macos')">
                <span class="app-icon">🍎</span>
                <span class="app-name">macOS</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('linux')">
                <span class="app-icon">🐧</span>
                <span class="app-name">Linux</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
        </div>
    </div>

    <div class="configs-section">
        <div class="config-item">
            <span class="config-name">⟦label⟧-Default</span>
            <span class="config-type">⟦protocol_name⟧ · ⟦http_name⟧</span>
            <span class="config-action" onclick="copyConfig('⟦vless_link⟧')">📋</span>
        </div>
    </div>

    <div class="footer">
        <span class="brand-name">✦ PERSEPOLIS</span> · نسخه کیهانی ۲.۰ · ⟦protocol_icon⟧ ⟦protocol_name⟧
    </div>
</div>

<script>
// === ✦ ULTRA COSMIC: ستاره‌های پارالاکس + شهاب‌سنگ Canvas ===
const canvas = document.getElementById('starfield');
const ctx = canvas.getContext('2d');
let stars = [], meteors = [], mouse = {x: 0.5, y: 0.5};
function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    stars = [];
    const count = Math.floor((canvas.width * canvas.height) / 8000);
    for (let i = 0; i < count; i++) {
        stars.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            r: Math.random() * 1.4 + 0.3,
            o: Math.random() * 0.7 + 0.2,
            tw: Math.random() * Math.PI * 2,
            depth: Math.random(),
            color: Math.random() > 0.85 ? '#00f0ff' : (Math.random() > 0.7 ? '#ff2e9a' : '#ffffff')
        });
    }
}
function spawnMeteor() {
    const sx = Math.random() * canvas.width * 0.8 + canvas.width * 0.1;
    meteors.push({
        x: sx, y: -30,
        vx: -(Math.random() * 5 + 3),
        vy: Math.random() * 3.5 + 3,
        len: Math.random() * 80 + 50,
        life: 1, hue: Math.random() > 0.5 ? '#00f0ff' : '#ff2e9a'
    });
}
function drawStars() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const px = (mouse.x - 0.5), py = (mouse.y - 0.5);
    stars.forEach(s => {
        s.tw += 0.018;
        const op = s.o * (0.5 + 0.5 * Math.sin(s.tw));
        const ox = px * 20 * s.depth, oy = py * 14 * s.depth;
        ctx.beginPath();
        ctx.arc(s.x + ox, s.y + oy, s.r, 0, Math.PI * 2);
        ctx.fillStyle = s.color;
        ctx.globalAlpha = op;
        ctx.shadowBlur = 7 + s.depth * 5;
        ctx.shadowColor = s.color;
        ctx.fill();
    });
    if (Math.random() < 0.01 && meteors.length < 3) spawnMeteor();
    for (let i = meteors.length - 1; i >= 0; i--) {
        const m = meteors[i];
        m.x += m.vx; m.y += m.vy; m.life -= 0.007;
        if (m.life <= 0 || m.y > canvas.height + 100) { meteors.splice(i, 1); continue; }
        const grad = ctx.createLinearGradient(m.x, m.y, m.x - m.vx * (m.len / 8), m.y - m.vy * (m.len / 8));
        grad.addColorStop(0, m.hue);
        grad.addColorStop(1, 'transparent');
        ctx.strokeStyle = grad;
        ctx.lineWidth = 2;
        ctx.globalAlpha = Math.min(m.life, 1);
        ctx.shadowBlur = 12;
        ctx.shadowColor = m.hue;
        ctx.beginPath();
        ctx.moveTo(m.x, m.y);
        ctx.lineTo(m.x - m.vx * (m.len / 8), m.y - m.vy * (m.len / 8));
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(m.x, m.y, 2.2, 0, Math.PI * 2);
        ctx.fillStyle = '#fff';
        ctx.fill();
    }
    ctx.globalAlpha = 1;
    ctx.shadowBlur = 0;
    requestAnimationFrame(drawStars);
}
window.addEventListener('resize', resizeCanvas);
window.addEventListener('mousemove', e => { mouse.x = e.clientX / window.innerWidth; mouse.y = e.clientY / window.innerHeight; });
resizeCanvas();
drawStars();

// === ✦ جلوه صوتی سبک (WebAudio) ===
const SFX = {
    ac: null,
    ensure() {
        if (!this.ac) { try { this.ac = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) { return false; } }
        if (this.ac && this.ac.state === 'suspended') this.ac.resume();
        return !!this.ac;
    },
    tone(f1, f2, dur, type, vol, delay) {
        if (localStorage.getItem('pp-sfx') === 'off' || !this.ensure()) return;
        try {
            const t0 = this.ac.currentTime + (delay || 0);
            const o = this.ac.createOscillator(), g = this.ac.createGain();
            o.type = type || 'sine';
            o.frequency.setValueAtTime(f1, t0);
            if (f2) o.frequency.exponentialRampToValueAtTime(f2, t0 + dur);
            g.gain.setValueAtTime(0.0001, t0);
            g.gain.exponentialRampToValueAtTime(vol || 0.05, t0 + 0.015);
            g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
            o.connect(g); g.connect(this.ac.destination);
            o.start(t0); o.stop(t0 + dur + 0.05);
        } catch (e) {}
    },
    click() { this.tone(520, 760, 0.08, 'triangle', 0.04); },
    success() { this.tone(523, 0, 0.1, 'sine', 0.055); this.tone(659, 0, 0.1, 'sine', 0.055, 0.09); this.tone(784, 1046, 0.18, 'sine', 0.065, 0.18); },
    error() { this.tone(220, 110, 0.25, 'sawtooth', 0.045); }
};
document.addEventListener('click', e => { if (e.target.closest('button, .app-btn, .config-item, .menu-item, .btn')) SFX.click(); }, true);

const subUrl = `⟦sub_url⟧`;
const uuid = `⟦uuid⟧`;
const vlessLink = `⟦vless_link⟧`;
const isExpired = false;

function toast(msg, type) {
    const t = document.getElementById('toast');
    t.textContent = msg;
    t.className = 'toast show' + (type ? ' ' + type : '');
    clearTimeout(t._timeout);
    t._timeout = setTimeout(() => t.classList.remove('show'), 2000);
    if (type === 'ok') SFX.success();
    else if (type === 'err') SFX.error();
}

function copySub() {
    const btn = document.getElementById('copySubBtn');
    navigator.clipboard.writeText(subUrl).then(() => {
        toast('✅ ساب‌لینک کپی شد!', 'ok');
        btn.classList.add('copied');
        btn.innerHTML = '<i class="ti ti-check"></i> کپی شد!';
        setTimeout(() => {
            btn.classList.remove('copied');
            btn.innerHTML = '<i class="ti ti-copy"></i> کپی لینک';
        }, 1500);
    }).catch(() => toast('❌ خطا در کپی', 'err'));
}

function copyUUID() {
    navigator.clipboard.writeText(uuid).then(() => toast('✅ کپی شد', 'ok'));
}

function copyConfig(link) {
    navigator.clipboard.writeText(link).then(() => toast('✅ کانفیگ کپی شد!', 'ok'));
}

function openApp(app) {
    const apps = {
        'hiddify': 'https://github.com/hiddify/hiddify-app/releases',
        'v2rayng': 'https://github.com/2dust/v2rayNG/releases',
        'v2box': 'https://apps.apple.com/app/v2box/id6446814670',
        'clash': 'https://github.com/MetaCubeX/ClashMetaForAndroid/releases',
        'windows': 'https://github.com/2dust/v2rayN/releases',
        'macos': 'https://github.com/ShadowLaunch/ShadowLaunch/releases',
        'linux': 'https://github.com/SagerNet/sing-box/releases'
    };
    const url = apps[app];
    if (url) {
        window.open(url, '_blank');
    } else {
        toast('📋 لینک در کلیپ‌بورد', 'ok');
        copySub();
    }
}

// === مدیریت تم‌های کیهانی ===
let currentTheme = localStorage.getItem('cosmic-sub-theme') || 'cosmic_neon';
const themeList = ['cosmic_neon','cosmic_aurora','cosmic_void','cosmic_purple','cosmic_sunset','cosmic_ocean','cosmic_gold','cosmic_mint','cosmic_rose','cosmic_matrix'];
const themeNames = {
    'cosmic_neon':'🌌 نئون کیهانی',
    'cosmic_aurora':'✨ شفق قطبی',
    'cosmic_void':'🕳️ خلاء سیاه',
    'cosmic_purple':'🔮 بنفش کیهانی',
    'cosmic_sunset':'🌅 غروب کیهانی',
    'cosmic_ocean':'🌊 اقیانوس عمیق',
    'cosmic_gold':'🏛️ طلایی تخت جمشید',
    'cosmic_mint':'🌱 سبز نعنایی',
    'cosmic_rose':'🌸 رز کیهانی',
    'cosmic_matrix':'💻 ماتریکس'
};

function applyTheme(theme) {
    currentTheme = theme;
    localStorage.setItem('cosmic-sub-theme', theme);
    document.documentElement.setAttribute('data-theme', theme);
    document.getElementById('themeDisplay').textContent = themeNames[theme] || 'انتخاب تم';
    document.querySelectorAll('.theme-dropdown .menu-item').forEach(el => {
        el.classList.toggle('active', el.dataset.theme === theme);
    });
    document.getElementById('themeMenu').classList.remove('open');
    document.getElementById('themeArrow').classList.remove('open');
    document.getElementById('themeBtn').textContent = theme.includes('light') || theme.includes('gold') ? '🌙' : '☀️';
}

function toggleThemeMenu() {
    const menu = document.getElementById('themeMenu');
    const arrow = document.getElementById('themeArrow');
    menu.classList.toggle('open');
    arrow.classList.toggle('open');
}

function selectTheme(theme) {
    applyTheme(theme);
    toast('✅ ' + themeNames[theme], 'ok');
}

function toggleTheme() {
    const current = currentTheme;
    const idx = themeList.indexOf(current);
    const next = themeList[(idx + 1) % themeList.length];
    selectTheme(next);
}

document.addEventListener('click', function(e) {
    const dropdown = document.querySelector('.theme-dropdown');
    if (dropdown && !dropdown.contains(e.target)) {
        document.getElementById('themeMenu').classList.remove('open');
        document.getElementById('themeArrow').classList.remove('open');
    }
});

applyTheme(currentTheme);

// انیمیشن نوار پیشرفت
setTimeout(() => {
    const fill = document.getElementById('progressFill');
    if (fill) fill.style.width = '0.0%';
}, 100);
</script>
</body></html>
"""


SUB_PAGE_DENIED = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>✦ ⟦label⟧ · Persepolis</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#030418;--card:rgba(10,14,35,0.55);--card-border:rgba(0,240,255,0.12);
  --text:#e8efff;--text2:#94a3b8;--text3:#64748b;
  --accent:#00f0ff;--accent2:#7b2ff7;--accent3:#ff2e9a;
  --green:#10ffa0;--green-bg:rgba(16,255,160,0.08);--green-text:#10ffa0;
  --red:#ff4d6d;--red-bg:rgba(255,77,109,0.08);--red-text:#ff6b8a;
  --shadow:0 25px 80px rgba(0,0,0,0.6),0 0 120px rgba(0,240,255,0.04);
  --transition:all 0.4s cubic-bezier(0.34,1.56,0.64,1);--radius:18px
}
[data-theme="cosmic_neon"]{--bg:#030418;--card:rgba(10,14,35,0.55);--card-border:rgba(0,240,255,0.12);--accent:#00f0ff;--accent2:#7b2ff7;--accent3:#ff2e9a;--text:#e8efff;--text2:#94a3b8;--text3:#64748b}
[data-theme="cosmic_aurora"]{--bg:#020815;--card:rgba(8,15,30,0.6);--card-border:rgba(16,255,160,0.12);--accent:#10ffa0;--accent2:#00f0ff;--accent3:#7b2ff7;--text:#d4ffe8;--text2:#7eb8a0;--text3:#4a7868}
[data-theme="cosmic_void"]{--bg:#000005;--card:rgba(15,15,25,0.7);--card-border:rgba(100,100,200,0.1);--accent:#8a8aff;--accent2:#aaaaff;--accent3:#cc66ff;--text:#e0e0ff;--text2:#9090c0;--text3:#505078}
[data-theme="cosmic_purple"]{--bg:#08051a;--card:rgba(20,10,40,0.6);--card-border:rgba(123,47,247,0.15);--accent:#7b2ff7;--accent2:#ff2e9a;--accent3:#00f0ff;--text:#f0e8ff;--text2:#a890c0;--text3:#685088}
[data-theme="cosmic_sunset"]{--bg:#1a0810;--card:rgba(40,15,25,0.6);--card-border:rgba(255,46,154,0.12);--accent:#ff2e9a;--accent2:#ffb800;--accent3:#7b2ff7;--text:#ffe8e8;--text2:#c0a090;--text3:#806058}
[data-theme="cosmic_ocean"]{--bg:#001525;--card:rgba(8,25,50,0.6);--card-border:rgba(0,150,255,0.15);--accent:#00f0ff;--accent2:#0066ff;--accent3:#10ffa0;--text:#e0f0ff;--text2:#80b0d0;--text3:#5080a0}
[data-theme="cosmic_gold"]{--bg:#0a0805;--card:rgba(25,20,8,0.6);--card-border:rgba(212,168,67,0.12);--accent:#D4A843;--accent2:#F5D060;--accent3:#B8922E;--text:#F5ECD7;--text2:#C4A35A;--text3:#8A7A4A}
[data-theme="cosmic_mint"]{--bg:#001510;--card:rgba(8,30,20,0.6);--card-border:rgba(16,255,160,0.12);--accent:#10ffa0;--accent2:#00f0ff;--accent3:#7b2ff7;--text:#d0ffe8;--text2:#80c0a0;--text3:#508070}
[data-theme="cosmic_rose"]{--bg:#1a0515;--card:rgba(40,15,30,0.6);--card-border:rgba(255,46,154,0.12);--accent:#ff2e9a;--accent2:#ffb6c1;--accent3:#7b2ff7;--text:#ffe8f0;--text2:#c090a0;--text3:#806070}
[data-theme="cosmic_matrix"]{--bg:#000a00;--card:rgba(0,20,0,0.65);--card-border:rgba(0,255,0,0.15);--accent:#00ff00;--accent2:#00cc00;--accent3:#008800;--text:#c0ffc0;--text2:#80a080;--text3:#506050}

@keyframes twinkle{0%,100%{opacity:0.15}50%{opacity:0.9}}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
@keyframes cardIn{from{opacity:0;transform:translateY(40px) scale(0.92);filter:blur(10px)}to{opacity:1;transform:translateY(0) scale(1);filter:blur(0)}}
@keyframes float{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(20px,-20px) scale(1.05)}}
@keyframes shimmer{0%{background-position:-200% 0}100%{background-position:200% 0}}
@keyframes gradientFlow{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes orbit{0%{transform:rotate(0deg) translateX(120px) rotate(0deg)}100%{transform:rotate(360deg) translateX(120px) rotate(-360deg)}}

body{font-family:'Vazirmatn',sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:16px;background:radial-gradient(ellipse at top,var(--bg),#000 80%);color:var(--text);transition:var(--transition);position:relative;overflow-x:hidden}

#starfield{position:fixed;inset:0;z-index:0;pointer-events:none}
.nebula{position:fixed;border-radius:50%;filter:blur(120px);z-index:0;pointer-events:none;animation:float 12s ease-in-out infinite}
.nebula1{width:500px;height:500px;background:radial-gradient(circle,rgba(0,240,255,0.1),transparent 70%);top:-150px;right:-100px}
.nebula2{width:400px;height:400px;background:radial-gradient(circle,rgba(255,46,154,0.08),transparent 70%);bottom:-100px;left:-80px;animation-delay:-6s}
.nebula3{width:350px;height:350px;background:radial-gradient(circle,rgba(123,47,247,0.08),transparent 70%);top:40%;left:30%;animation-delay:-3s}

/* خطوط هولوگرافیک */
.grid-bg{position:fixed;inset:0;z-index:0;opacity:0.1;background-image:linear-gradient(rgba(0,240,255,0.3) 1px,transparent 1px),linear-gradient(90deg,rgba(0,240,255,0.3) 1px,transparent 1px);background-size:40px 40px;mask-image:radial-gradient(ellipse at center,#000 0%,transparent 60%);-webkit-mask-image:radial-gradient(ellipse at center,#000 0%,transparent 60%);pointer-events:none;animation:gridShift 20s linear infinite}
@keyframes gridShift{from{background-position:0 0}to{background-position:40px 40px}}

/* === دراپ‌داون تم === */
.theme-dropdown{position:fixed;top:20px;left:50%;transform:translateX(-50%);z-index:100}
.theme-dropdown .toggle-btn{background:var(--card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--card-border);border-radius:14px;padding:10px 20px;color:var(--text);font-family:'Vazirmatn',sans-serif;font-size:13px;font-weight:700;cursor:pointer;display:flex;align-items:center;gap:10px;transition:var(--transition);box-shadow:0 8px 40px rgba(0,0,0,0.3)}
.theme-dropdown .toggle-btn:hover{border-color:var(--accent);transform:scale(1.02);box-shadow:0 0 30px rgba(0,240,255,0.2)}
.theme-dropdown .toggle-btn .arrow{transition:transform .3s;font-size:12px}
.theme-dropdown .toggle-btn .arrow.open{transform:rotate(180deg)}
.theme-dropdown .menu{display:none;position:absolute;top:calc(100% + 8px);left:50%;transform:translateX(-50%);background:var(--card);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border:1px solid var(--card-border);border-radius:14px;padding:8px;min-width:220px;box-shadow:0 12px 50px rgba(0,0,0,0.5),0 0 30px rgba(0,240,255,0.1);animation:cardIn .3s ease}
.theme-dropdown .menu.open{display:block}
.theme-dropdown .menu-item{display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:10px;cursor:pointer;transition:var(--transition);color:var(--text2);font-size:13px;font-weight:600}
.theme-dropdown .menu-item:hover{background:rgba(0,240,255,0.06);color:var(--text);transform:translateX(-3px)}
.theme-dropdown .menu-item .dot{display:inline-block;width:20px;height:20px;border-radius:6px;flex-shrink:0;border:1px solid rgba(255,255,255,0.1);box-shadow:0 0 10px rgba(0,240,255,0.2)}
.theme-dropdown .menu-item .check{margin-right:auto;opacity:0;transition:opacity .2s;color:var(--accent);font-weight:900}
.theme-dropdown .menu-item.active .check{opacity:1}
.theme-dropdown .menu-item.active{background:rgba(0,240,255,0.06);color:var(--text)}

/* === کارت اصلی === */
.card{position:relative;z-index:10;background:var(--card);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border:1px solid var(--card-border);border-radius:var(--radius);padding:28px 24px 24px;max-width:520px;width:100%;box-shadow:var(--shadow);animation:cardIn 0.7s var(--transition);transition:var(--transition);margin-top:70px}
.card::before{content:'';position:absolute;inset:0;border-radius:var(--radius);padding:1px;background:linear-gradient(135deg,rgba(0,240,255,0.5),transparent 30%,transparent 70%,rgba(255,46,154,0.5));-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;opacity:0.4;pointer-events:none;animation:borderGlow 6s ease-in-out infinite}
@keyframes borderGlow{0%,100%{opacity:0.3}50%{opacity:0.7}}
.card::after{content:'';position:absolute;top:0;left:30px;right:30px;height:2px;background:linear-gradient(90deg,transparent,var(--accent),var(--accent3),transparent);opacity:0.6;pointer-events:none}

/* هدر */
.card-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:18px;padding-bottom:14px;border-bottom:1px solid var(--card-border);position:relative}
.brand{display:flex;align-items:center;gap:10px}
.brand-icon{width:40px;height:40px;border-radius:12px;background:linear-gradient(135deg,var(--accent),var(--accent2),var(--accent3));display:flex;align-items:center;justify-content:center;font-size:20px;box-shadow:0 0 30px rgba(0,240,255,0.3);animation:iconPulse 4s ease-in-out infinite;position:relative}
.brand-icon::before{content:'';position:absolute;inset:-3px;border-radius:14px;background:inherit;filter:blur(10px);opacity:0.5;z-index:-1}
@keyframes iconPulse{0%,100%{box-shadow:0 0 30px rgba(0,240,255,0.4);transform:scale(1)}50%{box-shadow:0 0 50px rgba(255,46,154,0.5);transform:scale(1.05)}}
.brand-text{font-size:13px;font-weight:900;background:linear-gradient(135deg,#fff,var(--accent),var(--accent3));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;letter-spacing:0.5px}
.brand-sub{font-size:7px;color:var(--text3);letter-spacing:1.5px;text-transform:uppercase;margin-top:1px}
.theme-toggle-btn{background:rgba(0,240,255,0.05);border:1px solid var(--card-border);color:var(--text2);width:34px;height:34px;border-radius:10px;cursor:pointer;font-size:16px;transition:var(--transition)}
.theme-toggle-btn:hover{background:rgba(0,240,255,0.1);transform:rotate(20deg);color:var(--accent);box-shadow:0 0 15px rgba(0,240,255,0.3)}

/* نام کاربر */
.user-name-row{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;flex-wrap:wrap;gap:8px}
.user-name{font-size:22px;font-weight:900;color:var(--text);display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.user-name .proto-badge{font-size:10px;font-weight:700;background:linear-gradient(135deg,rgba(0,240,255,0.12),rgba(255,46,154,0.08));padding:3px 12px;border-radius:14px;color:var(--accent);letter-spacing:0.3px;border:1px solid var(--card-border);box-shadow:0 0 15px rgba(0,240,255,0.1)}
.status-badge{display:inline-flex;align-items:center;gap:5px;padding:4px 14px;border-radius:14px;font-size:11px;font-weight:700;letter-spacing:0.3px}
.status-badge.active{background:var(--green-bg);color:var(--green-text);border:1px solid rgba(16,255,160,0.2);box-shadow:0 0 15px rgba(16,255,160,0.15)}
.status-badge.inactive{background:var(--red-bg);color:var(--red-text);border:1px solid rgba(255,77,109,0.2);box-shadow:0 0 15px rgba(255,77,109,0.15)}
.status-dot{width:7px;height:7px;border-radius:50%;display:inline-block;animation:pulse 1.5s infinite}
.status-dot.green{background:var(--green-text);box-shadow:0 0 8px var(--green-text)}
.status-dot.red{background:var(--red-text);box-shadow:0 0 8px var(--red-text)}

/* UUID */
.uuid-box{background:rgba(0,240,255,0.04);border:1px solid var(--card-border);border-radius:10px;padding:8px 12px;font-size:10px;font-family:monospace;color:var(--accent);word-break:break-all;cursor:pointer;transition:var(--transition);text-align:center;margin:8px 0 12px;letter-spacing:0.3px}
.uuid-box:hover{background:rgba(0,240,255,0.08);transform:scale(1.01);box-shadow:0 0 20px rgba(0,240,255,0.15)}

/* کارت‌های آمار */
.stats-card-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 0}
.stat-info-card{background:rgba(0,240,255,0.03);border:1px solid var(--card-border);border-radius:12px;padding:12px 14px;transition:var(--transition);position:relative;overflow:hidden}
.stat-info-card::before{content:'';position:absolute;top:0;left:0;width:100%;height:1px;background:linear-gradient(90deg,transparent,var(--accent),transparent);opacity:0.5}
.stat-info-card:hover{background:rgba(0,240,255,0.06);transform:translateY(-3px);box-shadow:0 8px 25px rgba(0,240,255,0.1)}
.stat-info-label{font-size:8px;color:var(--text3);font-weight:700;text-transform:uppercase;letter-spacing:0.6px}
.stat-info-value{font-size:17px;font-weight:900;color:var(--text);margin-top:3px}
.stat-info-value .unit{font-size:10px;font-weight:400;color:var(--text2)}
.stat-info-value.used{color:var(--accent);text-shadow:0 0 12px rgba(0,240,255,0.3)}
.stat-info-value.limit{color:var(--text2)}

/* نوار پیشرفت */
.progress-section{margin:10px 0}
.progress-bar{height:6px;border-radius:6px;background:rgba(0,240,255,0.05);overflow:hidden;position:relative;border:1px solid var(--card-border)}
.progress-fill{height:100%;border-radius:6px;background:linear-gradient(90deg,var(--accent),var(--accent2),var(--accent3));background-size:200% 200%;animation:gradientFlow 4s ease infinite;width:0%;transition:width 1.2s ease;box-shadow:0 0 12px rgba(0,240,255,0.5);position:relative}
.progress-fill::after{content:'';position:absolute;top:0;right:0;width:30px;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.6),transparent);animation:shimmer 2s linear infinite}
.progress-text{display:flex;justify-content:space-between;font-size:9px;color:var(--text3);margin-top:5px;letter-spacing:0.3px}
.progress-text .pct{font-weight:900;color:var(--accent);text-shadow:0 0 8px rgba(0,240,255,0.4)}

/* لینک ساب */
.sub-link-section{background:rgba(0,240,255,0.03);border:1px solid var(--card-border);border-radius:12px;padding:10px 14px;margin:10px 0;position:relative;overflow:hidden}
.sub-link-section::before{content:'';position:absolute;top:0;left:0;width:100%;height:1px;background:linear-gradient(90deg,transparent,var(--accent),transparent);opacity:0.5}
.sub-link-label{font-size:8px;font-weight:700;color:var(--text3);text-transform:uppercase;letter-spacing:0.6px;display:flex;align-items:center;gap:5px;margin-bottom:5px}
.sub-link-label i{color:var(--accent);font-size:10px;filter:drop-shadow(0 0 4px var(--accent))}
.sub-link-url{font-family:monospace;font-size:9px;color:var(--accent);word-break:break-all;line-height:1.6;background:rgba(0,0,15,0.4);padding:6px 8px;border-radius:6px;border:1px solid var(--card-border);text-shadow:0 0 8px rgba(0,240,255,0.2)}
.sub-link-actions{display:flex;gap:6px;margin-top:6px;flex-wrap:wrap}
.sub-link-actions .btn{flex:1;font-size:9px;padding:6px 10px;justify-content:center}

/* اپلیکیشن‌ها */
.apps-section{margin:12px 0}
.apps-title{font-size:10px;font-weight:700;color:var(--text3);margin-bottom:8px;display:flex;align-items:center;gap:5px;letter-spacing:0.5px;text-transform:uppercase}
.apps-title i{color:var(--accent);font-size:11px;filter:drop-shadow(0 0 4px var(--accent))}
.apps-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}
.app-btn{background:rgba(0,240,255,0.03);border:1px solid var(--card-border);border-radius:12px;padding:8px 4px;text-align:center;cursor:pointer;transition:var(--transition);text-decoration:none;color:var(--text);position:relative;overflow:hidden}
.app-btn::before{content:'';position:absolute;top:0;left:0;width:100%;height:1px;background:linear-gradient(90deg,transparent,var(--accent),transparent);opacity:0;transition:opacity .3s}
.app-btn:hover{background:rgba(0,240,255,0.08);transform:translateY(-3px);border-color:var(--accent);box-shadow:0 8px 25px rgba(0,240,255,0.15)}
.app-btn:hover::before{opacity:1}
.app-btn .app-icon{font-size:24px;display:block;margin-bottom:4px;filter:drop-shadow(0 0 6px rgba(0,240,255,0.4))}
.app-btn:hover .app-icon{transform:scale(1.15)}
.app-btn .app-name{font-size:7px;color:var(--text2);font-weight:700;display:block;letter-spacing:0.3px}
.app-btn .app-action{font-size:6px;color:var(--text3);display:block;margin-top:1px}
.app-btn .app-action.copy{color:var(--accent)}

/* کانفیگ */
.configs-section{margin:12px 0}
.config-item{display:flex;align-items:center;justify-content:space-between;background:rgba(0,240,255,0.03);border:1px solid var(--card-border);border-radius:10px;padding:8px 12px;margin-bottom:4px;transition:var(--transition)}
.config-item:hover{background:rgba(0,240,255,0.06);transform:translateX(-3px)}
.config-item .config-name{font-size:10px;font-weight:700;color:var(--text)}
.config-item .config-type{font-size:8px;color:var(--text3);background:rgba(0,240,255,0.06);padding:2px 8px;border-radius:6px;letter-spacing:0.3px}
.config-item .config-action{font-size:10px;color:var(--accent);cursor:pointer;transition:var(--transition);padding:4px 8px;border-radius:6px}
.config-item .config-action:hover{color:var(--accent2);background:rgba(0,240,255,0.08)}

/* دکمه‌ها */
.btn{font-family:inherit;font-size:10px;font-weight:700;border-radius:10px;padding:6px 12px;cursor:pointer;display:inline-flex;align-items:center;gap:4px;border:none;transition:var(--transition);white-space:nowrap;justify-content:center;letter-spacing:0.3px}
.btn i{font-size:11px}
.btn-success{background:linear-gradient(135deg,var(--green-bg),rgba(16,255,160,0.15));border:1px solid rgba(16,255,160,0.2);color:var(--green-text)}
.btn-success:hover{background:linear-gradient(135deg,rgba(16,255,160,0.15),rgba(16,255,160,0.25));transform:translateY(-2px);box-shadow:0 4px 20px rgba(16,255,160,0.3)}
.btn-success.copied{background:linear-gradient(135deg,#10ffa0,#00cc80);color:#000;transform:scale(0.95)}
.btn-secondary{background:rgba(255,255,255,0.03);border:1px solid var(--card-border);color:var(--text2)}
.btn-secondary:hover{background:rgba(0,240,255,0.06);color:var(--text);transform:translateY(-2px)}
.btn-gold{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#000;box-shadow:0 0 20px rgba(0,240,255,0.25)}
.btn-gold:hover{transform:translateY(-2px);box-shadow:0 4px 25px rgba(0,240,255,0.4)}

.footer{margin-top:14px;padding-top:12px;border-top:1px solid var(--card-border);text-align:center;font-size:7px;color:var(--text3);letter-spacing:0.5px}
.footer .brand-name{color:var(--accent);font-weight:900;text-shadow:0 0 8px rgba(0,240,255,0.4)}

.toast{position:fixed;bottom:20px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border:1px solid var(--card-border);color:var(--text);border-radius:12px;padding:8px 16px;font-size:10px;opacity:0;transition:var(--transition);z-index:999;pointer-events:none;box-shadow:var(--shadow);display:flex;align-items:center;gap:5px;font-weight:600}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,255,160,0.3);color:var(--green-text);box-shadow:0 8px 30px rgba(16,255,160,0.2)}

@media(max-width:420px){.card{padding:20px 14px;margin-top:80px}.user-name{font-size:19px}.stats-card-grid{gap:6px}.stat-info-value{font-size:15px}.apps-grid{grid-template-columns:repeat(4,1fr)}.app-btn .app-icon{font-size:20px}}

/* ============================================
   ✦ ULTRA COSMIC v3.0 — صفحه اشتراک ✦
   ============================================ */
.aurora{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden;opacity:.85}
.aurora i{position:absolute;display:block;border-radius:50%;filter:blur(100px);mix-blend-mode:screen;will-change:transform,opacity}
.aurora .a1{width:800px;height:280px;top:-90px;right:-10%;background:linear-gradient(100deg,transparent,rgba(16,255,160,0.14),rgba(0,240,255,0.2),transparent);transform:rotate(-12deg);animation:auroraSweep 17s ease-in-out infinite}
.aurora .a2{width:700px;height:240px;top:14%;left:-12%;background:linear-gradient(80deg,transparent,rgba(123,47,247,0.17),rgba(0,240,255,0.11),transparent);transform:rotate(9deg);animation:auroraSweep 22s ease-in-out infinite reverse;animation-delay:-6s}
.aurora .a3{width:600px;height:200px;bottom:-60px;right:10%;background:linear-gradient(90deg,transparent,rgba(255,46,154,0.13),rgba(123,47,247,0.1),transparent);transform:rotate(-5deg);animation:auroraSweep 26s ease-in-out infinite;animation-delay:-13s}
@keyframes auroraSweep{0%,100%{transform:translateX(0) rotate(-11deg) scaleY(1);opacity:.5}33%{transform:translateX(-60px) rotate(-6deg) scaleY(1.4);opacity:.85}66%{transform:translateX(50px) rotate(-15deg) scaleY(.8);opacity:.4}}

.brand-icon{overflow:visible}
.brand-icon svg{width:62%;height:62%;filter:drop-shadow(0 0 8px rgba(0,240,255,0.7))}
.brand-icon .pp-col{animation:ppColWave 2.6s ease-in-out infinite}
.brand-icon .pp-col.c2{animation-delay:.25s}
.brand-icon .pp-col.c3{animation-delay:.5s}
.brand-icon .pp-roof{animation:ppRoofGlow 3.2s ease-in-out infinite}
@keyframes ppColWave{0%,100%{opacity:.65;transform:translateY(0)}50%{opacity:1;transform:translateY(-1.5px)}}
@keyframes ppRoofGlow{0%,100%{filter:drop-shadow(0 0 3px rgba(0,240,255,0.6))}50%{filter:drop-shadow(0 0 10px rgba(255,46,154,0.9))}}
.orbit-ring{position:absolute;inset:-7px;border-radius:14px;border:1px dashed rgba(0,240,255,0.35);animation:spinOrbit 14s linear infinite;pointer-events:none}
@keyframes spinOrbit{to{transform:rotate(360deg)}}
</style>
</head>
<body>
<canvas id="starfield"></canvas>
<div class="aurora"><i class="a1"></i><i class="a2"></i><i class="a3"></i></div>
<div class="nebula nebula1"></div><div class="nebula nebula2"></div><div class="nebula nebula3"></div>
<div class="grid-bg"></div>
<div class="toast" id="toast"></div>

<div class="theme-dropdown">
    <button class="toggle-btn" onclick="toggleThemeMenu()">
        <span>🎨</span>
        <span id="themeDisplay">انتخاب تم کیهانی</span>
        <span class="arrow" id="themeArrow">▾</span>
    </button>
    <div class="menu" id="themeMenu">
        
        <div class="menu-item" data-theme="cosmic_neon" onclick="selectTheme('cosmic_neon')">
            <span class="dot" style="background:linear-gradient(135deg,#00f0ff,#7b2ff7)"></span>
            🌌 نئون کیهانی
            <span class="check">✓</span>
        </div>
        
        <div class="menu-item" data-theme="cosmic_aurora" onclick="selectTheme('cosmic_aurora')">
            <span class="dot" style="background:linear-gradient(135deg,#10ffa0,#00f0ff,#7b2ff7)"></span>
            ✨ شفق قطبی
            <span class="check">✓</span>
        </div>
        
        <div class="menu-item" data-theme="cosmic_void" onclick="selectTheme('cosmic_void')">
            <span class="dot" style="background:linear-gradient(135deg,#0a0a1a,#1a1a3a)"></span>
            🕳️ خلاء سیاه
            <span class="check">✓</span>
        </div>
        
        <div class="menu-item" data-theme="cosmic_purple" onclick="selectTheme('cosmic_purple')">
            <span class="dot" style="background:linear-gradient(135deg,#7b2ff7,#ff2e9a)"></span>
            🔮 بنفش کیهانی
            <span class="check">✓</span>
        </div>
        
        <div class="menu-item" data-theme="cosmic_sunset" onclick="selectTheme('cosmic_sunset')">
            <span class="dot" style="background:linear-gradient(135deg,#ff2e9a,#ffb800)"></span>
            🌅 غروب کیهانی
            <span class="check">✓</span>
        </div>
        
        <div class="menu-item" data-theme="cosmic_ocean" onclick="selectTheme('cosmic_ocean')">
            <span class="dot" style="background:linear-gradient(135deg,#0066ff,#00f0ff)"></span>
            🌊 اقیانوس عمیق
            <span class="check">✓</span>
        </div>
        
        <div class="menu-item" data-theme="cosmic_gold" onclick="selectTheme('cosmic_gold')">
            <span class="dot" style="background:linear-gradient(135deg,#D4A843,#F5D060)"></span>
            🏛️ طلایی تخت جمشید
            <span class="check">✓</span>
        </div>
        
        <div class="menu-item" data-theme="cosmic_mint" onclick="selectTheme('cosmic_mint')">
            <span class="dot" style="background:linear-gradient(135deg,#10ffa0,#00f0ff)"></span>
            🌱 سبز نعنایی
            <span class="check">✓</span>
        </div>
        
        <div class="menu-item" data-theme="cosmic_rose" onclick="selectTheme('cosmic_rose')">
            <span class="dot" style="background:linear-gradient(135deg,#ff2e9a,#ffb6c1)"></span>
            🌸 رز کیهانی
            <span class="check">✓</span>
        </div>
        
        <div class="menu-item" data-theme="cosmic_matrix" onclick="selectTheme('cosmic_matrix')">
            <span class="dot" style="background:linear-gradient(135deg,#00ff00,#008800)"></span>
            💻 ماتریکس
            <span class="check">✓</span>
        </div>
        
    </div>
</div>

<div class="card" id="mainCard">
    <div class="card-header">
        <div class="brand">
            <div class="brand-icon"><img class="logo-img" src="data:image/jpeg;base64,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" alt="P443"></div>
            <div>
                <div class="brand-text">PERSEPOLIS</div>
                <div class="brand-sub">COSMIC SUBSCRIPTION · v3.0</div>
            </div>
        </div>
        <button class="theme-toggle-btn" onclick="toggleTheme()" id="themeBtn">🌙</button>
    </div>

    <div class="user-name-row">
        <div class="user-name">
            ⟦label⟧
            <span class="proto-badge">⟦protocol_icon⟧ ⟦protocol_name⟧ · ⟦http_name⟧</span>
        </div>
        <span class="status-badge inactive">
            <span class="status-dot red"></span>
            غیرفعال
        </span>
    </div>

    <div class="uuid-box" onclick="copyUUID()">🔑 ⟦uuid⟧</div>

    <div class="stats-card-grid">
        <div class="stat-info-card">
            <div class="stat-info-label">📊 مصرف</div>
            <div class="stat-info-value used">⟦used_val⟧ <span class="unit">⟦used_unit⟧</span></div>
        </div>
        <div class="stat-info-card">
            <div class="stat-info-label">📦 سهمیه</div>
            <div class="stat-info-value limit">⟦limit_val⟧ <span class="unit">⟦limit_unit⟧</span></div>
        </div>
        <div class="stat-info-card">
            <div class="stat-info-label">⏳ زمان باقی</div>
            <div class="stat-info-value">⟦days_left⟧</div>
        </div>
        <div class="stat-info-card">
            <div class="stat-info-label">📱 دستگاه‌ها</div>
            <div class="stat-info-value">⟦max_devices⟧</div>
        </div>
    </div>

    <div class="progress-section">
        <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
        <div class="progress-text">
            <span>میزان مصرف</span>
            <span class="pct">0.0%</span>
        </div>
    </div>

    <div class="sub-link-section">
        <div class="sub-link-label"><i class="ti ti-link"></i> لینک اشتراک</div>
        <div class="sub-link-url" id="subLink">⟦sub_url⟧</div>
        <div class="sub-link-actions">
            <button class="btn btn-success" onclick="copySub()" id="copySubBtn"><i class="ti ti-copy"></i> کپی لینک</button>
            <button class="btn btn-gold" onclick="window.open('⟦sub_url⟧', '_blank')"><i class="ti ti-external-link"></i> باز کردن</button>
        </div>
    </div>

    <div class="apps-section">
        <div class="apps-title"><i class="ti ti-devices"></i> نصب روی دستگاه‌ها</div>
        <div class="apps-grid">
            <div class="app-btn" onclick="openApp('hiddify')">
                <span class="app-icon">📱</span>
                <span class="app-name">Hiddify</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('v2rayng')">
                <span class="app-icon">📲</span>
                <span class="app-name">V2rayNG</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('v2box')">
                <span class="app-icon">📱</span>
                <span class="app-name">V2Box</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="copySub()">
                <span class="app-icon">📋</span>
                <span class="app-name">نکست‌وی‌پی‌ان</span>
                <span class="app-action copy">کپی لینک</span>
            </div>
            <div class="app-btn" onclick="openApp('clash')">
                <span class="app-icon">⚔️</span>
                <span class="app-name">Clash Meta</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('windows')">
                <span class="app-icon">🪟</span>
                <span class="app-name">Windows</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('macos')">
                <span class="app-icon">🍎</span>
                <span class="app-name">macOS</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
            <div class="app-btn" onclick="openApp('linux')">
                <span class="app-icon">🐧</span>
                <span class="app-name">Linux</span>
                <span class="app-action">ضربه بزنید</span>
            </div>
        </div>
    </div>

    <div class="configs-section">
        <div class="config-item">
            <span class="config-name">⟦label⟧-Default</span>
            <span class="config-type">⟦protocol_name⟧ · ⟦http_name⟧</span>
            <span class="config-action" onclick="copyConfig('⟦vless_link⟧')">📋</span>
        </div>
    </div>

    <div class="footer">
        <span class="brand-name">✦ PERSEPOLIS</span> · نسخه کیهانی ۲.۰ · ⟦protocol_icon⟧ ⟦protocol_name⟧
    </div>
</div>

<script>
// === ✦ ULTRA COSMIC: ستاره‌های پارالاکس + شهاب‌سنگ Canvas ===
const canvas = document.getElementById('starfield');
const ctx = canvas.getContext('2d');
let stars = [], meteors = [], mouse = {x: 0.5, y: 0.5};
function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    stars = [];
    const count = Math.floor((canvas.width * canvas.height) / 8000);
    for (let i = 0; i < count; i++) {
        stars.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            r: Math.random() * 1.4 + 0.3,
            o: Math.random() * 0.7 + 0.2,
            tw: Math.random() * Math.PI * 2,
            depth: Math.random(),
            color: Math.random() > 0.85 ? '#00f0ff' : (Math.random() > 0.7 ? '#ff2e9a' : '#ffffff')
        });
    }
}
function spawnMeteor() {
    const sx = Math.random() * canvas.width * 0.8 + canvas.width * 0.1;
    meteors.push({
        x: sx, y: -30,
        vx: -(Math.random() * 5 + 3),
        vy: Math.random() * 3.5 + 3,
        len: Math.random() * 80 + 50,
        life: 1, hue: Math.random() > 0.5 ? '#00f0ff' : '#ff2e9a'
    });
}
function drawStars() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const px = (mouse.x - 0.5), py = (mouse.y - 0.5);
    stars.forEach(s => {
        s.tw += 0.018;
        const op = s.o * (0.5 + 0.5 * Math.sin(s.tw));
        const ox = px * 20 * s.depth, oy = py * 14 * s.depth;
        ctx.beginPath();
        ctx.arc(s.x + ox, s.y + oy, s.r, 0, Math.PI * 2);
        ctx.fillStyle = s.color;
        ctx.globalAlpha = op;
        ctx.shadowBlur = 7 + s.depth * 5;
        ctx.shadowColor = s.color;
        ctx.fill();
    });
    if (Math.random() < 0.01 && meteors.length < 3) spawnMeteor();
    for (let i = meteors.length - 1; i >= 0; i--) {
        const m = meteors[i];
        m.x += m.vx; m.y += m.vy; m.life -= 0.007;
        if (m.life <= 0 || m.y > canvas.height + 100) { meteors.splice(i, 1); continue; }
        const grad = ctx.createLinearGradient(m.x, m.y, m.x - m.vx * (m.len / 8), m.y - m.vy * (m.len / 8));
        grad.addColorStop(0, m.hue);
        grad.addColorStop(1, 'transparent');
        ctx.strokeStyle = grad;
        ctx.lineWidth = 2;
        ctx.globalAlpha = Math.min(m.life, 1);
        ctx.shadowBlur = 12;
        ctx.shadowColor = m.hue;
        ctx.beginPath();
        ctx.moveTo(m.x, m.y);
        ctx.lineTo(m.x - m.vx * (m.len / 8), m.y - m.vy * (m.len / 8));
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(m.x, m.y, 2.2, 0, Math.PI * 2);
        ctx.fillStyle = '#fff';
        ctx.fill();
    }
    ctx.globalAlpha = 1;
    ctx.shadowBlur = 0;
    requestAnimationFrame(drawStars);
}
window.addEventListener('resize', resizeCanvas);
window.addEventListener('mousemove', e => { mouse.x = e.clientX / window.innerWidth; mouse.y = e.clientY / window.innerHeight; });
resizeCanvas();
drawStars();

// === ✦ جلوه صوتی سبک (WebAudio) ===
const SFX = {
    ac: null,
    ensure() {
        if (!this.ac) { try { this.ac = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) { return false; } }
        if (this.ac && this.ac.state === 'suspended') this.ac.resume();
        return !!this.ac;
    },
    tone(f1, f2, dur, type, vol, delay) {
        if (localStorage.getItem('pp-sfx') === 'off' || !this.ensure()) return;
        try {
            const t0 = this.ac.currentTime + (delay || 0);
            const o = this.ac.createOscillator(), g = this.ac.createGain();
            o.type = type || 'sine';
            o.frequency.setValueAtTime(f1, t0);
            if (f2) o.frequency.exponentialRampToValueAtTime(f2, t0 + dur);
            g.gain.setValueAtTime(0.0001, t0);
            g.gain.exponentialRampToValueAtTime(vol || 0.05, t0 + 0.015);
            g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
            o.connect(g); g.connect(this.ac.destination);
            o.start(t0); o.stop(t0 + dur + 0.05);
        } catch (e) {}
    },
    click() { this.tone(520, 760, 0.08, 'triangle', 0.04); },
    success() { this.tone(523, 0, 0.1, 'sine', 0.055); this.tone(659, 0, 0.1, 'sine', 0.055, 0.09); this.tone(784, 1046, 0.18, 'sine', 0.065, 0.18); },
    error() { this.tone(220, 110, 0.25, 'sawtooth', 0.045); }
};
document.addEventListener('click', e => { if (e.target.closest('button, .app-btn, .config-item, .menu-item, .btn')) SFX.click(); }, true);

const subUrl = `⟦sub_url⟧`;
const uuid = `⟦uuid⟧`;
const vlessLink = `⟦vless_link⟧`;
const isExpired = true;

function toast(msg, type) {
    const t = document.getElementById('toast');
    t.textContent = msg;
    t.className = 'toast show' + (type ? ' ' + type : '');
    clearTimeout(t._timeout);
    t._timeout = setTimeout(() => t.classList.remove('show'), 2000);
    if (type === 'ok') SFX.success();
    else if (type === 'err') SFX.error();
}

function copySub() {
    const btn = document.getElementById('copySubBtn');
    navigator.clipboard.writeText(subUrl).then(() => {
        toast('✅ ساب‌لینک کپی شد!', 'ok');
        btn.classList.add('copied');
        btn.innerHTML = '<i class="ti ti-check"></i> کپی شد!';
        setTimeout(() => {
            btn.classList.remove('copied');
            btn.innerHTML = '<i class="ti ti-copy"></i> کپی لینک';
        }, 1500);
    }).catch(() => toast('❌ خطا در کپی', 'err'));
}

function copyUUID() {
    navigator.clipboard.writeText(uuid).then(() => toast('✅ کپی شد', 'ok'));
}

function copyConfig(link) {
    navigator.clipboard.writeText(link).then(() => toast('✅ کانفیگ کپی شد!', 'ok'));
}

function openApp(app) {
    const apps = {
        'hiddify': 'https://github.com/hiddify/hiddify-app/releases',
        'v2rayng': 'https://github.com/2dust/v2rayNG/releases',
        'v2box': 'https://apps.apple.com/app/v2box/id6446814670',
        'clash': 'https://github.com/MetaCubeX/ClashMetaForAndroid/releases',
        'windows': 'https://github.com/2dust/v2rayN/releases',
        'macos': 'https://github.com/ShadowLaunch/ShadowLaunch/releases',
        'linux': 'https://github.com/SagerNet/sing-box/releases'
    };
    const url = apps[app];
    if (url) {
        window.open(url, '_blank');
    } else {
        toast('📋 لینک در کلیپ‌بورد', 'ok');
        copySub();
    }
}

// === مدیریت تم‌های کیهانی ===
let currentTheme = localStorage.getItem('cosmic-sub-theme') || 'cosmic_neon';
const themeList = ['cosmic_neon','cosmic_aurora','cosmic_void','cosmic_purple','cosmic_sunset','cosmic_ocean','cosmic_gold','cosmic_mint','cosmic_rose','cosmic_matrix'];
const themeNames = {
    'cosmic_neon':'🌌 نئون کیهانی',
    'cosmic_aurora':'✨ شفق قطبی',
    'cosmic_void':'🕳️ خلاء سیاه',
    'cosmic_purple':'🔮 بنفش کیهانی',
    'cosmic_sunset':'🌅 غروب کیهانی',
    'cosmic_ocean':'🌊 اقیانوس عمیق',
    'cosmic_gold':'🏛️ طلایی تخت جمشید',
    'cosmic_mint':'🌱 سبز نعنایی',
    'cosmic_rose':'🌸 رز کیهانی',
    'cosmic_matrix':'💻 ماتریکس'
};

function applyTheme(theme) {
    currentTheme = theme;
    localStorage.setItem('cosmic-sub-theme', theme);
    document.documentElement.setAttribute('data-theme', theme);
    document.getElementById('themeDisplay').textContent = themeNames[theme] || 'انتخاب تم';
    document.querySelectorAll('.theme-dropdown .menu-item').forEach(el => {
        el.classList.toggle('active', el.dataset.theme === theme);
    });
    document.getElementById('themeMenu').classList.remove('open');
    document.getElementById('themeArrow').classList.remove('open');
    document.getElementById('themeBtn').textContent = theme.includes('light') || theme.includes('gold') ? '🌙' : '☀️';
}

function toggleThemeMenu() {
    const menu = document.getElementById('themeMenu');
    const arrow = document.getElementById('themeArrow');
    menu.classList.toggle('open');
    arrow.classList.toggle('open');
}

function selectTheme(theme) {
    applyTheme(theme);
    toast('✅ ' + themeNames[theme], 'ok');
}

function toggleTheme() {
    const current = currentTheme;
    const idx = themeList.indexOf(current);
    const next = themeList[(idx + 1) % themeList.length];
    selectTheme(next);
}

document.addEventListener('click', function(e) {
    const dropdown = document.querySelector('.theme-dropdown');
    if (dropdown && !dropdown.contains(e.target)) {
        document.getElementById('themeMenu').classList.remove('open');
        document.getElementById('themeArrow').classList.remove('open');
    }
});

applyTheme(currentTheme);

// انیمیشن نوار پیشرفت
setTimeout(() => {
    const fill = document.getElementById('progressFill');
    if (fill) fill.style.width = '0.0%';
}, 100);
</script>
</body></html>
"""


_NOT_FOUND_TPL = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🏛️ کاربر یافت نشد</title>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700;800&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Vazirmatn',sans-serif;background:#0a0a1a;min-height:100vh;display:flex;align-items:center;justify-content:center;color:#F5ECD7}
.card{background:rgba(10,10,30,0.85);backdrop-filter:blur(30px);border:1px solid rgba(212,175,55,0.12);border-radius:28px;padding:40px;max-width:420px;text-align:center}
.icon{font-size:64px;margin-bottom:16px}
h2{font-size:22px;font-weight:800;margin-bottom:8px}
p{color:#8A7A4A;font-size:13px;line-height:1.8}
</style>
</head>
<body>
<div class="card">
    <div class="icon">🏛️</div>
    <h2>کاربر یافت نشد</h2>
    <p>__MSG__</p>
</div>
</body>
</html>
"""


_DISABLED_TPL = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>⛔ کاربر غیرفعال</title>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700;800&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Vazirmatn',sans-serif;background:#0a0a1a;min-height:100vh;display:flex;align-items:center;justify-content:center;color:#F5ECD7}
.card{background:rgba(10,10,30,0.85);backdrop-filter:blur(30px);border:1px solid rgba(239,68,68,0.12);border-radius:28px;padding:40px;max-width:420px;text-align:center}
.icon{font-size:64px;margin-bottom:16px}
h2{font-size:22px;font-weight:800;margin-bottom:8px}
p{color:#8A7A4A;font-size:13px;line-height:1.8}
.status{color:#F87171}
</style>
</head>
<body>
<div class="card">
    <div class="icon">⛔</div>
    <h2>کاربر غیرفعال یا منقضی</h2>
    <p class="status">__MSG__</p>
</div>
</body>
</html>
"""



def not_found_page(msg: str) -> str:
    return _NOT_FOUND_TPL.replace("__MSG__", msg or "")


def disabled_page(msg: str) -> str:
    return _DISABLED_TPL.replace("__MSG__", msg or "")


def get_sub_page_html(uuid: str, link: dict) -> str:
    """رندر صفحه ساب — دقیقاً مثل renderSubPage ورکر کلادفلری"""
    allowed = (link.get("active") is not False) and (not link.get("expired", False))
    tpl = SUB_PAGE_ALLOWED if allowed else SUB_PAGE_DENIED
    max_dev = link.get("max_devices", 0)
    try:
        max_dev_s = str(int(max_dev)) if max_dev and float(max_dev) > 0 else "∞"
    except (TypeError, ValueError):
        max_dev_s = "∞"
    mapping = {
        "uuid": uuid if uuid else link.get("uuid", ""),
        "label": link.get("label", "کاربر"),
        "sub_url": link.get("sub_url", ""),
        "vless_link": link.get("vless_link", ""),
        "days_left": link.get("days_left", "نامحدود"),
        "used_val": link.get("used_val", "0"),
        "used_unit": link.get("used_unit", "B"),
        "limit_val": link.get("limit_val", "∞"),
        "limit_unit": link.get("limit_unit", ""),
        "protocol_icon": link.get("protocol_icon", ""),
        "protocol_name": link.get("protocol_name", "VLESS-WS"),
        "http_name": link.get("http_name", "h2"),
        "max_devices": max_dev_s,
    }
    for k, v in mapping.items():
        tpl = tpl.replace("⟦" + k + "⟧", "" if v is None else str(v))
    return tpl
