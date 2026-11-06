# -*- coding: utf-8 -*-
"""공개용 홈페이지 만들기: build_preview.py가 만든 시안 HTML을 영문 주소로 바꿔 _site 폴더에 모읍니다.
GitHub Actions가 자동으로 실행합니다. (직접 실행: python3 build_preview.py && python3 publish.py)"""
import os, re, glob, shutil, posixpath, html as _h, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.normpath(os.path.join(HERE, "..", "site"))
OUT = os.path.join(HERE, "_site")
DOMAIN = os.environ.get("SITE_URL", "https://www.stvision.co.kr")
CAT = {"제품목록_현미경.html": "products/microscope", "제품목록_측정시스템.html": "products/metrology", "제품목록_AI검사측정.html": "products/ai-inspection",
       "제품목록_머신비전.html": "products/machine-vision", "제품목록_3D특수센싱.html": "products/3d-sensing"}
TOP = {"index.html": "", "회사소개.html": "about", "적용사례.html": "cases", "고객지원.html": "support"}

def target(rel):
    """시안 파일 경로(01_시안 기준) → 공개 주소(앞 / 없이, 확장자 없이)"""
    if rel in TOP: return TOP[rel]
    if rel in CAT: return CAT[rel]
    m = re.match(r"상세/cases/(.+)\.html$", rel)
    if m: return "cases/" + m.group(1)
    m = re.match(r"상세/(.+)\.html$", rel)
    if m: return "products/" + m.group(1)
    return None

def outfile(url):
    return os.path.join(OUT, (url or "index") + ".html")

ATTR = re.compile(r'((?:href|src|poster|data-full|data-js)=")([^"]*)(")|(url\()([^)]*)(\))')
def rewrite(text, rel):
    base = posixpath.dirname(rel)
    def fix(v):
        if not v or v.startswith(("http:", "https:", "#", "mailto:", "tel:", "data:", "/", "javascript:")): return v
        m = re.match(r"([^?#]*)(.*)$", v); path, tail = m.group(1), m.group(2)
        if not path: return v
        p = posixpath.normpath(posixpath.join(base, path))
        if p.startswith("../site/"): return "/" + p[len("../site/"):] + tail
        t = target(p)
        if t is not None: return "/" + t + tail
        return v
    def sub(m):
        if m.group(1): return m.group(1) + _h.escape(fix(_h.unescape(m.group(2))), quote=True) + m.group(3)
        return m.group(4) + fix(m.group(5)) + m.group(6)
    text = ATTR.sub(sub, text)
    text = re.sub(r'<div class="note-bar">.*?</div>\s*', "", text, count=1)   # '디자인 시안' 띠 제거
    return text

def main():
    if os.path.exists(OUT):
        try: shutil.rmtree(OUT)
        except OSError: pass          # 지울 수 없는 환경이면 덮어쓰기
    os.makedirs(OUT, exist_ok=True)
    import sys; sys.path.insert(0, HERE)
    from seo import SEO
    seo = SEO(SITE, DOMAIN)
    pages = []
    for fp in glob.glob(os.path.join(HERE, "*.html")) + glob.glob(os.path.join(HERE, "상세", "*.html")) + glob.glob(os.path.join(HERE, "상세", "cases", "*.html")):
        rel = os.path.relpath(fp, HERE).replace(os.sep, "/")
        url = target(rel)
        if url is None: continue
        s = rewrite(open(fp, encoding="utf-8").read(), rel)
        if 'draft' in rel or 'seil-example' in rel: continue        # 작성 예시(draft) 글은 공개하지 않음
        s = seo.apply(s, url)
        o = outfile(url); os.makedirs(os.path.dirname(o), exist_ok=True)
        open(o, "w", encoding="utf-8").write(s); pages.append(url)
    shutil.copytree(os.path.join(SITE, "assets"), os.path.join(OUT, "assets"), dirs_exist_ok=True)
    today = datetime.date.today().isoformat()
    open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
        "".join(f"<url><loc>{DOMAIN}/{u}</loc><lastmod>{today}</lastmod></url>\n" for u in sorted(pages)) + "</urlset>\n")
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    open(os.path.join(OUT, ".nojekyll"), "w").write("")
    if os.environ.get("CNAME"): open(os.path.join(OUT, "CNAME"), "w").write(os.environ["CNAME"] + "\n")
    nf = open(outfile(""), encoding="utf-8").read()
    open(os.path.join(OUT, "404.html"), "w", encoding="utf-8").write(re.sub(r'<link rel="canonical"[^>]*>\n?', "", re.sub(r"<title>.*?</title>", "<title>페이지를 찾을 수 없습니다 | 세일테크노</title>", nf, count=1)).replace("</head>", '<meta name="robots" content="noindex">\n</head>', 1))
    # 링크 점검
    bad = set()
    for f in glob.glob(os.path.join(OUT, "**", "*.html"), recursive=True):
        for m in re.finditer(r'(?:href|src|poster|data-full|data-js)="(/[^"#?]*)', open(f, encoding="utf-8").read()):
            p = m.group(1).rstrip("/")
            if p == "": continue
            ok = os.path.exists(os.path.join(OUT, p.lstrip("/"))) or os.path.exists(os.path.join(OUT, p.lstrip("/") + ".html"))
            if not ok: bad.add(p)
    print(f"공개용 페이지 {len(pages)}개 → {OUT}")
    if bad: print("※ 없는 파일을 가리키는 링크:", len(bad)); [print("  ", b) for b in sorted(bad)[:40]]
if __name__ == "__main__":
    main()
