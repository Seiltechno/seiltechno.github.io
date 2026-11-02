# -*- coding: utf-8 -*-
# 게시판형 카테고리(3D·특수 센싱) + 3D 모델 뷰어 + 영상 구역 (build_preview.py 안에서 실행)
CATCFG["3D·특수 센싱"] = {"file": "제품목록_3D특수센싱.html", "board": True,
  "desc": "3D 스캐너, 백색광 간섭계, 원샷 측정기, 3D 레이저 측정기, 이벤트 카메라처럼 특별한 측정이 필요할 때 쓰는 장비들입니다. 새 장비가 들어올 때마다 하나씩 소개합니다.",
  "subs": [("3D 스캐닝", "3D Scanning", "물체의 형상을 3D 데이터로 그대로 옮기는 스캐너"),
           ("표면 형상 측정", "Surface Metrology", "나노미터 단위로 표면의 높낮이와 거칠기를 재는 장비"),
           ("원샷 측정", "One-Shot Measurement", "카메라 한 번 촬영으로 여러 치수를 한꺼번에 재는 측정기"),
           ("3D 레이저 측정", "3D Laser Profiling", "라인 레이저로 제품 전면을 스캔해 평탄도·높이를 재는 장비"),
           ("이벤트 카메라", "Event-based Vision", "밝기가 변한 픽셀만 신호를 내는 새로운 방식의 카메라")],
  "banner_after": None}
for _i, (_s, _en, _ds) in enumerate(CATCFG["3D·특수 센싱"]["subs"]):
    SUB_INFO[_s] = {"cat": "3D·특수 센싱", "n": _i + 1, "en": _en, "desc": _ds, "id": "sub%d" % (_i + 1)}

