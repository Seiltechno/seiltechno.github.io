# -*- coding: utf-8 -*-
# 적용사례 게시판 (build_preview.py 안에서 실행됩니다)
TYPES = [("case", "고객 사례", "Case Study"), ("appnote", "애플리케이션 노트", "Application Note"), ("article", "기술 칼럼", "Article")]
TLABEL = {k: v for k, v, _ in TYPES}
PMAP = [("mantis", "mantis"), ("lynx evo", "lynx-evo"), ("swift pro edge", "edge-series"), ("edge series", "edge-series"),
        ("swift pro", "swift-pro"), ("tvm", "tvm-series"), ("hawk", "hawk"), ("drv stereo cam", "drv-stereo-cam"),
        ("drv-z1", "drv-z1"), ("opta", "opta"), ("evo cam halo", "evocam-aura-4k")]
def prod_slug(name):
    n = name.lower()
    for k, s in PMAP:
        if n.startswith(k): return s
    return None

def load_cases():
    out = []
    for f in glob.glob(os.path.join(SITE, "_cases", "*.md")):
        t = open(f, encoding="utf-8").read()
        _, fm, body = t.split("---", 2)
        d = yaml.safe_load(fm); d["slug"] = os.path.splitext(os.path.basename(f))[0]; d["body"] = body.strip()
        d["date"] = str(d.get("date") or "")
        d["seil"] = d.get("maker") == "세일테크노"
        out.append(d)
    return sorted(out, key=lambda d: (d["date"][:7], -int(d.get("order") or 0)), reverse=True)

def cdate(d): return d["date"][:7].replace("-", ".")

def case_img(root, d, cls=""):
    if not d.get("image"):
        return f'<div class="cs-noimg {cls}"><span>{MARK}</span>사진 준비 중</div>'
    fb = f' onerror="this.onerror=null;this.src=\'{e(d["image_src"])}\'"' if d.get("image_src") else ""
    return f'<img class="{cls}" loading="lazy" src="{img(root, d["image"])}"{fb} alt="{e(d["title"])}">'

