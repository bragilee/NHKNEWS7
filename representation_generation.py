import os
import sys
import argparse
import subprocess

"""
The feature extraction is running in the shell. Generally we use the command directly to extract feature of 
image by referencing "https://cmusatyalab.github.io/openface/models-and-accuracies/".

In this script, it is supposed you are in the "openface" directory with this script.

The description is not good, but you can have a reference.
"""

def main():
	parser = argparse.ArgumentParser()

	# provide the path of dataset
	parser.add_argument("--datasetPath", type=str, help="The path of Openface.")
	# provide the name of datasetName, this one is used to store aligned data within "openface" directory.
	parser.add_argument("--datasetName", tyoe=str, help="The name of the dataset.")
	args = parser.parse_args()

	datasetPath = args.datasetPath
	datasetName = args.datasetName
	# note the aligned image will be stored in "data/{datasetName}" in openface directory
    meanFaceAlignedPath = "data/" + datasetName + "/dlib-affine-sz:96"

    # note the feature representation will be stored in "evaluation/{datasetName}.{model}"
    repsPath = "evaluation/" + datasetName + ".nn4.small2.v1.reps"
    os.chdir(os.getcwd())

    # to process image and store aligned images
    subprocess.call(["./util/align-dlib.py", datasetPath, "align", "outerEyesAndNose", meanFaceAlignedPath])

    # to fallback images which cannot be aligned
    subprocess.call(["./util/align-dlib.py", datasetPath, "align", "outerEyesAndNose", meanFaceAlignedPath, "--size", "96", "--fallbackLfw", datasetPath])

    # to get representation
    subprocess.call(["./batch-represent/main.lua", "-outDir", repsPath, "-model", "models/openface/nn4.small2.v1.t7", "-data", meanFaceAlignedPath])

if __name__ == '__main__':
    main()