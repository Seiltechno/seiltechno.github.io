# -*- coding: utf-8 -*-
# 제품 상세 '사용 가이드' 구역 — 매뉴얼 장(chapter)마다 설명 + 동영상 + 화면 캡처
# 제품 파일 항목:
#   guide_title / guide_tab / guide_desc (선택)
#   guide:
#     - title: 장 제목
#       text: 한두 문장 설명
#       points: [핵심 항목, ...]            (선택)
#       video: {src: ..mp4, poster: ..jpg, len: "0:43"}   (선택)
#       images: [{src: ..., cap: 설명}, ...]  (선택)
# build_preview.py 끝에서 exec 됨 (e, img, os 등을 함께 사용)

GUIDE_CSS = """
.gd-nav{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 26px}
.gd-nav a{padding:7px 13px;border-radius:999px;background:var(--bg);font-size:13px;font-weight:700;color:var(--sub);text-decoration:none}
.gd-nav a:hover{background:var(--navy);color:#fff}
.gd{border:1px solid var(--line);border-radius:18px;background:#fff;padding:26px;margin-bottom:22px;scroll-margin-top:150px}
.gd-top{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:28px;align-items:start}
.gd-top.nov{grid-template-columns:1fr}
.gd-no{display:inline-block;font-size:12px;font-weight:800;letter-spacing:.5px;color:var(--blue);background:#eaf2ff;border-radius:6px;padding:3px 9px;margin-bottom:10px}
.gd h3{font-size:21px;color:var(--navy);margin:0 0 10px;letter-spacing:-.3px}
.gd .ld{font-size:15px;color:var(--sub);line-height:1.75;margin:0 0 12px}
.gd ul{margin:0;padding-left:18px}.gd li{font-size:14px;line-height:1.7;color:#334;margin:3px 0}
.gd-vid{position:relative;border-radius:12px;overflow:hidden;background:#0f1622}
.gd-vid video{display:block;width:100%;height:auto;aspect-ratio:1280/675;background:#0f1622}
.gd-one{all:unset;cursor:zoom-in;display:block;border-radius:12px;overflow:hidden;border:1px solid var(--line)}.gd-one img{display:block;width:100%;height:auto}
.gd-vid .tm{position:absolute;top:10px;left:10px;background:rgba(15,22,34,.78);color:#fff;font-size:12px;font-weight:700;border-radius:6px;padding:3px 8px;pointer-events:none}
.gd-imgs{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:14px;margin-top:20px}
.gd-imgs button{all:unset;cursor:zoom-in;display:flex;flex-direction:column;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:#fff}
.gd-imgs button:focus-visible{outline:3px solid var(--blue)}
.gd-imgs .ph{display:block;aspect-ratio:16/10;background:#0f1622;overflow:hidden}
.gd-imgs img{width:100%;height:100%;object-fit:contain;transition:transform .35s}
.gd-imgs button:hover img{transform:scale(1.04)}
.gd-imgs span.cp{font-size:13px;color:var(--sub);padding:9px 11px;line-height:1.5}
.gd-lb{position:fixed;inset:0;z-index:999;background:rgba(8,12,20,.92);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:24px}
.gd-lb[hidden]{display:none}
.gd-lb img{max-width:96vw;max-height:82vh;object-fit:contain;border-radius:8px;background:#fff}
.gd-lb .lc{color:#fff;font-size:14px;margin-top:12px;text-align:center}
.gd-lb button{all:unset;cursor:pointer;color:#fff;font-weight:700}
.gd-lb .lx{position:absolute;top:16px;right:20px;font-size:15px}
.gd-lb .ln{position:absolute;top:50%;font-size:44px;padding:10px;transform:translateY(-50%)}
@media(max-width:860px){.gd-top{grid-template-columns:1fr}.gd{padding:18px}}
"""