CASE_CSS = """
.cs-hero{background:linear-gradient(120deg,var(--navy),var(--navy2));color:#fff;padding:56px 0 0;position:relative;overflow:hidden}
.cs-hero:before{content:"";position:absolute;right:-120px;top:-160px;width:520px;height:520px;border-radius:50%;border:1px solid rgba(255,255,255,.08);box-shadow:0 0 0 60px rgba(255,255,255,.025),0 0 0 140px rgba(255,255,255,.02)}
.cs-hero h1{font-size:38px;letter-spacing:-.8px}.cs-hero p{opacity:.85;margin-top:8px;max-width:640px}
.cs-stats{display:flex;gap:40px;margin-top:28px;flex-wrap:wrap}
.cs-stats div{font-size:13px;opacity:.8}.cs-stats b{display:block;font-size:30px;font-weight:800;color:var(--mint);opacity:1;line-height:1.2;font-variant-numeric:tabular-nums}
.cs-tabs{display:flex;gap:4px;margin-top:36px;overflow-x:auto;scrollbar-width:none}
.cs-tabs button{all:unset;cursor:pointer;padding:14px 20px;font-weight:700;font-size:15px;color:rgba(255,255,255,.72);border-radius:12px 12px 0 0;white-space:nowrap}
.cs-tabs button b{font-size:12px;margin-left:6px;opacity:.7}
.cs-tabs button.on{background:#fff;color:var(--navy)}.cs-tabs button.seil{color:var(--mint)}.cs-tabs button.seil.on{color:var(--navy)}
.cs-tabs button:focus-visible{outline:2px solid var(--mint)}
.cs-bar{display:flex;gap:12px;align-items:center;flex-wrap:wrap;padding:22px 0;border-bottom:1px solid var(--line)}
.cs-bar .lbl{font-size:12px;font-weight:800;color:var(--sub);letter-spacing:.5px;margin-right:2px}
.cs-chips{display:flex;gap:6px;flex-wrap:wrap}
.cs-chips button{all:unset;cursor:pointer;padding:6px 12px;border-radius:999px;background:var(--bg);font-size:13px;font-weight:600;color:var(--sub)}
.cs-chips button.on{background:var(--navy);color:#fff}.cs-chips button:hover{background:#e3eaf5}.cs-chips button.on:hover{background:var(--navy)}
.cs-search{margin-left:auto;display:flex;align-items:center;gap:8px;border:1px solid var(--line);border-radius:999px;padding:8px 14px;min-width:240px}
.cs-search input{border:0;outline:0;font:inherit;font-size:14px;flex:1;min-width:0;background:transparent}
.cs-count{font-size:14px;color:var(--sub);padding:18px 0 4px}.cs-count b{color:var(--navy)}
.cs-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:22px;padding:14px 0 8px}
.cs-card{background:#fff;border:1px solid var(--line);border-radius:16px;overflow:hidden;display:flex;flex-direction:column;transition:.2s}
.cs-card:hover{transform:translateY(-3px);box-shadow:0 12px 28px rgba(27,43,75,.12);border-color:#c9d6ea}
.cs-card[hidden]{display:none}
.cs-thumb{aspect-ratio:16/10;background:var(--bg);position:relative;overflow:hidden}
.cs-thumb img{width:100%;height:100%;object-fit:cover;transition:transform .5s}.cs-card:hover .cs-thumb img{transform:scale(1.04)}
.cs-type{position:absolute;left:12px;top:12px;font-size:11px;font-weight:800;padding:4px 9px;border-radius:5px;background:rgba(255,255,255,.95);color:var(--navy);letter-spacing:.2px}
.cs-type.case{background:var(--mint);color:var(--navy)}.cs-type.appnote{background:var(--blue);color:#fff}
.cs-type.seil{background:var(--navy);color:var(--mint)}
.cs-draft{position:absolute;right:12px;top:12px;font-size:11px;font-weight:800;padding:4px 9px;border-radius:5px;background:#ffb020;color:#3a2600}
.cs-body{padding:18px 20px 20px;display:flex;flex-direction:column;gap:6px;flex:1}
.cs-maker{font-size:12px;font-weight:700;color:var(--blue)}.cs-maker.seil{color:#0a8f78}
.cs-card h3{font-size:18px;line-height:1.4;letter-spacing:-.3px;color:var(--ink)}
.cs-ex{font-size:14px;color:#3a4356;flex:1}
.cs-meta{display:flex;gap:6px 10px;flex-wrap:wrap;font-size:12px;color:var(--sub);margin-top:8px;padding-top:12px;border-top:1px dashed var(--line)}
.cs-meta span+span:before{content:"·";margin-right:10px;opacity:.6}
.cs-noimg{width:100%;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;color:#8a94a6;font-size:13px;font-weight:600;background:linear-gradient(135deg,#eef3fa,#e6f7f3)}
.cs-noimg .seil-mark{width:46px;height:46px;color:#b9c6d8}
.cs-more{display:flex;justify-content:center;padding:26px 0 10px}
.cs-empty{padding:60px 0;text-align:center;color:var(--sub)}
.cs-seilband{margin:40px 0 0;border-radius:18px;background:linear-gradient(110deg,#0f2440,#1B2B4B 60%,#163a52);color:#fff;padding:30px 34px;display:grid;grid-template-columns:1fr auto;gap:20px;align-items:center}
.cs-seilband h3{font-size:22px;letter-spacing:-.4px}.cs-seilband h3 em{font-style:normal;color:var(--mint)}
.cs-seilband p{opacity:.8;font-size:14px;margin-top:6px;max-width:620px}
.cs-seilband .actions{display:flex;gap:8px;flex-wrap:wrap}
/* 상세 */
.cd-head{background:linear-gradient(120deg,var(--navy),var(--navy2));color:#fff;padding:44px 0 120px}
.cd-head .crumb a:hover{text-decoration:underline}
.cd-tags{display:flex;gap:8px;flex-wrap:wrap;margin:14px 0 14px}
.cd-tags span{font-size:12px;font-weight:800;padding:4px 10px;border-radius:5px;background:rgba(255,255,255,.12)}
.cd-tags .t-case{background:var(--mint);color:var(--navy)}.cd-tags .t-appnote{background:var(--blue)}.cd-tags .t-seil{background:#fff;color:var(--navy)}
.cd-head h1{font-size:34px;line-height:1.35;letter-spacing:-.8px;max-width:880px}
.cd-en{opacity:.6;font-size:14px;margin-top:10px;max-width:880px}
.cd-wrap{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:40px;margin-top:-84px;position:relative}
.cd-fig{border-radius:18px;overflow:hidden;background:#fff;box-shadow:0 18px 40px rgba(27,43,75,.16);aspect-ratio:16/9}
.cd-fig img{width:100%;height:100%;object-fit:cover;display:block}
.cd-cap{font-size:12px;color:var(--sub);margin-top:10px}
.cd-art{padding:30px 0 10px;font-size:17px;line-height:1.85;color:#283041}
.cd-art p{margin-bottom:1.15em}.cd-art strong{color:var(--navy)}
.cd-art .notice{background:#fff8e6;border-left:4px solid #ffb020;padding:12px 16px;border-radius:6px;font-size:14px;color:#6b5000}
.cd-src{margin-top:18px;padding:16px 18px;border-radius:12px;background:var(--bg);font-size:13px;color:var(--sub)}
.cd-side{display:flex;flex-direction:column;gap:16px;padding-top:0}
.cd-box{background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px}
.cd-box h4{font-size:12px;font-weight:800;letter-spacing:.6px;color:var(--sub);margin-bottom:12px}
.cd-box dl{display:grid;grid-template-columns:64px 1fr;gap:8px 10px;font-size:14px}.cd-box dt{color:var(--sub)}.cd-box dd{font-weight:600}
.cd-prods{display:flex;flex-direction:column;gap:8px}
.cd-prods a,.cd-prods span{display:flex;justify-content:space-between;align-items:center;padding:10px 12px;border-radius:10px;background:var(--bg);font-weight:700;font-size:14px}
.cd-prods a{background:#eaf3ff;color:var(--blue)}.cd-prods a:hover{background:#dbeaff}
.cd-links{display:flex;flex-direction:column;gap:8px}.cd-links .btn{justify-content:center}
.cd-sticky{position:sticky;top:92px;display:flex;flex-direction:column;gap:16px}
.cd-pn{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:30px 0 0}
.cd-pn a{border:1px solid var(--line);border-radius:12px;padding:14px 16px;font-size:14px;font-weight:700}
.cd-pn a small{display:block;font-size:12px;color:var(--sub);font-weight:600;margin-bottom:2px}.cd-pn a:hover{border-color:var(--blue)}
.cd-pn .nx{text-align:right}
.cd-rel{padding:56px 0 0}.cd-rel h2{font-size:22px;color:var(--navy);margin-bottom:6px}
@media(max-width:900px){.cd-wrap{grid-template-columns:1fr;margin-top:-70px}.cd-head h1{font-size:26px}.cs-search{margin-left:0;width:100%}.cs-seilband{grid-template-columns:1fr}.cd-sticky{position:static}}
@media(max-width:600px){.cs-hero h1{font-size:30px}.cs-stats{gap:24px}.cs-stats b{font-size:24px}.cd-art{font-size:16px}.cd-pn{grid-template-columns:1fr}}
"""

