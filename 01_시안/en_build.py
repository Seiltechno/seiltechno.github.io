# -*- coding: utf-8 -*-
# 영문 제품 페이지 — site/_products_en/<제품파일명>.md 가 있는 제품만 영문판을 만듭니다.
#   · 영문 파일에는 글만 적고, 사진·영상 경로는 한국어 파일에서 순서대로 가져옵니다.
#   · 시안: 01_시안/en/<제품파일명>.html  →  공개 주소: /en/products/<제품파일명>
#   · 한국어 페이지에는 'English' 버튼, 영문 페이지에는 '한국어' 버튼이 생깁니다.
#   · 한국어 제품이 published: false 이면 영문판도 공개용에서 빠집니다.
# build_preview.py 끝에서 exec 됨

EN_DIR = os.path.join(SITE, "_products_en")
EN_ADDR = "806, Ace Techno Tower, 12 Dangsan-ro 2-gil, Yeongdeungpo-gu, Seoul, Korea"
EN_CSS = """
.lang-sw{display:inline-flex;align-items:center;gap:4px;font-size:12.5px;font-weight:700;color:var(--navy);border:1px solid var(--line);border-radius:999px;padding:4px 11px;text-decoration:none;background:#fff}
.lang-sw:hover{border-color:var(--navy)}
header .btn{white-space:nowrap}
"""

def load_en():
    out = {}
    for f in glob.glob(os.path.join(EN_DIR, "*.md")):
        t = open(f, encoding="utf-8").read()
        _, fm, body = t.split("---", 2)
        x = yaml.safe_load(fm) or {}
        x["body"] = body.strip()
        out[os.path.splitext(os.path.basename(f))[0]] = x
    return out

def _merge_en(ko, en):
    """한국어 데이터(사진·영상) + 영문 글"""
    d = dict(en); d["slug"] = ko["slug"]
    for k in ("image", "gallery", "brand", "order", "published"):
        if k in ko: d[k] = ko[k]
    d["specs"] = [(x.get("label", ""), x.get("value", "")) if isinstance(x, dict) else tuple(x) for x in (en.get("specs") or [])]
    for k in ("highlights", "applications", "tags"): d[k] = en.get(k) or []
    if ko.get("shots"):
        tx = en.get("shots") or []
        d["shots"] = [dict(s, **(tx[i] if i < len(tx) else {})) for i, s in enumerate(ko["shots"])]
    if ko.get("setups"):
        caps = en.get("setups_caps") or []
        d["setups"] = [dict(x, cap=(caps[i] if i < len(caps) else x.get("cap", ""))) for i, x in enumerate(ko["setups"])]
    if ko.get("guide"):
        tx = en.get("guide") or []
        g = []
        for i, ch in enumerate(ko["guide"]):
            t = tx[i] if i < len(tx) else {}
            caps = t.get("caps") or []
            g.append({"title": t.get("title", ch["title"]), "text": t.get("text", ""), "points": t.get("points") or [],
                      "video": ch.get("video"),
                      "images": [dict(im, cap=(caps[j] if j < len(caps) else im.get("cap", ""))) for j, im in enumerate(ch.get("images") or [])]})
        d["guide"] = g
    return d

