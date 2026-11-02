# -*- coding: utf-8 -*-
# 고객지원 페이지 (문의·견적 / 샘플 테스트·데모 / 자료실 / 오시는 길) + 사이트 전체 버튼 링크 연결
import urllib.parse as _up
FORM_ENDPOINT = "https://formspree.io/f/myeebykv"   # ← Formspree 가입 후 받은 주소로 바꾸면 문의가 메일로 옵니다
ADDR = "서울특별시 영등포구 당산로2길 12, 에이스테크노타워 806호"
DL_KINDS = [("brochures", "브로셔"), ("datasheets", "데이터시트"), ("manuals", "사용설명서"), ("software", "소프트웨어"), ("technical", "기술자료")]
DL_LABEL = dict(DL_KINDS)

def load_downloads():
    """자료실 목록: _data/downloads.yml(제목·종류·관련 제품·외부 링크) + downloads 폴더의 파일 자동 표시"""
    base = os.path.join(SITE, "assets", "downloads")
    ents, seen = [], set()
    yp = os.path.join(SITE, "_data", "downloads.yml")
    for x in ((yaml.safe_load(open(yp, encoding="utf-8")) or []) if os.path.exists(yp) else []):
        f = str(x.get("file") or "").replace("/assets/downloads/", "").lstrip("/")
        url = str(x.get("url") or "")
        if not f and not url: continue
        kind = x.get("kind") or (f.split("/")[0] if "/" in f else "technical")
        if kind not in DL_LABEL: kind = "technical"
        full = os.path.join(base, f) if f else ""
        if f and not os.path.exists(full): continue
        seen.add(f)
        ext = (os.path.splitext(f)[1][1:].upper() if f else "LINK") or "FILE"
        ents.append({"file": f, "url": url, "kind": kind, "title": x.get("title") or os.path.splitext(os.path.basename(f))[0],
                     "product": x.get("product", "") or "", "lang": x.get("lang", "") or "", "date": str(x.get("date", "") or ""),
                     "size": os.path.getsize(full) if f else 0, "ext": ext})
    for kind, _ in DL_KINDS:
        for fp in sorted(glob.glob(os.path.join(base, kind, "*"))):
            rel = kind + "/" + os.path.basename(fp)
            if os.path.isdir(fp) or os.path.basename(fp).startswith(".") or rel in seen: continue
            ents.append({"file": rel, "url": "", "kind": kind, "title": os.path.splitext(os.path.basename(fp))[0].replace("_", " ").replace("-", " "),
                         "product": "", "lang": "", "date": "", "size": os.path.getsize(fp), "ext": os.path.splitext(fp)[1][1:].upper() or "FILE"})
    return sorted(ents, key=lambda d: (d["date"], d["title"]), reverse=True)

def fsize(n):
    return f"{n/1048576:.1f} MB" if n >= 1048576 else f"{max(1, n//1024)} KB"