def case_card(d, root, hidden=False):
    tcls = "seil" if d["seil"] else d["type"]
    tlab = "세일테크노 사례" if d["seil"] else TLABEL[d["type"]]
    meta = [x for x in [cdate(d), d.get("industry"), d.get("country")] if x]
    attrs = f'data-type="{d["type"]}" data-seil="{1 if d["seil"] else 0}" data-ind="{e(d.get("industry",""))}" data-maker="{e(d.get("maker",""))}" data-q="{e((d["title"]+" "+d.get("title_en","")+" "+d.get("customer","")+" "+" ".join(d.get("products") or [])).lower())}"'
    return f"""<a class="cs-card" href="{root}상세/cases/{d['slug']}.html" {attrs}{' hidden' if hidden else ''}>
<div class="cs-thumb">{case_img(root, d)}<span class="cs-type {tcls}">{tlab}</span>{'<span class="cs-draft">작성 예시</span>' if d.get('draft') else ''}</div>
<div class="cs-body"><div class="cs-maker{' seil' if d['seil'] else ''}">{e(d.get('maker',''))}{' · ' + e(d['customer']) if d.get('customer') and d['type']=='case' else ''}</div>
<h3>{e(d['title'])}</h3><div class="cs-ex">{e(d.get('excerpt',''))}</div>
<div class="cs-meta">{''.join(f'<span>{e(m)}</span>' for m in meta)}</div></div></a>"""

