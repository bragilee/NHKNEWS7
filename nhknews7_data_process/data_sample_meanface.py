"""
This script is to generate meanface-dataset of NHKNEWS7.
To change the path when you are running.
"""

import os
import sys
import cv2

facetrack_path = '/Users/bragilee/NII-Research/Data/facetrack/nhknews7/nhknews_track'
# facetrack_path = '/Users/bragilee/NII-Research/Data/facetrack/nhknews7/nhknews_track_test'
# meanface_path = '/Users/bragilee/NII-Research/Data/facetrack/nhknews7/nhknews_meanface'
meanface_path = '/Users/bragilee/Computer Vision/openface/data/nhknews_meanface/raw'
k = 20
person_dir_list = os.listdir(facetrack_path)
for person_dir in person_dir_list:
	if not person_dir.startswith('.'):
		print(person_dir)

# ------------------- code for build directory in meanface ------------------- 
		# person_dir_path_in_meanface = os.path.join(meanface_path,person_dir)
		# if not os.path.exists(person_dir_path_in_meanface):
			# os.makedirs(person_dir_path_in_meanface)
		# print(person_dir_path_in_meanface)
# ---------------------------------------------------------------------------- 

		person_dir_path = os.path.join(facetrack_path,person_dir)
		# print(person_dir_path)
		track_dir_list_in_person = os.listdir(person_dir_path)
		# print(len(track_dir_list_in_person))
		for track_dir in track_dir_list_in_person:
			if not track_dir.startswith('.'):
				track_dir_path = os.path.join(person_dir_path,track_dir)
				# print(track_dir)
# ------------------- code for build directory in meanface ------------------- 
				person_track_dir_in_meanface = person_dir + '_' + track_dir
				# print(person_track_dir_in_meanface)
				track_dir_path_in_person_in_meanface = os.path.join(meanface_path,person_track_dir_in_meanface)
				if not os.path.exists(track_dir_path_in_person_in_meanface):
					os.makedirs(track_dir_path_in_person_in_meanface)
				# print(track_dir_path_in_person_in_meanface)
# ----------------------------------------------------------------------------
				image_list_in_track = os.listdir(track_dir_path)
				# print(len(image_list_in_track))
				try:
					image_list_in_track.remove('.')
					image_list_in_track.remove('..')
					image_list_in_track.remove('.DS_Store')
				except ValueError:
					pass
				# print(image_list_in_track[0])

				number_images = len(image_list_in_track)
				# print(number_images)
				sub_number = number_images / k
				# print(sub_number)
				start_index = sub_number / 2
				# print(start_index)
				end_index = sub_number * k 
				# print(end_index)
				# last_image_index = (end_index + (number_images - end_index) / 2)
				# print(last_image_index)
				while start_index < end_index:
				# 	# print(image_list_in_track[start_index])
				# 	# print(start_index)
				# 	# print(image_list_in_track[start_index])
					image_path_in_track = os.path.join(track_dir_path,image_list_in_track[start_index])
					image_path_in_meanface = os.path.join(track_dir_path_in_person_in_meanface,image_list_in_track[start_index])
				# 	# print(image_path_in_track)
					img = cv2.imread(image_path_in_track)
					cv2.imwrite(image_path_in_meanface,img)
					start_index = start_index + sub_number
				# print(image_list_in_track[last_image_index])
				# last_image_path_in_track = os.path.join(track_dir_path,image_list_in_track[last_image_index])
				# last_image_path_in_meanface = os.path.join(track_dir_path_in_person_in_meanface,image_list_in_track[last_image_index])
				# print(image_path_in_track)
				# img = cv2.imread(last_image_path_in_track)
				# cv2.imwrite(last_image_path_in_meanface,img)
print('************* Finished! ******************')