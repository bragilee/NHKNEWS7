The script is calling subprocess model to finish the shell execution.

In openface official website, it provides way to run directly in shell environment, but it will take a long time on large dataset.

####This example is for lfw dataset

* Preprocess the raw lfw images, change 8 to however many separate processes you want to run: 

```
for N in {1..8}; do ./util/align-dlib.py data/lfw/raw align outerEyesAndNose data/lfw/dlib-affine-sz:96 --size 96 & done. 
```
or just run in single process:

script + original data location + align + alignment model + alignment data location + size specification 

```
./util/align-dlib.py data/lfw/raw align outerEyesAndNose data/lfw/dlib-affine-sz:96 --size 96
```
* Fallback to deep funneled versions for images that dlib failed to align: 

script + original data location + align + alignment model + alignment data location + size specification + fallbackLfw + fallback data location

```
./util/align-dlib.py data/lfw/raw align outerEyesAndNose data/lfw/dlib-affine-sz:96 --size 96 --fallbackLfw data/lfw/deepfunneled
```

* Generate representations with:

script + output dir specification and fileapth + model specification and filepath + data specification and filepath

```
./batch-represent/main.lua -outDir evaluation/lfw.nn4.small2.v1.reps -model models/openface/nn4.small2.v1.t7 -data data/lfw/dlib-affine-sz:96
```

* Generate the ROC curve from the evaluation directory with:

script + representation specification and filepath

``` 
./lfw.py --wordDir lfw.nn4.small2.v1.reps 
```

This creates roc.pdf in the lfw.nn4.small2.v1.reps directory.


####Note for NHKNEWS7 Dataset

In nhknews7 dataset, we donot have the specifically fallback dataset, so I make it the same as the raw dataset.

In nhknews7 dataset, when we evaluat, I generate my labels and pairs for evaluation. I will upload it later. 