CASE_JS = r"""<script>
(function(){
 var cards=[].slice.call(document.querySelectorAll('.cs-card')),st={type:'all',ind:'all',maker:'all',q:''},PAGE=12,shown=PAGE;
 var more=document.getElementById('csMore'),cnt=document.getElementById('csCnt'),empty=document.getElementById('csEmpty');
 function match(c){
  if(st.type==='seil'){if(c.dataset.seil!=='1')return false}
  else if(st.type!=='all'&&c.dataset.type!==st.type)return false;
  if(st.ind!=='all'&&c.dataset.ind!==st.ind)return false;
  if(st.maker!=='all'&&c.dataset.maker!==st.maker)return false;
  if(st.q&&c.dataset.q.indexOf(st.q)<0)return false;return true}
 function render(){var n=0;cards.forEach(function(c){var m=match(c);if(m)n++;c.hidden=!(m&&n<=shown)});
  cnt.textContent=n;more.hidden=n<=shown;empty.hidden=n>0}
 function group(sel,key){var bs=[].slice.call(document.querySelectorAll(sel+' button'));bs.forEach(function(b){b.addEventListener('click',function(){
  bs.forEach(function(x){x.classList.remove('on');x.setAttribute('aria-pressed','false')});b.classList.add('on');b.setAttribute('aria-pressed','true');
  st[key]=b.dataset.v;shown=PAGE;if(key==='type'){try{history.replaceState(null,'','#'+b.dataset.v)}catch(e){}}render()})});return bs}
 var tabs=group('#csTabs','type');group('#csInd','ind');group('#csMaker','maker');
 document.getElementById('csQ').addEventListener('input',function(){st.q=this.value.trim().toLowerCase();shown=PAGE;render()});
 more.addEventListener('click',function(){shown+=PAGE;render()});
 var h=location.hash.slice(1);tabs.forEach(function(b){if(b.dataset.v===h)b.click()});render();
})();</script>"""

