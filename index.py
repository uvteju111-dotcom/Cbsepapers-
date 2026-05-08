python3 << 'PYEOF'
html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CBSE Class 10 PYQ Hub - All Subjects All Years</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:sans-serif;background:#0a0e1a;color:#e2e8f0;overflow-x:hidden}
a{text-decoration:none;color:inherit}
::-webkit-scrollbar{width:5px}::-webkit-scrollbar-thumb{background:#3b82f6;border-radius:3px}
nav{position:fixed;top:0;left:0;right:0;z-index:999;background:rgba(10,14,26,.95);border-bottom:1px solid rgba(99,179,237,.1);height:58px;display:flex;align-items:center;justify-content:space-between;padding:0 2rem}
.logo{font-size:1.3rem;font-weight:800;color:#60a5fa}
.logo span{color:#8b5cf6}
.navlinks{display:flex;gap:4px}
.navlinks a{color:#94a3b8;font-size:13px;padding:6px 12px;border-radius:7px;transition:.2s}
.navlinks a:hover{color:#60a5fa;background:rgba(59,130,246,.1)}
.nsearch{display:flex;align-items:center;gap:8px;background:#111827;border:1px solid rgba(99,179,237,.15);border-radius:9px;padding:6px 12px}
.nsearch input{background:none;border:none;outline:none;color:#e2e8f0;font-size:13px;width:180px}
.hero{min-height:90vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:80px 2rem 3rem;background:radial-gradient(ellipse at 20% 50%,rgba(59,130,246,.08) 0,transparent 60%),radial-gradient(ellipse at 80% 20%,rgba(139,92,246,.08) 0,transparent 60%)}
.hero-badge{display:inline-flex;align-items:center;gap:8px;background:rgba(59,130,246,.1);border:1px solid rgba(59,130,246,.3);border-radius:100px;padding:5px 16px;font-size:11px;font-weight:700;color:#60a5fa;text-transform:uppercase;letter-spacing:1px;margin-bottom:20px}
.hero-badge::before{content:'';width:6px;height:6px;background:#34d399;border-radius:50%;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}
.hero h1{font-size:clamp(2rem,5vw,4rem);font-weight:900;line-height:1.1;letter-spacing:-2px;margin-bottom:18px}
.hero h1 .g{background:linear-gradient(135deg,#60a5fa,#8b5cf6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.hero p{color:#94a3b8;font-size:1rem;max-width:540px;margin:0 auto 32px;line-height:1.7}
.stats{display:flex;justify-content:center;gap:36px;margin-bottom:36px;flex-wrap:wrap}
.stat-num{display:block;font-size:1.9rem;font-weight:900;color:#60a5fa;line-height:1}
.stat-label{font-size:11px;color:#64748b;text-transform:uppercase;letter-spacing:.5px;margin-top:3px}
.sbox{display:flex;align-items:center;gap:10px;background:#111827;border:1px solid rgba(99,179,237,.2);border-radius:13px;padding:10px 18px;max-width:520px;margin:0 auto 18px;transition:.2s}
.sbox:focus-within{border-color:#3b82f6;box-shadow:0 0 30px rgba(59,130,246,.15)}
.sbox input{flex:1;background:none;border:none;outline:none;color:#e2e8f0;font-size:14px}
.sbox button{background:#3b82f6;border:none;border-radius:8px;padding:7px 16px;color:#fff;font-size:13px;font-weight:700;cursor:pointer}
.htags{display:flex;gap:8px;justify-content:center;flex-wrap:wrap}
.htag{padding:4px 12px;border-radius:100px;font-size:12px;font-weight:600;border:1px solid;cursor:pointer}
.htag.s{color:#f59e0b;border-color:rgba(245,158,11,.3)}
.htag.c{color:#10b981;border-color:rgba(16,185,129,.3)}
.htag.e{color:#3b82f6;border-color:rgba(59,130,246,.3)}
.htag.h{color:#ec4899;border-color:rgba(236,72,153,.3)}
.htag.p{color:#8b5cf6;border-color:rgba(139,92,246,.3)}
.sec{max-width:1300px;margin:0 auto;padding:60px 2rem}
.sec-tag{font-size:11px;font-weight:700;color:#60a5fa;text-transform:uppercase;letter-spacing:1.5px;margin-bottom:8px}
.sec-title{font-size:clamp(1.6rem,3vw,2.4rem);font-weight:900;letter-spacing:-1px;margin-bottom:10px}
.sec-title span{background:linear-gradient(135deg,#60a5fa,#8b5cf6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.sec-sub{color:#94a3b8;font-size:14px;margin-bottom:36px;max-width:540px}
.div{height:1px;background:linear-gradient(90deg,transparent,rgba(99,179,237,.15),transparent);max-width:1300px;margin:0 auto}
.sbanner{background:linear-gradient(135deg,rgba(59,130,246,.08),rgba(139,92,246,.08));border:1px solid rgba(99,102,241,.2);border-radius:16px;padding:24px 32px;display:flex;align-items:center;gap:18px;flex-wrap:wrap;margin-bottom:48px}
.sbanner-icon{font-size:34px}
.sbanner h3{font-size:1.1rem;font-weight:800;margin-bottom:6px}
.sbanner p{font-size:13px;color:#94a3b8}
.sbanner-links{display:flex;gap:8px;flex-wrap:wrap;margin-left:auto}
.bext{padding:8px 16px;border-radius:8px;font-size:13px;font-weight:700;display:flex;align-items:center;gap:5px}
.bext.p{background:#3b82f6;color:#fff}.bext.o{border:1px solid rgba(99,179,237,.2);color:#94a3b8}
.sgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}
.sc{background:#111827;border:1px solid rgba(99,179,237,.1);border-radius:16px;padding:24px;text-decoration:none;color:inherit;display:block;position:relative;transition:.3s}
.sc:hover{transform:translateY(-4px);border-color:rgba(99,179,237,.22)}
.sc-icon{width:48px;height:48px;border-radius:13px;display:flex;align-items:center;justify-content:center;font-size:24px;margin-bottom:16px}
.sc-arr{position:absolute;top:24px;right:24px;width:28px;height:28px;border:1px solid rgba(99,179,237,.15);border-radius:7px;display:flex;align-items:center;justify-content:center;color:#64748b;transition:.2s}
.sc:hover .sc-arr{background:#3b82f6;border-color:#3b82f6;color:#fff;transform:rotate(-45deg)}
.sc-name{font-size:16px;font-weight:800;margin-bottom:5px}
.sc-desc{font-size:12px;color:#94a3b8;line-height:1.5;margin-bottom:14px}
.sc-meta{display:flex;gap:12px}
.sc-meta b{font-size:12px;font-weight:700;font-family:monospace}
.sc-meta span{font-size:11px;color:#64748b}
.snav{position:sticky;top:58px;z-index:100;background:rgba(10,14,26,.95);border-bottom:1px solid rgba(99,179,237,.1);padding:0 2rem}
.snav-inner{max-width:1300px;margin:0 auto;display:flex;overflow-x:auto;scrollbar-width:none}
.snav-inner::-webkit-scrollbar{display:none}
.stab{padding:12px 16px;font-size:13px;font-weight:600;color:#64748b;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap;text-decoration:none;transition:.2s}
.stab:hover{color:#e2e8f0}
.stab.sa{color:#f59e0b;border-color:#f59e0b}
.stab.sc2{color:#10b981;border-color:#10b981}
.stab.se{color:#3b82f6;border-color:#3b82f6}
.stab.sh{color:#ec4899;border-color:#ec4899}
.stab.sp{color:#8b5cf6;border-color:#8b5cf6}
.stab.sg{color:#60a5fa;border-color:#60a5fa}
.subj-sec{max-width:1300px;margin:0 auto;padding:50px 2rem;scroll-margin-top:110px}
.subj-head{display:flex;align-items:center;gap:16px;margin-bottom:24px;padding-bottom:20px;border-bottom:1px solid rgba(99,179,237,.1)}
.sh-icon{width:56px;height:56px;border-radius:15px;display:flex;align-items:center;justify-content:center;font-size:26px;flex-shrink:0}
.sh-title{font-size:1.7rem;font-weight:900;letter-spacing:-.5px}
.sh-count{font-size:11px;color:#64748b;font-family:monospace;margin-top:3px}
.ybar{background:#111827;border:1px solid rgba(99,179,237,.1);border-radius:12px;padding:14px 18px;display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:18px}
.yl{font-size:11px;font-weight:700;color:#64748b;text-transform:uppercase;flex-shrink:0}
.ycs{display:flex;gap:6px;flex-wrap:wrap;flex:1}
.yc{padding:4px 12px;border-radius:7px;font-size:12px;font-weight:700;font-family:monospace;border:1px solid rgba(99,179,237,.12);background:#141c32;color:#94a3b8;cursor:pointer;transition:.2s}
.yc:hover,.yc.ya{background:#3b82f6;border-color:#3b82f6;color:#fff}
.yc.yn{border-color:#f59e0b;color:#f59e0b;position:relative}
.yc.yn::after{content:'NEW';position:absolute;top:-8px;right:-8px;background:#f59e0b;color:#000;font-size:7px;font-weight:900;padding:1px 4px;border-radius:3px}
.yc.yn:hover,.yc.yn.ya{background:#f59e0b;color:#000}
.ttabs{display:flex;gap:5px;margin-bottom:18px;flex-wrap:wrap}
.ttab{padding:6px 13px;border-radius:8px;font-size:12px;font-weight:600;cursor:pointer;border:1px solid rgba(99,179,237,.1);background:#141c32;color:#94a3b8;transition:.2s;user-select:none}
.ttab:hover{color:#e2e8f0;background:#1a2235}
.ttab.ta{background:#3b82f6;border-color:#3b82f6;color:#fff}
.tw{background:#111827;border:1px solid rgba(99,179,237,.1);border-radius:12px;overflow:hidden;overflow-x:auto;margin-bottom:18px}
.pt{width:100%;border-collapse:collapse;font-size:12px}
.pt thead th{padding:10px 13px;text-align:left;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.7px;color:#64748b;border-bottom:1px solid rgba(99,179,237,.1);background:#0f1526;white-space:nowrap}
.pt tbody tr{border-bottom:1px solid rgba(99,179,237,.07);transition:background .15s}
.pt tbody tr:hover{background:#1a2235}
.pt tbody tr:last-child{border:none}
.pt td{padding:10px 13px;color:#94a3b8;vertical-align:middle;white-space:nowrap}
.pt td:first-child{font-family:monospace;font-weight:700;color:#60a5fa}
.tb{display:inline-flex;align-items:center;gap:3px;padding:4px 10px;border-radius:6px;font-size:11px;font-weight:700;text-decoration:none;transition:.2s}
.tb.d{background:rgba(59,130,246,.12);color:#60a5fa}.tb.d:hover{background:#3b82f6;color:#fff}
.tb.s{background:rgba(16,185,129,.1);color:#34d399}.tb.s:hover{background:#10b981;color:#fff}
.bm{background:rgba(16,185,129,.12);color:#34d399;font-size:9px;font-weight:800;border-radius:4px;padding:2px 7px;text-transform:uppercase}
.bc{background:rgba(59,130,246,.12);color:#60a5fa;font-size:9px;font-weight:800;border-radius:4px;padding:2px 7px;text-transform:uppercase}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:13px;margin-top:20px}
.pc{background:#111827;border:1px solid rgba(99,179,237,.1);border-radius:13px;padding:16px;display:flex;flex-direction:column;gap:10px;transition:.2s}
.pc:hover{border-color:rgba(99,179,237,.22);transform:translateY(-2px);box-shadow:0 0 24px rgba(59,130,246,.08)}
.pc-top{display:flex;align-items:center;justify-content:space-between}
.ytag{font-family:monospace;font-size:10px;font-weight:700;background:#141c32;border:1px solid rgba(99,179,237,.12);border-radius:5px;padding:2px 8px;color:#60a5fa}
.pc-title{font-size:13px;font-weight:700;line-height:1.4}
.pc-meta{display:flex;gap:8px;flex-wrap:wrap}
.pm{font-size:10px;color:#64748b}
.pc-btns{display:flex;gap:6px;margin-top:auto}
.pdb{flex:1;padding:7px;border-radius:8px;font-size:12px;font-weight:700;border:none;text-decoration:none;display:flex;align-items:center;justify-content:center;gap:4px;cursor:pointer;transition:.2s;font-family:sans-serif}
.pdb.pr{background:#3b82f6;color:#fff}.pdb.pr:hover{background:#60a5fa}
.pdb.ps{background:#141c32;color:#94a3b8;border:1px solid rgba(99,179,237,.12)}.pdb.ps:hover{color:#e2e8f0}
.rgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:10px}
.rc{background:#111827;border:1px solid rgba(99,179,237,.1);border-radius:12px;padding:16px 20px;display:flex;align-items:center;gap:12px;transition:.2s}
.rc:hover{border-color:rgba(99,179,237,.22);transform:translateX(4px)}
.ri{width:42px;height:42px;border-radius:11px;display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0}
.rb{flex:1}
.rt{font-weight:700;font-size:13px;margin-bottom:2px}
.rs{font-size:11px;color:#64748b}
.ra{color:#64748b;font-size:15px}
.tgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}
.tc{background:#111827;border:1px solid rgba(99,179,237,.1);border-radius:13px;padding:20px;transition:.2s}
.tc:hover{border-color:rgba(99,179,237,.22);transform:translateY(-2px)}
.tn{font-size:10px;font-weight:700;color:#3b82f6;font-family:monospace;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px}
.tt2{font-size:14px;font-weight:800;margin-bottom:6px}
.tt3{font-size:12px;color:#94a3b8;line-height:1.6}
.flist{display:flex;flex-direction:column;gap:9px}
.fi{background:#111827;border:1px solid rgba(99,179,237,.1);border-radius:12px;overflow:hidden;transition:border-color .2s}
.fi.fo{border-color:#3b82f6}
.fq{padding:15px 20px;display:flex;align-items:center;justify-content:space-between;cursor:pointer;font-weight:600;font-size:13px;gap:12px;transition:background .2s}
.fq:hover{background:#141c32}
.ftog{width:24px;height:24px;border-radius:6px;background:#141c32;display:flex;align-items:center;justify-content:center;font-size:16px;color:#60a5fa;flex-shrink:0;transition:transform .3s}
.fi.fo .ftog{transform:rotate(45deg)}
.fa{padding:0 20px;max-height:0;overflow:hidden;transition:all .3s;font-size:12px;color:#94a3b8;line-height:1.7}
.fi.fo .fa{max-height:180px;padding:0 20px 14px}
.mgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px}
.mc{background:#111827;border:1px solid rgba(99,179,237,.1);border-radius:13px;overflow:hidden}
.mc-head{padding:13px 16px;border-bottom:1px solid rgba(99,179,237,.1);font-weight:800;font-size:13px}
.mc-body{padding:13px 16px}
.mr{display:flex;justify-content:space-between;font-size:12px;padding:6px 0;border-bottom:1px solid rgba(99,179,237,.06)}
.mr:last-of-type{border:none}
.mr span{color:#94a3b8}
.mr b{font-family:monospace;font-weight:700;font-size:11px}
.mn{background:rgba(59,130,246,.07);border-radius:7px;padding:8px 11px;font-size:11px;color:#94a3b8;margin-top:8px}
footer{background:#0f1526;border-top:1px solid rgba(99,179,237,.1);padding:44px 2rem 22px}
.fg{max-width:1300px;margin:0 auto;display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:32px;margin-bottom:36px}
.fd{font-size:12px;color:#64748b;line-height:1.7;margin-top:12px;max-width:260px}
.fct{font-size:11px;font-weight:800;color:#e2e8f0;text-transform:uppercase;letter-spacing:.5px;margin-bottom:12px}
.fl{list-style:none;display:flex;flex-direction:column;gap:8px}
.fl a{color:#64748b;font-size:12px;transition:color .2s}.fl a:hover{color:#60a5fa}
.fb{max-width:1300px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;padding-top:18px;border-top:1px solid rgba(99,179,237,.08);flex-wrap:wrap;gap:8px}
.fc{font-size:11px;color:#64748b}
.fdiscl{font-size:10px;color:#64748b;max-width:440px;text-align:right;line-height:1.5}
#stbtn{position:fixed;bottom:20px;right:20px;width:40px;height:40px;background:#3b82f6;border:none;border-radius:10px;color:#fff;font-size:17px;cursor:pointer;box-shadow:0 4px 16px rgba(59,130,246,.35);z-index:999;display:none;align-items:center;justify-content:center}
.notif{background:linear-gradient(135deg,rgba(245,158,11,.1),rgba(239,68,68,.07));border-bottom:1px solid rgba(245,158,11,.18);padding:6px 2rem;text-align:center;font-size:12px;color:#fbbf24;display:flex;align-items:center;justify-content:center;gap:8px;position:relative;z-index:998;margin-top:58px}
.notif a{color:#f59e0b;font-weight:700;text-decoration:underline}
@media(max-width:768px){.navlinks{display:none}.fg{grid-template-columns:1fr 1fr}.sbanner{flex-direction:column}.sbanner-links{margin-left:0}}
</style>
</head>
<body>
<nav>
  <div class="logo">CBSE<span>PYQ</span>Hub</div>
  <div class="navlinks">
    <a href="#subjects">Subjects</a><a href="#sst">SST</a><a href="#science">Science</a>
    <a href="#english">English</a><a href="#hindi">Hindi</a><a href="#computer">Computer</a>
    <a href="#resources">Resources</a><a href="#tips">Tips</a><a href="#faq">FAQ</a>
  </div>
  <div class="nsearch"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg><input type="text" placeholder="Search papers..." oninput="doSearch(this.value)"></div>
</nav>
<div class="notif">🎯 2025 CBSE Board Papers are now available! <a href="#sst">Browse All →</a></div>
<section class="hero">
  <div>
    <div class="hero-badge">Free · All Years · All Subjects · Class 10</div>
    <h1>CBSE Class 10<br><span class="g">Previous Year Papers</span></h1>
    <p>The most complete collection of CBSE Class 10 board exam papers — SST, Science, English, Hindi &amp; Computer. All sets, all years, completely free.</p>
    <div class="stats">
      <div><span class="stat-num">500+</span><span class="stat-label">Papers</span></div>
      <div><span class="stat-num">2008–25</span><span class="stat-label">Years</span></div>
      <div><span class="stat-num">5</span><span class="stat-label">Subjects</span></div>
      <div><span class="stat-num">100%</span><span class="stat-label">Free</span></div>
    </div>
    <div class="sbox"><input type="text" placeholder="Search e.g. Science 2024 Delhi Set 1..." oninput="doSearch(this.value)"><button>Search</button></div>
    <div class="htags">
      <a href="#sst" class="htag s">📚 Social Science</a>
      <a href="#science" class="htag c">🔬 Science</a>
      <a href="#english" class="htag e">📖 English</a>
      <a href="#hindi" class="htag h">🇮🇳 Hindi</a>
      <a href="#computer" class="htag p">💻 Computer</a>
    </div>
  </div>
</section>
<div class="sec" id="subjects">
  <div class="sec-tag">Browse by Subject</div>
  <h2 class="sec-title">All <span>Subjects</span></h2>
  <p class="sec-sub">Click any subject to see all year-wise papers, solutions, and marking schemes.</p>
  <div class="sgrid">
    <a href="#sst" class="sc" style="border-left:3px solid #f59e0b"><div class="sc-icon" style="background:rgba(245,158,11,.12)">📚</div><div class="sc-arr">→</div><div class="sc-name" style="color:#f59e0b">Social Science</div><div class="sc-desc">History, Geography, Political Science &amp; Economics. 2008–2025 with marking schemes.</div><div class="sc-meta"><span><b style="color:#f59e0b">18</b> Years</span><span><b style="color:#f59e0b">120+</b> Papers</span></div></a>
    <a href="#science" class="sc" style="border-left:3px solid #10b981"><div class="sc-icon" style="background:rgba(16,185,129,.12)">🔬</div><div class="sc-arr">→</div><div class="sc-name" style="color:#10b981">Science</div><div class="sc-desc">Physics, Chemistry &amp; Biology. Full papers with NCERT solutions from 2008–2025.</div><div class="sc-meta"><span><b style="color:#10b981">18</b> Years</span><span><b style="color:#10b981">120+</b> Papers</span></div></a>
    <a href="#english" class="sc" style="border-left:3px solid #3b82f6"><div class="sc-icon" style="background:rgba(59,130,246,.12)">📖</div><div class="sc-arr">→</div><div class="sc-name" style="color:#3b82f6">English</div><div class="sc-desc">Language &amp; Literature and Communicative. Reading, writing, grammar, literature.</div><div class="sc-meta"><span><b style="color:#3b82f6">18</b> Years</span><span><b style="color:#3b82f6">100+</b> Papers</span></div></a>
    <a href="#hindi" class="sc" style="border-left:3px solid #ec4899"><div class="sc-icon" style="background:rgba(236,72,153,.12)">🇮🇳</div><div class="sc-arr">→</div><div class="sc-name" style="color:#ec4899">Hindi</div><div class="sc-desc">Hindi Course A and Course B. Grammar, literature and writing from 2008–2025.</div><div class="sc-meta"><span><b style="color:#ec4899">18</b> Years</span><span><b style="color:#ec4899">100+</b> Papers</span></div></a>
    <a href="#computer" class="sc" style="border-left:3px solid #8b5cf6"><div class="sc-icon" style="background:rgba(139,92,246,.12)">💻</div><div class="sc-arr">→</div><div class="sc-name" style="color:#8b5cf6">Computer</div><div class="sc-desc">Computer Applications (Code 165) &amp; Information Technology (Code 402).</div><div class="sc-meta"><span><b style="color:#8b5cf6">12</b> Years</span><span><b style="color:#8b5cf6">60+</b> Papers</span></div></a>
  </div>
</div>
<div style="max-width:1300px;margin:0 auto;padding:0 2rem 50px">
  <div class="sbanner">
    <div class="sbanner-icon">🏛️</div>
    <div><h3>Official &amp; Trusted Sources</h3><p>All papers from CBSE.gov.in (official) and trusted platforms: myCBSEguide, LearnCBSE, Educart, Vedantu, Selfstudys &amp; ALLEN.</p></div>
    <div class="sbanner-links">
      <a href="https://cbse.gov.in/cbsenew/question-paper.html" target="_blank" class="bext p">🏛️ CBSE Official</a>
      <a href="https://mycbseguide.com/cbse-question-papers.html" target="_blank" class="bext o">📱 myCBSEguide</a>
      <a href="https://www.learncbse.in/cbse-class-10-previous-year-question-papers/" target="_blank" class="bext o">📘 LearnCBSE</a>
      <a href="https://www.educart.co/previous-year-question-paper/cbse-previous-year-question-papers-class-10" target="_blank" class="bext o">🎯 Educart</a>
    </div>
  </div>
</div>
<div class="snav">
  <div class="snav-inner">
    <a href="#sst" class="stab sa" id="st-sst">📚 SST</a>
    <a href="#science" class="stab sc2" id="st-science">🔬 Science</a>
    <a href="#english" class="stab se" id="st-english">📖 English</a>
    <a href="#hindi" class="stab sh" id="st-hindi">🇮🇳 Hindi</a>
    <a href="#computer" class="stab sp" id="st-computer">💻 Computer</a>
    <a href="#resources" class="stab sg" id="st-resources">🔗 Resources</a>
    <a href="#tips" class="stab sg" id="st-tips">💡 Tips</a>
    <a href="#marking" class="stab sg" id="st-marking">📋 Pattern</a>
    <a href="#faq" class="stab sg" id="st-faq">❓ FAQ</a>
  </div>
</div>"""

# Helper to make a table row
def row(year, name, set_, region, typ, dl_url, sol_url, ms_url=None):
    badge = '<span class="bm">Main</span>' if typ == 'Main' else '<span class="bc">Compt.</span>'
    ms = f'<a href="{ms_url}" target="_blank" class="tb d">📋 Scheme</a>' if ms_url else '—'
    return f"""<tr data-y="{year}"><td>{year}</td><td>{name}</td><td>{set_}</td><td>{region}</td><td>{badge}</td>
<td><a href="{dl_url}" target="_blank" class="tb d">⬇ PDF</a></td>
<td><a href="{sol_url}" target="_blank" class="tb s">✓ View</a></td>
<td>{ms}</td></tr>"""

cbse = "https://cbse.gov.in/cbsenew/question-paper.html"
mcbse = "https://mycbseguide.com/cbse-question-papers.html"
learn = "https://www.learncbse.in/cbse-class-10-previous-year-question-papers/"
edu = "https://www.educart.co/previous-year-question-paper/cbse-previous-year-question-papers-class-10"
self_ = "https://www.selfstudys.com/books/cbse-prev-paper/english/class-10th"

# SST rows
sst_rows = ""
for yr, url, sol in [
    (2025, cbse, self_), (2024, learn, learn), (2023, edu, edu),
    (2022, learn, learn), (2020, mcbse, mcbse), (2019, mcbse, mcbse),
    (2018, mcbse, mcbse), (2017, mcbse, mcbse), (2016, mcbse, mcbse),
    (2015, mcbse, mcbse), (2014, mcbse, mcbse), (2013, mcbse, mcbse)
]:
    ms = cbse if yr >= 2015 else None
    sets = ["Set 1", "Set 2", "Set 3"] if yr >= 2018 else ["Set 1", "Set 2"] if yr >= 2015 else ["Set 1"]
    for s in sets:
        sst_rows += row(yr, "Social Science", s, "Delhi", "Main", url, sol, ms)
    if yr >= 2017:
        sst_rows += row(yr, "Social Science", "Set 1", "Outside Delhi", "Main", url, sol, ms)
    if yr == 2024:
        sst_rows += row(yr, "Social Science Compt.", "Set 1", "Delhi", "Compt.", mcbse, mcbse)

# Science rows
sci_rows = ""
for yr, url, sol in [
    (2025, cbse, self_), (2024, learn, learn), (2023, edu, edu),
    (2022, learn, learn), (2020, mcbse, mcbse), (2019, mcbse, mcbse),
    (2018, mcbse, mcbse), (2017, mcbse, mcbse), (2016, mcbse, mcbse),
    (2015, mcbse, mcbse), (2014, mcbse, mcbse), (2013, mcbse, mcbse)
]:
    ms = cbse if yr >= 2015 else None
    sets = ["Set 1", "Set 2", "Set 3"] if yr >= 2018 else ["Set 1", "Set 2"] if yr >= 2015 else ["Set 1"]
    for s in sets:
        sci_rows += row(yr, "Science", s, "Delhi", "Main", url, sol, ms)
    if yr >= 2017:
        sci_rows += row(yr, "Science", "Set 1", "Outside Delhi", "Main", url, sol, ms)
    if yr == 2024:
        sci_rows += row(yr, "Science Compartment", "Set 1", "Delhi", "Compt.", mcbse, mcbse)

# English rows
eng_rows = ""
for yr, url, sol in [
    (2025, cbse, self_), (2024, learn, learn), (2023, edu, edu),
    (2022, mcbse, mcbse), (2020, mcbse, mcbse), (2019, mcbse, mcbse),
    (2018, mcbse, mcbse), (2017, mcbse, mcbse), (2016, mcbse, mcbse)
]:
    ms = cbse if yr >= 2022 else None
    eng_rows += row(yr, "English Lang & Lit", "Set 1", "Delhi", "Main", url, sol, ms)
    eng_rows += row(yr, "English Lang & Lit", "Set 2", "Delhi", "Main", url, sol, ms)
    eng_rows += row(yr, "English Communicative", "Set 1", "Delhi", "Main", url, sol, ms)
    if yr >= 2019:
        eng_rows += row(yr, "English Lang & Lit", "Set 1", "Outside Delhi", "Main", url, sol, ms)

# Hindi rows
hin_rows = ""
for yr, url, sol in [
    (2025, cbse, self_), (2024, learn, learn), (2023, edu, edu),
    (2022, mcbse, mcbse), (2020, mcbse, mcbse), (2019, mcbse, mcbse),
    (2018, mcbse, mcbse), (2017, mcbse, mcbse), (2016, mcbse, mcbse)
]:
    ms = cbse if yr >= 2022 else None
    hin_rows += row(yr, "Hindi Course A", "Set 1", "Delhi", "Main", url, sol, ms)
    hin_rows += row(yr, "Hindi Course A", "Set 2", "Delhi", "Main", url, sol, ms)
    hin_rows += row(yr, "Hindi Course B", "Set 1", "Delhi", "Main", url, sol, ms)
    hin_rows += row(yr, "Hindi Course A", "Set 1", "Outside Delhi", "Main", url, sol, ms)

# Computer rows
com_rows = ""
for yr, url, sol in [
    (2025, cbse, self_), (2024, edu, edu), (2023, learn, learn),
    (2022, mcbse, mcbse), (2020, mcbse, mcbse), (2019, mcbse, mcbse),
    (2018, mcbse, mcbse), (2017, mcbse, mcbse), (2016, mcbse, mcbse)
]:
    ms = cbse if yr >= 2022 else None
    com_rows += row(yr, "Computer Applications (165)", "Set 1", "Delhi", "Main", url, sol, ms)
    com_rows += row(yr, "Information Technology (402)", "Set 1", "Delhi", "Main", url, sol, ms)
    if yr >= 2022:
        com_rows += row(yr, "Computer Applications", "Set 1", "Outside Delhi", "Main", url, sol, ms)

def chapter_cards(subject_color, items):
    cards = ""
    for tag, title, qs, years in items:
        cards += f"""<div class="pc">
<div class="pc-top"><span class="ytag">{tag}</span><span class="bm">Chapter</span></div>
<div class="pc-title">{title}</div>
<div class="pc-meta"><span class="pm">📋 {qs}</span><span class="pm">🗓 {years}</span></div>
<div class="pc-btns">
<a href="{learn}" target="_blank" class="pdb pr">⬇ Download PDF</a>
<a href="{mcbse}" target="_blank" class="pdb ps">Solutions</a>
</div></div>"""
    return cards

sst_chapters = chapter_cards("#f59e0b", [
    ("History","Rise of Nationalism in Europe — All PYQs","25+ Qs","2014–2025"),
    ("History","Nationalism in India (Non-Cooperation, CDM) — PYQs","30+ Qs","2014–2025"),
    ("History","Making of Global World — Trade & Industry PYQs","20+ Qs","2015–2025"),
    ("History","Print Culture & Novels — Board Questions","16+ Qs","2015–2025"),
    ("Geography","Resources & Development — Soil Types & Map","22+ Qs","2013–2025"),
    ("Geography","Water Resources — Dams, Conservation PYQs","18+ Qs","2013–2025"),
    ("Geography","Agriculture — Crops, Land Use, Map Marking","20+ Qs","2014–2025"),
    ("Geography","Minerals & Energy Resources — Map Questions","17+ Qs","2014–2025"),
    ("Civics","Power Sharing & Federalism — All Board Qs","25+ Qs","2015–2025"),
    ("Civics","Democracy & Political Parties — PYQ Collection","20+ Qs","2015–2025"),
    ("Economics","Development & Sectors of Economy PYQs","22+ Qs","2014–2025"),
    ("Economics","Money, Banking & Globalisation — PYQs","24+ Qs","2014–2025"),
    ("Map Work","SST Map Skill — All Standard Map Items","5-mark items","2013–2025"),
])

sci_chapters = chapter_cards("#10b981", [
    ("Physics","Electricity — Ohm's Law, Circuits, Power PYQs","40+ Qs","2013–2025"),
    ("Physics","Light — Reflection, Refraction & Lens Formula","35+ Qs","2013–2025"),
    ("Physics","Magnetic Effects of Current — Motor, Generator","22+ Qs","2014–2025"),
    ("Physics","Sources of Energy — Renewable vs Non-renewable","16+ Qs","2014–2025"),
    ("Chemistry","Chemical Reactions & Equations — All PYQs","30+ Qs","2012–2025"),
    ("Chemistry","Acids, Bases & Salts — pH, Indicators PYQs","28+ Qs","2013–2025"),
    ("Chemistry","Metals & Non-metals — Reactivity, Extraction","24+ Qs","2014–2025"),
    ("Chemistry","Carbon Compounds — Organic Series PYQs","22+ Qs","2014–2025"),
    ("Biology","Life Processes — Nutrition, Respiration PYQs","35+ Qs","2013–2025"),
    ("Biology","Control & Coordination — Brain, Hormones PYQs","26+ Qs","2014–2025"),
    ("Biology","How Organisms Reproduce — Sexual & Asexual","20+ Qs","2014–2025"),
    ("Biology","Heredity & Evolution — Mendel's Laws, Darwin","25+ Qs","2014–2025"),
    ("Biology","Our Environment — Ecosystems, Food Chains","18+ Qs","2013–2025"),
])

eng_chapters = chapter_cards("#3b82f6", [
    ("Reading","Unseen Passages — Factual & Discursive (2015–2025)","50+ Passages","2015–2025"),
    ("Writing","Formal Letters, Articles, Notices — All Formats","40+ Writing Tasks","2014–2025"),
    ("Grammar","Gap Filling, Editing, Transformation PYQs","60+ Grammar Qs","2013–2025"),
    ("Literature","First Flight — Prose Chapters (All) PYQs","All Chapters","2015–2025"),
    ("Literature","First Flight — Poetry Chapters PYQs","All Poems","2015–2025"),
    ("Literature","Footprints Without Feet — Supplementary PYQs","All Chapters","2015–2025"),
    ("Writing","Story Writing & Diary Entry PYQs","20+ Tasks","2015–2025"),
    ("Grammar","Reported Speech & Modals — Board Questions","22+ Qs","2015–2025"),
])

hin_chapters = chapter_cards("#ec4899", [
    ("व्याकरण","रस, अलंकार, समास, संधि — All Grammar PYQs","50+ Qs","2015–2025"),
    ("साहित्य","Kshitij — All Prose Chapters PYQs","All Chapters","2015–2025"),
    ("साहित्य","Kshitij — All Poetry Chapters PYQs","All Poems","2015–2025"),
    ("साहित्य","Kritika — Supplementary Reader PYQs","All Chapters","2015–2025"),
    ("अपठित","Hindi Unseen Passages — Board Questions","30+ Passages","2015–2025"),
    ("लेखन","पत्र, निबंध, संवाद, विज्ञापन लेखन PYQs","40+ Tasks","2014–2025"),
    ("व्याकरण","मुहावरे, लोकोक्तियाँ, वाक्य रूपांतरण","28+ Qs","2015–2025"),
])

com_chapters = chapter_cards("#8b5cf6", [
    ("Java","Java Programming — OOP, Loops, Arrays, Methods","45+ Qs","2013–2025"),
    ("Java","Java — String Handling, Math Class, Constructors","30+ Qs","2014–2025"),
    ("HTML","HTML — Tags, Forms, Tables, Links, Images","30+ Qs","2013–2025"),
    ("Database","SQL & Databases — SELECT, WHERE, JOIN PYQs","25+ Qs","2015–2025"),
    ("Networking","Networking & Internet — Topologies, Protocols","20+ Qs","2015–2025"),
    ("IT","Digital Documentation & Spreadsheets (IT-402)","22+ Qs","2016–2025"),
])

def make_table(tid, rows):
    return f"""<div class="tw"><table class="pt" id="{tid}">
<thead><tr><th>Year</th><th>Paper</th><th>Set</th><th>Region</th><th>Type</th><th>Download</th><th>Solutions</th><th>Marking Scheme</th></tr></thead>
<tbody>{rows}</tbody></table></div>"""

def make_ybar(tid, years):
    chips = ""
    for y in years:
        cls = "yc yn" if y == years[0] else "yc"
        chips += f'<span class="{cls}" onclick="ft(\'{tid}\',this,\'{y}\')">{y}</span>'
    chips += f'<span class="yc" onclick="ft(\'{tid}\',this,\'all\')">All Years</span>'
    return f'<div class="ybar"><span class="yl">Year:</span><div class="ycs">{chips}</div></div>'

html += make_ybar("t-sst", [2025,2024,2023,2022,2020,2019,2018,2017,2016,2015,2014,2013])
html += """<div id="sst" class="subj-sec">
<div class="subj-head"><div class="sh-icon" style="background:rgba(245,158,11,.12)">📚</div>
<div><div class="sh-title" style="color:#f59e0b">Social Science</div>
<div class="sh-count">120+ papers · 2008–2025 · History · Geography · Civics · Economics</div></div></div>"""
html += make_ybar("t-sst", [2025,2024,2023,2022,2020,2019,2018,2017,2016,2015,2014,2013])
html += """<div class="ttabs"><div class="ttab ta" onclick="tt(this)">All</div><div class="ttab" onclick="tt(this)">History</div><div class="ttab" onclick="tt(this)">Geography</div><div class="ttab" onclick="tt(this)">Civics</div><div class="ttab" onclick="tt(this)">Economics</div><div class="ttab" onclick="tt(this)">Delhi</div><div class="ttab" onclick="tt(this)">Outside Delhi</div></div>"""
html += make_table("t-sst", sst_rows)
html += f'<h3 style="font-weight:800;font-size:1rem;margin-bottom:12px;color:#f59e0b">📜 Chapter-wise Important Questions</h3>'
html += f'<div class="pgrid">{sst_chapters}</div></div><div class="div"></div>'

html += """<div id="science" class="subj-sec">
<div class="subj-head"><div class="sh-icon" style="background:rgba(16,185,129,.12)">🔬</div>
<div><div class="sh-title" style="color:#10b981">Science</div>
<div class="sh-count">120+ papers · 2008–2025 · Physics · Chemistry · Biology</div></div></div>"""
html += make_ybar("t-sci", [2025,2024,2023,2022,2020,2019,2018,2017,2016,2015,2014,2013])
html += """<div class="ttabs"><div class="ttab ta" onclick="tt(this)">All</div><div class="ttab" onclick="tt(this)">Physics</div><div class="ttab" onclick="tt(this)">Chemistry</div><div class="ttab" onclick="tt(this)">Biology</div><div class="ttab" onclick="tt(this)">Delhi</div><div class="ttab" onclick="tt(this)">Outside Delhi</div></div>"""
html += make_table("t-sci", sci_rows)
html += f'<h3 style="font-weight:800;font-size:1rem;margin-bottom:12px;color:#10b981">🔬 Chapter-wise Important Questions</h3>'
html += f'<div class="pgrid">{sci_chapters}</div></div><div class="div"></div>'

html += """<div id="english" class="subj-sec">
<div class="subj-head"><div class="sh-icon" style="background:rgba(59,130,246,.12)">📖</div>
<div><div class="sh-title" style="color:#3b82f6">English (Language &amp; Literature)</div>
<div class="sh-count">100+ papers · 2008–2025 · Communicative &amp; Lang-Lit</div></div></div>"""
html += make_ybar("t-eng", [2025,2024,2023,2022,2020,2019,2018,2017,2016])
html += """<div class="ttabs"><div class="ttab ta" onclick="tt(this)">All</div><div class="ttab" onclick="tt(this)">Lang & Lit</div><div class="ttab" onclick="tt(this)">Communicative</div><div class="ttab" onclick="tt(this)">Reading</div><div class="ttab" onclick="tt(this)">Writing</div><div class="ttab" onclick="tt(this)">Literature</div></div>"""
html += make_table("t-eng", eng_rows)
html += f'<h3 style="font-weight:800;font-size:1rem;margin-bottom:12px;color:#3b82f6">📖 Section-wise Practice</h3>'
html += f'<div class="pgrid">{eng_chapters}</div></div><div class="div"></div>'

html += """<div id="hindi" class="subj-sec">
<div class="subj-head"><div class="sh-icon" style="background:rgba(236,72,153,.12)">🇮🇳</div>
<div><div class="sh-title" style="color:#ec4899">Hindi</div>
<div class="sh-count">100+ papers · 2008–2025 · Course A &amp; Course B</div></div></div>"""
html += make_ybar("t-hin", [2025,2024,2023,2022,2020,2019,2018,2017,2016])
html += """<div class="ttabs"><div class="ttab ta" onclick="tt(this)">All</div><div class="ttab" onclick="tt(this)">Course A</div><div class="ttab" onclick="tt(this)">Course B</div><div class="ttab" onclick="tt(this)">व्याकरण</div><div class="ttab" onclick="tt(this)">साहित्य</div><div class="ttab" onclick="tt(this)">लेखन</div></div>"""
html += make_table("t-hin", hin_rows)
html += f'<h3 style="font-weight:800;font-size:1rem;margin-bottom:12px;color:#ec4899">🇮🇳 Section-wise Practice</h3>'
html += f'<div class="pgrid">{hin_chapters}</div></div><div class="div"></div>'

html += """<div id="computer" class="subj-sec">
<div class="subj-head"><div class="sh-icon" style="background:rgba(139,92,246,.12)">💻</div>
<div><div class="sh-title" style="color:#8b5cf6">Computer Applications / IT</div>
<div class="sh-count">60+ papers · 2013–2025 · Code 165 &amp; Code 402</div></div></div>"""
html += make_ybar("t-com", [2025,2024,2023,2022,2020,2019,2018,2017,2016])
html += """<div class="ttabs"><div class="ttab ta" onclick="tt(this)">All</div><div class="ttab" onclick="tt(this)">Computer Apps</div><div class="ttab" onclick="tt(this)">Information Tech</div><div class="ttab" onclick="tt(this)">Java/HTML</div><div class="ttab" onclick="tt(this)">Database</div><div class="ttab" onclick="tt(this)">Networking</div></div>"""
html += make_table("t-com", com_rows)
html += f'<h3 style="font-weight:800;font-size:1rem;margin-bottom:12px;color:#8b5cf6">💻 Topic-wise Practice</h3>'
html += f'<div class="pgrid">{com_chapters}</div></div><div class="div"></div>'

resources = [
    ("🏛️","rgba(59,130,246,.1)","CBSE Official — cbse.gov.in","Official papers directly from CBSE. Most authentic source.",cbse),
    ("📱","rgba(16,185,129,.1)","myCBSEguide — Papers from 2005","Archive from 2005 with mobile app and practice tests.",mcbse),
    ("📘","rgba(245,158,11,.1)","LearnCBSE — Expert Solutions","Solved papers with NCERT-aligned solutions.",learn),
    ("🎯","rgba(236,72,153,.1)","Educart — 2013–2025 All Sets","All sets with compartment papers and topper sheets.",edu),
    ("📊","rgba(139,92,246,.1)","Selfstudys — Region-wise Papers","Region-wise organized with Maths Basic/Standard split.",self_),
    ("🌊","rgba(6,182,212,.1)","Vedantu — Solved + Video","Step-by-step solutions and video explanations.","https://www.vedantu.com/previous-year-question-paper/cbse-previous-year-question-papers-class-10"),
    ("🔥","rgba(239,68,68,.1)","ALLEN — Expert Analysis","Exam-ready solutions by ALLEN faculty with trend analysis.","https://allen.in/cbse/class-10-previous-year-question-papers"),
    ("🦉","rgba(245,158,11,.1)","Oswaal Books — Marking Schemes","Chapter-wise with marking schemes and topper answers.","https://oswaalbooks.com/pages/cbse-class-10-previous-year-question-papers"),
    ("📙","rgba(16,185,129,.1)","NCERT Official — Textbooks","Official NCERT books and exemplar problems.","https://ncert.nic.in"),
    ("🏆","rgba(59,130,246,.1)","TopperLearning — Video Answers","Video explanations of board answers for visual learners.","https://www.topperlearning.com"),
    ("📗","rgba(6,182,212,.1)","Oswaal360 — Free PDF","Multiple years with solutions in clean PDF format.","https://www.oswaal360.com"),
    ("🎓","rgba(139,92,246,.1)","ShikshaNation — 2016–2025","Year-wise with chapter-level topic filtering.","https://shikshanation.com/blog/cbse-class-10-previous-year-question-papers/"),
]

res_html = '<div class="rgrid">'
for icon, bg, title, sub, url in resources:
    res_html += f'<a href="{url}" target="_blank" class="rc"><div class="ri" style="background:{bg}">{icon}</div><div class="rb"><div class="rt">{title}</div><div class="rs">{sub}</div></div><div class="ra">→</div></a>'
res_html += '</div>'

html += f'''<div id="resources" class="sec">
<div class="sec-tag">Trusted Platforms</div>
<h2 class="sec-title">Best <span>Online Resources</span></h2>
<p class="sec-sub">Top platforms for CBSE Class 10 PYQs, solutions, and study materials — all free.</p>
{res_html}
</div><div class="div"></div>'''

tips = [
    ("Tip 01","Solve Under Exam Conditions","Set a 3-hour timer, sit at a desk, attempt the full paper without help. This builds mental stamina and time-sense needed for the real board exam."),
    ("Tip 02","Study the Marking Scheme","After solving, compare with the official marking scheme — not just for correct answers but to learn how CBSE wants answers structured and what key points to include."),
    ("Tip 03","Spot Repeating Questions","Many questions appear every 2–3 years. Mark repeating topics — these are highest priority. SST: Federalism. Science: Electricity, Chemical Reactions."),
    ("Tip 04","Start 2 Months Before Boards","Begin PYQs after covering 70–80% of syllabus. Solve 5–7 full papers per subject and leave time to plug gaps before the final exam."),
    ("Tip 05","Chapter-wise First, Full Papers Later","Start with chapter-wise PYQs to build confidence, then graduate to full timed papers. This two-phase approach gives both depth and breadth."),
    ("Tip 06","Maps = Free Marks in SST","Map questions are predictable 5-mark opportunities. Practice all standard map items from History and Geography until you mark them from memory."),
    ("Tip 07","Review Errors Within 24 Hours","Check your paper within 24 hours. Keep an error log and revisit it before every subsequent paper you solve."),
    ("Tip 08","Check Current Year Pattern First","Always check the current year's sample paper before solving old ones to understand the latest format and mark distribution."),
    ("Tip 09","Diagrams = Guaranteed Marks in Science","Well-labeled Science diagrams fetch 2–3 marks each. Practice human heart, nephron, eye, ray diagrams, and circuits until you draw them cleanly from memory."),
]

tips_html = '<div class="tgrid">'
for num, title, text in tips:
    tips_html += f'<div class="tc"><div class="tn">{num}</div><div class="tt2">{title}</div><div class="tt3">{text}</div></div>'
tips_html += '</div>'

html += f'''<div id="tips" class="sec">
<div class="sec-tag">Study Strategy</div>
<h2 class="sec-title">How to Use <span>PYQs Effectively</span></h2>
<p class="sec-sub">Expert tips to maximize your board exam score using previous year papers.</p>
{tips_html}
</div><div class="div"></div>'''

html += '''<div id="marking" class="sec">
<div class="sec-tag">Paper Structure</div>
<h2 class="sec-title">CBSE Class 10 <span>Exam Pattern 2025</span></h2>
<p class="sec-sub">Understand the mark distribution for each subject before solving papers.</p>
<div class="mgrid">
<div class="mc"><div class="mc-head" style="color:#f59e0b">📚 Social Science — 80 Marks</div><div class="mc-body">
<div class="mr"><span>Section A: MCQ (1 mark each)</span><b style="color:#f59e0b">20 Marks</b></div>
<div class="mr"><span>Section B: Short Answer (2 marks)</span><b style="color:#f59e0b">20 Marks</b></div>
<div class="mr"><span>Section C: Long Answer (5 marks)</span><b style="color:#f59e0b">20 Marks</b></div>
<div class="mr"><span>Section D: Map Skills</span><b style="color:#f59e0b">5 Marks</b></div>
<div class="mr"><span>Source-based Questions</span><b style="color:#f59e0b">15 Marks</b></div>
<div class="mn">⏱ 3 Hours | Internal Assessment: 20 Marks</div></div></div>
<div class="mc"><div class="mc-head" style="color:#10b981">🔬 Science — 80 Marks</div><div class="mc-body">
<div class="mr"><span>Section A: MCQ (1 mark each)</span><b style="color:#10b981">20 Marks</b></div>
<div class="mr"><span>Section B: Very Short (2 marks)</span><b style="color:#10b981">20 Marks</b></div>
<div class="mr"><span>Section C: Short Answer (3 marks)</span><b style="color:#10b981">24 Marks</b></div>
<div class="mr"><span>Section D: Long Answer (5 marks)</span><b style="color:#10b981">16 Marks</b></div>
<div class="mn">⏱ 3 Hours | Internal Assessment: 20 Marks</div></div></div>
<div class="mc"><div class="mc-head" style="color:#3b82f6">📖 English L&amp;L — 80 Marks</div><div class="mc-body">
<div class="mr"><span>Section A: Reading (2 passages)</span><b style="color:#3b82f6">20 Marks</b></div>
<div class="mr"><span>Section B: Writing (letters, articles)</span><b style="color:#3b82f6">20 Marks</b></div>
<div class="mr"><span>Section B: Grammar</span><b style="color:#3b82f6">10 Marks</b></div>
<div class="mr"><span>Section C: Literature</span><b style="color:#3b82f6">30 Marks</b></div>
<div class="mn">⏱ 3 Hours | Internal Assessment: 20 Marks</div></div></div>
<div class="mc"><div class="mc-head" style="color:#ec4899">🇮🇳 Hindi Course A — 80 Marks</div><div class="mc-body">
<div class="mr"><span>Section A: Unseen Passages</span><b style="color:#ec4899">14 Marks</b></div>
<div class="mr"><span>Section B: Grammar (व्याकरण)</span><b style="color:#ec4899">16 Marks</b></div>
<div class="mr"><span>Section C: Literature (Kshitij)</span><b style="color:#ec4899">30 Marks</b></div>
<div class="mr"><span>Section D: Writing (लेखन)</span><b style="color:#ec4899">20 Marks</b></div>
<div class="mn">⏱ 3 Hours | Internal Assessment: 20 Marks</div></div></div>
<div class="mc"><div class="mc-head" style="color:#8b5cf6">💻 Computer Applications — 100 Marks</div><div class="mc-body">
<div class="mr"><span>Theory Paper (Written Exam)</span><b style="color:#8b5cf6">50 Marks</b></div>
<div class="mr"><span>Practical Exam</span><b style="color:#8b5cf6">30 Marks</b></div>
<div class="mr"><span>Project Work</span><b style="color:#8b5cf6">10 Marks</b></div>
<div class="mr"><span>Internal Assessment</span><b style="color:#8b5cf6">10 Marks</b></div>
<div class="mn">⏱ Theory: 2 Hours | Practical: School-based</div></div></div>
</div></div><div class="div"></div>'''

faqs = [
    ("Where can I download official CBSE Class 10 PYQs?","Download from cbse.gov.in. For older archives (2005 onwards), myCBSEguide, LearnCBSE, Educart, Selfstudys and Vedantu have free collections with solutions."),
    ("Are PYQs enough to score 90+ in board exams?","PYQs are crucial but complement — not replace — NCERT textbooks. Complete NCERT first, then solve 5–7 years per subject. CBSE often lifts questions directly from NCERT examples."),
    ("How many years of papers should I solve?","Solve at least 5–7 years per subject. Start with 2024 and 2023 (current pattern), then go backwards. Pre-2013 papers are less useful as the pattern has changed."),
    ("What is the difference between Delhi and Outside Delhi papers?","Both have similar difficulty. Some questions differ. Solving both sets gives broader coverage of possible question types — highly recommended."),
    ("Are 2021–22 Term 1 and Term 2 papers useful?","Term 2 descriptive papers are fully useful. Term 1 MCQ papers have limited value since CBSE returned to the traditional 80-mark format from 2023 onwards."),
    ("How do I use the marking scheme effectively?","After solving, compare each answer with the marking scheme. Note missing key points, expected word limits, and how marks are distributed. This teaches you exactly how CBSE wants answers structured."),
    ("What is the difference between Computer Applications and IT?","Computer Applications (Code 165): Java, HTML, networking, SQL. Information Technology (Code 402): LibreOffice tools, digital documentation, spreadsheets. Very different papers — practice the correct one."),
    ("When should I start solving PYQs?","Start when you've covered 70–80% of the syllabus — ideally 2–3 months before boards. Begin with chapter-wise PYQs, then move to full timed papers for best results."),
    ("What is a Compartment paper?","The Compartment Exam is for students who fail in 1–2 subjects. Compartment papers are separate, usually slightly easier, but follow the same syllabus. Great extra practice for main exam prep."),
]

faq_html = '<div class="flist">'
for q, a in faqs:
    faq_html += f'<div class="fi" onclick="faq(this)"><div class="fq">{q}<div class="ftog">+</div></div><div class="fa">{a}</div></div>'
faq_html += '</div>'

html += f'''<div id="faq" class="sec">
<div class="sec-tag">FAQ</div>
<h2 class="sec-title">Frequently <span>Asked Questions</span></h2>
{faq_html}
</div>'''

html += '''<footer>
<div class="fg">
<div>
<div style="font-size:1.2rem;font-weight:900;color:#60a5fa">CBSE<span style="color:#8b5cf6">PYQ</span>Hub</div>
<div class="fd">The most comprehensive free collection of CBSE Class 10 board exam papers for SST, Science, English, Hindi, and Computer. Built for students.</div>
</div>
<div><div class="fct">Subjects</div><ul class="fl"><li><a href="#sst">📚 Social Science</a></li><li><a href="#science">🔬 Science</a></li><li><a href="#english">📖 English</a></li><li><a href="#hindi">🇮🇳 Hindi</a></li><li><a href="#computer">💻 Computer</a></li></ul></div>
<div><div class="fct">Resources</div><ul class="fl"><li><a href="https://cbse.gov.in" target="_blank">CBSE Official</a></li><li><a href="https://ncert.nic.in" target="_blank">NCERT Website</a></li><li><a href="https://mycbseguide.com" target="_blank">myCBSEguide</a></li><li><a href="https://learncbse.in" target="_blank">LearnCBSE</a></li><li><a href="https://vedantu.com" target="_blank">Vedantu</a></li><li><a href="https://educart.co" target="_blank">Educart</a></li></ul></div>
<div><div class="fct">Quick Links</div><ul class="fl"><li><a href="#subjects">All Subjects</a></li><li><a href="#resources">Platforms</a></li><li><a href="#tips">Study Tips</a></li><li><a href="#marking">Exam Pattern</a></li><li><a href="#faq">FAQ</a></li></ul></div>
</div>
<div class="fb">
<div class="fc">© 2025 CBSEPYQHub — Free Educational Resource for Class 10 Students</div>
<div class="fdiscl">⚠️ Papers linked from official CBSE and trusted platforms. We do not host PDF files. Free index resource for students.</div>
</div>
</footer>
<button id="stbtn" onclick="window.scrollTo({top:0,behavior:'smooth'})">↑</button>
<script>
window.addEventListener('scroll',()=>{document.getElementById('stbtn').style.display=window.scrollY>400?'flex':'none'});
function faq(el){const o=el.classList.contains('fo');document.querySelectorAll('.fi').forEach(f=>f.classList.remove('fo'));if(!o)el.classList.add('fo')}
function tt(el){el.closest('.ttabs').querySelectorAll('.ttab').forEach(t=>t.classList.remove('ta'));el.classList.add('ta')}
function ft(tid,chip,year){
  const t=document.getElementById(tid);
  if(!t)return;
  t.querySelectorAll('tbody tr').forEach(r=>{r.style.display=(year==='all'||r.getAttribute('data-y')===year)?'':'none'});
  chip.closest('.ycs').querySelectorAll('.yc').forEach(c=>c.classList.remove('ya'));
  chip.classList.add('ya');
}
function doSearch(q){
  q=q.toLowerCase().trim();
  ['t-sst','t-sci','t-eng','t-hin','t-com'].forEach(id=>{
    const t=document.getElementById(id);
    if(t)t.querySelectorAll('tbody tr').forEach(r=>{r.style.display=(!q||r.textContent.toLowerCase().includes(q))?'':'none'});
  });
}
const sids=['sst','science','english','hindi','computer','resources','tips','marking','faq'];
window.addEventListener('scroll',()=>{
  let cur='sst';
  sids.forEach(id=>{const el=document.getElementById(id);if(el&&window.scrollY>=el.offsetTop-130)cur=id});
  document.querySelectorAll('.stab').forEach(t=>t.className=t.className.replace(/ s[a-z0-9]+$/,''));
  const m={'sst':'sa','science':'sc2','english':'se','hindi':'sh','computer':'sp'};
  const active=document.getElementById('st-'+cur);
  if(active){const cls=m[cur]||'sg';active.classList.add(cls)}
});
</script>
</body></html>'''

with open('/mnt/user-data/outputs/cbse_pyq.html','w',encoding='utf-8') as f:
    f.write(html)

import os
size = os.path.getsize('/mnt/user-data/outputs/cbse_pyq.html')
lines = html.count('\n')
print(f"SUCCESS! File written: {size:,} bytes, ~{lines:,} lines")
PYEOF
