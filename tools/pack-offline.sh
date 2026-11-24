#!/bin/sh
# Pack the offline edition of Web3 行业安全资损 101 into web3-loss-101-site/:
# the source (index.html, data/, labs/ at the repo root) wrapped in a full HTML document,
# with Mermaid served from vendor/ instead of cdnjs so charts render without a network,
# plus the Slides player (slides.html) with GSAP served from vendor/ too.
set -e
cd "$(dirname "$0")/.."
OUT=web3-loss-101-site
MERMAID_VERSION=11.12.0
CDN="https://cdnjs.cloudflare.com/ajax/libs/mermaid/$MERMAID_VERSION/mermaid.min.js"
GSAP_VERSION=3.12.5
GSAP_CDN="https://cdnjs.cloudflare.com/ajax/libs/gsap/$GSAP_VERSION/gsap.min.js"

mkdir -p "$OUT/vendor"
if [ ! -s "$OUT/vendor/mermaid.min.js" ]; then
  curl -fsSL "$CDN" -o "$OUT/vendor/mermaid.min.js"
fi
if [ ! -s "$OUT/vendor/gsap.min.js" ]; then
  curl -fsSL "$GSAP_CDN" -o "$OUT/vendor/gsap.min.js"
fi
grep -q "$GSAP_CDN" slides.html || { echo "slides.html no longer loads GSAP $GSAP_VERSION from cdnjs; update GSAP_VERSION" >&2; exit 1; }
grep -q "$CDN" index.html || { echo "index.html no longer loads Mermaid $MERMAID_VERSION from cdnjs; update MERMAID_VERSION" >&2; exit 1; }

rm -rf "$OUT/data" "$OUT/labs" && cp -R data "$OUT/data" && cp -R labs "$OUT/labs"
{
  echo '<!doctype html>'
  echo '<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
  echo '<style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}html{scroll-padding-top:env(safe-area-inset-top,0px)}body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif}img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style>'
  echo '</head><body>'
  sed "s#<script src=\"$CDN\"></script>#<script src=\"vendor/mermaid.min.js\"></script>#" index.html
  echo '</body></html>'
} > "$OUT/index.html"
# Slides player: GSAP from vendor/ as well
sed "s#<script src=\"$GSAP_CDN\"></script>#<script src=\"vendor/gsap.min.js\"></script>#" slides.html > "$OUT/slides.html"
echo "packed $OUT ($(wc -c < "$OUT/index.html") bytes index.html)"