BOARD_CSS = """
.bd-bar{display:flex;gap:10px;align-items:center;flex-wrap:wrap;padding:22px 0;border-bottom:1px solid var(--line)}
.bd-chips{display:flex;gap:6px;flex-wrap:wrap}
.bd-chips button{all:unset;cursor:pointer;padding:8px 14px;border-radius:999px;background:var(--bg);font-size:13px;font-weight:700;color:var(--sub)}
.bd-chips button b{margin-left:5px;opacity:.6}.bd-chips button.on{background:var(--navy);color:#fff}
.bd-chips button:focus-visible{outline:2px solid var(--blue);outline-offset:2px}
.bd-search{margin-left:auto;display:flex;align-items:center;gap:8px;border:1px solid var(--line);border-radius:999px;padding:8px 14px;min-width:240px}
.bd-search input{border:0;outline:0;font:inherit;font-size:14px;flex:1;min-width:0;background:transparent}
.bd-head{display:grid;grid-template-columns:70px 1fr 120px;gap:20px;padding:14px 8px;font-size:12px;font-weight:800;color:var(--sub);letter-spacing:.5px;border-bottom:2px solid var(--navy);margin-top:18px}
.bd-list{list-style:none}
.bp{display:grid;grid-template-columns:70px 1fr 120px;gap:20px;align-items:center;padding:22px 8px;border-bottom:1px solid var(--line);transition:background .2s}
.bp:hover{background:#f7f9fc}.bp[hidden]{display:none}
.bp-no{font-size:22px;font-weight:800;color:#c3cddb;font-variant-numeric:tabular-nums;text-align:center}
.bp-main{display:grid;grid-template-columns:260px 1fr;gap:24px;align-items:center}
.bp-img{aspect-ratio:4/3;border-radius:14px;overflow:hidden;background:#fff;border:1px solid var(--line);display:flex;align-items:center;justify-content:center}
.bp-img img{max-width:100%;max-height:100%;object-fit:contain;transition:transform .4s}.bp:hover .bp-img img{transform:scale(1.04)}
.bp-tags{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px}
.bp-tags span{font-size:11px;font-weight:800;padding:3px 9px;border-radius:5px;background:#e8f1ff;color:var(--blue)}.bp-tags span.br{background:var(--bg);color:var(--sub)}
.bp-tags span.new{background:var(--mint);color:var(--navy)}
.bp h3{font-size:22px;letter-spacing:-.4px;color:var(--navy);line-height:1.3}
.bp .st{font-size:14px;color:var(--sub);font-weight:600;margin-top:2px}
.bp .sm{font-size:14.5px;color:#3a4356;margin-top:8px;max-width:680px}
.bp-keys{display:flex;gap:6px;flex-wrap:wrap;margin-top:12px}.bp-keys span{font-size:12px;font-weight:700;color:var(--navy);border:1px solid var(--line);padding:4px 10px;border-radius:999px}
.bp-side{text-align:right;font-size:13px;color:var(--sub)}.bp-side b{display:block;color:var(--ink);font-size:14px;margin-bottom:10px;font-variant-numeric:tabular-nums}
.bp-side span{display:inline-block;font-weight:800;color:var(--blue)}
.bd-empty{padding:60px 0;text-align:center;color:var(--sub)}
.bd-note{margin:28px 0 0;font-size:13px;color:var(--sub)}
@media(max-width:900px){.bd-head{display:none}.bp{grid-template-columns:1fr;gap:10px;padding:22px 0}.bp-no{display:none}.bp-main{grid-template-columns:1fr;gap:14px}.bp-side{text-align:left;display:flex;justify-content:space-between}.bp-side b{margin:0}.bd-search{margin-left:0;width:100%}}
/* 3D 뷰어 */
.v3{border-radius:20px;background:radial-gradient(900px 400px at 70% 0%,#1d3a63,#0b1424 70%);color:#fff;display:grid;grid-template-columns:260px 1fr;overflow:hidden;min-height:440px}
.v3-side{padding:26px 22px;display:flex;flex-direction:column;gap:10px;border-right:1px solid rgba(255,255,255,.08)}
.v3-side .lbl{font-size:11px;letter-spacing:2px;font-weight:800;color:var(--mint);margin-bottom:4px}
.v3-m{all:unset;cursor:pointer;display:block;padding:14px 16px;border-radius:12px;border:1px solid rgba(255,255,255,.12);background:rgba(255,255,255,.04)}
.v3-m b{display:block;font-size:16px}.v3-m small{display:block;font-size:12.5px;color:rgba(255,255,255,.6);margin-top:2px}
.v3-m.on{background:#fff;color:var(--navy);border-color:#fff}.v3-m.on small{color:var(--sub)}
.v3-m:focus-visible{outline:2px solid var(--mint)}
.v3-help{margin-top:auto;font-size:12px;color:rgba(255,255,255,.55);line-height:1.7}
.v3-stage{position:relative;min-height:440px}
.v3-canvas{position:absolute;inset:0}.v3-canvas canvas{display:block;width:100%!important;height:100%!important;touch-action:none;cursor:grab}
.v3-tools{position:absolute;right:14px;bottom:14px;display:flex;gap:8px}
.v3-tools button{all:unset;cursor:pointer;font-size:12px;font-weight:700;padding:8px 12px;border-radius:999px;background:rgba(255,255,255,.12);backdrop-filter:blur(6px)}
.v3-tools button:hover{background:rgba(255,255,255,.22)}.v3-tools button:focus-visible{outline:2px solid var(--mint)}
.v3-msg{position:absolute;inset:0;display:grid;place-items:center;font-size:14px;color:rgba(255,255,255,.7);pointer-events:none}
.v3-msg[hidden]{display:none}
.v3-badge{position:absolute;left:16px;top:14px;font-size:11px;letter-spacing:1.5px;font-weight:800;color:rgba(255,255,255,.6)}
.v3-note{font-size:13px;color:var(--sub);margin-top:12px}
.vids{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.vids figure{margin:0;border-radius:16px;overflow:hidden;border:1px solid var(--line);background:#0b1424}
.vids video{display:block;width:100%;aspect-ratio:16/9;object-fit:contain;background:#0b1424}
.vids.one{grid-template-columns:1fr;max-width:960px}.vids.one video{aspect-ratio:16/9}
.vids figcaption.vt{display:flex;flex-direction:column;gap:4px;padding:14px 18px 16px}.vids figcaption.vt b{font-size:16.5px;color:var(--navy)}.vids figcaption.vt span{font-size:14px;font-weight:500;color:var(--sub);line-height:1.6}
.vids figcaption{background:#fff;padding:12px 16px;font-size:14px;font-weight:600}
@media(max-width:900px){.v3{grid-template-columns:1fr}.v3-side{border-right:0;border-bottom:1px solid rgba(255,255,255,.08);flex-direction:row;flex-wrap:wrap}.v3-side .lbl,.v3-help{width:100%}.v3-m{flex:1}.v3-stage{min-height:340px}.vids{grid-template-columns:1fr}}
"""

