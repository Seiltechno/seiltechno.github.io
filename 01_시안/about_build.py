# -*- coding: utf-8 -*-
# 회사소개 (2025 회사소개서 반영) — build_preview.py의 build_about()을 대체합니다
HISTORY = [
 ("1991–2001", "시작", [("1991.07", "세일테크노교역 설립"), ("1993.03", "영국 Vision Engineering 한국 총판매점 계약"), ("1994.04", "㈜세일테크노 법인 전환")]),
 ("2002–2012", "성장 · 제조", [("2002.07", "당산동에서 문래동 사옥으로 확장 이전"), ("2004.03", "영국 X-TEK 한국 특약점"), ("2010.02", "중국 South Optics 한국 특약점"),
   ("2011.05", "자동 납땜 로봇(Auto Solder Robot) Max Korea와 공동 개발, 국내외 판매 시작"), ("2012.03", "자동 납땜 로봇 인라인화, 오므론전장㈜ 납품"),
   ("2012.06", "기업부설연구소 인정 (한국산업기술진흥협회)"), ("2012.06", "삼성전기 협력업체 승인"), ("2012.10", "광학기기 제조업 공장 등록")]),
 ("2013–2019", "확장 · R&D", [("2013.09", "SDA와 협력업체 계약 (IC 테스트 프로브 / 스프링 포고핀)"), ("2013.10", "천안사업소 개설"), ("2013.10", "영국 Domino 잉크젯 마킹기 협력업체 등록"),
   ("2014.03", "사용자 사양 방식 납땜 로봇 개발"), ("2014.10", "미세코일 확산접합기 — ㈜ACE 협력업체"), ("2014.11", "중소기업청 기술혁신과제 완료 — 블루투스 4.0 비콘 단말기 개발"),
   ("2015.03", "안양공장 개소 (자동화 사업부)"), ("2017.11", "중소기업청 구매조건부 신제품개발 과제 완료 — 스트레스 생리신호 측정 복합센서 칩 개발")]),
 ("2020–", "AI · 신사업", [("2021.10", "대덕특구 과제 — 스트레스 측정 패드와 지능형 판정 학습 모듈 연계 개발 (KAIST)"), ("2022.12", "딥러닝 자동 검사·측정 소프트웨어 공동 개발 및 사업화"),
   ("2023.03", "아이메저 — 독일 Schneider 비접촉 측정기 협약점"), ("2023.04", "비접촉 3차원 측정기 · 원샷 측정기 협약점"), ("2024.12", "HIKVISION 초고심도 3D 디지털 현미경 대리점"),
   ("2025.02", "HIKROBOT 스마트 카메라 · 엣지 러닝 SW 응용 개발"), ("2026", "홈페이지 새 단장")]),
]
ORG = [("경영지원팀", ["관리", "재무 · 회계", "구매"]), ("경영마케팅", ["국내외 마케팅", "영업 · 서비스"]), ("자동화 사업부 (협력사)", ["라인 자동화", "AI (딥러닝)", "시스템 개발"]),
       ("생산", ["생산 관리", "외주 관리"]), ("기업부설연구소", ["무선 통신", "광학 응용", "소프트웨어"]), ("특수사업부", ["접합기", "마킹기", "협력사"])]
APPS = [("의료기기", "Medical Device", "스텐트, 니들, 카테터, 보철물"), ("자동차", "Automotive", "엔진 부품, 주조품, 가공품"), ("플라스틱", "Plastics", "사출 성형품, 커넥터, 조립품, 화장품 용기"),
        ("전자 · 반도체", "Electronics", "PCB, 전자부품, MLCC, 마이크로 전자"), ("기계", "Mechanical", "기어, 선삭 부품, 형상 가공품"), ("정밀 공학", "Precision Eng.", "베어링, 씰, 공구·툴링")]
PARTNERS = [("Vision Engineering", "영국", "1993", "대한민국 총판", "접안렌즈 없는 실체현미경, 디지털·3D 현미경, 비접촉 측정 시스템"),
            ("HIKVISION", "중국", "2024", "대리점", "초고심도 3D 고배율 디지털 현미경 (Deep Vision)"),
            ("HIKROBOT", "중국", "2025", "응용 개발", "스마트 비전 센서, 엣지 러닝 솔루션"),
            ("WENZEL", "독일", "", "파트너", "3차원 측정기, 기어 측정기"),
            ("Schneider", "독일", "2023", "협약점 (아이메저)", "비접촉 측정기"),
            ("ATOMETRICS", "중국", "", "파트너", "백색광 간섭계, 3D 표면 측정"),
            ("AIMS ㈜에임즈", "대한민국", "", "협력사", "AI 공구 상태진단·마모 계측")]