SUP_CSS = """
.sp-sec{padding:72px 0;scroll-margin-top:80px}.sp-sec.alt{background:var(--bg)}
.sp-h{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;margin-bottom:28px;flex-wrap:wrap}
.sp-h .eb{font-size:11px;letter-spacing:2.2px;font-weight:800;color:var(--blue)}
.sp-h h2{font-size:30px;letter-spacing:-.7px;color:var(--navy);line-height:1.25}
.sp-h p{color:var(--sub);margin-top:6px;max-width:620px}
.iq{display:grid;grid-template-columns:320px 1fr;gap:28px;align-items:start}
.iq-side{background:var(--navy);color:#fff;border-radius:18px;padding:28px;position:sticky;top:96px}
.iq-side h3{font-size:19px;margin-bottom:6px}.iq-side p{font-size:14px;opacity:.78}
.iq-side dl{margin-top:22px;display:grid;gap:14px}.iq-side dt{font-size:11px;letter-spacing:1.6px;font-weight:800;color:var(--mint)}
.iq-side dd{font-size:17px;font-weight:700}.iq-side dd a:hover{text-decoration:underline}
.iq-side .tip{margin-top:22px;padding-top:18px;border-top:1px solid rgba(255,255,255,.12);font-size:13px;opacity:.75;line-height:1.7}
form.iq-f{background:#fff;border:1px solid var(--line);border-radius:18px;padding:28px;display:grid;grid-template-columns:1fr 1fr;gap:16px 18px}
.iq-f .full{grid-column:1/-1}
.iq-f label{display:flex;flex-direction:column;gap:6px;font-size:13px;font-weight:700;color:var(--ink)}
.iq-f label i{color:#e5484d;font-style:normal}
.iq-f input,.iq-f select,.iq-f textarea{font:inherit;font-size:15px;font-weight:500;padding:12px 14px;border:1px solid #d4dbe6;border-radius:10px;background:#fff;color:var(--ink)}
.iq-f textarea{min-height:140px;resize:vertical}
.iq-f input:focus,.iq-f select:focus,.iq-f textarea:focus{outline:2px solid var(--blue);outline-offset:-1px;border-color:var(--blue)}
.iq-type{display:flex;flex-wrap:wrap;gap:8px}
.iq-type input{position:absolute;opacity:0;pointer-events:none}
.iq-type span{display:inline-block;padding:9px 16px;border-radius:999px;border:1px solid #d4dbe6;font-size:14px;font-weight:700;color:var(--sub);cursor:pointer}
.iq-type input:checked+span{background:var(--navy);border-color:var(--navy);color:#fff}
.iq-type input:focus-visible+span{outline:2px solid var(--blue);outline-offset:2px}
.iq-legend{font-size:13px;font-weight:700;margin-bottom:8px}
.iq-agree{display:flex!important;flex-direction:row!important;align-items:flex-start;gap:10px!important;font-weight:600!important}
.iq-agree input{margin-top:3px;width:18px;height:18px;accent-color:var(--blue)}
.iq-f details{font-size:13px;color:var(--sub);background:var(--bg);border-radius:10px;padding:10px 14px}
.iq-f details summary{cursor:pointer;font-weight:700;color:var(--ink)}
.iq-f details p{margin-top:8px;line-height:1.7}
.iq-f .send{display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.iq-f .send .btn{padding:14px 28px;font-size:15px}
.iq-msg{font-size:14px;font-weight:600;color:#0a8f78}.iq-msg.err{color:#c43d3d}
.sm-steps{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;counter-reset:s}
.sm-steps li{list-style:none;background:#fff;border:1px solid var(--line);border-radius:16px;padding:22px 20px;position:relative}
.sm-steps li:before{counter-increment:s;content:"0" counter(s);font-size:13px;font-weight:800;color:var(--blue)}
.sm-steps h4{font-size:17px;color:var(--navy);margin:8px 0 6px}.sm-steps p{font-size:14px;color:var(--sub)}
.sm-steps li:not(:last-child):after{content:"";position:absolute;right:-10px;top:50%;width:6px;height:6px;border-top:2px solid #b8c4d6;border-right:2px solid #b8c4d6;transform:translateY(-50%) rotate(45deg)}
.sm-ship{margin-top:20px;display:grid;grid-template-columns:1fr auto;gap:20px;align-items:center;background:#fff;border:1px dashed #b8c4d6;border-radius:16px;padding:22px 24px}
.sm-ship b{display:block;font-size:12px;letter-spacing:1.4px;color:var(--blue);margin-bottom:4px}
.sm-ship p{font-size:16px;font-weight:700;color:var(--ink)}.sm-ship small{display:block;color:var(--sub);font-size:13px;margin-top:4px;font-weight:500}
.dl-bar{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:8px}
.dl-chips{display:flex;gap:6px;flex-wrap:wrap}
.dl-chips button{all:unset;cursor:pointer;padding:8px 14px;border-radius:999px;background:#fff;border:1px solid var(--line);font-size:13px;font-weight:700;color:var(--sub)}
.dl-chips button b{margin-left:5px;opacity:.6}.dl-chips button.on{background:var(--navy);border-color:var(--navy);color:#fff}
.dl-chips button:focus-visible{outline:2px solid var(--blue);outline-offset:2px}
.dl-search{margin-left:auto;display:flex;align-items:center;gap:8px;border:1px solid var(--line);background:#fff;border-radius:999px;padding:8px 14px;min-width:240px}
.dl-search input{border:0;outline:0;font:inherit;font-size:14px;flex:1;min-width:0;background:transparent}
.dl-list{list-style:none;background:#fff;border:1px solid var(--line);border-radius:16px;overflow:hidden;margin-top:14px}
.dl-row{display:grid;grid-template-columns:54px 1fr 150px 90px 110px 120px;gap:16px;align-items:center;padding:16px 20px;border-bottom:1px solid var(--line)}
.dl-row:last-child{border-bottom:0}.dl-row[hidden]{display:none}.dl-row:hover{background:#f9fbfd}
.dl-ic{width:44px;height:52px;border-radius:8px;background:#fdecec;color:#c43d3d;font-size:11px;font-weight:800;display:grid;place-items:center;position:relative}
.dl-ic:after{content:"";position:absolute;right:0;top:0;border-style:solid;border-width:0 12px 12px 0;border-color:transparent #fff transparent transparent}
.dl-t b{display:block;font-size:15.5px;color:var(--ink)}.dl-t small{font-size:12px;color:var(--sub)}
.dl-t small a{color:var(--blue);font-weight:700}
.dl-kind{font-size:12px;font-weight:800;color:var(--navy);background:var(--bg);padding:4px 10px;border-radius:5px;justify-self:start}
.dl-row .meta{font-size:13px;color:var(--sub);font-variant-numeric:tabular-nums}
.dl-row .btn{justify-content:center;padding:9px 14px}
.dl-empty{padding:40px;text-align:center;color:var(--sub)}
.dl-note{font-size:13px;color:var(--sub);margin-top:14px}
.loc{display:grid;grid-template-columns:1.4fr 1fr;gap:24px}
.loc-map{border-radius:18px;overflow:hidden;border:1px solid var(--line);min-height:380px;background:#e9eef5;position:relative}
.loc-map iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.loc-card{background:#fff;border:1px solid var(--line);border-radius:18px;padding:26px}
.loc-card h3{font-size:20px;color:var(--navy);margin-bottom:4px}.loc-card .ad{font-size:15px;font-weight:600}
.loc-card dl{display:grid;grid-template-columns:72px 1fr;gap:12px 10px;margin:20px 0;font-size:15px}.loc-card dt{color:var(--sub)}.loc-card dd{font-weight:700}
.loc-card .maps{display:flex;gap:8px;flex-wrap:wrap}
@media(max-width:900px){.iq{grid-template-columns:1fr}.iq-side{position:static}form.iq-f{grid-template-columns:1fr;padding:20px}.sm-steps{grid-template-columns:1fr 1fr}.sm-steps li:after{display:none}.sm-ship{grid-template-columns:1fr}
.dl-row{grid-template-columns:44px 1fr;gap:6px 14px}.dl-row .dl-kind,.dl-row .meta{grid-column:2}.dl-row .meta{display:inline}.dl-row .btn{grid-column:1/-1}.dl-search{margin-left:0;width:100%}.loc{grid-template-columns:1fr}.loc-map{min-height:300px}}
"""
SUP_ICONS = {
 "inquiry": '<path d="M4 5h16v11H8l-4 4z"/><path d="M8 9.5h8M8 12.5h5"/>',
 "sample": '<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 1.8 3h10.4A2 2 0 0 0 19 18l-5-9V3"/><path d="M7.5 15h9"/>',
 "downloads": '<path d="M12 3v12M7 10l5 5 5-5"/><path d="M4 17v3h16v-3"/>',
 "location": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
}