def build_board(all_items, cat):
    root = ""; cfg = CATCFG[cat]
    items = sorted([d for d in all_items if d["category"] == cat], key=lambda d: (str(d.get("posted", "")), d.get("order", 0)), reverse=True)
    subs = [x[0] for x in cfg["subs"]]
    chips = f'<button class="on" data-v="all" aria-pressed="true">전체<b>{len(items)}</b></button>' + "".join(
        f'<button data-v="{SUB_INFO[s]["id"]}" aria-pressed="false">{s}<b>{sum(1 for d in items if d["subcategory"]==s)}</b></button>' for s in subs)
    rows = ""
    newest = str(items[0].get("posted", "")) if items else ""
    for i, d in enumerate(items):
        no = len(items) - i
        keys = "".join(f"<span>{e(t)}</span>" for t in d.get("tags", [])[:3])
        isnew = str(d.get("posted", "")) == newest
        q = (d["title"] + " " + d.get("subtitle", "") + " " + str(d.get("brand", "")) + " " + " ".join(d.get("tags", []))).lower()
        rows += f"""<li class="bp" data-sub="{SUB_INFO[d['subcategory']]['id']}" data-q="{e(q)}"><div class="bp-no">{no:02d}</div>
<a class="bp-main" href="{root}상세/{d['slug']}.html"><div class="bp-img">{pic(root, d)}</div><div>
<div class="bp-tags">{'<span class="new">NEW</span>' if isnew else ''}<span>{e(d['subcategory'])}</span>{f'<span class="br">{e(d["brand"])}</span>' if d.get('brand') else ''}</div>
<h3>{e(d['title'])}</h3><div class="st">{e(d['subtitle'])}</div><p class="sm">{e(d['summary'])}</p><div class="bp-keys">{keys}</div></div></a>
<div class="bp-side"><b>{e(str(d.get('posted','')).replace('-','.'))}</b><span>자세히 보기 →</span></div></li>"""
    js = """<script>(function(){var bs=[].slice.call(document.querySelectorAll('#bdF button')),rows=[].slice.call(document.querySelectorAll('.bp')),q='',f='all';
function r(){var n=0;rows.forEach(function(x){var ok=(f==='all'||x.dataset.sub===f)&&(!q||x.dataset.q.indexOf(q)>-1);x.hidden=!ok;if(ok)n++});document.getElementById('bdE').hidden=n>0}
bs.forEach(function(b){b.addEventListener('click',function(){bs.forEach(function(x){x.classList.remove('on');x.setAttribute('aria-pressed','false')});b.classList.add('on');b.setAttribute('aria-pressed','true');f=b.dataset.v;r()})});
document.getElementById('bdQ').addEventListener('input',function(){q=this.value.trim().toLowerCase();r()});
var h=location.hash.slice(1);bs.forEach(function(b){if(b.dataset.v===h)b.click()});})();</script>"""
    inner = cat_hero(cat, all_items, root, cfg["desc"]) + f"""<style>{BOARD_CSS}</style>
<div class="wrap"><div class="bd-bar"><div class="bd-chips" id="bdF" role="group" aria-label="분야">{chips}</div>
<label class="bd-search"><span aria-hidden="true">🔍</span><input id="bdQ" type="search" placeholder="장비 이름·키워드 검색" aria-label="장비 검색"></label></div>
<div class="bd-head" aria-hidden="true"><span style="text-align:center">No.</span><span>장비</span><span style="text-align:right">등록일</span></div>
<ul class="bd-list">{rows}</ul><div class="bd-empty" id="bdE" hidden>조건에 맞는 장비가 없습니다.</div>
<p class="bd-note">※ 이 카테고리는 장비를 하나씩 게시판 형식으로 소개합니다. 찾으시는 장비가 없으면 문의해 주세요.</p></div>{js}"""
    open(os.path.join(HERE, cfg["file"]), "w", encoding="utf-8").write(page(f"{cat} | 세일테크노", inner, root))

