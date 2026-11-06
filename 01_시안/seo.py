# -*- coding: utf-8 -*-
"""검색엔진 최적화(SEO): 공개용 페이지마다 설명·키워드·대표 이미지·구조화 데이터를 자동으로 넣습니다.
publish.py가 불러 씁니다. 제품은 site/_products 의 summary·tags·keywords 를, 적용사례는 excerpt 를 씁니다.
검색엔진 소유 확인 코드는 site/_config.yml 의 google_site_verification / naver_site_verification 에 적습니다."""
import os, re, glob, json, html as _h
import yaml

ORG_NAME = "㈜세일테크노"
BASE_KW = ["세일테크노", "SEIL TECHNO"]
PAGES = {   # 주소: (제목, 설명, 키워드)
    "": ("세일테크노 — 현미경·측정기·머신비전 검사 장비 전문 (Since 1991)",
         "1991년부터 접안렌즈 없는 실체현미경, 디지털현미경, 비디오 측정기(VMM), 비접촉 측정기, 머신비전 카메라와 검사 소프트웨어를 산업 현장에 공급합니다. Vision Engineering 한국 총판.",
         ["현미경", "실체현미경", "무접안 현미경", "디지털현미경", "비디오측정기", "VMM", "비접촉측정기", "머신비전", "외관검사", "Vision Engineering", "Mantis", "Lynx EVO"]),
    "about": ("회사소개 | 세일테크노", "1991년 설립, Vision Engineering 한국 총판으로 정밀 광학·측정·검사 장비를 공급해 온 ㈜세일테크노의 연혁, 조직, 주요 고객과 사업장을 소개합니다.", ["회사소개", "Vision Engineering 총판"]),
    "cases": ("적용사례 | 세일테크노", "현미경·측정기·머신비전 장비의 산업별 적용 사례, 애플리케이션 노트와 기술 칼럼을 모았습니다.", ["적용사례", "애플리케이션 노트", "검사 사례"]),
    "support": ("고객지원 · 자료실 | 세일테크노", "견적·데모·샘플 테스트 문의, 제품 브로셔·데이터시트·사용설명서·소프트웨어 자료실, 프리젠테이션, 오시는 길 안내.", ["견적 문의", "데모", "샘플 테스트", "브로셔", "데이터시트", "사용설명서"]),
    "products/microscope": ("현미경 — 무접안 실체현미경·디지털현미경 | 세일테크노", "접안렌즈 없는 실체현미경(Mantis, Lynx EVO)부터 4K·3D 디지털현미경까지, 검사·작업용 현미경을 소개합니다.", ["실체현미경", "무접안 현미경", "디지털현미경", "4K 현미경", "3D 현미경"]),
    "products/metrology": ("측정 시스템 — 측정 현미경·비디오 측정기(VMM) | 세일테크노", "측정 현미경, 고배율 비접촉 측정기, 비디오 측정기(VMM)로 소형 정밀 부품의 치수를 측정합니다.", ["측정현미경", "비디오측정기", "VMM", "비접촉측정기", "치수측정"]),
    "products/ai-inspection": ("AI 검사·측정 | 세일테크노", "하이브리드 검사·측정, 기상(가공기 내) AI 분석과 비전 검사로 공구·가공물을 자동으로 검사합니다.", ["AI 검사", "기상측정", "공구마모 측정", "비전검사"]),
    "products/machine-vision": ("머신비전 — 스마트카메라·비전 소프트웨어 | 세일테크노", "하이크로봇 스마트카메라, 맞춤형 비전 시스템, 자체 개발 비전·측정 소프트웨어와 광학 부품.", ["머신비전", "스마트카메라", "비전센서", "HIKROBOT", "비전 소프트웨어", "외관검사"]),
    "products/3d-sensing": ("3D·특수 센싱 | 세일테크노", "3D 스캐너, 백색광 간섭계, 원샷 3D 측정기, 3D 레이저 측정, 이벤트 카메라 등 특수 센싱 장비.", ["3D 스캐너", "백색광 간섭계", "3D 측정", "레이저 프로파일", "이벤트 카메라"]),
}

def _fm(path):
    t = open(path, encoding="utf-8").read()
    try: return yaml.safe_load(t.split("---", 2)[1]) or {}
    except Exception: return {}

def _clip(s, n=155):
    s = re.sub(r"\s+", " ", re.sub(r"[*_`>#\[\]]", "", str(s or ""))).strip()
    return s if len(s) <= n else s[:n - 1].rstrip() + "…"

def _kw(*lists):
    out = []
    for l in lists:
        for k in (l or []):
            k = str(k).strip()
            if k and k not in out: out.append(k)
    return out[:20]

