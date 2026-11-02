# -*- coding: utf-8 -*-
# 제품목록 상단 대표 카테고리 데크 (build_preview.py 안에서 실행)
CAT_META = {
 "현미경": ("MICROSCOPE", '<circle cx="9" cy="5" r="2"/><path d="M9 7l3 7M7.5 14h7M6 21h13M8 21v-3h7v3M15 10a5 5 0 0 1 1 9"/>'),
 "측정 시스템": ("METROLOGY", '<rect x="2.5" y="8" width="19" height="8" rx="1.5"/><path d="M6.5 8v3M10 8v4.5M13.5 8v3M17 8v4.5"/>'),
 "AI 검사·측정": ("AI INSPECTION", '<rect x="6" y="6" width="12" height="12" rx="2.5"/><path d="M9 2.5V6M15 2.5V6M9 18v3.5M15 18v3.5M2.5 9H6M2.5 15H6M18 9h3.5M18 15h3.5"/><path d="M10 14.5l2-5 2 5M10.7 13h2.6"/>'),
 "머신비전": ("MACHINE VISION", '<rect x="2.5" y="7" width="13" height="10" rx="2"/><path d="M15.5 10.5l6-3.5v10l-6-3.5"/><circle cx="9" cy="12" r="2.5"/>'),
 "3D·특수 센싱": ("3D & SENSING", '<path d="M12 2.8l8 4.6v9.2L12 21.2l-8-4.6V7.4z"/><path d="M12 12l8-4.6M12 12v9.2M12 12L4 7.4"/>'),
}
CAT_CSS = """
.hx{padding:0 0 44px;background:radial-gradient(1200px 380px at 85% -10%,rgba(0,201,167,.10),transparent 60%),linear-gradient(120deg,var(--navy),var(--navy2))}
.hx nav.deck{display:block!important;flex:none;gap:0;font-weight:400;font-size:inherit;background:rgba(6,14,30,.35);border-bottom:1px solid rgba(255,255,255,.08);padding:22px 0 24px}
.deck-head{display:flex;align-items:baseline;gap:12px;margin-bottom:14px}
.deck-head b{font-size:13px;font-weight:800;letter-spacing:.4px;color:#fff}
.deck-head span{font-size:11px;letter-spacing:2px;color:rgba(255,255,255,.45);font-weight:700}
.deck-row{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}
.dk{position:relative;display:flex;flex-direction:column;gap:10px;padding:16px 16px 14px;border-radius:14px;border:1px solid rgba(255,255,255,.12);background:rgba(255,255,255,.04);color:#fff;transition:background .25s cubic-bezier(.4,0,.2,1),transform .25s cubic-bezier(.4,0,.2,1),border-color .25s}
.dk:hover{background:rgba(255,255,255,.09);border-color:rgba(255,255,255,.26);transform:translateY(-2px)}
.dk:focus-visible{outline:2px solid var(--mint);outline-offset:2px}
.dk-top{display:flex;justify-content:space-between;align-items:center}
.dk-ic{width:38px;height:38px;border-radius:10px;display:grid;place-items:center;background:rgba(255,255,255,.08);color:#9fd9ff}
.dk-ic svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.dk-n{font-size:12px;font-weight:800;color:rgba(255,255,255,.4);font-variant-numeric:tabular-nums}
.dk-name{font-size:17px;font-weight:800;letter-spacing:-.3px;line-height:1.25}
.dk-en{font-size:10.5px;letter-spacing:1.6px;font-weight:700;color:rgba(255,255,255,.5)}
.dk-cnt{font-size:12px;font-weight:700;color:var(--mint)}
.dk.soon{opacity:.55}.dk.soon .dk-cnt{color:rgba(255,255,255,.6)}
.dk.on{background:#fff;border-color:#fff;color:var(--navy);box-shadow:0 14px 34px rgba(0,0,0,.28)}
.dk.on:before{content:"";position:absolute;left:16px;right:16px;top:0;height:3px;border-radius:0 0 3px 3px;background:var(--mint)}
.dk.on .dk-ic{background:var(--navy);color:var(--mint)}.dk.on .dk-n{color:var(--blue)}.dk.on .dk-en{color:var(--sub)}.dk.on .dk-cnt{color:#0a8f78}
.dk.on:hover{transform:none}
.dk.on.soon{opacity:1}
.hx-body{display:flex;align-items:flex-end;gap:26px;padding-top:34px}
.hx-num{font-size:96px;line-height:.8;font-weight:800;letter-spacing:-4px;color:transparent;-webkit-text-stroke:1.5px rgba(255,255,255,.28);flex:none}
.hx-eb{font-size:11px;letter-spacing:2.4px;font-weight:800;color:var(--mint);margin:10px 0 4px}
.hx h1{font-size:44px;letter-spacing:-1.2px;line-height:1.1}
.hx .crumb{margin:0}
.hx p.hx-desc{opacity:.82;margin-top:10px;max-width:680px}
@media(max-width:900px){.deck-row{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-left:24px;margin:0 -24px;padding:0 24px 4px;scrollbar-width:none}.deck-row::-webkit-scrollbar{display:none}.dk{flex:0 0 160px;scroll-snap-align:start}.hx-num{font-size:64px;letter-spacing:-3px}.hx h1{font-size:32px}.hx-body{gap:16px}}
@media(max-width:600px){.hx-num{display:none}.hx-body{padding-top:26px}}
"""
ARIA = ' aria-current="page"'
def cat_deck(cat, all_items, root):
    tiles = ""
    for i, c in enumerate(CATS):
        en, ic = CAT_META[c]
        n = sum(1 for d in all_items if d.get("category") == c)
        on = c == cat
        cnt = f"{n}개 제품" if n else "준비 중"
        tiles += (f'<a class="dk{" on" if on else ""}{" soon" if not n else ""}" href="{cat_link(c, root)}"{ARIA if on else ""}>'
                  f'<div class="dk-top"><span class="dk-ic"><svg viewBox="0 0 24 24" aria-hidden="true">{ic}</svg></span><span class="dk-n">{i+1:02d}</span></div>'
                  f'<div><div class="dk-name">{c}</div><div class="dk-en">{en}</div></div><div class="dk-cnt">{cnt}</div></a>')
    return f'<nav class="deck" aria-label="제품 카테고리"><div class="wrap"><div class="deck-head"><b>제품 카테고리</b><span>{len(CATS)} CATEGORIES</span></div><div class="deck-row">{tiles}</div></div></nav>'
def cat_hero(cat, all_items, root, desc):
    i = CATS.index(cat) + 1
    en = CAT_META[cat][0]
    return (f'<style>{CAT_CSS}</style><section class="hero hx">{cat_deck(cat, all_items, root)}'
            f'<div class="wrap hx-body"><div class="hx-num" aria-hidden="true">{i:02d}</div><div><div class="crumb">홈 › 제품소개 › {cat}</div>'
            f'<div class="hx-eb">{en}</div><h1>{cat}</h1><p class="hx-desc">{desc}</p></div></div></section>'
            '<script>(function(){var r=document.querySelector(".deck-row"),a=r&&r.querySelector(".dk.on");if(a&&r.scrollWidth>r.clientWidth){r.scrollLeft=a.offsetLeft-r.offsetLeft-24}})();</script>')