V3_JS = r"""<script type="importmap">{"imports":{"three":"https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js","three/addons/":"https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"}}</script>
<script type="module">
import * as THREE from 'three';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';
import {mergeVertices} from 'three/addons/utils/BufferGeometryUtils.js';
const box=document.getElementById('v3d');if(box){
const cv=box.querySelector('.v3-canvas'),msg=box.querySelector('.v3-msg'),btns=[...box.querySelectorAll('.v3-m')];
let renderer;try{renderer=new THREE.WebGLRenderer({antialias:true,alpha:true})}catch(err){msg.textContent='이 브라우저에서는 3D 보기를 지원하지 않습니다.'}
if(renderer){
renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.outputColorSpace=THREE.SRGBColorSpace;cv.appendChild(renderer.domElement);
const scene=new THREE.Scene(),cam=new THREE.PerspectiveCamera(32,1,0.1,5000);scene.add(cam);
scene.add(new THREE.HemisphereLight(0xe6f2ff,0x223a5c,1.3));
const k=new THREE.DirectionalLight(0xffffff,2.4);k.position.set(1.2,1.6,1.4);cam.add(k);
const r=new THREE.DirectionalLight(0x7ff0d8,1.0);r.position.set(-1.4,-.4,-1);cam.add(r);
const ctl=new OrbitControls(cam,renderer.domElement);ctl.enableDamping=true;ctl.dampingFactor=.08;
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;ctl.autoRotate=!reduce;ctl.autoRotateSpeed=1.4;
const mat=new THREE.MeshStandardMaterial({color:0x4a97ff,roughness:.42,metalness:.18});
const cache={};let mesh=null,home=null;
function fit(){const w=cv.clientWidth,h=cv.clientHeight;renderer.setSize(w,h,false);cam.aspect=w/h;cam.updateProjectionMatrix()}
new ResizeObserver(fit).observe(cv);
function getData(key,src){return new Promise((ok,no)=>{if(window.STL_MODELS&&STL_MODELS[key])return ok(STL_MODELS[key]);const s=document.createElement('script');s.src=src;s.onload=()=>ok(STL_MODELS[key]);s.onerror=no;document.head.appendChild(s)})}
function geo(d){const bin=atob(d.b),u=new Uint8Array(bin.length);for(let i=0;i<bin.length;i++)u[i]=bin.charCodeAt(i);
 const q=new Int16Array(u.buffer),p=new Float32Array(q.length),sc=d.s/32767;for(let i=0;i<q.length;i++)p[i]=q[i]*sc;
 let g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.BufferAttribute(p,3));g=mergeVertices(g,1e-3);g.computeVertexNormals();g.rotateX(-Math.PI/2);g.center();g.computeBoundingSphere();return g}
async function show(b){btns.forEach(x=>{x.classList.toggle('on',x===b);x.setAttribute('aria-pressed',x===b)});msg.textContent='3D 데이터 불러오는 중…';msg.hidden=false;
 try{const key=b.dataset.key;if(!cache[key])cache[key]=geo(await getData(key,b.dataset.js));
  if(mesh)scene.remove(mesh);mesh=new THREE.Mesh(cache[key],mat);scene.add(mesh);
  const R=cache[key].boundingSphere.radius,dist=R/Math.sin(THREE.MathUtils.degToRad(cam.fov/2))*1.05;
  cam.near=dist/100;cam.far=dist*20;cam.position.set(dist*.55,dist*.5,dist*.68);ctl.target.set(0,0,0);cam.updateProjectionMatrix();ctl.update();home=cam.position.clone();msg.hidden=true}
 catch(err){msg.textContent='3D 데이터를 불러오지 못했습니다.'}}
btns.forEach(b=>b.addEventListener('click',()=>show(b)));
box.querySelector('[data-act=spin]').addEventListener('click',e=>{ctl.autoRotate=!ctl.autoRotate;e.target.textContent=ctl.autoRotate?'자동 회전 끄기':'자동 회전 켜기'});
box.querySelector('[data-act=home]').addEventListener('click',()=>{if(home){cam.position.copy(home);ctl.target.set(0,0,0);ctl.update()}});
if(reduce)box.querySelector('[data-act=spin]').textContent='자동 회전 켜기';
let vis=false;new IntersectionObserver(es=>{vis=es[0].isIntersecting;if(vis&&!mesh)show(btns[0])},{rootMargin:'200px'}).observe(box);
renderer.setAnimationLoop(()=>{if(!vis)return;ctl.update();renderer.render(scene,cam)});
}}
</script>"""