CUSTOMERS = ["대구텍", "오스템임플란트", "MOBIS", "보쉬코리아", "삼성전자", "삼성전기", "삼성SDI", "심텍", "AMKOR", "OMRON", "YG-1", "리슨트",
             "LG전자", "SKC코오롱PI", "자화전자", "코웨이", "콘티넨탈오토모티브", "KMW", "하이게인안테나", "한국야금", "현대자동차", "로타렉스", "하나머티리얼즈", "인트로메딕",
             "태웅메디칼", "아바텍", "아모텍", "스마트코리아피씨비", "LG이노텍", "한국생산기술연구원", "테크노파크", "아드반테스트코리아", "S&S INC", "제4기텍", "SK하이닉스",
             "한선엔지니어링", "코박메드", "한화에어로스페이스", "오송첨단바이오", "국방연구소", "극지연구소", "삼화이앤피", "유니온머티리얼", "DMS", "은성전장"]
SERVICE = [("1년", "제품 보증", "구매일로부터 1년간 보증합니다. 별도 계약으로 납품한 제품은 계약 내용을 따릅니다."),
           ("2명+", "정규 서비스 인력", "2명 이상의 정규직 서비스 엔지니어가 직접 대응합니다."),
           ("모듈", "부품 모듈화", "대부분의 소모품·핵심 파츠를 모듈 형태로 보유해 문제가 생기면 쉽고 빠르게 교체합니다."),
           ("2년", "소프트웨어 교육 무상", "장비와 함께 쓰는 소프트웨어 교육을 2년간 무상으로 지원합니다.")]
SITES = [("본사", "서울특별시 영등포구 당산로2길 12, 에이스테크노타워 806호 (문래동)", "영업 · 서비스 · 연구소"),
         ("안양공장", "경기도 안양시 만안구 전파로 30, B3층 315호", "자동화 사업부")]

