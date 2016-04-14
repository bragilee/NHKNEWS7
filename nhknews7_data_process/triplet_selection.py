"""
This script is to select 5 most different face images in each facetrack using face representations generated 
by openface model.
"""

import os
import sys
import cv2
import math
import numpy as np
import pandas as pd
import argparse

# data_path = '/Users/bragilee/NII-Research/Data/facetrack/nhknews7/nhknews7_identity_facetrack'
data_path = '/Users/bragilee/NII-Research/Data/facetrack/nhknews7/nhknews7_no_photo/raw'
triplet_path = '/Users/bragilee/NII-Research/Data/facetrack/nhknews7/nhknews7_no_photo/triplet'

def main():
    # this provides the path of feature representaions so that all the embeddings could be loaded.
    workDir = "/Users/bragilee/NII-Research/Data/facetrack/nhknews7/nhknews7_no_photo/rep"
    print("Loading embeddings.")
    fname = "{}/labels.csv".format(workDir)
    paths = pd.read_csv(fname, header=None).as_matrix()[:, 1]
    paths = map(os.path.basename, paths)  # Get the filename.

    # Remove the extension.
    paths = map(lambda path: os.path.splitext(path)[0], paths)
    fname = "{}/reps.csv".format(workDir)
    rawEmbeddings = pd.read_csv(fname, header=None).as_matrix()
    embeddings = dict(zip(*[paths, rawEmbeddings]))
    tripletGeneration(embeddings)
    # print embeddings['sadakazutanigaki_2011_01_23_19_00-shot23_36-Track1-Frame19628-Face1']
    # print embeddings['akihito_2006_01_02_19_00-shot02_32-Track1-Frame9244-Face1']
    print 'Finished!'

def removeHiddenFile(list):
    if '.' in list:
        list.remove('.')
    if '..' in list:
        list.remove('..')
    if '.DS_Store' in list:
        list.remove('.DS_Store')
    return list


def tripletSelection(faceimage_directory,embeddings):
    faceimage_dir_return = []
    size = len(faceimage_directory)
    faceimage_directory = (map((lambda faceimage: faceimage.split('.')[0]), faceimage_directory))
    faceimage_rep = {}
    for faceimage in faceimage_directory:
        faceimage_rep[faceimage] = embeddings[faceimage]
    faceimage_distance = np.zeros((size,size))

    for index, value in enumerate(faceimage_directory):
        for sub_index in range(0,size):
            difference = faceimage_rep[faceimage_directory[index]] - faceimage_rep[faceimage_directory[sub_index]]
            distance = np.dot(difference.T, difference)
            faceimage_distance[index][sub_index] = distance
    faceimage_distance_mean = np.mean(faceimage_distance, axis=0)

    for conut in range(0,5):
        ind = np.argmax(faceimage_distance_mean)
        faceimage_dir_return.append(faceimage_directory[ind])
        faceimage_distance_mean[ind] = 0.0 

    faceimage_re = (map((lambda faceimage: faceimage + '.jpg'), faceimage_dir_return))
    return faceimage_re

def tripletGeneration(embeddings):

    identity_directory = removeHiddenFile(os.listdir(data_path))
    for identity in identity_directory:
        identity_directory_path = os.path.join(data_path,identity)
        identity_triplet_directory_path = os.path.join(triplet_path,identity)
        if not os.path.exists(identity_triplet_directory_path):
          os.makedirs(identity_triplet_directory_path)

        facetrack_identity_directory = removeHiddenFile(os.listdir(identity_directory_path))
        for facetrack in facetrack_identity_directory:
            facetrack_identity_directory_path = os.path.join(identity_directory_path,facetrack)  
            facetrack_identity_triplet_directory_path = os.path.join(identity_triplet_directory_path,facetrack)
            if not os.path.exists(facetrack_identity_triplet_directory_path):
                os.makedirs(facetrack_identity_triplet_directory_path)

            faceimage_facetrack_identity_directory = removeHiddenFile(os.listdir(facetrack_identity_directory_path))
            faceimage_selected_directory = tripletSelection(faceimage_facetrack_identity_directory,embeddings)

            for faceimage in faceimage_selected_directory:
                faceimage_facetrack_identity_directory_path = os.path.join(facetrack_identity_directory_path,faceimage)
                faceimage_facetrack_identity_triplet_directory_path = os.path.join(facetrack_identity_triplet_directory_path,faceimage)
                img = cv2.imread(faceimage_facetrack_identity_directory_path)
                cv2.imwrite(faceimage_facetrack_identity_triplet_directory_path,img)

if __name__ == '__main__':
    main()