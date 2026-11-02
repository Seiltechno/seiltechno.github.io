# -*- coding: utf-8 -*-
"""입력 화면(Pages CMS) 설정 파일(.pages.yml)을 만듭니다. 카테고리·소분류를 바꾼 뒤 다시 실행하세요."""
import os, re, yaml
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "build_preview.py"), encoding="utf-8").read()
ns = {"__file__": os.path.join(HERE, "build_preview.py")}
exec(src[:src.index("import urllib.parse")], ns)          # CATCFG(카테고리 설정)만 읽기
exec(open(os.path.join(HERE, "board_build.py"), encoding="utf-8").read().split("BOARD_CSS")[0], ns)
CATCFG = ns["CATCFG"]; CATS = ns["CATS"]
subs = [s for c in CATS if c in CATCFG for s, _, _ in CATCFG[c]["subs"]]
EXCLUDE = ["hybrid-mi.md", "aims-aitcd.md", "aims-aitwm.md", "desktop-3d-scanner.md"]   # 특수 구성 페이지(직접/Claude로 수정)
S = lambda n, l, **k: dict(name=n, label=l, type="string", **k)
T = lambda n, l, **k: dict(name=n, label=l, type="text", **k)
IMG = lambda n, l, **k: dict(name=n, label=l, type="image", options={"media": "images"}, **k)
cfg = {
 "media": [
  {"name": "images", "label": "이미지", "input": "site/assets/img", "output": "/assets/img", "rename": "safe", "categories": ["image"]},
  {"name": "videos", "label": "동영상(가볍게 줄인 mp4)", "input": "site/assets/img/videos", "output": "/assets/img/videos", "rename": "safe", "categories": ["video"]},
  {"name": "downloads", "label": "자료실 파일", "input": "site/assets/downloads", "output": "/assets/downloads", "rename": "safe", "categories": ["document", "compressed", "spreadsheet"]}],
 "content": [
  {"name": "products", "label": "제품", "type": "collection", "path": "site/_products", "format": "yaml-frontmatter",
   "filename": "{file_id}.md", "exclude": EXCLUDE,
   "view": {"fields": ["title", "category", "subcategory", "order"], "primary": "title", "sort": ["category", "order", "title"], "default": {"sort": "order", "order": "asc"}},
   "fields": [
    S("file_id", "파일 이름(영문)", description="처음 만들 때만 사용. 영문 소문자·숫자·하이픈 (예: hikrobot-sc2000). 홈페이지 주소가 됩니다."),
    S("title", "제품명", required=True), S("subtitle", "한 줄 설명"),
    {"name": "category", "label": "카테고리", "type": "select", "required": True, "options": {"values": [c for c in CATS if c in CATCFG]}},
    {"name": "subcategory", "label": "소분류", "type": "select", "required": True, "options": {"values": subs}, "description": "고른 카테고리 안의 소분류를 선택하세요."},
    S("brand", "브랜드(제조사)", description="표기하지 않으려면 비워 두세요."),
    {"name": "order", "label": "표시 순서", "type": "number", "description": "작은 숫자가 앞에 나옵니다. (예: 머신비전 401~)"},
    {"name": "posted", "label": "등록일(게시판형 카테고리)", "type": "date", "options": {"format": "yyyy-MM-dd"}},
    {"name": "published", "label": "홈페이지에 공개", "type": "boolean", "default": True},
    S("badge", "배지(예: NEW)"),
    IMG("image", "대표 사진", required=True),
    {"name": "image_fit", "label": "대표 사진 채우기", "type": "select", "options": {"values": ["", "cover"]}, "description": "사진을 칸에 꽉 채우려면 cover"},
    {"name": "gallery", "label": "추가 사진", "type": "image", "options": {"media": "images", "multiple": True}},
    T("summary", "요약(2~3문장)", required=True),
    S("tags", "핵심 키워드(3개)", list=True),
    {"name": "highlights", "label": "주요 특징", "type": "object", "list": True, "fields": [S("title", "제목"), T("text", "설명")]},
    {"name": "specs", "label": "사양", "type": "object", "list": True, "fields": [S("label", "항목"), S("value", "내용")]},
    S("applications", "적용 분야", list=True),
    {"name": "models", "label": "모델 구성", "type": "object", "list": True, "fields": [S("name", "모델명"), T("text", "설명")]},
    {"name": "process", "label": "작동 과정", "type": "object", "list": True, "fields": [IMG("img", "사진"), S("step", "단계(예: STEP 01)"), S("title", "제목"), T("text", "설명")]},
    S("samples_title", "갤러리 제목"), S("samples_tab", "갤러리 탭 이름"), S("samples_desc", "갤러리 설명"),
    {"name": "samples", "label": "갤러리 사진", "type": "object", "list": True, "fields": [IMG("full", "사진"), IMG("thumb", "작은 사진(없으면 같은 사진)"), S("cap", "설명"), S("tag", "분류")]},
    S("videos_title", "영상 구역 제목"), S("videos_tab", "영상 탭 이름"), S("videos_desc", "영상 구역 설명"),
    {"name": "videos", "label": "영상", "type": "object", "list": True, "fields": [
        {"name": "src", "label": "영상 파일(mp4)", "type": "file", "options": {"media": "videos"}}, IMG("poster", "미리보기 사진"),
        S("title", "제목"), T("desc", "설명"), S("cap", "한 줄 설명(제목 대신)")]},
    {"name": "stats", "label": "실측 검증 숫자", "type": "object", "fields": [S("title", "제목"), T("sub", "설명"),
        {"name": "items", "label": "숫자 칸", "type": "object", "list": True, "fields": [S("num", "숫자"), S("unit", "단위"), S("label", "설명")]}, T("note", "주석")]},
    {"name": "partner", "label": "협력사 상자", "type": "object", "fields": [S("name", "회사명"), S("desc", "설명"), S("url", "홈페이지 주소"), IMG("logo", "로고")]},
    S("series", "시리즈명"), S("formerly", "이전 모델명"), S("gallery_note", "사진 아래 안내"),
    {"name": "body", "label": "제품 소개(본문)", "type": "rich-text", "options": {"format": "markdown", "media": "images"}}]},
  {"name": "cases", "label": "적용사례", "type": "collection", "path": "site/_cases", "format": "yaml-frontmatter",
   "filename": "{file_id}.md",
   "view": {"fields": ["title", "type", "maker", "date"], "primary": "title", "sort": ["date", "title"], "default": {"sort": "date", "order": "desc"}},
   "fields": [
    S("file_id", "파일 이름(영문)", description="처음 만들 때만 사용. 예: seil-2026-pcb-flatness"),
    S("title", "제목", required=True), S("title_en", "원문 제목(영문, 선택)"),
    {"name": "type", "label": "유형", "type": "select", "required": True, "options": {"values": [{"name": "case", "label": "고객 사례"}, {"name": "appnote", "label": "애플리케이션 노트"}, {"name": "article", "label": "기술 칼럼"}]}},
    S("maker", "출처·제조사", description="세일테크노 사례는 '세일테크노'라고 적으면 '★ 세일테크노 사례'로 분류됩니다."),
    S("date", "게시 연월", description="예: 2026-11"),
    S("author", "글쓴이"), S("customer", "고객(공개 동의 없으면 '○○ 제조사 (비공개)')"), S("country", "국가"),
    {"name": "industry", "label": "산업", "type": "select", "options": {"values": ["전자·PCB", "의료기기", "항공·방산", "자동차", "플라스틱·사출", "정밀가공·금속", "연구·바이오", "식품·농업", "보석·소재", "일반 품질관리"]}},
    S("products", "관련 제품명", list=True),
    IMG("image", "대표 사진"),
    S("original_url", "원문 링크(선택)"), S("pdf", "원문 PDF 링크(선택)"),
    T("excerpt", "목록에 보이는 한 줄 요약(70자 이내)", required=True),
    {"name": "draft", "label": "작성 중(공개 안 함)", "type": "boolean", "default": False},
    {"name": "body", "label": "본문", "type": "rich-text", "options": {"format": "markdown", "media": "images"}}]},
  {"name": "downloads", "label": "자료실", "type": "file", "path": "site/_data/downloads.yml", "format": "yaml", "list": True,
   "fields": [
    S("title", "자료 이름", required=True),
    {"name": "kind", "label": "종류", "type": "select", "required": True, "options": {"values": [{"name": "brochures", "label": "브로셔"}, {"name": "datasheets", "label": "데이터시트"}, {"name": "manuals", "label": "사용설명서"}, {"name": "software", "label": "소프트웨어"}, {"name": "technical", "label": "기술자료"}]}},
    {"name": "file", "label": "파일 올리기 (25MB 이하)", "type": "file", "options": {"media": "downloads"}},
    S("url", "또는 링크 (큰 파일은 구글 드라이브 공유 링크)"),
    S("product", "관련 제품 파일 이름(예: mantis)"),
    {"name": "lang", "label": "언어", "type": "select", "options": {"values": ["한국어", "영어", "기타"]}},
    {"name": "date", "label": "등록일", "type": "date", "options": {"format": "yyyy-MM-dd"}}]}]}
out = os.path.join(HERE, "..", ".pages.yml")
open(out, "w", encoding="utf-8").write("# 입력 화면(Pages CMS) 설정 — make_cms_config.py로 만듭니다.\n" + yaml.safe_dump(cfg, allow_unicode=True, sort_keys=False, width=200))
print("작성:", os.path.normpath(out), "/ 소분류", len(subs), "개")
