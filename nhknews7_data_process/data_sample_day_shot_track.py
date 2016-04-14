""" This script is to sample obtained data on the local in different format,
:to be used in further steps

@nameFilePath: the path of annotation file.
@nameRawFolder: the directory path of raw data.
@nameNewFolder: the directory path to sampled data.

"""

import os
import sys
import cv2

nameFilePath = '/Users/bragilee/NII-Research/Data/metadata/nhknews7.facetrack.annotation.txt'
nameRawFolder = '/Users/bragilee/NII-Research/Data/facetrack/nhknews7/nhknews'
nameNewFolder = '/Users/bragilee/NII-Research/Data/facetrack/nhknews7/nhknews_track'

# =======================================================
# This part of code is to align images into sub directories,
# according to shot ID.
# The folder should be created in advance.
# =======================================================

for folder_in_raw in os.listdir(nameRawFolder):
	if not folder_in_raw.startswith('.'):
		for folder_in_new in os.listdir(nameNewFolder):
			if folder_in_new == folder_in_raw:
				path_raw = os.path.join(nameRawFolder,folder_in_raw)
				# print(pathraw)
				path_new = os.path.join(nameNewFolder,folder_in_new)
				# print(pathnew)
				for file_in_raw in os.listdir(path_raw):
					if not file_in_raw.startswith('.'):
						# print(fileinraw)
						file_in_raw_path = os.path.join(path_raw,file_in_raw)
						# # print(fileinraw)
						file_in_raw_list = file_in_raw.split('-')
						# print(file_in_raw_list)

						file_in_raw_list_track = file_in_raw_list[1] + '_' + file_in_raw_list[2]
						# print(file_in_raw_list_track)
						sub_dir_name = file_in_raw_list[0]+'_' + file_in_raw_list_track
						# print(sub_dir_name)
						sub_dir_path = os.path.join(path_new,sub_dir_name)
						# print(sub_dir_path)
						if not os.path.exists(sub_dir_path):
							os.makedirs(sub_dir_path)

						file_prefix = file_in_raw_list[0]+'_' + file_in_raw_list_track
						# print(file_prefix)
						if file_prefix == sub_dir_name:
							# print(file_prefix)
							file_in_sub_dir_path = os.path.join(sub_dir_path,file_in_raw)
							if not os.path.exists(file_in_sub_dir_path):
								image = cv2.imread(file_in_raw_path)
								cv2.imwrite(file_in_sub_dir_path,image)

print('\n++++++++++++++++Finished+++++++++++++++++++')