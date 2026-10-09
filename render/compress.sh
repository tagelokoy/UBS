#!/bin/sh
# Compress the rendered clip for the site. The page background is baked into each
# frame (no alpha), which keeps the soft shadow smooth and the files small; one set
# per theme, and the page loads only the one it needs.
#   sh render/compress.sh  ->  img/bb74-open/{light,dark}/f000.webp (1600 wide) and …/m/ (960 wide)
set -e
cd "$(dirname "$0")/.."
IN=render/out/seq; OUT=img/bb74-open; TMP=$(mktemp -d)
for theme in light:E3E5E0 dark:0D0F0E; do   # must match --bg in index.html
  name=${theme%%:*}; col=${theme##*:}
  mkdir -p $OUT/$name/m
  for f in $IN/f*.png; do
    n=$(basename $f .png)
    ffmpeg -loglevel error -y -f lavfi -i "color=c=0x${col}:s=1920x1080" -i $f -filter_complex overlay -frames:v 1 $TMP/$n.png
    cwebp -quiet -q 76 -m 6 -sharp_yuv -resize 1600 0 $TMP/$n.png -o $OUT/$name/$n.webp
    cwebp -quiet -q 74 -m 6 -sharp_yuv -resize 960 0 $TMP/$n.png -o $OUT/$name/m/$n.webp
  done
done
rm -rf $TMP
du -sh $OUT/*/ $OUT/*/m