def build_support(items):
    root = ""
    dls = load_downloads()
    pidx = {d["slug"]: d for d in items}
    cards = [("inquiry", "견적·문의", "INQUIRY", "장비 견적과 기술 상담"), ("sample", "샘플 테스트·데모", "SAMPLE TEST", "시료 측정, 방문 시연"),
             ("downloads", "자료실", "DOWNLOADS", f"브로셔·설명서 {len(dls)}건"), ("location", "오시는 길", "LOCATION", "본사 위치·연락처")]
    tiles = "".join(f'<a class="dk" href="#{k}"><div class="dk-top"><span class="dk-ic"><svg viewBox="0 0 24 24" aria-hidden="true">{SUP_ICONS[k]}</svg></span><span class="dk-n">{i+1:02d}</span></div>'
                    f'<div><div class="dk-name">{n}</div><div class="dk-en">{en}</div></div><div class="dk-cnt">{ds}</div></a>' for i, (k, n, en, ds) in enumerate(cards))
    hero = (f'<style>{CAT_CSS}</style><section class="hero hx"><div class="wrap hx-body" style="padding-bottom:30px"><div class="hx-num" aria-hidden="true">CS</div><div><div class="crumb">홈 › 고객지원</div>'
            f'<div class="hx-eb">CUSTOMER SUPPORT</div><h1>고객지원</h1><p class="hx-desc">견적과 기술 상담, 샘플 테스트, 제품 자료까지. 필요한 것을 바로 찾으실 수 있도록 모았습니다.</p></div></div>'
            f'<nav class="deck" aria-label="고객지원 메뉴" style="border-bottom:0;border-top:1px solid rgba(255,255,255,.08)"><div class="wrap"><div class="deck-row" style="grid-template-columns:repeat(4,1fr)">{tiles}</div></div></nav></section>')
    # 관심 제품 select
    opts = '<option value="">선택 안 함 / 잘 모르겠음</option>'
    for c in CATS:
        g = [d for d in items if d["category"] == c]
        if g: opts += f'<optgroup label="{e(c)}">' + "".join(f'<option value="{d["slug"]}">{e(d["title"])}</option>' for d in sorted(g, key=lambda d: d.get("order", 0))) + "</optgroup>"
    opts += '<option value="custom">맞춤형 구성 상담</option>'
    types = [("quote", "견적 요청"), ("consult", "기술 상담"), ("sample", "샘플 테스트"), ("demo", "데모·방문 시연"), ("etc", "기타")]
    tradio = "".join(f'<label><input type="radio" name="문의유형" value="{v}" data-k="{k}"{" checked" if i==0 else ""}><span>{v}</span></label>' for i, (k, v) in enumerate(types))
    inquiry = f"""<section class="sp-sec" id="inquiry"><div class="wrap"><div class="sp-h"><div><div class="eb">01 · INQUIRY</div><h2>견적·문의</h2><p>궁금한 장비와 측정하려는 대상을 알려 주시면 담당 엔지니어가 확인 후 연락드립니다.</p></div></div>
<div class="iq"><aside class="iq-side"><h3>전화로 바로 상담</h3><p>급한 문의는 전화나 메일로 연락 주세요.</p>
<dl><div><dt>TEL</dt><dd><a href="tel:0226323211">02-2632-3211</a></dd></div><div><dt>FAX</dt><dd>02-2632-3214</dd></div><div><dt>E-MAIL</dt><dd><a href="mailto:seil@stvision.co.kr">seil@stvision.co.kr</a></dd></div></dl>
<div class="tip">측정할 제품의 사진이나 도면이 있으면 메일로 함께 보내 주세요. 더 정확하게 장비를 제안해 드릴 수 있습니다.</div></aside>
<form class="iq-f" id="iqForm" action="{FORM_ENDPOINT}" method="POST">
<div class="full"><div class="iq-legend">문의 유형</div><div class="iq-type" role="radiogroup" aria-label="문의 유형">{tradio}</div></div>
<label><span>회사명 <i>*</i></span><input name="회사명" required autocomplete="organization"></label>
<label><span>담당자 성함 <i>*</i></span><input name="담당자" required autocomplete="name"></label>
<label><span>연락처 <i>*</i></span><input name="연락처" type="tel" required autocomplete="tel" placeholder="010-0000-0000"></label>
<label><span>이메일 <i>*</i></span><input name="email" type="email" required autocomplete="email"></label>
<label class="full"><span>관심 제품</span><select name="관심제품" id="iqProduct">{opts}</select></label>
<label class="full"><span>문의 내용 <i>*</i></span><textarea name="문의내용" required placeholder="예) 측정 대상(제품·크기·재질), 보고 싶은 것(치수·외관·높이 등), 필요한 정밀도, 수량, 희망 일정"></textarea></label>
<div class="full"><details><summary>개인정보 수집·이용 안내</summary><p>수집 항목: 회사명, 담당자 성함, 연락처, 이메일, 문의 내용<br>이용 목적: 문의에 대한 답변 및 상담, 견적 제공<br>보유 기간: 문의 처리 완료 후 1년 (관계 법령에 따라 보존이 필요한 경우 그 기간)<br>전송 방식: 입력하신 내용은 양식 전송 서비스(Formspree, 미국)를 거쳐 당사 메일로 전달됩니다.<br>동의를 거부할 수 있으며, 이 경우 문의 접수가 제한됩니다.</p></details></div>
<label class="full iq-agree"><input type="checkbox" required name="개인정보동의" value="동의">개인정보 수집·이용에 동의합니다. <i>*</i></label>
<div class="full send"><button class="btn btn-primary" type="submit">문의 보내기</button><span class="iq-msg" id="iqMsg" role="status" aria-live="polite"></span></div>
<input type="hidden" name="_subject" value="[홈페이지 문의] 세일테크노"><input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px;opacity:0"></form></div></div></section>"""
    sample = f"""<section class="sp-sec alt" id="sample"><div class="wrap"><div class="sp-h"><div><div class="eb">02 · SAMPLE TEST &amp; DEMO</div><h2>샘플 테스트·데모</h2><p>장비를 고르기 전에 실제 시료로 확인해 보세요. 측정 결과를 보고 결정하시면 됩니다.</p></div>
<a class="btn btn-primary" href="#inquiry" data-settype="sample">샘플 테스트 신청</a></div>
<ol class="sm-steps"><li><h4>상담·접수</h4><p>문의 양식이나 전화로 측정 대상과 목적을 알려 주세요.</p></li>
<li><h4>시료 보내기</h4><p>시료를 택배로 보내시거나 직접 가져오셔도 됩니다.</p></li>
<li><h4>측정·분석</h4><p>알맞은 장비로 측정하고 반복성까지 확인합니다.</p></li>
<li><h4>결과 리포트·시연</h4><p>결과를 리포트로 보내 드리고, 원하시면 방문 시연을 진행합니다.</p></li></ol>
<div class="sm-ship"><div><b>시료 보내실 곳</b><p>{ADDR}</p><small>받는 분: ㈜세일테크노 기술영업부 · 02-2632-3211 · 보내시기 전에 먼저 연락 주시면 빠르게 처리됩니다.</small></div>
<a class="btn btn-ghost" href="#inquiry" data-settype="demo">방문 시연 예약</a></div></div></section>"""
    kchips = f'<button class="on" data-v="all" aria-pressed="true">전체<b>{len(dls)}</b></button>' + "".join(
        f'<button data-v="{k}" aria-pressed="false">{v}<b>{sum(1 for d in dls if d["kind"]==k)}</b></button>' for k, v in DL_KINDS if any(d["kind"] == k for d in dls))
    rows = ""
    for d in dls:
        p = pidx.get(d["product"])
        plink = f' · 관련 제품 <a href="{root}상세/{p["slug"]}.html">{e(p["title"])}</a>' if p else ""
        q = (d["title"] + " " + (p["title"] if p else "") + " " + d["file"]).lower()
        rows += (f'<li class="dl-row" data-k="{d["kind"]}" data-q="{e(q)}"><span class="dl-ic">{e(d["ext"])}</span>'
                 f'<div class="dl-t"><b>{e(d["title"])}</b><small>{e(d["lang"] or "")}{plink}</small></div><span class="dl-kind">{DL_LABEL[d["kind"]]}</span>'
                 f'<span class="meta">{fsize(d["size"]) if d["size"] else "외부 링크"}</span><span class="meta">{e(d["date"].replace("-", "."))}</span>'
                 + (f'<a class="btn btn-ghost" href="{e(d["url"])}" target="_blank" rel="noopener">열기 ↗</a></li>' if d["url"] and not d["file"] else
                    f'<a class="btn btn-ghost" href="{img(root, "/assets/downloads/" + d["file"])}" target="_blank" rel="noopener" download>내려받기 ↓</a></li>'))
    downloads = f"""<section class="sp-sec" id="downloads"><div class="wrap"><div class="sp-h"><div><div class="eb">03 · DOWNLOADS</div><h2>자료실</h2><p>제품 브로셔, 데이터시트, 사용설명서를 내려받으실 수 있습니다.</p></div></div>
<div class="dl-bar"><div class="dl-chips" id="dlF" role="group" aria-label="자료 종류">{kchips}</div><label class="dl-search"><span aria-hidden="true">🔍</span><input id="dlQ" type="search" placeholder="제품명·자료 이름 검색" aria-label="자료 검색"></label></div>
<ul class="dl-list">{rows}</ul><div class="dl-empty" id="dlE" hidden>찾는 자료가 없습니다. 문의 주시면 보내 드립니다.</div>
<p class="dl-note">※ 찾으시는 자료가 없으면 문의 양식이나 메일로 요청해 주세요.</p></div></section>"""
    qa = _up.quote(ADDR.split(",")[0])
    location = f"""<section class="sp-sec alt" id="location"><div class="wrap"><div class="sp-h"><div><div class="eb">04 · LOCATION</div><h2>오시는 길</h2></div></div>
<div class="loc"><div class="loc-map"><iframe title="세일테크노 위치 지도" loading="lazy" src="https://www.google.com/maps?q={qa}&amp;output=embed"></iframe></div>
<div class="loc-card"><h3>㈜세일테크노</h3><p class="ad">{ADDR}</p>
<dl><dt>대표전화</dt><dd><a href="tel:0226323211">02-2632-3211</a></dd><dt>팩스</dt><dd>02-2632-3214</dd><dt>이메일</dt><dd><a href="mailto:seil@stvision.co.kr">seil@stvision.co.kr</a></dd></dl>
<div class="maps"><a class="btn btn-ghost" href="https://map.naver.com/p/search/{qa}" target="_blank" rel="noopener">네이버 지도 ↗</a><a class="btn btn-ghost" href="https://map.kakao.com/?q={qa}" target="_blank" rel="noopener">카카오맵 ↗</a></div>
<p style="font-size:13px;color:var(--sub);margin-top:16px">방문 시연은 미리 예약해 주시면 장비를 준비해 두겠습니다.</p></div></div></div></section>"""
    js = """<script>(function(){
var f=document.getElementById('iqForm'),msg=document.getElementById('iqMsg'),sel=document.getElementById('iqProduct');
var ps=new URLSearchParams(location.search);if(ps.get('product')){sel.value=ps.get('product')}
function setType(k){var r=f.querySelector('input[data-k="'+k+'"]');if(r)r.checked=true}
if(ps.get('type'))setType(ps.get('type'));
[].forEach.call(document.querySelectorAll('[data-settype]'),function(a){a.addEventListener('click',function(){setType(a.dataset.settype)})});
f.addEventListener('submit',function(ev){ev.preventDefault();msg.className='iq-msg';
 if(f.action.indexOf('your-form-id')>-1){msg.textContent='시안에서는 전송되지 않습니다. (홈페이지 공개 시 메일로 전송되도록 연결합니다)';return}
 msg.textContent='보내는 중…';fetch(f.action,{method:'POST',body:new FormData(f),headers:{Accept:'application/json'}}).then(function(r){
  if(r.ok){f.reset();msg.textContent='문의가 접수되었습니다. 확인 후 연락드리겠습니다.'}else{throw 0}}).catch(function(){msg.className='iq-msg err';msg.textContent='전송에 실패했습니다. 02-2632-3211 또는 seil@stvision.co.kr로 연락 부탁드립니다.'})});
var bs=[].slice.call(document.querySelectorAll('#dlF button')),rows=[].slice.call(document.querySelectorAll('.dl-row')),k='all',q='';
function r(){var n=0;rows.forEach(function(x){var ok=(k==='all'||x.dataset.k===k)&&(!q||x.dataset.q.indexOf(q)>-1);x.hidden=!ok;if(ok)n++});document.getElementById('dlE').hidden=n>0}
bs.forEach(function(b){b.addEventListener('click',function(){bs.forEach(function(x){x.classList.remove('on');x.setAttribute('aria-pressed','false')});b.classList.add('on');b.setAttribute('aria-pressed','true');k=b.dataset.v;r()})});
var qi=document.getElementById('dlQ');qi.addEventListener('input',function(){q=this.value.trim().toLowerCase();r()});
if(ps.get('q')){qi.value=ps.get('q');q=ps.get('q').toLowerCase();r()}
})();</script>"""
    inner = hero + f"<style>{SUP_CSS}</style>" + inquiry + sample + downloads + location + js
    open(os.path.join(HERE, "고객지원.html"), "w", encoding="utf-8").write(page("고객지원 | 세일테크노", inner, root, active="support", cta=False))
    return dls

