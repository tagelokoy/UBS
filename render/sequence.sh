#!/bin/sh
# Render the BB·74 explode clip as numbered transparent PNGs.
#   sh render/sequence.sh [frames] [WxH] [samples]
set -e
cd "$(dirname "$0")/.."
N=${1:-90}; RES=${2:-1920x1080}; SAMPLES=${3:-96}
OUT=render/out/seq; mkdir -p $OUT
i=0
while [ $i -lt $N ]; do
  f=$(printf "%03d" $i)
  if [ ! -f $OUT/f$f.png ]; then   # skip frames already rendered, so a stopped run can resume
    t=$(python3 -c "print($i/($N-1))")
    blender -b -P render/bb74.py -- --t $t --out $OUT/f$f.png --res $RES --samples $SAMPLES >/dev/null 2>&1
    echo "frame $f done"
  fi
  i=$((i+1))
done
echo "all $N frames done"
