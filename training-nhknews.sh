#!/bin/bash

cd ./../

for N in {1..8}; do ./util/align-dlib.py \
  /home/runzeli/local/nhknews7/nhknews_day/raw align outerEyesAndNose \
  data/nhknewsday//dlib-affine-size:96 --size 96 & done

./util/prune-dataset.py data/nhknewsday//dlib-affine-size:96 --numImagesThreshold 3

./training/main.lua -data data/nhknewsday/dlib-affine-size:96 \
  -cache /home/runzeli/local/openface/training/work \
  -peoplePerBatch 15 \
  -imagesPerPerson 20 \
  -nEpochs 5
  -testing false