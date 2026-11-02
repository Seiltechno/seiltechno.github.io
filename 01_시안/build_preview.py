# -*- coding: utf-8 -*-
"""site/_products/*.md 를 읽어 디자인 시안 HTML(목록 + 상세)을 만듭니다.
실행: python3 build_preview.py  → 이 폴더에 결과 HTML 생성"""
import glob, os, re, html, yaml
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(HERE, "..", "site")
# ───── 카테고리 설정: 새 카테고리는 여기에 추가 ─────
CATCFG = {
 "현미경": {"file": "제품목록_현미경.html",
   "desc": "접안렌즈 없는 실체 현미경부터 4K·3D 디지털 현미경까지. 작업 방식과 배율에 맞는 제품을 찾아보세요.",
   "subs": [("실체 현미경(무접안)", "Eyepiece-less Stereo", "접안렌즈 없이 넓은 뷰어로 보는 광학 입체 현미경"),
            ("디지털 현미경", "Digital", "모니터로 보고 측정·기록까지 하는 카메라 현미경"),
            ("3D 디지털 현미경", "3D Digital", "디지털 영상을 입체로 보고 저장·공유하는 차세대 현미경"),
            ("고배율·자동화 디지털 현미경", "High-mag & Automated", "수천 배 고배율과 전동 자동화, 3D 형상 분석")],
   "banner_after": "디지털 현미경"},
 "측정 시스템": {"file": "제품목록_측정시스템.html",
   "desc": "측정 현미경부터 고배율 측정기, 자동 비디오 측정기(VMM)까지. 부품 크기와 정밀도, 자동화 수준에 맞는 측정 장비를 찾아보세요.",
   "subs": [("측정 현미경", "Measuring Microscope", "눈으로 보고 정확하게 재는 광학·비디오 측정 현미경"),
            ("고배율 비접촉 측정기", "High-mag VMM", "금속현미경 광학계로 초소형 부품을 고배율 측정"),
            ("비디오 측정기(VMM)", "Video Measuring Machine", "카메라와 소프트웨어로 치수를 자동·반복 측정")],
   "banner_after": "고배율 비접촉 측정기"},
 "AI 검사·측정": {"file": "제품목록_AI검사측정.html",
   "desc": "측정과 외관 검사를 하나로, 공정 안에서 바로. AI와 비전 기술로 검사 공정을 줄이는 솔루션입니다.",
   "subs": [("하이브리드 검사·측정", "Hybrid M&I", "VMM 치수 측정과 AI 외관 검사를 한 번에 판정"),
            ("기상 AI분석", "On-Machine AI Analysis", "가공기 안에서 찍은 공구 영상을 AI가 바로 진단·계측"),
            ("기상 검사/측정 비전", "On-Machine Inspection & Measurement", "가공기 안에 카메라를 달아 공구·가공물을 떼지 않고 확대 검사·측정")],
   "banner_after": None},
}
CATCFG["머신비전"] = {"file": "제품목록_머신비전.html", "show_empty": True,
   "desc": "현장에 맞춘 비전 시스템부터 스마트 카메라, 자체 개발 소프트웨어, 광학 부품까지. 검사 자동화에 필요한 구성을 함께 찾습니다.",
   "subs": [("머신비전 Customized", "Customized Vision", "현장 조건에 맞춰 카메라·렌즈·조명·소프트웨어를 조합한 맞춤형 비전 시스템"),
            ("Smart Camera", "Smart Camera", "카메라 안에서 판독·검사까지 처리하는 스마트 카메라"),
            ("Software", "Software", "세일테크노 자체 개발 소프트웨어 — 비전 검사, 현미경 응용"),
            ("Optical Component", "Optical Component", "산업용 렌즈, 텔레센트릭 렌즈, 조명 등 광학 부품")],
   "banner_after": None}
CATS = ["현미경", "측정 시스템", "AI 검사·측정", "머신비전", "3D·특수 센싱"]
SUB_INFO = {}
for _c, _cfg in CATCFG.items():
    for _i, (_s, _en, _ds) in enumerate(_cfg["subs"]):
        SUB_INFO[_s] = {"cat": _c, "n": _i + 1, "en": _en, "desc": _ds, "id": "sub%d" % (_i + 1)}
def cat_link(c, root):
    return root + CATCFG[c]["file"] if c in CATCFG else "#"

import urllib.parse
_MARK_RAW = open(os.path.join(SITE, "assets", "img", "brand", "seil-mark.svg"), encoding="utf-8").read()
MARK = _MARK_RAW.replace('<svg ', '<svg class="seil-mark" aria-hidden="true" focusable="false" ', 1).replace('fill="#12365A"', 'fill="currentColor"')
FAVICON = '<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,' + urllib.parse.quote(_MARK_RAW) + '">'

def load():
    out = []
    for f in glob.glob(os.path.join(SITE, "_products", "*.md")):
        t = open(f, encoding="utf-8").read()
        _, fm, body = t.split("---", 2)
        d = yaml.safe_load(fm); d["slug"] = os.path.splitext(os.path.basename(f))[0]; d["body"] = body.strip()
        d["specs"] = [(x.get("label", ""), x.get("value", "")) if isinstance(x, dict) else tuple(x) for x in (d.get("specs") or [])]
        for k in ("highlights", "applications", "tags", "gallery"): d[k] = d.get(k) or []
        if d.get("published") is False and os.environ.get("PUBLISH"): continue   # 공개 안 함 표시된 제품은 공개용에서 제외
        out.append(d)
    return sorted(out, key=lambda d: d.get("order", 99))

e = lambda s: html.escape(str(s))
def md(s):
    blocks = []
    for b in re.split(r"\n\s*\n", s):
        b = e(b.strip()); b = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", b)
        if b.startswith("&gt;"): blocks.append('<div class="notice">' + b[4:].strip() + "</div>")
        elif b: blocks.append("<p>" + b.replace("\n", " ") + "</p>")
    return "\n".join(blocks)

