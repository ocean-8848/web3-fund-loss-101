#!/bin/sh
# 一条命令从 src/ 重建全部产物到 dist/：
#   dist/site/      在线版（发布到 claude.ai artifact 的就是这个目录）：手册 + Slides，Mermaid / GSAP 走 cdnjs
#   dist/learning/  学习站：手册 + 学习层（src/learning/）
#   dist/offline/   离线包：完整 HTML 文档，Mermaid / GSAP 放 vendor/，双击即开
set -e
cd "$(dirname "$0")/.."
HB=src/handbook
SITE=dist/site
LEARN=dist/learning
OFF=dist/offline
MERMAID_VERSION=11.12.0
MERMAID_CDN="https://cdnjs.cloudflare.com/ajax/libs/mermaid/$MERMAID_VERSION/mermaid.min.js"
GSAP_VERSION=3.12.5
GSAP_CDN="https://cdnjs.cloudflare.com/ajax/libs/gsap/$GSAP_VERSION/gsap.min.js"

grep -q "$MERMAID_CDN" "$HB/index.html" || { echo "$HB/index.html no longer loads Mermaid $MERMAID_VERSION from cdnjs; update MERMAID_VERSION" >&2; exit 1; }
grep -q "$GSAP_CDN" src/slides/player.tpl.html || { echo "src/slides/player.tpl.html no longer loads GSAP $GSAP_VERSION from cdnjs; update GSAP_VERSION" >&2; exit 1; }

# 1. 在线版：源稿原样 + Slides（slides.html、data/slides.js）
rm -rf "$SITE" && mkdir -p "$SITE"
cp "$HB/index.html" "$SITE/" && cp -R "$HB/data" "$HB/labs" "$SITE/"
python3 tools/make_slides.py

# 2. 学习站：手册外壳 + 学习层
rm -rf "$LEARN" && mkdir -p "$LEARN"
sed -e 's#<title>Web3 行业安全资损 101</title>#<title>Web3 资损 101 学习站</title>#' "$SITE/index.html" > "$LEARN/index.html"
cp -R "$SITE/data" "$SITE/labs" "$SITE/slides.html" "$LEARN/"
{
  # map this handbook's color tokens onto the names the learning layer uses
  echo '<style>:root{--paper:var(--surface);--ground:var(--bg);--ink-2:var(--muted);--rule:var(--line);--tint:var(--surface2);--risk:var(--danger);--risk-soft:var(--danger-soft);--info:var(--accent);--info-soft:var(--accent-soft)}
/* this handbook has its own 本章目录 */.lv-toc,.lv-tocbtn{display:none!important}</style>'
  echo '<script>'
  sed 's#</script#<\\/script#g' src/learning/learn.js
  sed 's#</script#<\\/script#g' src/learning/config.js
  sed 's#</script#<\\/script#g' src/learning/visual.js
  echo '</script>'
} >> "$LEARN/index.html"
{ echo '<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px -apple-system,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>'; cat "$LEARN/index.html"; } > "$LEARN/preview.html"

# 3. 离线包：包成完整文档，CDN 换成 vendor/
mkdir -p "$OFF/vendor"
[ -s "$OFF/vendor/mermaid.min.js" ] || curl -fsSL "$MERMAID_CDN" -o "$OFF/vendor/mermaid.min.js"
[ -s "$OFF/vendor/gsap.min.js" ] || curl -fsSL "$GSAP_CDN" -o "$OFF/vendor/gsap.min.js"
rm -rf "$OFF/data" "$OFF/labs" && cp -R "$SITE/data" "$SITE/labs" "$OFF/"
{
  echo '<!doctype html>'
  echo '<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
  echo '<style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}html{scroll-padding-top:env(safe-area-inset-top,0px)}body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif}img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style>'
  echo '</head><body>'
  sed "s#<script src=\"$MERMAID_CDN\"></script>#<script src=\"vendor/mermaid.min.js\"></script>#" "$SITE/index.html"
  echo '</body></html>'
} > "$OFF/index.html"
sed "s#<script src=\"$GSAP_CDN\"></script>#<script src=\"vendor/gsap.min.js\"></script>#" "$SITE/slides.html" > "$OFF/slides.html"
cp tools/offline-README.md "$OFF/README.md"

echo "built dist/site, dist/learning, dist/offline"
