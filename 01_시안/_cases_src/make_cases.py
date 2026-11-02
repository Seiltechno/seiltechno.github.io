# -*- coding: utf-8 -*-
"""_cases_src/*.txt (VE 자료 요약 원본) → site/_cases/*.md 로 변환합니다.
한 번만 실행하면 됩니다. 실행: python3 _cases_src/make_cases.py"""
import os, re, glob, yaml
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(HERE, "..", "..", "site")
OUT = os.path.join(SITE, "_cases"); os.makedirs(OUT, exist_ok=True)
KEYS = ["title","title_en","type","maker","date","author","customer","country","industry","products","image","image_src","original_url","pdf","excerpt","order"]
dl = []
cnt = {}
for src in sorted(glob.glob(os.path.join(HERE, "ve_*.txt"))):
    text = open(src, encoding="utf-8").read()
    for n, blk in enumerate(re.split(r"^@@ ", text, flags=re.M)[1:]):
        slug, rest = blk.split("\n", 1)
        head, body = rest.split("\n==\n", 1)
        d = {}
        for line in head.strip().split("\n"):
            k, _, v = line.partition(":"); d[k.strip()] = v.strip()
        d["maker"] = "Vision Engineering"
        d["products"] = [p.strip() for p in d.get("products", "").split(",") if p.strip()]
        d["original_url"] = d.pop("url", "")
        ext = os.path.splitext(d["image_src"].split("?")[0])[1].lower() or ".jpg"
        d["image"] = "/assets/img/cases/%s%s" % (slug.strip(), ext)
        cnt[d["type"]] = cnt.get(d["type"], 0) + 1; d["order"] = cnt[d["type"]]
        dl.append((slug.strip() + ext, d["image_src"]))
        fm = {k: d.get(k, "") for k in KEYS}
        out = "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=1000) + "---\n" + body.strip() + "\n"
        open(os.path.join(OUT, slug.strip() + ".md"), "w", encoding="utf-8").write(out)
# 이미지 내려받기 목록 (Windows 배치 파일이 사용)
os.makedirs(os.path.join(SITE, "assets", "img", "cases"), exist_ok=True)
open(os.path.join(HERE, "..", "..", "_tools", "case_images.txt"), "w", encoding="utf-8").write("".join("%s\t%s\n" % x for x in dl))
print("변환 완료:", len(dl), "건")