CSS = """
:root{--navy:#1B2B4B;--navy2:#24385f;--blue:#2A7BE4;--mint:#00C9A7;--ink:#1d2433;--sub:#5b6577;--line:#e3e8ef;--bg:#f5f7fa;--card:#fff}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Pretendard,"Pretendard Variable","Malgun Gothic","Apple SD Gothic Neo",sans-serif;color:var(--ink);background:#fff;line-height:1.65;word-break:keep-all}
a{color:inherit;text-decoration:none}
.wrap{max-width:1200px;margin:0 auto;padding:0 24px}
header{position:sticky;top:0;z-index:10;background:rgba(255,255,255,.96);backdrop-filter:blur(6px);border-bottom:1px solid var(--line)}
header .wrap{display:flex;align-items:center;height:72px;gap:40px}
.logo{display:flex;align-items:center;gap:10px;font-weight:800;font-size:19px;color:#12365A;letter-spacing:-.3px}.logo .seil-mark{width:34px;height:34px;flex:none}.logo span span{color:var(--blue)}
footer .fmark{display:flex;align-items:center;gap:10px;margin-bottom:10px;color:#fff;font-weight:700}footer .fmark .seil-mark{width:26px;height:26px}
nav{display:flex;gap:32px;flex:1;font-weight:600;font-size:15px}nav a.on{color:var(--blue)}
.btn{display:inline-flex;align-items:center;gap:6px;padding:11px 20px;border-radius:8px;font-weight:700;font-size:14px;border:1px solid transparent;cursor:pointer}
.btn-primary{background:var(--blue);color:#fff}.btn-primary:hover{background:#1f68c7}
.btn-ghost{border-color:var(--line);background:#fff;color:var(--ink)}.btn-mint{background:var(--mint);color:var(--navy)}
.hero{background:linear-gradient(120deg,var(--navy),var(--navy2));color:#fff;padding:56px 0 48px}
.crumb{font-size:13px;opacity:.7;margin-bottom:10px}.hero h1{font-size:34px;letter-spacing:-.5px}
.hero p{opacity:.85;margin-top:8px;max-width:640px}
.cats{display:flex;gap:8px;margin-top:28px;flex-wrap:wrap}
.cats a{padding:9px 16px;border-radius:999px;border:1px solid rgba(255,255,255,.25);font-size:14px;font-weight:600}
.cats a.on{background:#fff;color:var(--navy);border-color:#fff}
.toolbar{display:flex;gap:8px;flex-wrap:wrap;padding:20px 0;border-bottom:1px solid var(--line);position:sticky;top:72px;background:#fff;z-index:5}
.chip{padding:7px 14px;border-radius:999px;background:var(--bg);font-size:13px;font-weight:600;color:var(--sub)}
.chip.on{background:var(--navy);color:#fff}
.group{padding:56px 0 56px;scroll-margin-top:140px}.group.alt{background:var(--bg);box-shadow:0 0 0 100vmax var(--bg);clip-path:inset(0 -100vmax)}
.ghead{display:flex;align-items:center;gap:20px;padding-bottom:20px;margin-bottom:28px;border-bottom:2px solid var(--navy)}
.gnum{flex:none;width:60px;height:60px;border-radius:14px;background:var(--navy);color:#fff;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:800;position:relative}
.gnum:after{content:"";position:absolute;right:-5px;bottom:-5px;width:16px;height:16px;border-radius:5px;background:var(--mint)}
.gen{font-size:12px;font-weight:800;letter-spacing:1.5px;color:var(--blue);text-transform:uppercase}
.ghead h2{font-size:30px;letter-spacing:-.6px;color:var(--navy);line-height:1.25;display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.gcount{font-size:13px;font-weight:700;color:var(--navy);background:#d9f7f0;padding:4px 10px;border-radius:999px;letter-spacing:0}
.gdesc{color:var(--sub);font-size:15px;margin-top:4px}
.chip b{margin-left:5px;opacity:.6;font-weight:700}a.chip:hover{background:#e3eaf5}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:20px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;display:flex;flex-direction:column;transition:.2s}
.card:hover{transform:translateY(-3px);box-shadow:0 12px 28px rgba(27,43,75,.12);border-color:#c9d6ea}
.thumb{aspect-ratio:4/3;background:#fff;display:flex;align-items:center;justify-content:center;padding:18px;position:relative;border-bottom:1px solid var(--line)}
.thumb img{max-width:100%;max-height:100%;object-fit:contain}
.thumb.cover{padding:0}.thumb.cover img{width:100%;height:100%;object-fit:cover}
.thumbs div{cursor:pointer}
.badge{position:absolute;top:12px;left:12px;background:var(--mint);color:var(--navy);font-size:11px;font-weight:800;padding:3px 8px;border-radius:4px}
.badge.warn{background:#ffb020}
.cbody{padding:18px 18px 20px;display:flex;flex-direction:column;gap:6px;flex:1}
.brand{font-size:12px;font-weight:700;color:var(--blue);letter-spacing:.2px}
.card h3{font-size:19px;letter-spacing:-.3px}.card .st{font-size:13px;color:var(--sub);font-weight:600}
.card .sm{font-size:14px;color:#3a4356;margin-top:4px;flex:1}
.tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}.tags span{font-size:12px;color:var(--sub);background:var(--bg);padding:3px 8px;border-radius:4px}
.more{margin-top:12px;font-size:13px;font-weight:700;color:var(--blue)}
.custom{margin:48px 0;border-radius:16px;background:linear-gradient(110deg,#eef5ff,#e6fbf6);padding:32px 36px;display:flex;align-items:center;gap:24px;justify-content:space-between;flex-wrap:wrap}
.custom h3{font-size:20px;color:var(--navy)}.custom p{color:var(--sub);font-size:14px;margin-top:4px}
.ribbon{display:inline-block;font-size:11px;font-weight:700;color:#b26b00;background:#fff3dc;padding:2px 8px;border-radius:4px;margin-bottom:6px}
.cta{background:var(--navy);color:#fff;padding:48px 0;margin-top:64px}
.cta .wrap{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap}.cta h3{font-size:24px}.cta p{opacity:.75}
footer{background:#121d33;color:#9aa6bd;font-size:13px;padding:32px 0}footer b{color:#fff}
/* detail */
.dhero{padding:40px 0 48px;background:var(--bg)}
.dgrid{display:grid;grid-template-columns:1.05fr 1fr;gap:48px;align-items:start}
.mainimg{background:#fff;border:1px solid var(--line);border-radius:16px;aspect-ratio:1/1;display:flex;align-items:center;justify-content:center;padding:28px}
.mainimg img{max-width:100%;max-height:100%;object-fit:contain}
.thumbs{display:flex;gap:10px;margin-top:12px}.thumbs div{width:76px;height:76px;background:#fff;border:1px solid var(--line);border-radius:10px;padding:6px;display:flex;align-items:center;justify-content:center}
.thumbs div.on{border:2px solid var(--blue)}.thumbs img{max-width:100%;max-height:100%}
.dinfo .crumb{opacity:1;color:var(--sub)}.dinfo h1{font-size:38px;letter-spacing:-.8px;color:var(--navy);line-height:1.2}
.dinfo .st{font-size:18px;font-weight:600;color:var(--sub);margin-top:6px}.dinfo .sm{font-size:16px;margin:18px 0}
.former{display:inline-block;background:#fff;border:1px dashed var(--blue);color:var(--blue);font-size:13px;font-weight:700;padding:4px 10px;border-radius:6px;margin-top:10px}
.keyspec{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:20px 0 24px}
.keyspec div{background:#fff;border:1px solid var(--line);border-radius:10px;padding:12px 14px}.keyspec small{display:block;font-size:12px;color:var(--sub)}.keyspec b{font-size:14px}
.actions{display:flex;gap:10px;flex-wrap:wrap}
.tabs{display:flex;gap:28px;border-bottom:1px solid var(--line);position:sticky;top:72px;background:#fff;z-index:5}
.tabs a{padding:16px 0;font-weight:700;font-size:15px;color:var(--sub);border-bottom:2px solid transparent}.tabs a.on{color:var(--navy);border-color:var(--navy)}
.sec{padding:52px 0 8px}.sec h2{font-size:24px;letter-spacing:-.4px;margin-bottom:20px;color:var(--navy)}
.hl{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}
.hl div{border:1px solid var(--line);border-radius:14px;padding:22px}.hl i{display:inline-flex;width:34px;height:34px;border-radius:9px;background:#e9f2ff;color:var(--blue);font-style:normal;font-weight:800;align-items:center;justify-content:center;margin-bottom:12px}
.hl h4{font-size:16px;margin-bottom:6px}.hl p{font-size:14px;color:var(--sub)}
.body p{font-size:16px;color:#2f3747;margin-bottom:14px;max-width:820px}
.notice{background:#e9f2ff;border-left:4px solid var(--blue);padding:14px 18px;border-radius:8px;margin-bottom:18px;font-size:15px}
.models{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}.models div{background:var(--bg);border-radius:12px;padding:20px}.models b{color:var(--navy);font-size:16px}.models p{font-size:14px;color:var(--sub);margin-top:4px}
table{width:100%;border-collapse:collapse;font-size:15px;border-top:2px solid var(--navy)}
th,td{text-align:left;padding:14px 16px;border-bottom:1px solid var(--line);vertical-align:top}th{width:220px;background:var(--bg);font-weight:700;color:var(--navy)}
.small{font-size:12px;color:var(--sub);margin-top:10px}
.apps{display:flex;flex-wrap:wrap;gap:10px}.apps span{border:1px solid var(--line);border-radius:999px;padding:8px 16px;font-size:14px;font-weight:600}
.noimg{width:100%;height:100%;min-height:160px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;background:repeating-linear-gradient(45deg,#f5f7fa,#f5f7fa 10px,#eef2f7 10px,#eef2f7 20px);color:var(--sub);font-size:13px;font-weight:700;border-radius:8px}
.partner-box{display:flex;align-items:center;gap:18px;flex-wrap:wrap;margin:-4px 0 22px;padding:16px 18px;border:1px solid var(--line);border-radius:12px;background:#fff}
.partner-box .pl{display:flex;flex-direction:column;gap:2px;min-width:0}
.partner-box .pk{font-size:11.5px;font-weight:800;letter-spacing:.06em;color:#fff;background:#12365A;border-radius:4px;padding:2px 8px;align-self:flex-start}
.partner-box .pn{font-size:15px;font-weight:700;color:var(--navy)}
.partner-box .pd{font-size:13px;color:var(--sub)}
.partner-box img{height:34px;width:auto}
.partner-box .pa{margin-left:auto;font-size:14px;font-weight:700;color:var(--blue);white-space:nowrap}
.partner-box .pa:hover{text-decoration:underline}
.card .brand .pt{display:inline-block;margin-left:6px;font-size:10.5px;font-weight:800;color:#12365A;background:#e3ebf6;border-radius:3px;padding:0 5px}
.samples{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.samples button{all:unset;cursor:zoom-in;display:flex;flex-direction:column;gap:8px;min-width:0}
.samples button:focus-visible{outline:2px solid var(--blue);outline-offset:3px;border-radius:12px}
.samples .sp{position:relative;aspect-ratio:4/3;border-radius:12px;overflow:hidden;background:#0b0f16;border:1px solid var(--line)}
.samples img{width:100%;height:100%;object-fit:cover;transition:transform .5s cubic-bezier(.22,1,.36,1)}
.samples button:hover img{transform:scale(1.05)}
.samples .tg{position:absolute;left:8px;top:8px;font-size:11px;font-weight:700;color:#fff;background:rgba(18,54,90,.85);border-radius:4px;padding:2px 7px}
.samples .cp{font-size:13.5px;color:#2f3747;line-height:1.45}
.sfilter{display:flex;gap:8px;flex-wrap:wrap;margin:-6px 0 20px}
.sfilter button{all:unset;cursor:pointer;font-size:13px;font-weight:600;padding:6px 14px;border-radius:999px;background:var(--bg);color:var(--sub)}
.sfilter button.on{background:var(--navy);color:#fff}
.lb{position:fixed;inset:0;z-index:100;background:rgba(5,8,14,.94);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:max(20px,env(safe-area-inset-top,0px)) max(16px,env(safe-area-inset-right,0px)) max(20px,env(safe-area-inset-bottom,0px)) max(16px,env(safe-area-inset-left,0px))}
.lb img{max-width:min(1400px,100%);max-height:calc(100vh - 140px);object-fit:contain;border-radius:8px;background:#000}
.lb .lc{color:#e8edf4;font-size:15px;text-align:center}
.lb .ln{all:unset;position:absolute;top:50%;transform:translateY(-50%);cursor:pointer;color:#fff;font-size:28px;width:52px;height:52px;border-radius:50%;background:rgba(255,255,255,.12);display:flex;align-items:center;justify-content:center}
.lb .lx{all:unset;position:absolute;right:20px;top:20px;cursor:pointer;color:#fff;font-size:15px;font-weight:700;padding:10px 16px;border-radius:999px;background:rgba(255,255,255,.12)}
@media(max-width:860px){.samples{grid-template-columns:1fr 1fr}}
.lb[hidden],.samples button[hidden]{display:none!important}
.proc{display:flex;flex-direction:column;gap:28px}
.proc figure{margin:0;display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:28px;align-items:center;padding:22px;border:1px solid var(--line);border-radius:16px;background:#fff}
.proc figure:nth-child(even){grid-template-columns:minmax(0,1fr) minmax(0,1.35fr)}
.proc figure:nth-child(even) img{order:2}
.proc img{width:100%;border-radius:10px;border:1px solid var(--line);cursor:zoom-in;background:#fff}
.proc .st{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:12.5px;font-weight:600;letter-spacing:.12em;color:var(--blue)}
.proc h3{font-size:21px;color:var(--navy);margin:6px 0 10px;letter-spacing:-.02em}
.proc p{font-size:15.5px;color:#2f3747}
.cmp{overflow-x:auto}
.cmp table{min-width:620px;border-top:0}
.cmp th,.cmp td{border:1px solid var(--line)}
.cmp thead th{background:var(--bg);text-align:center;width:auto;padding:16px}
.cmp thead th a{display:block;color:var(--navy)}
.cmp thead th b{display:block;font-size:19px}
.cmp thead th small{display:block;font-weight:600;color:var(--sub);font-size:12.5px;margin-top:2px}
.cmp thead th.me{background:#12365A}
.cmp thead th.me b,.cmp thead th.me small{color:#fff}
.cmp thead th .here{display:inline-block;margin-top:6px;font-size:11px;font-weight:800;color:#12365A;background:#00C9A7;border-radius:4px;padding:1px 7px}
.cmp thead th .go{display:inline-block;margin-top:6px;font-size:12px;font-weight:700;color:var(--blue)}
.cmp tbody th{width:150px;background:#fff;color:var(--navy);font-size:14px}
.cmp td{font-size:14.5px;color:#2f3747}
.cmp td.me{background:#eef4fb;font-weight:600;color:var(--navy)}
@media(max-width:860px){.proc figure,.proc figure:nth-child(even){grid-template-columns:1fr}.proc figure:nth-child(even) img{order:0}}
.note-bar{background:#fff3dc;color:#7a4b00;font-size:13px;text-align:center;padding:8px}
@media(max-width:860px){nav{display:none}.dgrid{grid-template-columns:1fr}.hero h1,.dinfo h1{font-size:28px}th{width:120px}.custom{padding:24px}}
"""
FONT = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">'
CTA_BAND = '''<section class="cta"><div class="wrap"><div><h3>어떤 장비가 맞을지 고민되시나요?</h3><p>시료를 보내주시거나 방문하시면 직접 비교 시연해 드립니다.</p></div>
<div class="actions"><a class="btn btn-mint" href="#">데모 신청</a><a class="btn btn-ghost" href="#">02-2632-3211</a></div></div></section>'''
def page(title, inner, root, active="product", cta=True):
    return f"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>{FAVICON}{FONT}<style>{CSS}</style></head><body>