AB2_CSS = """
.ov{display:grid;grid-template-columns:1.1fr 1fr;gap:28px;align-items:start}
.ov dl{display:grid;grid-template-columns:120px 1fr;border-top:2px solid var(--navy)}
.ov dt,.ov dd{padding:14px 4px;border-bottom:1px solid var(--line);font-size:15px}.ov dt{color:var(--sub);font-weight:700}.ov dd{font-weight:600}
.phil{display:grid;grid-template-columns:1fr 1.3fr;gap:18px;margin-top:4px}
.phil .eq{border-radius:18px;background:var(--navy);color:#fff;padding:28px;display:flex;flex-direction:column;justify-content:center}
.phil .eq small{font-size:11px;letter-spacing:2px;font-weight:800;color:var(--mint)}
.phil .eq b{font-size:30px;letter-spacing:-.8px;margin-top:8px;line-height:1.3}.phil .eq b em{font-style:normal;color:var(--mint)}
.phil .pr{display:grid;gap:10px}.phil .pr div{background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px 20px;display:flex;gap:14px;align-items:center;font-size:17px;font-weight:700;color:var(--navy)}
.phil .pr i{font-style:normal;font-size:12px;font-weight:800;color:var(--blue);min-width:26px}
.greet .sign{margin-top:22px;font-weight:700;color:var(--navy);text-align:right}.greet .sign b{font-size:22px;margin-left:8px;letter-spacing:2px}
.hist{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:34px}
.era{background:#fff;border:1px solid var(--line);border-radius:16px;padding:22px 20px}
.era h4{font-size:13px;letter-spacing:1px;color:var(--blue);font-weight:800}.era h5{font-size:20px;color:var(--navy);margin:2px 0 14px}
.era ol{list-style:none;display:grid;gap:12px;border-left:2px solid #dbe4f0;padding-left:14px}
.era li{position:relative;font-size:14px;line-height:1.55;color:#36405a}.era li:before{content:"";position:absolute;left:-19px;top:6px;width:8px;height:8px;border-radius:50%;background:var(--blue)}
.era li b{display:block;font-size:12.5px;color:var(--navy);font-variant-numeric:tabular-nums}
.org{display:flex;flex-direction:column;align-items:center;gap:0;margin-top:10px}
.org .ceo{background:var(--navy);color:#fff;border-radius:12px;padding:14px 34px;font-weight:800;font-size:17px;position:relative}
.org .side{display:flex;gap:10px;margin:14px 0 0}.org .side span{font-size:13px;font-weight:700;color:var(--navy);border:1px dashed #9db0cc;border-radius:8px;padding:6px 12px;background:#fff}
.org .vline{width:2px;height:22px;background:#9db0cc}
.org .teams{display:grid;grid-template-columns:repeat(6,1fr);gap:12px;width:100%;position:relative;padding-top:22px}
.org .teams:before{content:"";position:absolute;top:0;left:8.33%;right:8.33%;height:2px;background:#9db0cc}
.org .tm{position:relative;background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden}
.org .tm:before{content:"";position:absolute;top:-22px;left:50%;width:2px;height:22px;background:#9db0cc}
.org .tm h4{background:#eaf3ff;color:var(--navy);font-size:15px;text-align:center;padding:12px 6px}
.org .tm ul{list-style:none;padding:12px;display:grid;gap:6px}.org .tm li{font-size:13.5px;text-align:center;color:#3a4356}
.biz2{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}.biz2 span{font-size:14px;font-weight:700;color:var(--navy);background:#fff;border:1px solid var(--line);border-radius:999px;padding:8px 16px}
.biz2 span.new{background:var(--navy);color:#fff;border-color:var(--navy)}.biz2 span.new i{font-style:normal;color:var(--mint);font-size:11px;margin-right:6px}
.apps2{display:grid;grid-template-columns:repeat(6,1fr);gap:12px}
.apps2 div{background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px 16px}
.apps2 small{font-size:11px;letter-spacing:1px;color:var(--blue);font-weight:800}.apps2 h4{font-size:17px;color:var(--navy);margin:2px 0 6px}.apps2 p{font-size:13px;color:var(--sub)}
.pt2{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px}
.pt2 div{background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px;position:relative}
.pt2 h4{font-size:18px;color:var(--navy);letter-spacing:-.2px}.pt2 .meta{font-size:12px;font-weight:700;color:var(--sub);margin:4px 0 10px}
.pt2 .meta em{font-style:normal;color:#0a8f78;background:#d9f7f0;padding:2px 8px;border-radius:4px;margin-left:6px}
.pt2 p{font-size:14px;color:#3a4356}
.pt2 div.main{grid-column:span 2;background:var(--navy);color:#fff;border-color:var(--navy)}.pt2 div.main h4{color:#fff;font-size:22px}.pt2 div.main .meta{color:rgba(255,255,255,.7)}.pt2 div.main p{color:rgba(255,255,255,.85)}
.pt2 .yr{position:absolute;right:18px;top:16px;font-size:12px;font-weight:800;color:var(--blue)}.pt2 div.main .yr{color:var(--mint);font-size:14px}
.certs{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.certs a{display:block;background:#fff;border:1px solid var(--line);border-radius:16px;padding:16px;text-align:center;transition:.2s}
.certs a:hover{box-shadow:0 12px 28px rgba(27,43,75,.12);transform:translateY(-3px)}
.certs img{height:300px;width:100%;object-fit:contain;background:#f7f9fc;border-radius:8px}
.certs b{display:block;margin-top:12px;font-size:16px;color:var(--navy)}.certs small{font-size:13px;color:var(--sub)}
.cust{display:grid;grid-template-columns:repeat(6,1fr);border-top:1px solid var(--line);border-left:1px solid var(--line);background:#fff;border-radius:4px}
.cust span{border-right:1px solid var(--line);border-bottom:1px solid var(--line);padding:16px 8px;text-align:center;font-size:14.5px;font-weight:700;color:#3a4356}
.svc{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.svc div{background:#fff;border:1px solid var(--line);border-radius:16px;padding:22px 20px}
.svc b{display:block;font-size:30px;font-weight:800;color:var(--blue);letter-spacing:-1px}.svc h4{font-size:16px;color:var(--navy);margin:2px 0 6px}.svc p{font-size:13.5px;color:var(--sub)}
.sites{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-top:20px}
.sites div{background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px 20px}.sites div.hq{border-color:var(--blue);box-shadow:0 0 0 1px var(--blue) inset}
.sites h4{font-size:16px;color:var(--navy)}.sites small{font-size:12px;font-weight:700;color:var(--blue)}.sites p{font-size:14px;color:#3a4356;margin-top:6px}
.ab-note{font-size:13px;color:var(--sub);margin-top:14px}
@media(max-width:1000px){.hist{grid-template-columns:1fr 1fr}.apps2{grid-template-columns:repeat(3,1fr)}.org .teams{grid-template-columns:repeat(3,1fr)}.org .teams:before,.org .tm:before{display:none}.cust{grid-template-columns:repeat(4,1fr)}.svc{grid-template-columns:1fr 1fr}}
@media(max-width:700px){.ov,.phil{grid-template-columns:1fr}.ov dl{grid-template-columns:96px 1fr}.hist{grid-template-columns:1fr}.apps2{grid-template-columns:1fr 1fr}.org .teams{grid-template-columns:1fr 1fr}.pt2 div.main{grid-column:auto}.certs{grid-template-columns:1fr}.cust{grid-template-columns:repeat(3,1fr)}.cust span{font-size:13px}.sites{grid-template-columns:1fr}}
"""