def page_en(title, inner, root, ko_href, contact):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>{FAVICON}{FONT}<style>{CSS}{EN_CSS}</style></head><body>
<div class="note-bar">Design preview (for review) — not the live website</div>
<header><div class="wrap"><a class="logo" href="{root}index.html" aria-label="SEIL TECHNO home">{MARK}<span>SEIL<span>TECHNO</span></span></a>
<nav><a href="{root}회사소개.html">Company</a><a class="on" href="{root}제품목록_현미경.html">Products</a><a href="{root}적용사례.html">Applications</a><a href="{root}고객지원.html">Support</a></nav>
<div style="display:flex;gap:10px;align-items:center"><a class="lang-sw" href="{ko_href}" hreflang="ko" lang="ko">한국어</a><a class="btn btn-primary" href="{contact}">Contact us</a></div></div></header>
{inner}
<section class="cta"><div class="wrap"><div><h3>Want to see it in action?</h3><p>Send us your samples or visit us, and we will demonstrate it for you.</p></div>
<div class="actions"><a class="btn btn-mint" href="{contact}">Request a demo</a><a class="btn btn-ghost" href="tel:+82226323211">+82-2-2632-3211</a></div></div></section>
<footer><div class="wrap"><div class="fmark">{MARK}SEIL TECHNO</div><b>SEIL TECHNO CORP.</b> · {EN_ADDR} · Tel +82-2-2632-3211<br>Since 1991 · Exclusive distributor of Vision Engineering in Korea</div></footer></body></html>"""

def build_en_detail(ko, en):
    d = _merge_en(ko, en)
    root = "../"
    slug = d["slug"]
    ko_href = f"{root}상세/{slug}.html"
    contact = f"{root}고객지원.html?product={slug}#inquiry"
    ks = "".join(f"<div><small>{e(k)}</small><b>{e(v)}</b></div>" for k, v in d["specs"][:4])
    hl = "".join(f'<div><i>{i+1:02d}</i><h4>{e(h["title"])}</h4><p>{e(h["text"])}</p></div>' for i, h in enumerate(d["highlights"]))
    rows = "".join(f"<tr><th>{e(k)}</th><td>{e(v)}</td></tr>" for k, v in d["specs"])
    apps = "".join(f"<span>{e(a)}</span>" for a in d.get("applications", []))
    tags = "".join(f'<span style="color:var(--blue);font-weight:700;font-size:13px">#{e(t)}</span>' for t in d.get("tags", [])[:4])
    inner = f"""<section class="dhero"><div class="wrap dgrid"><div><div class="mainimg">{pic(root, d, 'id="main"')}</div></div>
<div class="dinfo"><div class="crumb">Home › Products › {e(d.get('category',''))} › {e(d.get('subcategory',''))}</div><div style="display:flex;gap:8px;align-items:center;margin:12px 0 8px;flex-wrap:wrap"><span style="background:var(--navy);color:#fff;font-size:13px;font-weight:700;padding:5px 12px;border-radius:6px">{e(d.get('subcategory',''))}</span>{f'<span style="color:var(--blue);font-weight:700;font-size:13px">#{e(d["brand"])}</span>' if d.get("brand") else ""}</div>
<h1>{e(d['title'])}</h1><div class="st">{e(d.get('subtitle',''))}</div><p class="sm">{e(d.get('summary',''))}</p>
<div class="keyspec">{ks}</div><div class="actions"><a class="btn btn-primary" href="{contact}">Request a quote</a><a class="btn btn-ghost" href="{root}고객지원.html?product={slug}&amp;type=demo#inquiry">Request a demo</a><a class="btn btn-ghost" href="#gd">User guide</a></div></div></div></section>
<div class="wrap"><div class="tabs"><a class="on" href="#f">Key features</a>{'<a href="#sh">Screenshots</a>' if d.get('shots') else ''}{f'<a href="#gd">{e(d.get("guide_tab","User guide"))}</a>' if d.get('guide') else ''}<a href="#s">Specifications</a><a href="#a">Applications</a></div>
{setups_section(d, root, en=True)}<section class="sec" id="f"><h2>Key features</h2><div class="hl">{hl}</div></section>
{shots_section(d, root)}{guide_section(d, root, en=True)}<section class="sec body"><h2>Overview</h2>{md(d['body'])}</section>
<section class="sec" id="s"><h2>Specifications</h2><table>{rows}</table><p class="small">※ Specifications are subject to change without notice. Please contact us for details.</p></section>
<section class="sec" id="a"><h2>Applications</h2><div class="apps">{apps}</div></section></div>"""
    os.makedirs(os.path.join(HERE, "en"), exist_ok=True)
    open(os.path.join(HERE, "en", slug + ".html"), "w", encoding="utf-8").write(page_en(f"{d['title']} | SEIL TECHNO", inner, root, ko_href, contact))
    # 한국어 페이지에 'English' 버튼
    kp = os.path.join(HERE, "상세", slug + ".html")
    s = open(kp, encoding="utf-8").read()
    btn = f'<a class="lang-sw" href="../en/{slug}.html" hreflang="en" lang="en">English</a>'
    if "lang-sw" not in s:
        s = s.replace("</style></head>", EN_CSS + "</style></head>", 1)
        s = s.replace('<div class="dinfo"><div class="crumb">', f'<div class="dinfo"><div style="float:right">{btn}</div><div class="crumb">', 1)
        open(kp, "w", encoding="utf-8").write(s)

def build_en(items):
    en = load_en()
    n = 0
    for d in items:
        if d["slug"] in en:
            build_en_detail(d, en[d["slug"]]); n += 1
    if n: print("영문 페이지:", n, "개")