<div class="note-bar">디자인 시안 (검토용) — 실제 홈페이지가 아닙니다</div>
<header><div class="wrap"><a class="logo" href="{root}index.html" aria-label="세일테크노 홈">{MARK}<span>SEIL<span>TECHNO</span></span></a>
<nav><a class="{"on" if active=="about" else ""}" href="{root}회사소개.html">회사소개</a><a class="{"on" if active=="product" else ""}" href="{root}제품목록_현미경.html">제품소개</a><a class="{"on" if active=="cases" else ""}" href="{root}적용사례.html">적용사례</a><a class="{"on" if active=="support" else ""}" href="{root}고객지원.html">고객지원</a></nav>
<a class="btn btn-primary" href="#">견적·데모 문의</a></div></header>
{inner}
{CTA_BAND if cta else ""}
<footer><div class="wrap"><div class="fmark">{MARK}SEIL TECHNO</div><b>㈜세일테크노</b> · 서울특별시 영등포구 당산로2길 12, 에이스테크노타워 806호 · 대표전화 02-2632-3211<br>Since 1991 · Vision Engineering 국내 총판</div></footer></body></html>"""

def img(root, p): return root + "../site" + p
def pic(root, d, attrs=""):
    if not d.get("image"):
        return '<div class="noimg"><span>📷</span>사진 준비 중</div>'
    return f'<img {attrs} src="{img(root, d["image"])}" alt="{e(d["title"])}">'


def samples_section(d, root):
    sm = d.get("samples")
    if not sm: return ""
    tags = []
    for x in sm:
        if x.get("tag") and x["tag"] not in tags: tags.append(x["tag"])
    filt = '<div class="sfilter" role="group" aria-label="샘플 종류"><button class="on" data-f="*">전체 {}</button>'.format(len(sm)) + "".join(
        f'<button data-f="{e(t)}">{e(t)} {sum(1 for x in sm if x.get("tag")==t)}</button>' for t in tags) + "</div>"
    items = "".join(
        f'<button data-i="{i}" data-t="{e(x.get("tag",""))}" data-full="{img(root,x["full"])}" data-cap="{e(x["cap"])}"><span class="sp"><img src="{img(root,x["thumb"])}" alt="{e(x["cap"])}" loading="lazy"><span class="tg">{e(x.get("tag",""))}</span></span><span class="cp">{e(x["cap"])}</span></button>'
        for i, x in enumerate(sm))
    js = """<script>(function(){var g=document.getElementById('sg');if(!g)return;var bs=[].slice.call(g.querySelectorAll('.samples button')),vis=bs,cur=0,lb=null;
[].forEach.call(g.querySelectorAll('.sfilter button'),function(f){f.addEventListener('click',function(){[].forEach.call(g.querySelectorAll('.sfilter button'),function(x){x.classList.remove('on')});f.classList.add('on');var k=f.dataset.f;vis=bs.filter(function(b){var ok=k==='*'||b.dataset.t===k;b.hidden=!ok;return ok})})});
function show(i){cur=(i+vis.length)%vis.length;var b=vis[cur];lb.querySelector('img').src=b.dataset.full;lb.querySelector('img').alt=b.dataset.cap;lb.querySelector('.lc').textContent=(cur+1)+' / '+vis.length+'  ·  '+b.dataset.cap}
function open(b){if(!lb){lb=document.createElement('div');lb.className='lb';lb.setAttribute('role','dialog');lb.setAttribute('aria-label','샘플 크게 보기');
lb.innerHTML='<button class="lx" aria-label="닫기">닫기 ✕</button><button class="ln" style="left:16px" aria-label="이전">‹</button><img alt=""><div class="lc"></div><button class="ln" style="right:16px" aria-label="다음">›</button>';
lb.querySelector('.lx').onclick=close;lb.querySelectorAll('.ln')[0].onclick=function(){show(cur-1)};lb.querySelectorAll('.ln')[1].onclick=function(){show(cur+1)};
lb.addEventListener('click',function(ev){if(ev.target===lb)close()});document.body.appendChild(lb)}lb.hidden=false;document.body.style.overflow='hidden';show(vis.indexOf(b));lb.querySelector('.lx').focus()}
function close(){lb.hidden=true;document.body.style.overflow=''}
document.addEventListener('keydown',function(ev){if(!lb||lb.hidden)return;if(ev.key==='Escape')close();if(ev.key==='ArrowLeft')show(cur-1);if(ev.key==='ArrowRight')show(cur+1)});
bs.forEach(function(b){b.addEventListener('click',function(){open(b)})})})();</script>"""
    return (f'<section class="sec" id="g"><h2>{e(d.get("samples_title","촬영 샘플 갤러리"))}</h2><p style="color:var(--sub);margin:-8px 0 18px">{e(d.get("samples_desc","이 장비로 직접 촬영한 이미지입니다."))} 사진을 누르면 크게 볼 수 있습니다.</p>'
            f'<div id="sg">{filt}<div class="samples">{items}</div></div></section>{js}')

def process_section(d, root):
    pr = d.get("process")
    if not pr: return ""
    figs = "".join(
        f'<figure><img src="{img(root,x["img"])}" alt="{e(x["step"])} {e(x["title"])}" loading="lazy" onclick="window.open(this.src)">'
        f'<figcaption><span class="st">{e(x["step"])}</span><h3>{e(x["title"])}</h3><p>{e(x["text"])}</p></figcaption></figure>' for x in pr)
    return f'<section class="sec" id="p"><h2>작동 과정</h2><div class="proc">{figs}</div></section>'

def compare_section(d, root):
    c = d.get("compare")
    if not c: return ""
    head = '<th></th>'
    for col in c["cols"]:
        me = col["slug"] == d["slug"]
        tag = '<span class="here">지금 보는 제품</span>' if me else f'<span class="go">자세히 보기 →</span>'
        inner = f'<b>{e(col["name"])}</b><small>{e(col["sub"])}</small>{tag}'
        head += f'<th class="{"me" if me else ""}">' + (inner if me else f'<a href="{col["slug"]}.html">{inner}</a>') + '</th>'
    idx = [i for i, col in enumerate(c["cols"]) if col["slug"] == d["slug"]]
    rows = ""
    for r in c["rows"]:
        rows += f'<tr><th>{e(r[0])}</th>' + "".join(f'<td class="{"me" if (i in idx) else ""}">{e(v)}</td>' for i, v in enumerate(r[1:])) + '</tr>'
    return f'<section class="sec" id="c"><h2>{e(c["title"])}</h2><div class="cmp"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div></section>'

def partner_box(d, root):
    p = d.get("partner")
    if not p: return ""
    logo = ""
    if p.get("logo") and os.path.exists(os.path.join(SITE, p["logo"].lstrip("/"))):
        logo = f'<img src="{img(root, p["logo"])}" alt="{e(p["name"])} 로고">'
    return (f'<div class="partner-box">{logo}<div class="pl"><span class="pk">협력사</span><span class="pn">{e(p["name"])}</span>'
            f'<span class="pd">{e(p.get("desc",""))}</span></div><a class="pa" href="{e(p["url"])}" target="_blank" rel="noopener">홈페이지 바로가기 ↗</a></div>')

def card(d, root):
    badge = ""
    if d.get("published") is False: badge = '<span class="badge warn">확인 필요</span>'
    elif d.get("badge"): badge = f'<span class="badge">{e(d["badge"])}</span>'
    tags = "".join(f"<span>{e(t)}</span>" for t in d.get("tags", [])[:3])
    return f"""<a class="card" href="{root}상세/{d['slug']}.html"><div class="thumb{' cover' if d.get('image_fit')=='cover' else ''}">{badge}{pic(root,d)}</div>
<div class="cbody"><div class="brand">{e(d['brand'] or '')}{'<span class="pt">협력사</span>' if d.get('partner') else ''}&nbsp;</div><h3>{e(d['title'])}</h3><div class="st">{e(d['subtitle'])}</div><div class="sm">{e(d['summary'])}</div>
<div class="tags">{tags}</div><div class="more">자세히 보기 →</div></div></a>"""

def build_list(all_items, cat):
    root = ""; cfg = CATCFG[cat]
    if cfg.get("board"): return build_board(all_items, cat)
    items = [d for d in all_items if d["category"] == cat]
    subs = [x[0] for x in cfg["subs"]]
    cats = "".join(f'<a class="{"on" if c==cat else ""}" href="{cat_link(c, root)}">{c}</a>' for c in CATS)
    brands = sorted({d["brand"] for d in items if d.get("brand")})
    chips = '<span class="chip on">전체 <b>%d</b></span>' % len(items) + "".join(f'<a class="chip" href="#{SUB_INFO[s]["id"]}">{s} <b>{sum(1 for d in items if d["subcategory"]==s)}</b></a>' for s in subs) + "".join(f'<span class="chip">#{b}</span>' for b in brands)
    groups = ""
    for s in subs:
        g = [d for d in items if d["subcategory"] == s]
        if not g and not cfg.get("show_empty"): continue
        si = SUB_INFO[s]; n = si["n"]
        groups += f'<section class="group{" alt" if n % 2 == 0 else ""}" id="{si["id"]}"><div class="ghead"><div class="gnum">{n:02d}</div><div><div class="gen">{si["en"]}</div><h2>{s}<span class="gcount">{len(g)}개 제품</span></h2><div class="gdesc">{si["desc"]}</div></div></div><div class="grid">' + ("".join(card(d, root) for d in g) if g else f'<div class="card" style="border-style:dashed;background:var(--bg);justify-content:center;align-items:flex-start;padding:28px;gap:10px;min-height:220px"><span class="badge" style="position:static">준비 중</span><h3 style="font-size:18px;color:var(--navy)">{e(s)} 제품을 준비하고 있습니다</h3><p style="font-size:14px;color:var(--sub)">곧 소개해 드리겠습니다. 먼저 상담이 필요하시면 문의해 주세요.</p><a class="more" href="고객지원.html?type=consult#inquiry">상담 문의 →</a></div>') + "</div></section>"
        if s == cfg.get("banner_after"):
            groups += """<div class="custom"><div><span class="ribbon">시안 A — 맞춤형 안내 배너</span><h3>현장에 맞춘 맞춤형(Customized) 구성</h3>
<p>스테이지·렌즈·조명·소프트웨어를 조합해 검사 대상과 공정에 꼭 맞는 시스템을 제안해 드립니다.</p></div><a class="btn btn-primary" href="#">맞춤 구성 상담</a></div>"""
    inner = cat_hero(cat, all_items, root, cfg["desc"]) + f"""
<div class="wrap"><div class="toolbar">{chips}</div>{groups}</div>"""
    open(os.path.join(HERE, cfg["file"]), "w", encoding="utf-8").write(page(f"{cat} | 세일테크노", inner, root))

def build_detail(d, items):
    if d.get("layout") == "custom":
        return build_custom(d, items)
    root = "../"
    gal = ([d["image"]] if d.get("image") else []) + d.get("gallery", [])
    thumbs = "" if len(gal) < 2 else '<div class="thumbs">' + "".join(f'<div class="{"on" if i==0 else ""}" onclick="document.getElementById(\'main\').src=this.firstChild.src;[...this.parentNode.children].forEach(x=>x.className=\'\');this.className=\'on\'"><img src="{img(root,g)}"></div>' for i, g in enumerate(gal)) + "</div>"
    if d.get("gallery_note"): thumbs += f'<p class="small">{e(d["gallery_note"])}</p>'
    ks = "".join(f"<div><small>{e(k)}</small><b>{e(v)}</b></div>" for k, v in d["specs"][:4])
    former = f'<div class="former">구 {e(d["formerly"])}</div>' if d.get("formerly") else ""
    hl = "".join(f'<div><i>{i+1:02d}</i><h4>{e(h["title"])}</h4><p>{e(h["text"])}</p></div>' for i, h in enumerate(d["highlights"]))
    models = ""
    if d.get("models"):
        models = '<section class="sec"><h2>모델 구성</h2><div class="models">' + "".join(f'<div><b>{e(m["name"])}</b><p>{e(m["text"])}</p></div>' for m in d["models"]) + "</div></section>"
    rows = "".join(f"<tr><th>{e(k)}</th><td>{e(v)}</td></tr>" for k, v in d["specs"])
    samples_h = samples_section(d, root)
    process_h = process_section(d, root)
    extra_h = (f"<style>{BOARD_CSS}</style>" if (d.get("viewer3d") or d.get("videos")) else "") + stats_section(d, root) + viewer3d_section(d, root) + videos_section(d, root)
    compare_h = compare_section(d, root)
    apps = "".join(f"<span>{e(a)}</span>" for a in d.get("applications", []))
    rel = [x for x in items if x["subcategory"] == d["subcategory"] and x["slug"] != d["slug"]][:3]
    relh = ""
    if rel: relh = '<section class="sec"><h2>함께 보면 좋은 제품</h2><div class="grid">' + "".join(card(x, root) for x in rel) + "</div></section>"
    inner = f"""<section class="dhero"><div class="wrap dgrid"><div><div class="mainimg">{pic(root, d, 'id="main"')}</div>{thumbs}</div>