GUIDE_JS = """<script>(function(){var box=document.getElementById('gd');if(!box)return;
var rm=matchMedia('(prefers-reduced-motion: reduce)').matches,vs=[].slice.call(box.querySelectorAll('video'));
/* 화면에 보이는 영상 하나만 자동 재생 (소리 없음) — 나머지는 정지해서 데이터 절약 */
if(!rm&&'IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(x){var v=x.target;
if(x.isIntersecting&&x.intersectionRatio>=.55){vs.forEach(function(o){if(o!==v)o.pause()});v.play().catch(function(){})}else{v.pause()}})},{threshold:[0,.55]});
vs.forEach(function(v){io.observe(v)})}
var bs=[].slice.call(box.querySelectorAll('.gd-imgs button')),cur=0,lb=null;
function show(i){cur=(i+bs.length)%bs.length;var b=bs[cur];lb.querySelector('img').src=b.dataset.full;lb.querySelector('img').alt=b.dataset.cap;lb.querySelector('.lc').textContent=(cur+1)+' / '+bs.length+'  ·  '+b.dataset.cap}
function close(){lb.hidden=true;document.body.style.overflow=''}
function open(b){if(!lb){lb=document.createElement('div');lb.className='gd-lb';lb.setAttribute('role','dialog');lb.setAttribute('aria-label','화면 크게 보기');
lb.innerHTML='<button class="lx" aria-label="닫기">닫기 ✕</button><button class="ln" style="left:12px" aria-label="이전">‹</button><img alt=""><div class="lc"></div><button class="ln" style="right:12px" aria-label="다음">›</button>';
lb.querySelector('.lx').onclick=close;lb.querySelectorAll('.ln')[0].onclick=function(){show(cur-1)};lb.querySelectorAll('.ln')[1].onclick=function(){show(cur+1)};
lb.addEventListener('click',function(ev){if(ev.target===lb)close()});document.body.appendChild(lb)}
vs.forEach(function(v){v.pause()});lb.hidden=false;document.body.style.overflow='hidden';show(bs.indexOf(b));lb.querySelector('.lx').focus()}
document.addEventListener('keydown',function(ev){if(!lb||lb.hidden)return;if(ev.key==='Escape')close();if(ev.key==='ArrowLeft')show(cur-1);if(ev.key==='ArrowRight')show(cur+1)});
bs.forEach(function(b){b.addEventListener('click',function(){open(b)})})})();</script>"""


def _gfile(src):
    """파일 있는지 확인 (없으면 미리보기에서만 표시)"""
    f = _shot_file(src) if src.lower().endswith((".jpg", ".png")) else (src if os.path.exists(os.path.join(SITE, src.lstrip("/"))) else None)
    return f


def guide_section(d, root, en=False):
    g = d.get("guide")
    if not g: return ""
    nav, arts = [], []
    for i, ch in enumerate(g, 1):
        aid = f"gd{i}"
        nav.append(f'<a href="#{aid}">{i}. {e(ch["title"])}</a>')
        pts = "".join(f"<li>{e(p)}</li>" for p in ch.get("points", []))
        txt = (f'<div><span class="gd-no">STEP {i:02d}</span><h3>{e(ch["title"])}</h3>'
               + (f'<p class="ld">{e(ch["text"])}</p>' if ch.get("text") else "") + (f"<ul>{pts}</ul>" if pts else "") + "</div>")
        vid = ""
        v = ch.get("video")
        if v:
            if _gfile(v["src"]):
                poster = f' poster="{img(root, v["poster"])}"' if v.get("poster") and _gfile(v["poster"]) else ""
                vid = (f'<div class="gd-vid"><video src="{img(root, v["src"])}"{poster} muted loop playsinline controls preload="none" '
                       f'aria-label="{e(ch["title"])} {"demo video" if en else "시연 영상"}"></video>' + (f'<span class="tm">▶ {e(v["len"])}</span>' if v.get("len") else "") + "</div>")
            elif not os.environ.get("PUBLISH"):
                vid = f'<div class="gd-vid" style="padding:40px;color:#fff;text-align:center">{"Video coming soon" if en else "영상 준비 중"}<br><code>site{e(v["src"])}</code></div>'
        thumbs = ""
        ims = ch.get("images", [])
        if not vid and len(ims) == 1 and _gfile(ims[0]["src"]):   # 영상 없이 사진 1장이면 오른쪽에 크게
            x = ims[0]; f = _gfile(x["src"]); ims = []
            vid = (f'<div class="gd-imgs" style="margin:0;display:block"><button type="button" class="gd-one" data-full="{img(root, f)}" data-cap="{e(x.get("cap",""))}">'
                   f'<img loading="lazy" src="{img(root, f)}" alt="{e(x.get("cap",""))}"></button></div>')
        for x in ims:
            f = _gfile(x["src"])
            if f:
                thumbs += (f'<button type="button" data-full="{img(root, f)}" data-cap="{e(x.get("cap",""))}"><span class="ph"><img loading="lazy" src="{img(root, f)}" alt="{e(x.get("cap",""))}"></span>'
                           f'<span class="cp">{e(x.get("cap",""))}</span></button>')
        arts.append(f'<article class="gd" id="{aid}"><div class="gd-top{"" if vid else " nov"}">{txt}{vid}</div>'
                    + (f'<div class="gd-imgs">{thumbs}</div>' if thumbs else "") + "</article>")
    desc = d.get("guide_desc", "")
    return (f'<style>{GUIDE_CSS}</style><section class="sec" id="gd"><h2>{e(d.get("guide_title","사용 가이드"))}</h2>'
            + (f'<p style="color:var(--sub);margin:-8px 0 16px">{e(desc)}</p>' if desc else "")
            + f'<nav class="gd-nav" aria-label="{"Guide contents" if en else "가이드 목차"}">{"".join(nav)}</nav>{"".join(arts)}</section>'
            + (GUIDE_JS.replace("화면 크게 보기", "Enlarged screenshot").replace("닫기 ✕", "Close ✕").replace("닫기", "Close").replace("이전", "Previous").replace("다음", "Next") if en else GUIDE_JS))