class SEO:
    def __init__(self, site_dir, domain):
        self.domain = domain.rstrip("/")
        cfg = {}
        try: cfg = yaml.safe_load(open(os.path.join(site_dir, "_config.yml"), encoding="utf-8")) or {}
        except Exception: pass
        self.verify = {"google-site-verification": cfg.get("google_site_verification"), "naver-site-verification": cfg.get("naver_site_verification")}
        self.prod = {os.path.splitext(os.path.basename(f))[0]: _fm(f) for f in glob.glob(os.path.join(site_dir, "_products", "*.md"))}
        self.cases = {os.path.splitext(os.path.basename(f))[0]: _fm(f) for f in glob.glob(os.path.join(site_dir, "_cases", "*.md"))}

    def info(self, url):
        D = self.domain
        img = "/assets/img/home/mantis-story.jpg"; ld = []; kind = "website"
        if url in PAGES:
            title, desc, kw = PAGES[url]; kw = _kw(kw, BASE_KW)
            if url == "":
                ld.append({"@context": "https://schema.org", "@type": "Organization", "name": ORG_NAME, "alternateName": ["세일테크노", "SEIL TECHNO CORP."],
                           "url": D + "/", "foundingDate": "1991", "telephone": "+82-2-2632-3211",
                           "address": {"@type": "PostalAddress", "streetAddress": "당산로2길 12, 에이스테크노타워 806호", "addressLocality": "영등포구", "addressRegion": "서울특별시", "addressCountry": "KR"}})
                ld.append({"@context": "https://schema.org", "@type": "WebSite", "name": "세일테크노", "url": D + "/"})
        elif url.startswith("products/") and url[9:] in self.prod:
            p = self.prod[url[9:]]; kind = "product"
            sub = p.get("subcategory") or ""
            title = f'{p.get("title","")} {sub} | 세일테크노'.replace("  ", " ")
            desc = _clip(f'{p.get("title","")} — {p.get("subtitle","")}. {p.get("summary","")}')
            kw = _kw(p.get("keywords"), [p.get("title"), p.get("brand"), sub, p.get("category")], p.get("tags"), (p.get("applications") or [])[:6], BASE_KW)
            if p.get("image"): img = p["image"]
            ld.append({"@context": "https://schema.org", "@type": "Product", "name": p.get("title"), "description": _clip(p.get("summary"), 300),
                       "category": " > ".join(x for x in [p.get("category"), sub] if x), "image": D + img,
                       **({"brand": {"@type": "Brand", "name": p["brand"]}} if p.get("brand") else {})})
            ld.append(self._crumbs([("제품소개", None), (p.get("category"), None), (p.get("title"), url)]))
        elif url.startswith("cases/") and url[6:] in self.cases:
            c = self.cases[url[6:]]; kind = "article"
            title = f'{c.get("title","")} | 적용사례 | 세일테크노'
            desc = _clip(c.get("excerpt") or c.get("title"))
            kw = _kw(c.get("keywords"), [c.get("industry"), c.get("maker")], c.get("products"), ["적용사례"], BASE_KW)
            if c.get("image"): img = c["image"]
            ld.append({"@context": "https://schema.org", "@type": "Article", "headline": c.get("title"), "description": desc, "image": D + img,
                       "publisher": {"@type": "Organization", "name": ORG_NAME}})
        else:
            return None
        return dict(title=title, desc=desc, kw=kw, img=img if img.startswith("http") else D + img, url=f"{D}/{url}", kind=kind, ld=ld)

    def _crumbs(self, items):
        return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, **({"item": f"{self.domain}/{u}"} if u else {})} for i, (n, u) in enumerate(items) if n]}

    def apply(self, html, url):
        i = self.info(url)
        if not i: return html
        a = lambda s: _h.escape(str(s), quote=True)
        tags = [f'<meta name="description" content="{a(i["desc"])}">',
                f'<meta name="keywords" content="{a(", ".join(i["kw"]))}">',
                f'<link rel="canonical" href="{a(i["url"])}">',
                '<meta property="og:site_name" content="세일테크노">', '<meta property="og:locale" content="ko_KR">',
                f'<meta property="og:type" content="{"article" if i["kind"]=="article" else "website"}">',
                f'<meta property="og:title" content="{a(i["title"])}">', f'<meta property="og:description" content="{a(i["desc"])}">',
                f'<meta property="og:url" content="{a(i["url"])}">', f'<meta property="og:image" content="{a(i["img"])}">',
                '<meta name="twitter:card" content="summary_large_image">']
        if url == "":
            tags += [f'<meta name="{k}" content="{a(v)}">' for k, v in self.verify.items() if v]
        tags += [f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in i["ld"]]
        html = re.sub(r"<title>.*?</title>", lambda m: f"<title>{_h.escape(i['title'])}</title>", html, count=1, flags=re.S)
        return html.replace("</head>", "\n".join(tags) + "\n</head>", 1)