def build_cases(items):
    cs = load_cases()
    pub = [d for d in cs if not (os.environ.get("PUBLISH") and d.get("draft"))]  # 공개용(PUBLISH=1)에서는 draft 제외
    pidx = {d["slug"]: d for d in items}
    n = {k: sum(1 for d in pub if d["type"] == k and not d["seil"]) for k, _, _ in TYPES}
    nseil = sum(1 for d in pub if d["seil"])
    tabs = f'<button class="on" data-v="all" aria-pressed="true">전체<b>{len(pub)}</b></button>' + "".join(
        f'<button data-v="{k}" aria-pressed="false">{v}<b>{sum(1 for d in pub if d["type"]==k)}</b></button>' for k, v, _ in TYPES) + \
        f'<button class="seil" data-v="seil" aria-pressed="false">★ 세일테크노 사례<b>{nseil}</b></button>'
    inds = [i for i in ["전자·PCB", "의료기기", "항공·방산", "자동차", "플라스틱·사출", "정밀가공·금속", "연구·바이오", "식품·농업", "보석·소재", "일반 품질관리"] if any(d.get("industry") == i for d in pub)]
    makers = sorted({d.get("maker", "") for d in pub if d.get("maker")}, key=lambda m: (m != "세일테크노", m))
    chips = lambda arr: '<button class="on" data-v="all" aria-pressed="true">전체</button>' + "".join(f'<button data-v="{e(x)}" aria-pressed="false">{e(x)}</button>' for x in arr)
    grid = "".join(case_card(d, "", i >= 12) for i, d in enumerate(pub))
    inner = f"""<style>{CASE_CSS}</style>
<section class="cs-hero"><div class="wrap"><div class="crumb">홈 › 적용사례</div><h1>적용사례</h1>
<p>현장의 문제를 어떤 장비와 방법으로 풀었는지, 산업별 고객 사례와 기술 자료로 확인해 보세요.</p>
<div class="cs-stats"><div><b>{n['case']}</b>고객 사례</div><div><b>{n['appnote']}</b>애플리케이션 노트</div><div><b>{n['article']}</b>기술 칼럼</div><div><b>{len(inds)}</b>산업 분야</div></div>
<div class="cs-tabs" id="csTabs" role="group" aria-label="자료 유형">{tabs}</div></div></section>
<div class="wrap">
<div class="cs-bar"><span class="lbl">산업</span><div class="cs-chips" id="csInd" role="group" aria-label="산업 분야">{chips(inds)}</div></div>
<div class="cs-bar"><span class="lbl">제조사</span><div class="cs-chips" id="csMaker" role="group" aria-label="제조사">{chips(makers)}</div>
<label class="cs-search"><span aria-hidden="true">🔍</span><input id="csQ" type="search" placeholder="제품명·고객사·키워드 검색" aria-label="적용사례 검색"></label></div>
<div class="cs-count" aria-live="polite">총 <b id="csCnt">{len(pub)}</b>건</div>
<div class="cs-grid">{grid}</div>
<div class="cs-empty" id="csEmpty" hidden>조건에 맞는 사례가 없습니다. 필터를 바꿔 보세요.</div>
<div class="cs-more"><button class="btn btn-ghost" id="csMore">더 보기 ↓</button></div>
<div class="cs-seilband"><div><h3>우리 현장의 문제도 <em>사례</em>가 될 수 있습니다</h3><p>검사·측정 고민을 알려 주시면 시료 테스트부터 장비 구성까지 함께 검토해 드립니다. 해결된 과제는 고객 동의를 받아 세일테크노 사례로 소개합니다.</p></div>
<div class="actions"><a class="btn btn-mint" href="#">샘플 테스트 의뢰</a><a class="btn btn-ghost" href="#">기술 상담</a></div></div>
</div>{CASE_JS}"""
    open(os.path.join(HERE, "적용사례.html"), "w", encoding="utf-8").write(page("적용사례 | 세일테크노", inner, "", active="cases"))
    # 상세
    os.makedirs(os.path.join(HERE, "상세", "cases"), exist_ok=True)
    root = "../../"
    for d in pub:
        same = [x for x in pub if x["type"] == d["type"] and x["seil"] == d["seil"]]
        i = same.index(d); prv = same[i - 1] if i > 0 else None; nxt = same[i + 1] if i + 1 < len(same) else None
        rel = [x for x in pub if x is not d and x.get("industry") == d.get("industry")][:3]
        if len(rel) < 3: rel += [x for x in pub if x is not d and x not in rel and x["type"] == d["type"]][:3 - len(rel)]
        prods = ""
        for p in d.get("products") or []:
            s = prod_slug(p)
            if s and s in pidx: prods += f'<a href="{root}상세/{s}.html">{e(pidx[s]["title"])}<span>→</span></a>'
            else: prods += f'<span>{e(p)}</span>'
        info = [("유형", "세일테크노 사례" if d["seil"] else TLABEL[d["type"]]), ("출처", d.get("maker")), ("고객", d.get("customer")), ("국가", d.get("country")),
                ("산업", d.get("industry")), ("게시", cdate(d)), ("글쓴이", d.get("author"))]
        dl_ = "".join(f"<dt>{k}</dt><dd>{e(v)}</dd>" for k, v in info if v)
        links = ""
        if d.get("original_url"): links += f'<a class="btn btn-ghost" href="{e(d["original_url"])}" target="_blank" rel="noopener">원문 보기 (영문) ↗</a>'
        if d.get("pdf"): links += f'<a class="btn btn-ghost" href="{e(d["pdf"])}" target="_blank" rel="noopener">원문 PDF ↗</a>'
        links += '<a class="btn btn-primary" href="#">이 사례로 상담하기</a>'
        src = "" if d["seil"] else f'<div class="cd-src">이 글은 {e(d.get("maker"))}의 원문을 ㈜세일테크노가 한국어로 요약·정리한 것입니다. 사진 출처: {e(d.get("maker"))}</div>'
        cap = "" if d["seil"] or not d.get("image") else f'<div class="cd-cap">사진: {e(d.get("maker"))}</div>'
        tags = f'<span class="t-{"seil" if d["seil"] else d["type"]}">{"세일테크노 사례" if d["seil"] else TLABEL[d["type"]]}</span>' + (f'<span>{e(d["industry"])}</span>' if d.get("industry") else "") + ('<span style="background:#ffb020;color:#3a2600">작성 예시</span>' if d.get("draft") else "")
        pn = '<div class="cd-pn">' + (f'<a href="{prv["slug"]}.html"><small>← 이전 글</small>{e(prv["title"])}</a>' if prv else "<span></span>") + (f'<a class="nx" href="{nxt["slug"]}.html"><small>다음 글 →</small>{e(nxt["title"])}</a>' if nxt else "") + "</div>"
        inner = f"""<style>{CASE_CSS}</style>
<section class="cd-head"><div class="wrap"><div class="crumb"><a href="{root}index.html">홈</a> › <a href="{root}적용사례.html">적용사례</a> › <a href="{root}적용사례.html#{'seil' if d['seil'] else d['type']}">{"세일테크노 사례" if d["seil"] else TLABEL[d["type"]]}</a></div>
<div class="cd-tags">{tags}</div><h1>{e(d['title'])}</h1>{f'<div class="cd-en">{e(d["title_en"])}</div>' if d.get('title_en') else ''}</div></section>
<div class="wrap"><div class="cd-wrap"><div>
<div class="cd-fig">{case_img(root, d)}</div>{cap}
<article class="cd-art">{md(d['body'])}</article>{src}{pn}</div>
<aside class="cd-side"><div class="cd-sticky">
<div class="cd-box"><h4>사례 정보</h4><dl>{dl_}</dl></div>
{f'<div class="cd-box"><h4>적용 제품</h4><div class="cd-prods">{prods}</div></div>' if prods else ''}
<div class="cd-box cd-links">{links}</div></div></aside></div>
<section class="cd-rel"><h2>함께 보면 좋은 사례</h2><div class="cs-grid">{''.join(case_card(x, root) for x in rel)}</div></section></div>"""
        open(os.path.join(HERE, "상세", "cases", d["slug"] + ".html"), "w", encoding="utf-8").write(page(f"{d['title']} | 적용사례 | 세일테크노", inner, root, active="cases"))
    print("적용사례:", len(pub), "건")