# ── 구성 예(사진 여러 장을 같은 높이로 나란히) ─────────────────────────────
#   setups_title / setups_desc (선택)
#   setups: [{src: 사진, cap: 설명}, ...]
def _img_size(path):
    """jpg/png 가로·세로 (추가 설치 없이 읽기)"""
    import struct
    try:
        with open(path, "rb") as f:
            h = f.read(26)
            if h[:8] == b"\x89PNG\r\n\x1a\n": return struct.unpack(">II", h[16:24])
            f.seek(2)
            while True:
                b = f.read(1)
                while b and b != b"\xff": b = f.read(1)
                while b == b"\xff": b = f.read(1)
                if not b: return None
                if b[0] in (0xC0, 0xC1, 0xC2):
                    f.read(3); hh, ww = struct.unpack(">HH", f.read(4)); return ww, hh
                ln = struct.unpack(">H", f.read(2))[0]; f.seek(ln - 2, 1)
    except Exception:
        return None

SETUP_CSS = """
.su{display:flex;gap:18px;align-items:flex-start}
.su figure{min-width:0;margin:0;border:1px solid var(--line);border-radius:16px;overflow:hidden;background:#fff}
.su a{display:block;cursor:zoom-in}.su img{display:block;width:100%;height:auto}
.su figcaption{font-size:13.5px;color:var(--sub);padding:10px 14px;line-height:1.55}
@media(max-width:760px){.su{flex-direction:column}.su figure{flex:none!important;width:100%}}
"""

def setups_section(d, root, en=False):
    su = d.get("setups")
    if not su: return ""
    figs = ""
    for x in su:
        f = _gfile(x["src"])
        if not f: continue
        wh = _img_size(os.path.join(SITE, f.lstrip("/"))) or (4, 3)
        figs += (f'<figure style="flex:{wh[0]/wh[1]:.3f} 1 0"><a href="{img(root, f)}" target="_blank" rel="noopener"><img loading="lazy" src="{img(root, f)}" alt="{e(x.get("cap",""))}"></a>'
                 + (f'<figcaption>{e(x["cap"])}</figcaption>' if x.get("cap") else "") + "</figure>")
    if not figs: return ""
    desc = d.get("setups_desc", "")
    return (f'<style>{SETUP_CSS}</style><section class="sec" id="su"><h2>{e(d.get("setups_title", "Setup examples" if en else "구성 예"))}</h2>'
            + (f'<p style="color:var(--sub);margin:-8px 0 16px">{e(desc)}</p>' if desc else "") + f'<div class="su">{figs}</div></section>')