<div class="dinfo"><div class="crumb">홈 › 제품소개 › {e(d['category'])} › {e(d['subcategory'])}</div><div style="display:flex;gap:8px;align-items:center;margin:12px 0 8px;flex-wrap:wrap"><a href="{cat_link(d['category'], root)}#{SUB_INFO[d['subcategory']]['id']}" style="background:var(--navy);color:#fff;font-size:13px;font-weight:700;padding:5px 12px;border-radius:6px">{e(d['subcategory'])}</a>{f'<span style="color:var(--blue);font-weight:700;font-size:13px">#{e(d["brand"])}</span>' if d.get("brand") else ""}</div>
<h1>{e(d['title'])}</h1><div class="st">{e(d['subtitle'])}</div>{former}<p class="sm">{e(d['summary'])}</p>
<div class="keyspec">{ks}</div>{partner_box(d, root)}<div class="actions"><a class="btn btn-primary" href="#">견적 문의</a><a class="btn btn-ghost" href="#">데모 신청</a><a class="btn btn-ghost" href="#">브로셔 PDF</a></div></div></div></section>
<div class="wrap"><div class="tabs"><a class="on" href="#f">주요 특징</a>{'<a href="#p">작동 과정</a>' if d.get('process') else ''}{'<a href="#v3s">3D 모델</a>' if d.get('viewer3d') else ''}{'<a href="#st">실측 검증</a>' if d.get('stats') else ''}{f'<a href="#vid">{e(d.get("videos_tab","스캔 영상"))}</a>' if d.get('videos') else ''}{f'<a href="#g">{e(d.get("samples_tab","샘플 갤러리"))}</a>' if d.get('samples') else ''}{'<a href="#c">제품 비교</a>' if d.get('compare') else ''}<a href="#s">사양</a><a href="#a">적용 분야</a></div>
<section class="sec" id="f"><h2>주요 특징</h2><div class="hl">{hl}</div></section>
{process_h}{extra_h}{samples_h}<section class="sec body"><h2>제품 소개</h2>{md(d['body'])}</section>{compare_h}{models}
<section class="sec" id="s"><h2>주요 사양</h2><table>{rows}</table><p class="small">※ 사양은 제조사 사정에 따라 예고 없이 변경될 수 있습니다. 상세 사양은 브로셔를 참고하거나 문의해 주세요.</p></section>
<section class="sec" id="a"><h2>적용 분야</h2><div class="apps">{apps}</div></section>{relh}</div>"""
    os.makedirs(os.path.join(HERE, "상세"), exist_ok=True)
    open(os.path.join(HERE, "상세", d["slug"] + ".html"), "w", encoding="utf-8").write(page(f"{d['title']} | 세일테크노", inner, root))


# ───── 회사소개 페이지 ─────
ABOUT_CSS = """
/* 레이아웃: 레티클(측정 눈금) 모티프 — 1991을 '초점'에 두고, 연혁은 1991~2026 눈금자 위에 놓는다 */
:root{--ink2:#3a4356;--reticle:#00C9A7;--rule:#c9d3e3;--display:"Big Shoulders Display","Pretendard",sans-serif;--mono:"IBM Plex Mono",ui-monospace,monospace}
.ab-hero{background:radial-gradient(120% 140% at 85% 20%,#24385f 0%,var(--navy) 55%,#121d33 100%);color:#fff;overflow:hidden}
.ab-hero .wrap{display:grid;grid-template-columns:1.05fr 1fr;gap:32px;align-items:center;padding-block:64px 56px}
.ab-hero .crumb{opacity:.65}
.ab-eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:2.5px;color:var(--reticle);text-transform:uppercase;margin:6px 0 14px}
.ab-hero h1{font-size:40px;line-height:1.3;letter-spacing:-.8px;text-wrap:balance}
.ab-hero h1 em{font-style:normal;color:var(--reticle)}
.ab-hero p.lead{margin-top:18px;font-size:17px;opacity:.82;max-width:34em}
.ab-facts{display:flex;flex-wrap:wrap;gap:28px;margin-top:32px;padding-top:24px;border-top:1px solid rgba(255,255,255,.15)}
.ab-facts div{display:flex;flex-direction:column;gap:2px}
.ab-facts b{font-family:var(--display);font-size:34px;font-weight:700;letter-spacing:.5px;line-height:1;font-variant-numeric:tabular-nums}
.ab-facts span{font-size:13px;opacity:.7}
/* 1991 + 레티클 */
.scope{position:relative;aspect-ratio:1/1;max-width:440px;width:100%;justify-self:center;display:flex;align-items:center;justify-content:center}
.scope svg{position:absolute;inset:0;width:100%;height:100%}
.scope .yr{position:relative;font-family:var(--display);font-weight:800;font-size:clamp(88px,15vw,168px);line-height:1;letter-spacing:2px;color:#fff;text-shadow:0 0 40px rgba(0,201,167,.25)}
.scope .since{position:absolute;top:27%;left:50%;transform:translateX(-50%);font-family:var(--mono);font-size:12px;letter-spacing:4px;color:var(--reticle)}
.scope .coord{position:absolute;bottom:24%;left:50%;transform:translateX(-50%);font-family:var(--mono);font-size:11px;letter-spacing:1px;opacity:.6;white-space:nowrap}
@media (prefers-reduced-motion:no-preference){
 .scope .yr{animation:focus 1.6s cubic-bezier(.2,.7,.2,1) both}
 .scope svg .ring{transform-origin:50% 50%;animation:turn 1.6s cubic-bezier(.2,.7,.2,1) both}
 @keyframes focus{from{filter:blur(10px);opacity:.35;letter-spacing:14px}to{filter:blur(0);opacity:1;letter-spacing:2px}}
 @keyframes turn{from{transform:rotate(-24deg)}to{transform:rotate(0)}}
}
/* 본문 공통 */
.ab-sec{padding-block:72px}
.ab-sec.alt{background:var(--bg)}
.ab-kicker{font-family:var(--mono);font-size:12px;letter-spacing:2px;color:var(--blue);text-transform:uppercase}
.ab-sec h2{font-size:30px;letter-spacing:-.6px;color:var(--navy);margin:6px 0 28px;text-wrap:balance}
/* 인사말 */
.greet{display:grid;grid-template-columns:1fr 1.4fr;gap:56px;align-items:start}
.greet blockquote{font-size:26px;line-height:1.5;font-weight:700;color:var(--navy);letter-spacing:-.5px;text-wrap:balance;padding-left:20px;border-left:3px solid var(--reticle)}
.greet blockquote small{display:block;margin-top:14px;font-family:var(--mono);font-size:13px;font-weight:500;color:var(--sub);letter-spacing:1px}
.greet .txt{display:flex;flex-direction:column;gap:16px;font-size:16.5px;color:var(--ink2);max-width:40em;min-width:0}
.greet .txt strong{color:var(--navy)}
/* 연혁: 눈금자 */
.ruler-wrap{overflow-x:auto;padding:0 14px 6px}
.ruler{position:relative;min-width:760px;height:96px;margin-top:8px}
.ruler .base{position:absolute;left:0;right:0;top:40px;height:2px;background:var(--navy)}
.ruler .tick{position:absolute;top:28px;width:1px;height:12px;background:var(--rule)}
.ruler .tick.major{top:20px;height:20px;background:var(--navy)}
.ruler .lab{position:absolute;top:50px;transform:translateX(-50%);font-family:var(--mono);font-size:12px;color:var(--sub);font-variant-numeric:tabular-nums}
.ruler .pin{position:absolute;top:6px;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center}
.ruler .pin i{width:14px;height:14px;border-radius:50%;background:var(--reticle);box-shadow:0 0 0 4px rgba(0,201,167,.2)}
.ruler .pin.now i{background:var(--blue);box-shadow:0 0 0 4px rgba(42,123,228,.2)}
.ruler .span{position:absolute;top:39px;height:4px;background:linear-gradient(90deg,var(--reticle),var(--blue));border-radius:2px}
.ruler .cap{position:absolute;top:72px;transform:translateX(-50%);font-size:12px;font-weight:700;color:var(--navy);white-space:nowrap}
.miles{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:16px;margin-top:28px}
.mile{display:flex;flex-direction:column;gap:6px;padding:22px;background:var(--card);border:1px solid var(--line);border-radius:12px}
.mile .y{font-family:var(--display);font-size:32px;font-weight:700;color:var(--navy);line-height:1;font-variant-numeric:tabular-nums}
.mile h4{font-size:16px;color:var(--ink)}
.mile p{font-size:14px;color:var(--sub)}
.mile.todo{background:transparent;border-style:dashed}
.mile.todo .y{color:var(--rule)}
/* 사업 분야 */
.biz{display:grid;grid-template-columns:repeat(5,1fr);border-top:2px solid var(--navy)}
.biz a,.biz div{display:flex;flex-direction:column;gap:8px;padding:24px 18px 26px;border-right:1px solid var(--line);border-bottom:1px solid var(--line);min-width:0}
.biz > :last-child{border-right:0}
.biz .no{font-family:var(--mono);font-size:12px;color:var(--blue)}
.biz h4{font-size:18px;color:var(--navy);letter-spacing:-.3px}
.biz p{font-size:13.5px;color:var(--sub)}
.biz .go{margin-top:auto;font-size:13px;font-weight:700;color:var(--blue)}
.biz .soon{margin-top:auto;font-size:12px;color:var(--sub)}
.biz a:hover{background:var(--bg)}
/* 파트너 */
.partners{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.partner{display:grid;grid-template-columns:auto 1fr;gap:6px 18px;align-items:baseline;padding:28px;border:1px solid var(--line);border-radius:14px;background:var(--card)}
.partner .since2{grid-row:span 3;font-family:var(--display);font-size:44px;font-weight:700;color:var(--navy);line-height:1}
.partner .since2 small{display:block;font-family:var(--mono);font-size:11px;font-weight:500;color:var(--sub);letter-spacing:1px;margin-bottom:4px}
.partner h4{font-size:19px;color:var(--navy)}
.partner .tag{font-size:13px;font-weight:700;color:var(--blue)}
.partner p{font-size:14.5px;color:var(--ink2);min-width:0}
/* 오시는 길 */
.visit{display:grid;grid-template-columns:1.2fr 1fr;gap:32px;align-items:stretch}
.mapcard{position:relative;border-radius:14px;overflow:hidden;min-height:280px;background:
 linear-gradient(var(--rule) 1px,transparent 1px) 0 0/28px 28px,
 linear-gradient(90deg,var(--rule) 1px,transparent 1px) 0 0/28px 28px,#f3f6fa;border:1px solid var(--line)}
.mapcard .road{position:absolute;background:#fff;box-shadow:0 0 0 1px var(--rule)}
.mapcard .mk{position:absolute;left:58%;top:44%;transform:translate(-50%,-100%);display:flex;flex-direction:column;align-items:center;gap:4px}
.mapcard .mk b{background:var(--navy);color:#fff;font-size:13px;padding:6px 10px;border-radius:6px;white-space:nowrap}
.mapcard .mk i{width:16px;height:16px;border-radius:50%;background:var(--reticle);box-shadow:0 0 0 6px rgba(0,201,167,.25)}
.mapcard .st{position:absolute;left:22%;top:70%;font-size:12px;font-weight:700;color:#fff;background:#3cb44a;padding:4px 8px;border-radius:999px}
.mapcard .note{position:absolute;right:12px;bottom:10px;font-size:11px;color:var(--sub);background:rgba(255,255,255,.85);padding:2px 6px;border-radius:4px}
.info{display:flex;flex-direction:column;gap:0;border-top:2px solid var(--navy)}
.info div{display:grid;grid-template-columns:96px 1fr;gap:12px;padding:14px 4px;border-bottom:1px solid var(--line);font-size:15px}
.info dt{font-weight:700;color:var(--navy)}
.info dd{color:var(--ink2);min-width:0;word-break:break-all}
.maplinks{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px}
.chk{display:inline-block;font-size:11px;font-weight:700;color:#b26b00;background:#fff3dc;padding:1px 6px;border-radius:4px;margin-left:6px;vertical-align:middle}
@media(max-width:860px){
 .ab-hero .wrap,.greet,.visit,.partners{grid-template-columns:1fr}
 .scope{max-width:300px;order:-1}
 .ab-hero h1{font-size:28px}
 .biz{grid-template-columns:1fr 1fr}
 .biz > *{border-right:1px solid var(--line)}
 .partner{grid-template-columns:1fr}.partner .since2{grid-row:auto}
}
"""
ABOUT_FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800&family=IBM+Plex+Mono:wght@400;500&display=swap">'

def reticle_svg():
    ticks = []
    for i in range(72):
        a = i * 5
        L = 14 if i % 6 == 0 else 7
        ticks.append(f'<line x1="200" y1="22" x2="200" y2="{22+L}" transform="rotate({a} 200 200)"/>')
    return f'''<svg viewBox="0 0 400 400" aria-hidden="true" fill="none">
<g class="ring" stroke="#00C9A7" stroke-opacity=".75" stroke-width="1.2">{''.join(ticks)}</g>
<circle cx="200" cy="200" r="178" stroke="#00C9A7" stroke-opacity=".55" stroke-width="1.5"/>
<circle cx="200" cy="200" r="132" stroke="#ffffff" stroke-opacity=".12" stroke-width="1"/>
<line x1="12" y1="200" x2="92" y2="200" stroke="#00C9A7" stroke-width="1.5"/><line x1="308" y1="200" x2="388" y2="200" stroke="#00C9A7" stroke-width="1.5"/>
<line x1="200" y1="12" x2="200" y2="70" stroke="#00C9A7" stroke-width="1.5"/><line x1="200" y1="330" x2="200" y2="388" stroke="#00C9A7" stroke-width="1.5"/>
</svg>'''

def ruler_html(y0=1991, y1=2026):
    span = y1 - y0
    pos = lambda y: (y - y0) / span * 100
    parts = []
    for y in range(y0, y1 + 1):
        major = (y % 5 == 0) or y in (y0, y1)
        parts.append(f'<span class="tick{" major" if major else ""}" style="left:{pos(y):.3f}%"></span>')
        if y % 5 == 0 and y not in (y0, y1):
            parts.append(f'<span class="lab" style="left:{pos(y):.3f}%">{y}</span>')
    parts.append(f'<span class="span" style="left:{pos(2025):.3f}%;width:{pos(2026)-pos(2025):.3f}%"></span>')
    for y, cap, now in [(1991, "1991 설립", False), (2025, "2025 HIKVISION", False), (2026, "2026 현재", True)]:
        parts.append(f'<span class="pin{" now" if now else ""}" style="left:{pos(y):.3f}%"><i></i></span>')
    # 라벨 겹침 방지: 2025/2026은 위치 보정
    parts.append(f'<span class="cap" style="left:{pos(1991):.3f}%;transform:none">1991 설립</span>')
    parts.append(f'<span class="cap" style="left:auto;right:0;transform:none;text-align:right">2025 HIKVISION · 2026 현재</span>')
    return '<div class="ruler-wrap"><div class="ruler" role="img" aria-label="1991년부터 2026년까지 연혁 눈금자"><span class="base"></span>' + "".join(parts) + "</div></div>"

def build_about():
    root = ""
    years = 2026 - 1991
    biz = ""
    for i, (c, ds) in enumerate([
        ("현미경", "접안렌즈 없는 실체 현미경, 4K·3D 디지털 현미경"),
        ("측정 시스템", "측정 현미경, 고배율 측정기, 비디오 측정기(VMM)"),
        ("AI 검사·측정", "하이브리드 검사·측정, 기상 AI분석, 기상 검사/측정 비전"),
        ("머신비전", "산업용 카메라, 렌즈·조명, 코드리더, 비전 SW"),
        ("3D·특수 센싱", "3D 프로파일러, 이벤트 카메라")]):
        inner = f'<span class="no">{i+1:02d}</span><h4>{c}</h4><p>{ds}</p>'
        if c in CATCFG:
            biz += f'<a href="{cat_link(c, root)}">{inner}<span class="go">제품 보기 →</span></a>'
        else:
            biz += f'<div>{inner}<span class="soon">준비 중</span></div>'
    inner = f"""{ABOUT_FONTS}<style>{ABOUT_CSS}</style>
<section class="ab-hero"><div class="wrap">
 <div><div class="crumb">홈 › 회사소개</div>
  <div class="ab-eyebrow">SEIL TECHNO · Since 1991</div>
  <h1>1991년부터, <em>정확하게 보는 일</em>을<br>산업 현장에 공급해 왔습니다.</h1>
  <p class="lead">㈜세일테크노는 정밀 광학과 현미경, 측정·검사 장비를 공급하는 기술 기업입니다. {years}년 동안 쌓은 현장 경험으로 고객의 품질 관리와 생산성을 함께 고민합니다.</p>
  <div class="ab-facts"><div><b>1991</b><span>설립</span></div><div><b>{years}년</b><span>광학 솔루션 경험</span></div><div><b>5</b><span>제품 분야</span></div></div>
 </div>
 <div class="scope">{reticle_svg()}<span class="since">SINCE</span><span class="yr">1991</span><span class="coord">X 1991.00 · Y 2026.00</span></div>
</div></section>

<section class="ab-sec"><div class="wrap greet">
 <div><div class="ab-kicker">Greeting</div><h2>인사말</h2>
  <blockquote>"보는 것이 믿는 것이다."<small>SEEING IS BELIEVING</small></blockquote></div>
 <div class="txt">
  <p>㈜세일테크노는 <strong>1991년</strong> 설립 이후 한결같이 '잘 보이는 것'에 집중해 왔습니다. 영국 <strong>Vision Engineering</strong>의 접안렌즈 없는 현미경을 중심으로 전자·전기·기계 부품 생산 현장의 개발, 품질 관리, 생산성 향상을 도왔습니다.</p>
  <p>수입·판매에 그치지 않고 연구기관, 기업과 함께 제품과 시스템을 개발해 왔으며, 딥러닝 기업과 협력해 자동 검사 시스템도 공급하고 있습니다.</p>
  <p>2025년에는 글로벌 기술 기업 <strong>HIKVISION</strong>과 파트너십을 맺어 검사·측정·분석 분야로 공급 범위를 넓혔습니다. 앞으로도 과학적이고 인체공학적인 장비로 고객의 합리적인 생산과 품질 관리를 돕는 'Well-being' 기업이 되겠습니다.</p>
 </div>
</div></section>

<section class="ab-sec alt"><div class="wrap">
 <div class="ab-kicker">History · 1991 — 2026</div><h2>{years}년의 눈금</h2>
 {ruler_html()}
 <div class="miles">
  <div class="mile"><span class="y">1991</span><h4>㈜세일테크노 설립</h4><p>영국 Vision Engineering과 함께 국내에 접안렌즈 없는 현미경 공급 시작</p></div>
  <div class="mile"><span class="y">2025</span><h4>HIKVISION 파트너십</h4><p>고배율 3D 디지털 현미경 등 검사·측정·분석 제품군 확대</p></div>
  <div class="mile"><span class="y">2026</span><h4>홈페이지 새 단장</h4><p>제품 분야별로 찾기 쉬운 새 홈페이지 공개</p></div>
  <div class="mile todo"><span class="y">19XX–20XX</span><h4>주요 연혁 추가 예정<span class="chk">확인 필요</span></h4><p>사옥 이전, 주요 납품·인증, 신규 파트너 등 연혁 자료를 받으면 눈금 위에 표시합니다.</p></div>
 </div>
</div></section>

<section class="ab-sec"><div class="wrap">
 <div class="ab-kicker">Business</div><h2>사업 분야</h2>
 <div class="biz">{biz}</div>
</div></section>

<section class="ab-sec alt"><div class="wrap">
 <div class="ab-kicker">Partners</div><h2>함께하는 파트너</h2>
 <div class="partners">
  <div class="partner"><div class="since2"><small>WITH US SINCE</small>1991</div><h4>Vision Engineering</h4><span class="tag">영국 · 1958년 설립</span>
   <p>접안렌즈 없는 인체공학 현미경과 광학·비디오 측정 시스템을 만드는 영국 제조사입니다. Mantis, Lynx EVO, Hawk 등을 공급합니다.</p></div>
  <div class="partner"><div class="since2"><small>WITH US SINCE</small>2025</div><h4>HIKVISION</h4><span class="tag">글로벌 스마트 IoT 기술 기업</span>
   <p>고배율 3D 디지털 현미경 Deep Vision 등 검사·측정·분석 제품을 함께 공급합니다.</p></div>
 </div>
</div></section>

<section class="ab-sec"><div class="wrap">
 <div class="ab-kicker">Location</div><h2>오시는 길</h2>
 <div class="visit">
  <div class="mapcard" aria-label="약도">
   <span class="road" style="left:0;right:0;top:62%;height:16px"></span>
   <span class="road" style="left:40%;top:0;bottom:0;width:14px"></span>
   <span class="road" style="left:0;right:0;top:30%;height:10px"></span>
   <span class="st">2호선 문래역</span>
   <span class="mk"><b>에이스테크노타워 806호</b><i></i></span>
   <span class="note">약도 (실제 지도는 홈페이지 공개 시 연결)</span>
  </div>
  <div>
   <dl class="info">
    <div><dt>주소</dt><dd>서울특별시 영등포구 당산로2길 12, 에이스테크노타워 806호</dd></div>
    <div><dt>지하철</dt><dd>2호선 문래역 7번 출구</dd></div>
    <div><dt>대표전화</dt><dd>02-2632-3211</dd></div>
    <div><dt>이메일</dt><dd>sales@stvision.co.kr<br>seil@stvision.co.kr</dd></div>
   </dl>
   <div class="maplinks">
    <a class="btn btn-ghost" href="https://map.naver.com/p/search/%EC%97%90%EC%9D%B4%EC%8A%A4%ED%85%8C%ED%81%AC%EB%85%B8%ED%83%80%EC%9B%8C%20%EB%8B%B9%EC%82%B0%EB%A1%9C2%EA%B8%B8%2012" target="_blank" rel="noopener">네이버 지도</a>
    <a class="btn btn-ghost" href="https://map.kakao.com/?q=%EB%8B%B9%EC%82%B0%EB%A1%9C2%EA%B8%B8%2012" target="_blank" rel="noopener">카카오맵</a>
   </div>
  </div>
 </div>
</div></section>"""
    open(os.path.join(HERE, "회사소개.html"), "w", encoding="utf-8").write(page("회사소개 | 세일테크노", inner, root, active="about"))


# ───── 메인페이지 (index.html) ─────
MAIN_TPL = r"""<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>세일테크노 — 정밀 광학·측정·검사 장비</title>%%FAV%%
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
html,body{background:#020306;color:#EEF2F7}
/* layout: 히어로 = 왼쪽 글 열 + 오른쪽 300X 다이 사진, 그 위를 레티클 렌즈가 지나가며 확대 */
:root{--bg:#020306;--fg:238 242 247;--accent:#00C9A7;--paper:#F5F7FA;--ink:#0E1A2E;--navy:#1B2B4B;--blue:#2A7BE4;--line-l:#DDE3EC;--sub-l:#5B6577;
--sans:"Pretendard","Pretendard Variable","Malgun Gothic","Apple SD Gothic Neo",system-ui,sans-serif;--num:"Big Shoulders Display","Pretendard",sans-serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;
--ease:cubic-bezier(.22,1,.36,1);--gut:clamp(20px,4.5vw,64px)}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--sans);-webkit-font-smoothing:antialiased;line-height:1.6;word-break:keep-all;overflow-x:clip}
::selection{background:rgba(0,201,167,.3)}
a{color:inherit;text-decoration:none}
a:focus-visible,button:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:999px}
.wrap{max-width:1320px;margin:0 auto;padding-left:max(var(--gut),env(safe-area-inset-left,0px));padding-right:max(var(--gut),env(safe-area-inset-right,0px))}
.mono{font-family:var(--mono)}
.note-bar{position:relative;z-index:30;background:#fff3dc;color:#7a4b00;font-size:12.5px;text-align:center;padding:6px}
/* material */
.glass{background:rgba(255,255,255,.06);backdrop-filter:blur(14px) saturate(140%);-webkit-backdrop-filter:blur(14px) saturate(140%);box-shadow:inset 0 0 0 1px rgba(255,255,255,.12)}
/* nav */
.nav{position:absolute;top:34px;left:0;right:0;z-index:20}
.nav .wrap{display:flex;align-items:center;gap:28px;height:76px}
.mark{display:flex;align-items:center;gap:10px;font-weight:700;font-size:19px;letter-spacing:-.02em}.mark .seil-mark{width:34px;height:34px;color:#fff;flex:none}
.fmark{display:flex;align-items:center;gap:10px;margin-bottom:10px;color:#fff;font-weight:700}.fmark .seil-mark{width:26px;height:26px}
.mark small{font-family:var(--mono);font-size:10.5px;font-weight:400;letter-spacing:.2em;color:rgb(var(--fg)/.5)}
.links{display:flex;gap:6px;margin-left:auto;border-radius:999px;padding:5px}
.links a{font-size:14px;font-weight:500;color:rgb(var(--fg)/.82);padding:8px 16px;border-radius:999px;transition:background .25s,color .25s}
.links a:hover{background:rgba(255,255,255,.1);color:rgb(var(--fg))}
.btn{display:inline-flex;align-items:center;gap:10px;border-radius:999px;font-weight:600;font-size:14.5px;white-space:nowrap;transition:transform .2s var(--ease),background .25s}
.btn:active{transform:scale(.97)}
.btn-white{background:#fff;color:#0B1220;padding:8px 8px 8px 22px}
.btn-white i{display:inline-flex;width:34px;height:34px;border-radius:50%;background:var(--accent);align-items:center;justify-content:center;transition:transform .3s var(--ease)}
.btn-white:hover i{transform:rotate(-45deg)}
.btn-glass{padding:13px 22px;color:rgb(var(--fg))}
.btn-glass:hover{background:rgba(255,255,255,.12)}
.nav .btn-white{padding:6px 6px 6px 18px;font-size:13.5px}.nav .btn-white i{width:28px;height:28px}
.burger{display:none}
/* hero */
.hero{position:relative;min-height:max(660px,min(100dvh,940px));display:flex;align-items:center;overflow:hidden;isolation:isolate}
.stage{position:absolute;inset:0 0 0 30%;z-index:0}
.stage .base{position:absolute;inset:0;background:var(--bg) url(%%IMG%%main/hero-pcb-3d-sm.jpg) 58% 50%/cover no-repeat;filter:brightness(.42) saturate(.7) blur(1.2px);
 -webkit-mask-image:linear-gradient(90deg,transparent 0%,#000 32%,#000 88%,transparent 100%);mask-image:linear-gradient(90deg,transparent 0%,#000 32%,#000 88%,transparent 100%);
 opacity:0;transform:scale(1.06);transition:opacity 1.2s var(--ease),transform 1.8s var(--ease)}
.ready .stage .base{opacity:1;transform:scale(1)}
.hero::after{content:"";position:absolute;inset:auto 0 0;height:180px;background:linear-gradient(transparent,var(--bg));z-index:1;pointer-events:none}
.lens{position:absolute;left:0;top:0;width:var(--d);height:var(--d);--d:clamp(150px,17vw,240px);border-radius:50%;z-index:2;pointer-events:none;
 background:#000 url(%%IMG%%main/hero-pcb-3d.jpg) no-repeat;box-shadow:0 0 0 2px var(--accent),0 0 0 9px rgba(0,201,167,.12),0 24px 60px rgba(0,0,0,.6);will-change:transform;opacity:0;transition:opacity .8s}
.ready .lens{opacity:1}
.lens svg{position:absolute;inset:-14px;width:calc(100% + 28px);height:calc(100% + 28px)}
.readout{position:absolute;z-index:3;font-family:var(--mono);font-size:11px;letter-spacing:.06em;color:rgb(var(--fg)/.8);white-space:nowrap;pointer-events:none;opacity:0;transition:opacity .8s;font-variant-numeric:tabular-nums}
.ready .readout{opacity:1}
.readout b{color:var(--accent);font-weight:500}
.cap{position:absolute;right:max(var(--gut),env(safe-area-inset-right,0px));bottom:72px;z-index:3;font-size:12px;color:rgb(var(--fg)/.45)}
.copy{position:relative;z-index:5;max-width:620px;padding-block:150px 110px}
.eyebrow{font-family:var(--mono);font-size:12px;letter-spacing:.22em;color:var(--accent);text-transform:uppercase}
.hero h1{margin-top:22px;font-size:clamp(44px,6.4vw,92px);font-weight:500;line-height:1.06;letter-spacing:-.035em}
.hero h1 .ln{display:block;overflow:hidden;padding-bottom:.06em}
.hero h1 .ln>span{display:block}
.hero h1 .ln:nth-child(2){color:rgb(var(--fg)/.55)}
.lead{margin-top:24px;font-size:17px;line-height:1.65;color:rgb(var(--fg)/.78);max-width:30rem;text-shadow:0 2px 18px rgba(0,0,0,.42)}
.ctas{display:flex;gap:12px;flex-wrap:wrap;margin-top:34px}
.ask{margin-top:44px;display:flex;flex-direction:column;gap:12px}
.ask .lb{font-size:13px;font-weight:600;color:rgb(var(--fg)/.55)}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{display:inline-flex;align-items:center;gap:8px;min-height:40px;padding:0 16px;border-radius:999px;font-size:14px;font-weight:500;color:rgb(var(--fg)/.9);transition:background .25s,transform .2s var(--ease)}
.chip:hover{background:rgba(255,255,255,.14);transform:translateY(-1px)}
.chip em{font-style:normal;font-size:11.5px;font-weight:600;color:var(--accent)}
/* entrance (rest state visible if JS fails) */
.js .rise{opacity:0;transform:translateY(24px)}
.js .ln>span{transform:translateY(110%)}
.ready .rise{opacity:1;transform:none;transition:opacity .9s var(--ease) var(--dl,0s),transform .9s var(--ease) var(--dl,0s)}
.ready .ln>span{transform:none;transition:transform 1s var(--ease) var(--dl,0s)}
/* sections */
.sheet{position:relative;z-index:10;background:var(--paper);color:var(--ink);border-radius:40px 40px 0 0;margin-top:-40px;padding-block:96px 104px}
.sec-head{display:flex;justify-content:space-between;align-items:end;gap:24px;flex-wrap:wrap;margin-bottom:40px}
.kick{font-family:var(--mono);font-size:12px;letter-spacing:.2em;color:var(--blue);text-transform:uppercase}
.sec-head h2{margin-top:8px;font-size:clamp(28px,3.6vw,44px);font-weight:600;letter-spacing:-.03em;line-height:1.15;color:var(--navy);text-wrap:balance}
.sec-head p{max-width:30rem;color:var(--sub-l);font-size:15.5px}
.cats{display:grid;grid-template-columns:repeat(6,1fr);gap:16px}
.cat{grid-column:span 2;position:relative;display:flex;flex-direction:column;background:#fff;border-radius:24px;overflow:hidden;box-shadow:0 0 0 1px var(--line-l);transition:box-shadow .3s,transform .3s var(--ease);min-width:0}
.cat.big{grid-column:span 3}
.cat:hover{transform:translateY(-3px);box-shadow:0 0 0 1px #c6d3e6,0 18px 40px rgba(27,43,75,.12)}
.cat .ph{height:clamp(220px,24vw,330px);display:flex;align-items:center;justify-content:center;padding:20px;background:#fff}
.cat .ph img{max-width:100%;max-height:100%;object-fit:contain;transition:transform .7s var(--ease)}
.cat:hover .ph img{transform:scale(1.04)}
.cat .tx{display:flex;flex-direction:column;gap:6px;padding:22px 24px 24px}
.cat .no{font-family:var(--mono);font-size:11px;letter-spacing:.14em;color:var(--sub-l)}
.cat h3{font-size:22px;letter-spacing:-.02em;color:var(--navy);display:flex;align-items:baseline;gap:10px}
.cat h3 sup{font-family:var(--mono);font-size:11px;font-weight:500;color:var(--blue)}
.cat p{font-size:14px;color:var(--sub-l)}
.cat .subs{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.cat .subs span{font-size:12px;color:var(--navy);background:#EEF2F8;padding:3px 9px;border-radius:999px}
.cat.soon{background:transparent;box-shadow:inset 0 0 0 1px var(--line-l)}
.cat.soon .ph{height:110px;background:repeating-linear-gradient(-45deg,transparent 0 10px,rgba(27,43,75,.035) 10px 11px)}
.cat.soon .ph b{font-family:var(--mono);font-size:12px;letter-spacing:.2em;color:var(--sub-l);font-weight:500}
.cat.soon h3{color:#7B869A}
.new{background:#fff;padding-block:96px}
.newgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.np{display:grid;grid-template-rows:auto 1fr;border-radius:24px;overflow:hidden;box-shadow:0 0 0 1px var(--line-l);background:#fff;transition:box-shadow .3s,transform .3s var(--ease);min-width:0}
.np:hover{transform:translateY(-3px);box-shadow:0 0 0 1px #c6d3e6,0 18px 40px rgba(27,43,75,.12)}
.np .ph{position:relative;aspect-ratio:4/3;display:flex;align-items:center;justify-content:center;padding:22px;background:#fff}
.np .ph img{max-width:100%;max-height:100%;object-fit:contain}
.np .tag{position:absolute;left:16px;top:16px;font-family:var(--mono);font-size:11px;letter-spacing:.14em;background:var(--accent);color:#04211b;padding:4px 9px;border-radius:999px;font-weight:500}
.np .tx{padding:20px 22px 24px;display:flex;flex-direction:column;gap:6px}
.np .ct{font-size:12.5px;color:var(--blue);font-weight:600}
.np h3{font-size:20px;color:var(--navy);letter-spacing:-.02em}
.np p{font-size:14px;color:var(--sub-l)}
.np.halo{background:var(--navy);color:#fff;box-shadow:none;display:flex;flex-direction:column;justify-content:space-between;padding:30px}
.np.halo .q{font-family:var(--mono);font-size:11px;letter-spacing:.18em;color:var(--accent)}
.np.halo h3{color:#fff;font-size:26px;line-height:1.3;margin-top:14px}
.np.halo p{color:rgba(255,255,255,.7);margin-top:10px}
.np.halo .go{margin-top:24px;font-weight:600;font-size:14.5px;display:inline-flex;align-items:center;gap:8px}
.since{background:var(--bg);color:rgb(var(--fg));padding-block:110px;overflow:hidden}
.since .wrap{display:grid;grid-template-columns:1.25fr 1fr;gap:48px;align-items:end}
.mega{font-family:var(--num);font-weight:800;font-size:clamp(120px,21vw,300px);line-height:.8;letter-spacing:-.02em;color:transparent;-webkit-text-stroke:1.5px rgba(238,242,247,.55);position:relative}
.mega span{position:absolute;left:0;top:0;color:rgb(var(--fg));-webkit-text-stroke:0;clip-path:inset(0 100% 0 0);transition:clip-path 1.6s var(--ease)}
.since.in .mega span{clip-path:inset(0 0 0 0)}
.since .eyebrow{display:block;margin-bottom:22px}
.since h2{font-size:clamp(26px,3vw,38px);font-weight:500;letter-spacing:-.03em;line-height:1.3}
.since p{margin-top:16px;color:rgb(var(--fg)/.7);font-size:15.5px;max-width:30rem}
.partners{display:flex;gap:28px;flex-wrap:wrap;margin-top:28px;padding-top:22px;border-top:1px solid rgba(255,255,255,.12)}
.partners div{display:flex;flex-direction:column;gap:2px}
.partners b{font-size:16px}
.partners span{font-family:var(--mono);font-size:11px;letter-spacing:.1em;color:rgb(var(--fg)/.5)}
.since .btn-glass{margin-top:30px}
.contact{background:var(--paper);color:var(--ink);padding-block:84px}
.contact .wrap{display:grid;grid-template-columns:1.2fr 1fr;gap:40px;align-items:center}
.contact h2{font-size:clamp(26px,3.2vw,40px);font-weight:600;letter-spacing:-.03em;color:var(--navy);line-height:1.25}
.contact p{margin-top:12px;color:var(--sub-l)}
.cbox{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.cbox div{background:#fff;border-radius:18px;padding:18px 20px;box-shadow:0 0 0 1px var(--line-l);display:flex;flex-direction:column;gap:4px;min-width:0}
.cbox small{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;color:var(--sub-l)}
.cbox b{font-size:17px;color:var(--navy);font-variant-numeric:tabular-nums;word-break:break-all}
.cbox .wide{grid-column:span 2}
.contact .ctas{margin-top:22px}
.contact .btn-white{background:var(--navy);color:#fff}
footer{background:#060a12;color:rgba(238,242,247,.55);font-size:13px;padding-block:34px}
footer b{color:#fff}
.in-view{opacity:1}
.js .rv{opacity:0;transform:translateY(24px)}
.rv.in{opacity:1;transform:none;transition:opacity .8s var(--ease) var(--dl,0s),transform .8s var(--ease) var(--dl,0s)}
@media (max-width:1024px){.links{display:none}.burger{display:inline-flex;margin-left:auto}.cats{grid-template-columns:1fr 1fr}.cat,.cat.big{grid-column:span 1}.newgrid{grid-template-columns:1fr 1fr}}
@media (max-width:767px){
 .nav .btn-white{display:none}
 .hero{flex-direction:column;align-items:stretch;min-height:auto}
 .stage{position:relative;inset:auto;height:46vh;min-height:300px;order:1;margin-top:96px}
 .hero>.wrap{order:2}
 .stage .base{-webkit-mask-image:linear-gradient(transparent 0%,#000 18%,#000 80%,transparent 100%);mask-image:linear-gradient(transparent 0%,#000 18%,#000 80%,transparent 100%)}
 .copy{padding-block:0 80px;margin-top:-24px}
 .cap{bottom:auto;top:104px;right:auto;left:max(var(--gut),env(safe-area-inset-left,0px));font-size:11px}
 .eyebrow{font-size:10.5px;letter-spacing:.14em}
 .cat .ph{height:220px}
 .hero h1{font-size:clamp(40px,11vw,56px)}
 .ctas .btn{flex:1 1 auto;justify-content:center}
 .cats,.newgrid,.since .wrap,.contact .wrap{grid-template-columns:1fr}
 .cbox{grid-template-columns:1fr}.cbox .wide{grid-column:auto}
 .sheet{border-radius:28px 28px 0 0}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important}.js .rise,.js .rv{opacity:1;transform:none}.js .ln>span{transform:none}.mega span{clip-path:none}}
</style></head>
<body>
<div class="note-bar">디자인 시안 (검토용) — 실제 홈페이지가 아닙니다</div>
<header class="nav"><div class="wrap">
 <a class="mark" href="index.html" aria-label="세일테크노 홈">%%MARK%%SEIL TECHNO <small>EST. 1991</small></a>
 <nav class="links glass" aria-label="주 메뉴"><a href="회사소개.html">회사소개</a><a href="제품목록_현미경.html">제품소개</a><a href="적용사례.html">적용사례</a><a href="#">고객지원</a></nav>
 <a class="btn btn-white" href="#contact">데모 신청 <i aria-hidden="true">%%ARROW%%</i></a>
 <a class="btn btn-glass glass burger" href="제품목록_현미경.html" aria-label="메뉴">메뉴</a>
</div></header>

<section class="hero" id="hero">
 <div class="stage" id="stage" aria-hidden="true">
  <div class="base"></div>
  <div class="lens" id="lens">%%RETICLE%%</div>
  <div class="readout" id="readout"><b>×3.0</b> · X <span id="rx">1440</span> · Y <span id="ry">1080</span> px</div>
 </div>
 <div class="wrap" style="width:100%"><div class="copy">
  <div class="eyebrow rise" style="--dl:.15s">Since 1991 · Optics · Metrology · Inspection</div>
  <h1><span class="ln"><span style="--dl:.27s">보는 것이</span></span><span class="ln"><span style="--dl:.39s">믿는 것이다.</span></span></h1>
  <p class="lead rise" style="--dl:.55s">1991년부터 접안렌즈 없는 현미경과 측정·검사 장비를 산업 현장에 공급해 왔습니다. 시료를 보내 주시면 맞는 장비로 직접 보여 드립니다.</p>
  <div class="ctas rise" style="--dl:.67s"><a class="btn btn-white" href="#products">제품 찾기 <i aria-hidden="true">%%ARROW%%</i></a><a class="btn btn-glass glass" href="#contact">데모 신청</a></div>
  <div class="ask rise" style="--dl:.8s"><span class="lb">무엇을 하시나요?</span>
   <div class="chips">%%CHIPS%%</div></div>
 </div></div>
 <div class="cap">PCB 3D 합성 이미지 · Deep Vision DI-AM1165 촬영</div>
</section>

<section class="sheet" id="products"><div class="wrap">
 <div class="sec-head rv"><div><div class="kick">Products</div><h2>찾으시는 장비를<br>분야별로 보세요.</h2></div><p>현미경부터 측정 시스템, 자동 검사까지. 분야를 고르면 세부 종류와 제품을 한눈에 볼 수 있습니다.</p></div>
 <div class="cats">%%CATS%%</div>
</div></section>

<section class="new"><div class="wrap">
 <div class="sec-head rv"><div><div class="kick">New</div><h2>새로 나온 제품</h2></div><p>제품 파일에 NEW 표시를 하면 이곳에 자동으로 나타납니다.</p></div>
 <div class="newgrid">%%NEW%%</div>
</div></section>

<section class="since" id="since"><div class="wrap">
 <div class="mega" aria-label="1991">1991<span aria-hidden="true">1991</span></div>
 <div class="rv"><span class="eyebrow">Since 1991 · %%YEARS%% years</span>
  <h2>%%YEARS%%년 동안, 정확하게 보는 일을 공급해 왔습니다.</h2>
  <p>연구기관, 기업과 함께 시스템을 개발하고, 딥러닝 기업과 협력해 자동 검사 시스템까지 공급합니다.</p>
  <div class="partners"><div><b>Vision Engineering</b><span>UK · SINCE 1991</span></div><div><b>HIKVISION</b><span>PARTNER · SINCE 2025</span></div></div>
  <a class="btn btn-glass glass" href="회사소개.html">회사소개 보기</a></div>
</div></section>

<section class="contact" id="contact"><div class="wrap">
 <div class="rv"><div class="kick">Contact</div><h2>시료를 보내 주시면,<br>맞는 장비로 보여 드립니다.</h2><p>문래역 데모룸에서 여러 장비를 직접 비교해 보실 수 있습니다.</p>
  <div class="ctas"><a class="btn btn-white" href="#">데모 신청 <i aria-hidden="true">%%ARROW%%</i></a></div></div>
 <div class="cbox rv" style="--dl:.1s"><div><small>TEL</small><b>02-2632-3211</b></div><div><small>E-MAIL</small><b>sales@stvision.co.kr</b></div><div class="wide"><small>DEMO ROOM</small><b>서울 영등포구 당산로2길 12, 에이스테크노타워 806호 · 2호선 문래역 7번 출구</b></div></div>
</div></section>
<footer><div class="wrap"><div class="fmark">%%MARK%%SEIL TECHNO</div><b>㈜세일테크노</b> · 서울특별시 영등포구 당산로2길 12, 에이스테크노타워 806호 · 대표전화 02-2632-3211 · Since 1991</div></footer>

<script>
(function(){
 var root=document.documentElement; root.classList.add('js');
 var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
 function go(){root.classList.add('ready')}
 requestAnimationFrame(function(){requestAnimationFrame(go)}); setTimeout(go,1200);
 // 화면 진입 reveal
 var rv=[].slice.call(document.querySelectorAll('.rv,.since'));
 if('IntersectionObserver' in window&&!reduce){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.18});rv.forEach(function(el){io.observe(el)})}else{rv.forEach(function(el){el.classList.add('in')})}
 // 렌즈
 var stage=document.getElementById('stage'),lens=document.getElementById('lens'),ro=document.getElementById('readout'),rx=document.getElementById('rx'),ry=document.getElementById('ry');
 var Z=3,IW=2880,IH=2160,tx=.55,ty=.48,x=tx,y=ty,hover=matchMedia('(hover: hover) and (pointer: fine)').matches,t0=performance.now();
 function cover(w,h){var s=Math.max(w/IW,h/IH),dw=IW*s,dh=IH*s;return{s:s,ox:(w-dw)*.58,oy:(h-dh)*.5,dw:dw,dh:dh}}
 function place(){
  var r=stage.getBoundingClientRect(),w=r.width,h=r.height,d=lens.offsetWidth,c=cover(w,h);
  var px=x*w,py=y*h; lens.style.transform='translate('+(px-d/2)+'px,'+(py-d/2)+'px)';
  var bw=c.dw*Z,bh=c.dh*Z; lens.style.backgroundSize=bw+'px '+bh+'px';
  var ix=(px-c.ox)*Z,iy=(py-c.oy)*Z; lens.style.backgroundPosition=(d/2-ix)+'px '+(d/2-iy)+'px';
  ro.style.transform='translate('+(px-ro.offsetWidth/2)+'px,'+(py+d/2+18)+'px)';
  var ix2=Math.round((px-c.ox)/c.s),iy2=Math.round((py-c.oy)/c.s); rx.textContent=String(Math.min(IW,Math.max(0,ix2))).padStart(4,'0'); ry.textContent=String(Math.min(IH,Math.max(0,iy2))).padStart(4,'0');
 }
 if(hover&&!reduce){document.getElementById('hero').addEventListener('pointermove',function(e){var r=stage.getBoundingClientRect();tx=Math.min(.92,Math.max(.12,(e.clientX-r.left)/r.width));ty=Math.min(.86,Math.max(.14,(e.clientY-r.top)/r.height))})}
 function loop(now){
  if(!hover&&!reduce){var t=(now-t0)/1000;tx=.6+.16*Math.sin(t*.21);ty=.5+.22*Math.sin(t*.29+1)}
  x+=(tx-x)*(reduce?1:.12); y+=(ty-y)*(reduce?1:.12); place(); if(!reduce)requestAnimationFrame(loop);
 }
 addEventListener('resize',place); requestAnimationFrame(loop);
})();
</script>
</body></html>"""

ARROW_SVG = '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M2 7h9M7.5 3l4 4-4 4" stroke="#04211b" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def lens_svg():
    t=[]
    for i in range(72):
        L = 9 if i % 6 == 0 else 4
        t.append(f'<line x1="50" y1="1.2" x2="50" y2="{1.2+L*0.35:.2f}" transform="rotate({i*5} 50 50)"/>')
    return ('<svg viewBox="0 0 100 100" fill="none" aria-hidden="true"><g stroke="#00C9A7" stroke-width=".35" stroke-opacity=".9">' + "".join(t) + '</g>'
            '<g stroke="#00C9A7" stroke-width=".3" stroke-opacity=".7"><line x1="50" y1="18" x2="50" y2="42"/><line x1="50" y1="58" x2="50" y2="82"/><line x1="18" y1="50" x2="42" y2="50"/><line x1="58" y1="50" x2="82" y2="50"/></g></svg>')

def build_main(items):
    R = "../site"
    def ip(p): return R + p
    years = 2026 - 1991
    chips = [("보면서 수작업", "제품목록_현미경.html#sub1", "현미경"), ("확대 촬영·기록", "제품목록_현미경.html#sub2", "현미경"),
             ("치수 측정", "제품목록_측정시스템.html", "측정"), ("자동 측정·검사", "제품목록_측정시스템.html#sub3", "VMM")]
    chips_h = "".join(f'<a class="chip glass" href="{h}">{e(a)} <em>{e(b)}</em></a>' for a, h, b in chips)
    cat_meta = [("현미경", "mantis.jpg", "접안렌즈 없는 실체 현미경부터 4K·3D 디지털 현미경까지", True),
                ("측정 시스템", "hawk.jpg", "측정 현미경, 고배율 측정기, 비디오 측정기(VMM)", True),
                ("AI 검사·측정", "hybrid/hero.jpg", "하이브리드 검사·측정, 기상 AI분석, 기상 검사/측정 비전", False),
                ("머신비전", None, "산업용 카메라, 렌즈·조명, 코드리더, 비전 SW", False),
                ("3D·특수 센싱", "desktop3d/main.jpg", "3D 스캐너, 백색광 간섭계 등 장비별 소개", False)]
    cats = ""
    for i, (c, im, ds, big) in enumerate(cat_meta):
        n = sum(1 for d in items if d["category"] == c)
        if c in CATCFG and n:
            subs = "".join(f"<span>{e(s[0])}</span>" for s in CATCFG[c]["subs"])
            cats += (f'<a class="cat{" big" if big else ""} rv" style="--dl:{i*.1:.1f}s" href="{CATCFG[c]["file"]}"><div class="ph"><img src="{ip("/assets/img/products/"+im)}" alt="{e(c)} 대표 제품" loading="lazy"></div>'
                     f'<div class="tx"><span class="no">{i+1:02d} / 05</span><h3>{e(c)}<sup>{n}</sup></h3><p>{e(ds)}</p><div class="subs">{subs}</div></div></a>')
        else:
            cats += (f'<div class="cat soon rv" style="--dl:{i*.1:.1f}s"><div class="ph"><b>COMING SOON</b></div>'
                     f'<div class="tx"><span class="no">{i+1:02d} / 05</span><h3>{e(c)}</h3><p>{e(ds)}</p></div></div>')
    news = [d for d in items if d.get("badge") == "NEW" and d.get("image")]
    nh = ""
    for i, d in enumerate(news[:2]):
        nh += (f'<a class="np rv" style="--dl:{i*.1:.1f}s" href="상세/{d["slug"]}.html"><div class="ph"><span class="tag">NEW</span><img src="{ip(d["image"])}" alt="{e(d["title"])}" loading="lazy"></div>'
               f'<div class="tx"><span class="ct">{e(d["category"])} · {e(d["subcategory"])}</span><h3>{e(d["title"])}</h3><p>{e(d["summary"])}</p></div></a>')
    nh += ('<a class="np halo rv" style="--dl:.2s" href="상세/evocam-aura-4k.html"><div><span class="q">LOOKING FOR</span><h3>EVO Cam HALO를<br>찾으시나요?</h3>'
           '<p>EVO Cam HALO는 EVO Cam AURA 4K로 이름과 기능이 새로워졌습니다.</p></div><span class="go">AURA 4K 보기 →</span></a>')
    html_ = (MAIN_TPL.replace("%%IMG%%", R + "/assets/img/").replace("%%ARROW%%", ARROW_SVG).replace("%%RETICLE%%", lens_svg())
             .replace("%%CHIPS%%", chips_h).replace("%%CATS%%", cats).replace("%%NEW%%", nh).replace("%%YEARS%%", str(years)).replace("%%MARK%%", MARK).replace("%%FAV%%", FAVICON))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(html_)


# ───── 긴 소개형 상세 페이지 (layout: custom) ─────
CX_CSS = """
.cx-hero{background:linear-gradient(120deg,#12365A,#1B2B4B 60%,#121d33);color:#fff;overflow:hidden}
.cx-hero .wrap{display:grid;grid-template-columns:1.05fr .95fr;gap:48px;align-items:center;padding-block:56px 64px}
.cx-hero .crumb{opacity:.65;font-size:13px}
.cx-badges{display:flex;gap:8px;flex-wrap:wrap;margin:14px 0 18px}
.cx-badges a,.cx-badges span{font-size:12.5px;font-weight:700;padding:5px 12px;border-radius:6px}
.cx-badges a{background:rgba(255,255,255,.14);color:#fff}
.cx-eyebrow{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:12.5px;letter-spacing:.14em;color:#00C9A7;text-transform:uppercase}
.cx-hero h1{font-size:clamp(34px,4.6vw,58px);line-height:1.15;letter-spacing:-.04em;margin-top:14px;text-wrap:balance}
.cx-hero .lead{margin-top:20px;font-size:17px;line-height:1.7;opacity:.82;max-width:34em}
.cx-sys{margin-top:22px;padding:14px 16px;border-radius:10px;background:rgba(255,255,255,.07);font-size:14px;line-height:1.6}
.cx-sys b{display:block;font-size:11.5px;letter-spacing:.12em;color:#00C9A7;font-family:"IBM Plex Mono",monospace;font-weight:500;margin-bottom:2px}
.cx-hero .actions{margin-top:26px}
.cx-hero .btn-ghost{background:transparent;color:#fff;border-color:rgba(255,255,255,.35)}
.cx-heroimg{background:#fff;border-radius:20px;padding:22px;display:flex;align-items:center;justify-content:center;max-height:520px}
.cx-heroimg img{max-width:100%;max-height:476px;object-fit:contain}
.cx-nav{position:sticky;top:72px;z-index:6;background:#fff;border-bottom:1px solid var(--line)}
.cx-nav .wrap{display:flex;gap:24px;overflow-x:auto;scrollbar-width:none}
.cx-nav a{padding:15px 0;font-size:14.5px;font-weight:700;color:var(--sub);white-space:nowrap;border-bottom:2px solid transparent}
.cx-nav a:hover{color:var(--navy);border-color:var(--navy)}
.cx-sec{padding-block:80px;scroll-margin-top:130px}
.cx-sec.alt{background:var(--bg)}
.cx-kick{font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:12px;letter-spacing:.16em;color:var(--blue);text-transform:uppercase}
.cx-sec h2{font-size:clamp(26px,3.2vw,38px);letter-spacing:-.035em;line-height:1.25;color:var(--navy);margin-top:8px;text-wrap:balance}
.cx-head{max-width:760px;margin-bottom:36px}
.cx-head p{margin-top:14px;font-size:16.5px;color:var(--sub)}
.cx-head a{color:var(--blue);font-weight:600;text-decoration:underline;text-underline-offset:3px}
.cx-why{display:grid;grid-template-columns:.9fr 1.1fr;gap:24px 56px}
.cx-prose{display:flex;flex-direction:column;gap:14px;font-size:16.5px;color:#2f3747;min-width:0}
.cx-prose strong{color:#c0392b}
.cx-vs{grid-column:1/-1;display:grid;grid-template-columns:1fr auto 1fr;gap:18px;align-items:stretch;margin-top:24px}
.cx-vs-col{border-radius:16px;padding:26px 26px 20px;display:flex;flex-direction:column;gap:2px}
.cx-vs-col.old{background:var(--bg);border:1px solid var(--line)}
.cx-vs-col.new{background:#12365A;color:#fff}
.cx-vs-h{font-size:13px;font-weight:800;letter-spacing:.02em;margin-bottom:8px}
.cx-vs-col.old .cx-vs-h{color:var(--sub)}.cx-vs-col.new .cx-vs-h{color:#00C9A7}
.cx-vs-col p{padding:12px 0;border-top:1px solid rgba(0,0,0,.08);font-size:15px}
.cx-vs-col.new p{border-color:rgba(255,255,255,.14)}
.cx-vs-arrow{align-self:center;font-size:28px;color:var(--blue);font-weight:300}
.cx-fig{margin:0 0 8px}
.cx-fig img{width:100%;border-radius:14px;border:1px solid var(--line);background:#fff;display:block}
.cx-fig figcaption{margin-top:12px;font-size:14px;color:var(--sub);max-width:60em}
.cx-fig.wide{margin-top:40px}
.cx-steps{list-style:none;counter-reset:s;display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin:36px 0 0}
.cx-steps li{counter-increment:s;position:relative;background:#fff;border:1px solid var(--line);border-radius:14px;padding:22px 20px;min-width:0}
.cx-steps li::before{content:counter(s,decimal-leading-zero);display:block;font-family:"IBM Plex Mono",monospace;font-size:13px;color:var(--blue);margin-bottom:10px}
.cx-steps b{font-size:16px;color:var(--navy)}
.cx-steps p{font-size:14px;color:var(--sub);margin-top:6px}
.cx-two{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:40px}
.cx-card{background:#fff;border:1px solid var(--line);border-radius:14px;padding:24px}
.cx-tag{font-size:12px;font-weight:700;color:var(--blue)}
.cx-card h3{font-size:19px;color:var(--navy);margin:6px 0 8px}
.cx-card p{font-size:14.5px;color:var(--sub)}
.cx-benefits{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border-top:2px solid var(--navy);margin-bottom:40px}
.cx-benefits div{padding:24px 22px 26px 0;border-bottom:1px solid var(--line);min-width:0}
.cx-benefits div+div{padding-left:22px;border-left:1px solid var(--line)}
.cx-benefits h3{font-size:18px;color:var(--navy);margin-bottom:8px;letter-spacing:-.02em}
.cx-benefits p{font-size:14.5px;color:var(--sub)}
.cx-table{overflow-x:auto;margin-bottom:8px}
.cx-table table{min-width:640px;background:#fff}
.cx-table thead th{background:#12365A;color:#fff;font-size:14px;width:auto}
.cx-table td:first-child{font-weight:700;color:var(--navy);width:210px}
.cx-table td small{display:block;font-weight:500;color:var(--sub);font-size:12px;font-family:"IBM Plex Mono",monospace}
.cx-cmp td:first-child{background:var(--bg)}
.cx-dl{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:40px}
.cx-dl div{background:#fff;border:1px solid var(--line);border-radius:14px;padding:22px;display:flex;flex-direction:column;gap:8px;min-width:0}
.cx-dl h3{font-size:17px;color:var(--navy)}
.cx-dl h3 small{display:block;font-size:12px;font-weight:500;color:var(--sub);font-family:"IBM Plex Mono",monospace;margin-top:2px}
.cx-dl p{font-size:14.5px;color:#2f3747;flex:1}
.cx-dl span{font-size:13px;font-weight:600;color:var(--blue);padding-top:10px;border-top:1px dashed var(--line)}
.cx-specnote{margin-top:20px;display:flex;flex-direction:column;gap:8px;font-size:15px;color:#2f3747}
.cx-specnote b{display:inline-block;min-width:76px;color:var(--navy)}
.cx-fine{font-size:13px;color:var(--sub)}
.cx-apps{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin-bottom:40px}
.cx-apps div{border:1px solid var(--line);border-radius:14px;padding:20px;min-width:0}
.cx-apps h3{font-size:17px;color:var(--navy);margin-bottom:10px}
.cx-apps h3 small{display:block;font-size:12.5px;font-weight:500;color:var(--sub)}
.cx-apps p{font-size:14px;color:#2f3747;padding:4px 0}
.cx-apps p span{display:inline-block;font-size:11.5px;font-weight:700;color:#fff;background:var(--blue);border-radius:4px;padding:1px 6px;margin-right:6px}
.cx-apps p+p span{background:#c0392b}
.cx-cta{background:#12365A;color:#fff;padding-block:64px}
.cx-cta .wrap{display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap}
.cx-cta h2{font-size:clamp(22px,2.6vw,30px);letter-spacing:-.03em}
.cx-cta p{opacity:.75;margin-top:6px}
.cx-btns{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.cx-cta .btn-ghost{background:transparent;color:#fff;border-color:rgba(255,255,255,.35)}
.cx-soon{font-size:12.5px;opacity:.55;width:100%}
@media(max-width:1024px){.cx-steps,.cx-benefits{grid-template-columns:1fr 1fr}.cx-benefits div+div{border-left:0;padding-left:0}.cx-dl{grid-template-columns:1fr 1fr}.cx-apps{grid-template-columns:repeat(3,1fr)}}
@media(max-width:767px){.cx-hero .wrap,.cx-why,.cx-two{grid-template-columns:1fr}.cx-heroimg{order:-1;max-height:340px}.cx-heroimg img{max-height:300px}
 .cx-vs{grid-template-columns:1fr}.cx-vs-arrow{transform:rotate(90deg);justify-self:center}.cx-steps,.cx-benefits,.cx-dl,.cx-apps{grid-template-columns:1fr}.cx-sec{padding-block:56px}}
"""

def build_custom(d, items):
    root = "../"
    si = SUB_INFO[d["subcategory"]]
    body = d["body"].replace("{{IMG}}", root + "../site").replace("{{ROOT}}", root)
    nav = "".join(f'<a href="#{a}">{t}</a>' for a, t in [("why","왜 필요한가"),("how","작동 원리"),("benefits","핵심 장점"),("tools","검사 툴"),("guide","선택 가이드"),("spec","사양"),("apps","적용 분야")])
    inner = f"""<style>{CX_CSS}</style>
<section class="cx-hero"><div class="wrap">
 <div><div class="crumb">홈 › 제품소개 › {e(d['category'])} › {e(d['subcategory'])}</div>
  <div class="cx-badges"><a href="{cat_link(d['category'], root)}#{si['id']}">{e(d['subcategory'])}</a></div>
  <div class="cx-eyebrow">{e(d.get('eyebrow',''))}</div>
  <h1>{d.get('headline', e(d['title']))}</h1>
  <p class="lead">{e(d.get('lead', d['summary']))}</p>
  <div class="cx-sys"><b>SYSTEM</b>{e(d.get('system',''))}</div>
  <div class="actions"><a class="btn btn-mint" href="#">샘플 테스트 의뢰</a><a class="btn btn-ghost" href="#">데모 문의</a></div>
 </div>
 <div class="cx-heroimg">{pic(root, d)}</div>
</div></section>
<nav class="cx-nav" aria-label="페이지 내 이동"><div class="wrap">{nav}</div></nav>
{body}"""
    os.makedirs(os.path.join(HERE, "상세"), exist_ok=True)
    open(os.path.join(HERE, "상세", d["slug"] + ".html"), "w", encoding="utf-8").write(page(f"{d['title']} | 세일테크노", inner, root, cta=False))

exec(open(os.path.join(HERE, "about_build.py"), encoding="utf-8").read())
exec(open(os.path.join(HERE, "cat_deck.py"), encoding="utf-8").read())
exec(open(os.path.join(HERE, "board_build.py"), encoding="utf-8").read())
exec(open(os.path.join(HERE, "support_build.py"), encoding="utf-8").read())
exec(open(os.path.join(HERE, "cases_build.py"), encoding="utf-8").read())
items = load()
build_about()
build_main(items)
for c in CATCFG: build_list(items, c)
for d in items: build_detail(d, items)
build_cases(items)
_dls = build_support(items)
fix_links(items, _dls)
print("완료:", len(items), "개 제품")
