#!/usr/bin/env python3
"""Build dist/site/slides.html (the Slides player, data inlined) and dist/site/data/slides.js (which chapters have slides).

Sources: src/slides/<chapter id>/narration.json + src/slides/<chapter id>/compositions/<scene id>.html,
player shell src/slides/player.tpl.html; chapter list from src/handbook/data/. There is no voice-over: each narration line gets a reading time
from its length, and those times drive the scene timelines the same way cues.json does in course-video.
"""
import argparse, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLIDES = os.path.join(ROOT, "src", "slides")
HANDBOOK = os.path.join(ROOT, "src", "handbook")
SITE = os.path.join(ROOT, "dist", "site")
GROUPS = {"o": "总论", "g": "手法归纳", "d": "防御与附录"}
LEAD, GAP, TAIL = 0.3, 0.0, 0.9  # seconds before the first line / between lines / after the last line


def read_time(text):
    """Seconds to read one caption line and watch its animation."""
    n = len(re.sub(r"\s", "", text))
    return round(min(max(1.6 + n * 0.17, 4.0), 10.0), 2)


def chapters():
    """O/G/D chapters in handbook order, read from the source data files."""
    out = []
    for f in ("core.js", "groups.js"):
        src = open(os.path.join(HANDBOOK, "data", f), encoding="utf-8").read()
        for m in re.finditer(r'\{id:"([ogd]\d\d)",code:', src):
            head = src[m.start(): m.start() + 400]
            code = re.search(r'code:"([^"]+)"', head).group(1)
            title = re.search(r'title:"([^"]+)"', head).group(1)
            out.append({"id": m.group(1), "code": code, "title": title, "group": GROUPS[m.group(1)[0]]})
    return out


def scene(ch, sc, lines):
    path = os.path.join(SLIDES, ch, "compositions", sc["id"] + ".html")
    t, cues = LEAD, []
    for text in lines:
        d = read_time(text)
        cues.append([round(t, 2), round(t + d, 2)])
        t += d + GAP
    dur = round(t - GAP + TAIL, 2)
    if not os.path.exists(path):
        raise SystemExit(f"missing scene file {path}")
    src = open(path, encoding="utf-8").read()
    inner = src[src.index("<template>") + 10: src.rindex("</template>")]
    sid = f"S-{ch}-{sc['id']}"
    inner = (inner.replace("/*CUES*/{}/*END*/", json.dumps({"L": cues, "d": dur}))
                  .replace('id="root"', f'id="{sid}"').replace("#root", "#" + sid))
    inner = re.sub(r'data-duration="[\d.]+"', f'data-duration="{dur}"', inner, count=1)
    js = "\n".join(re.findall(r"<script>(.*?)</script>", inner, re.S))
    html = re.sub(r"<script>.*?</script>", "", inner, flags=re.S).strip()
    return {"id": sc["id"], "title": sc.get("title", sc["id"]), "d": dur,
            "lines": [[c[0], c[1], x] for c, x in zip(cues, lines)], "html": html, "js": js}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="build just this chapter into slides/<id>/preview.html (for checking; touches nothing else)")
    a = ap.parse_args()
    chs = chapters()
    for c in chs:
        if a.only and c["id"] != a.only:
            continue
        n = os.path.join(SLIDES, c["id"], "narration.json")
        if not os.path.exists(n):
            continue
        nar = json.load(open(n, encoding="utf-8"))
        c["deck"] = nar.get("title", c["title"])
        c["scenes"] = [scene(c["id"], s, s["lines"]) for s in nar["scenes"]]
    tpl = open(os.path.join(SLIDES, "player.tpl.html"), encoding="utf-8").read()
    data = json.dumps(chs, ensure_ascii=False).replace("</", "<\\/").replace("<!--", "<\\u0021--")
    html = tpl.replace("/*DATA*/[]", data)
    ready = [c for c in chs if c.get("scenes")]
    stats = (f"{len(ready)}/{len(chs)} chapters, {sum(len(s['lines']) for c in ready for s in c['scenes'])} pages, "
             f"{sum(s['d'] for c in ready for s in c['scenes']):.0f}s")
    if a.only:
        out = os.path.join(SLIDES, a.only, "preview.html")
        open(out, "w", encoding="utf-8").write(html.replace('href="index.html', 'href="../../handbook/index.html'))
        print(f"{out}: {stats}")
        return
    os.makedirs(os.path.join(SITE, "data"), exist_ok=True)
    open(os.path.join(SITE, "slides.html"), "w", encoding="utf-8").write(html)
    idx = {c["id"]: {"pages": sum(len(s["lines"]) for s in c["scenes"])} for c in ready}
    open(os.path.join(SITE, "data", "slides.js"), "w", encoding="utf-8").write(
        "/* 生成文件：tools/make_slides.py。有 Slides 的章节及页数 */\nH.slides=" + json.dumps(idx) + ";\n")
    print(f"dist/site/slides.html: {stats}")


if __name__ == "__main__":
    main()
