#!/bin/bash

cd ./../

for N in {1..8}; do ./util/align-dlib.py data/lfw/raw align outerEyesAndNose \
  data/lfw/dlib-affine-sz:96 --size 96 & done

./util/align-dlib.py data/lfw/raw align outerEyesAndNose data/lfw/dlib-affine-sz:96 \
  --size 96 --fallbackLfw data/lfw/deepfunneled

./batch-represent/main.lua \
  -outDir evaluation/lfw.nn4.small2.v1.reps \
  -model models/openface/nn4.small2.v1.t7 \
  -data data/lfw/dlib-affine-sz:96

./evaluation/lfw.py \
  —-workDir lfw.nn4.small2.v1.reps