def fix_links(items, dls):
    """만들어진 모든 시안 HTML의 빈 버튼(href="#")을 고객지원 페이지로 연결합니다."""
    bro = {}
    for d in sorted(dls, key=lambda d: (d["kind"] != "brochures", d["kind"] != "datasheets")):
        if d["product"] and d["product"] not in bro: bro[d["product"]] = d
    slugs = {d["slug"] for d in items}
    for fp in glob.glob(os.path.join(HERE, "*.html")) + glob.glob(os.path.join(HERE, "상세", "*.html")) + glob.glob(os.path.join(HERE, "상세", "cases", "*.html")):
        rel = os.path.relpath(fp, HERE); depth = rel.count(os.sep); root = "../" * depth
        slug = os.path.splitext(os.path.basename(fp))[0] if depth == 1 and os.path.splitext(os.path.basename(fp))[0] in slugs else ""
        s = open(fp, encoding="utf-8").read(); o = s
        sup = root + "고객지원.html"
        pq = f"?product={slug}" if slug else ""
        amp = "&amp;" if slug else "?"
        s = s.replace('href="#">고객지원</a>', f'href="{sup}">고객지원</a>')
        s = re.sub(r'href="#"(\s*)>(견적·데모 문의|견적 문의)<', lambda m: f'href="{sup}{pq}#inquiry"{m.group(1)}>{m.group(2)}<', s)
        s = re.sub(r'href="#"(\s*)>(데모 신청|데모 문의)<', lambda m: f'href="{sup}{pq}{amp}type=demo#inquiry"{m.group(1)}>{m.group(2)}<', s)
        s = re.sub(r'href="#"(\s*)>(샘플 테스트 의뢰|샘플 테스트 신청)<', lambda m: f'href="{sup}{pq}{amp}type=sample#inquiry"{m.group(1)}>{m.group(2)}<', s)
        s = re.sub(r'href="#"(\s*)>(기술 상담|맞춤 구성 상담|이 사례로 상담하기)<', lambda m: f'href="{sup}?type=consult#inquiry"{m.group(1)}>{m.group(2)}<', s)
        s = s.replace('href="#">데모 신청 <i', f'href="{sup}?type=demo#inquiry">데모 신청 <i')
        s = s.replace('href="#">02-2632-3211<', 'href="tel:0226323211">02-2632-3211<')
        if slug and slug in bro:
            b = bro[slug]; bl = img(root, "/assets/downloads/" + b["file"]) if b["file"] else b["url"]
            s = s.replace('href="#">브로셔 PDF<', f'href="{bl}" target="_blank" rel="noopener">브로셔 PDF ↓<')
        else:
            s = s.replace('href="#">브로셔 PDF<', f'href="{sup}#downloads">자료실<')
        if s != o: open(fp, "w", encoding="utf-8").write(s)