def viewer3d_section(d, root):
    v = d.get("viewer3d")
    if not v: return ""
    ms = "".join(f'<button class="v3-m" data-key="{e(m["key"])}" data-js="{img(root, m["js"])}" aria-pressed="false"><b>{e(m["name"])}</b><small>{e(m.get("desc",""))}</small></button>' for m in v["items"])
    return (f'<section class="sec" id="v3s"><h2>{e(v.get("title","3D 모델 보기"))}</h2>'
            f'<div class="v3" id="v3d"><div class="v3-side"><div class="lbl">SCAN DATA · STL</div>{ms}'
            f'<div class="v3-help">드래그: 돌려 보기<br>휠·두 손가락: 확대·축소<br>오른쪽 드래그: 옮기기</div></div>'
            f'<div class="v3-stage"><div class="v3-canvas"></div><div class="v3-badge">INTERACTIVE 3D</div><div class="v3-msg">3D 보기 준비 중…</div>'
            f'<div class="v3-tools"><button data-act="spin">자동 회전 끄기</button><button data-act="home">처음 위치</button></div></div></div>'
            f'<p class="v3-note">{e(v.get("note",""))}</p></section>{V3_JS}')

def videos_section(d, root):
    vs = d.get("videos")
    if not vs: return ""
    def _cap(x):
        if x.get("title"):
            return f'<figcaption class="vt"><b>{e(x["title"])}</b><span>{e(x.get("desc",""))}</span></figcaption>'
        return f'<figcaption>{e(x["cap"])}</figcaption>'
    figs = "".join(f'<figure><video src="{img(root, x["src"])}" poster="{img(root, x["poster"])}" muted loop playsinline controls preload="none" aria-label="{e(x.get("title") or x.get("cap",""))}"></video>{_cap(x)}</figure>' for x in vs)
    js = """<script>(function(){if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;var vs=document.querySelectorAll('.vids video');var io=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.play().catch(function(){})}else{x.target.pause()}})},{threshold:.4});vs.forEach(function(v){io.observe(v)})})();</script>"""
    return f'<section class="sec" id="vid"><h2>{e(d.get("videos_title","실제 스캔 영상"))}</h2><p style="color:var(--sub);margin:-8px 0 18px">{e(d.get("videos_desc","스캔 과정을 빠르게 재생한 화면 녹화입니다."))}</p><div class="vids{" one" if len(vs)==1 else ""}">{figs}</div></section>{js}'

STATS_CSS = """
.st-box{border-radius:20px;background:linear-gradient(120deg,#0f2440,#1B2B4B 60%,#163a52);color:#fff;padding:30px 32px}
.st-box .st-sub{font-size:14px;color:rgba(255,255,255,.72);margin-bottom:22px}
.st-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.st-grid div{border:1px solid rgba(255,255,255,.12);background:rgba(255,255,255,.04);border-radius:14px;padding:18px}
.st-grid b{display:block;font-size:34px;font-weight:800;letter-spacing:-1px;color:var(--mint);line-height:1.1;font-variant-numeric:tabular-nums}
.st-grid b small{font-size:16px;margin-left:3px;color:#fff;font-weight:700}
.st-grid span{display:block;font-size:13px;color:rgba(255,255,255,.75);margin-top:6px}
.st-note{font-size:12.5px;color:rgba(255,255,255,.55);margin-top:16px;line-height:1.7}
@media(max-width:900px){.st-grid{grid-template-columns:1fr 1fr}.st-grid b{font-size:28px}}
"""
def stats_section(d, root):
    s = d.get("stats")
    if not s: return ""
    items = "".join(f'<div><b>{e(x["num"])}<small>{e(x.get("unit",""))}</small></b><span>{e(x["label"])}</span></div>' for x in s["items"])
    return (f'<style>{STATS_CSS}</style><section class="sec" id="st"><h2>{e(s.get("title","실측 검증"))}</h2>'
            f'<div class="st-box"><div class="st-sub">{e(s.get("sub",""))}</div><div class="st-grid">{items}</div><div class="st-note">{e(s.get("note",""))}</div></div></section>')