def ruler2(y0=1991, y1=2026):
    span = y1 - y0; pos = lambda y: (y - y0) / span * 100
    parts = []
    for y in range(y0, y1 + 1):
        major = (y % 5 == 0) or y in (y0, y1)
        parts.append(f'<span class="tick{" major" if major else ""}" style="left:{pos(y):.3f}%"></span>')
        if y % 5 == 0 and y not in (y0, y1): parts.append(f'<span class="lab" style="left:{pos(y):.3f}%">{y}</span>')
    for y in (1991, 1993, 2002, 2012, 2015, 2022, 2024, 2026):
        parts.append(f'<span class="pin{" now" if y == 2026 else ""}" style="left:{pos(y):.3f}%" title="{y}"><i></i></span>')
    parts.append(f'<span class="cap" style="left:0;transform:none">1991 설립</span>')
    parts.append(f'<span class="cap" style="left:auto;right:0;transform:none;text-align:right">2026 현재</span>')
    return '<div class="ruler-wrap"><div class="ruler" role="img" aria-label="1991년부터 2026년까지 주요 연혁 눈금자"><span class="base"></span>' + "".join(parts) + "</div></div>"

def build_about():
    root = ""
    years = 2026 - 1991
    biz = ""
    for i, (c, ds) in enumerate([
        ("현미경", "접안렌즈 없는 실체 현미경, 4K·3D 디지털 현미경"),
        ("측정 시스템", "측정 현미경, 고배율 측정기, 비디오 측정기(VMM)"),
        ("AI 검사·측정", "하이브리드 검사·측정, 기상 AI분석, 기상 검사/측정 비전"),
        ("머신비전", "산업용 카메라, 렌즈·조명, 코드리더, 비전 SW"),
        ("3D·특수 센싱", "3D 스캐너, 백색광 간섭계, 이벤트 카메라 등")]):
        inner = f'<span class="no">{i+1:02d}</span><h4>{c}</h4><p>{ds}</p>'
        biz += (f'<a href="{cat_link(c, root)}">{inner}<span class="go">제품 보기 →</span></a>' if c in CATCFG else f'<div>{inner}<span class="soon">준비 중</span></div>')
    hist = "".join(f'<div class="era"><h4>{r}</h4><h5>{t}</h5><ol>' + "".join(f"<li><b>{e(y)}</b>{e(x)}</li>" for y, x in it) + "</ol></div>" for r, t, it in HISTORY)
    org = ('<div class="org"><div class="ceo">대표이사</div><div class="side"><span>부설연구소장</span><span>외부 기술자문</span></div><div class="vline"></div><div class="teams">'
           + "".join(f'<div class="tm"><h4>{e(t)}</h4><ul>' + "".join(f"<li>{e(x)}</li>" for x in xs) + "</ul></div>" for t, xs in ORG) + "</div></div>")
    apps = "".join(f"<div><small>{e(en)}</small><h4>{e(k)}</h4><p>{e(d)}</p></div>" for k, en, d in APPS)
    pts = "".join(f'<div class="{"main" if i==0 else ""}">{f"<span class=yr>Since {y}</span>" if y else ""}<h4>{e(n)}</h4><div class="meta">{e(c)}<em>{e(r)}</em></div><p>{e(d)}</p></div>' for i, (n, c, y, r, d) in enumerate(PARTNERS))
    cimg = lambda n: img(root, f"/assets/img/about/{n}.jpg")
    certs = "".join(f'<a href="{cimg(n)}" target="_blank" rel="noopener"><img src="{cimg(n)}" alt="{e(t)}" loading="lazy"><b>{e(t)}</b><small>{e(s)}</small></a>'
                    for n, t, s in [("cert-ve", "Vision Engineering 대한민국 공식 총판", "영국 Vision Engineering, 1993~"),
                                    ("cert-lab", "기업부설연구소 인정서", "한국산업기술진흥협회 · 최초 인정 2012.06"),
                                    ("cert-tech", "기술역량 우수기업 인증서", "한국기업데이터 · 2018")])
    cust = "".join(f"<span>{e(c)}</span>" for c in CUSTOMERS)
    svc = "".join(f"<div><b>{e(a)}</b><h4>{e(b)}</h4><p>{e(c)}</p></div>" for a, b, c in SERVICE)
    sites = "".join(f'<div class="{"hq" if i==0 else ""}"><small>{e(r)}</small><h4>{e(n)}</h4><p>{e(a)}</p></div>' for i, (n, a, r) in enumerate(SITES))
    inner = f"""{ABOUT_FONTS}<style>{ABOUT_CSS}{AB2_CSS}</style>
<section class="ab-hero"><div class="wrap">
 <div><div class="crumb">홈 › 회사소개</div>
  <div class="ab-eyebrow">SEIL TECHNO · Since 1991</div>
  <h1>1991년부터, <em>정확하게 보는 일</em>을<br>산업 현장에 공급해 왔습니다.</h1>
  <p class="lead">㈜세일테크노는 정밀 광학 현미경과 측정·검사 장비를 공급하고, 자동화·AI 검사 솔루션을 직접 개발하는 기술 기업입니다. {years}년 동안 쌓은 현장 경험으로 고객의 품질 관리와 생산성을 함께 고민합니다.</p>
  <div class="ab-facts"><div><b>1991</b><span>설립</span></div><div><b>1993~</b><span>Vision Engineering 대한민국 총판</span></div><div><b>2012</b><span>기업부설연구소 인정</span></div></div>
 </div>
 <div class="scope">{reticle_svg()}<span class="since">SINCE</span><span class="yr">1991</span><span class="coord">X 1991.00 · Y 2026.00</span></div>
</div></section>

<section class="ab-sec"><div class="wrap greet">
 <div><div class="ab-kicker">CEO Greeting</div><h2>대표 인사말</h2>
  <blockquote>"고객만족 = 우리만족"<small>SEIL TECHNO 경영이념</small></blockquote></div>
 <div class="txt">
  <p>세일테크노는 <strong>1991년</strong> 창립 이래 무역·제조 전문기업으로서, 60년 역사를 지닌 영국 <strong>Vision Engineering</strong>의 접안렌즈 없는 특허 현미경을 중심으로 전자·전기·기계 부품 생산 현장의 제품 개발, 품질 관리, 생산성 향상에 기여해 왔습니다. 보다 과학적이고 인체공학적인 장비를 공급해 산업 현장의 발전을 이끄는 웰빙(Well-being) 기업이 되겠습니다.</p>
  <p>2011년에는 해외 의존도가 높던 <strong>자동 납땜 로봇</strong>을 국산화해 합리적인 가격과 높은 품질로 국내외 시장의 호응을 얻었고, 공장 자동화 사업을 더해 전기·전자 업체와 함께 성장하고 있습니다.</p>
  <p>나아가 <strong>AI 기술을 검사·측정 시스템에 접목한 하이브리드 솔루션</strong> 개발에 힘써 차별화된 검사·측정 솔루션을 산업 현장에 보급하고 있으며, 다중 생체신호 기반 패치형 센서를 활용한 멘탈 헬스케어 분야로도 사업을 넓혀 가고 있습니다.</p>
  <p>축적된 기술력과 노하우를 바탕으로 산업 발전과 사회에 기여하도록 전사적으로 노력하겠습니다. 감사합니다.</p>
  <div class="sign">㈜세일테크노 대표이사<b>김중석</b></div>
 </div>
</div></section>

<section class="ab-sec alt"><div class="wrap">
 <div class="ab-kicker">Philosophy</div><h2>경영이념 · 경영원칙</h2>
 <div class="phil"><div class="eq"><small>경영이념</small><b>고객만족 <em>=</em> 우리만족</b></div>
 <div class="pr"><div><i>01</i>긍정적인 목표</div><div><i>02</i>땀의 가치를 안다</div><div><i>03</i>날마다 좋아지고 있다</div></div></div>
</div></section>

<section class="ab-sec"><div class="wrap">
 <div class="ab-kicker">Company Overview</div><h2>회사 개요</h2>
 <div class="ov"><dl>
  <dt>상호</dt><dd>㈜세일테크노 (SEIL TECHNO CORP.)</dd><dt>대표이사</dt><dd>김중석</dd>
  <dt>설립</dt><dd>1991년 7월 (세일테크노교역) · 1994년 법인 전환</dd><dt>기업부설연구소</dt><dd>2012년 6월 인정 (한국산업기술진흥협회)</dd>
  <dt>공장 등록</dt><dd>2012년 · 광학기기 제조업</dd><dt>대표전화</dt><dd>02-2632-3211 · 팩스 02-2632-3214</dd><dt>이메일</dt><dd>seil@stvision.co.kr</dd>
 </dl>
 <div><h3 style="font-size:18px;color:var(--navy);margin-bottom:6px">사업장</h3><div class="sites" style="grid-template-columns:1fr;margin-top:8px">{sites}</div></div></div>
</div></section>

<section class="ab-sec alt"><div class="wrap">
 <div class="ab-kicker">History · 1991 — 2026</div><h2>{years}년의 눈금</h2>
 {ruler2()}
 <div class="hist">{hist}</div>
</div></section>

<section class="ab-sec"><div class="wrap">
 <div class="ab-kicker">Organization</div><h2>조직</h2>{org}
</div></section>

<section class="ab-sec alt"><div class="wrap">
 <div class="ab-kicker">Business</div><h2>사업 분야</h2>
 <div class="biz">{biz}</div>
 <div class="biz2"><span>자동 납땜 로봇 · 인라인 시스템</span><span>잉크젯 마킹 시스템</span><span>미세코일 확산 접합기</span><span>맞춤형 소프트웨어</span><span>정부 과제 R&amp;D</span><span class="new"><i>NEW</i>멘탈 헬스케어 (생체신호 패치 센서)</span></div>
</div></section>

<section class="ab-sec"><div class="wrap">
 <div class="ab-kicker">Application Field</div><h2>응용 분야</h2>
 <p style="color:var(--sub);margin:-6px 0 20px">세일테크노의 제품은 다양한 산업 현장에 맞춤 솔루션을 제공합니다.</p>
 <div class="apps2">{apps}</div>
</div></section>

<section class="ab-sec alt"><div class="wrap">
 <div class="ab-kicker">Partners</div><h2>함께하는 파트너</h2>
 <div class="pt2">{pts}</div>
</div></section>

<section class="ab-sec"><div class="wrap">
 <div class="ab-kicker">Certification</div><h2>인증 현황</h2>
 <div class="certs">{certs}</div>
</div></section>

<section class="ab-sec alt"><div class="wrap">
 <div class="ab-kicker">Customers</div><h2>주요 고객사</h2>
 <p style="color:var(--sub);margin:-6px 0 20px">반도체·전자부품, 자동차, 의료기기, 연구기관까지 다양한 고객과 함께하고 있습니다.</p>
 <div class="cust">{cust}</div>
</div></section>

<section class="ab-sec"><div class="wrap">
 <div class="ab-kicker">Service Policy</div><h2>서비스 방침</h2>
 <div class="svc">{svc}</div>
 <p class="ab-note">핵심 파츠를 모듈 형태로 구성해 문제가 생기면 쉽고 빠르게 대응합니다.</p>
</div></section>

<section class="ab-sec alt"><div class="wrap">
 <div class="ab-kicker">Location</div><h2>오시는 길</h2>
 <div class="sites">{sites}</div>
 <div class="maplinks" style="margin-top:18px"><a class="btn btn-primary" href="{root}고객지원.html#location">본사 지도 보기 →</a>
  <a class="btn btn-ghost" href="https://map.naver.com/p/search/%EC%97%90%EC%9D%B4%EC%8A%A4%ED%85%8C%ED%81%AC%EB%85%B8%ED%83%80%EC%9B%8C%20%EB%8B%B9%EC%82%B0%EB%A1%9C2%EA%B8%B8%2012" target="_blank" rel="noopener">네이버 지도</a>
  <a class="btn btn-ghost" href="https://map.kakao.com/?q=%EB%8B%B9%EC%82%B0%EB%A1%9C2%EA%B8%B8%2012" target="_blank" rel="noopener">카카오맵</a></div>
</div></section>"""
    open(os.path.join(HERE, "회사소개.html"), "w", encoding="utf-8").write(page("회사소개 | 세일테크노", inner, root, active="about"))
