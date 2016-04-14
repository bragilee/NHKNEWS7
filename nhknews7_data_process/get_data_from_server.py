"""
:This part of code is to extract all images from the dataset on the server,
:using ssh protocol and scp command to transfer files from remote to local,
:accordring to annotation file.

@rootDataPath: the directory path of all data on the server.
@alignedDataPath: the local directory path to store data.
@nameFilePath: the file path of annotation file.

"""
import pysftp
import os
import sys
import cv2
import paramiko
from scp import SCPClient

rootDataPath = '/net/per610a/export/das11f/ledduy/Demo-MMWeb/video.archive/facetrack/nhknews7/nhk2002'   
alignedDataPath = '/Users/bragilee/NII-Research/Data/facetrack/nhknews7/nhknews'   
nameFilePath = '/Users/bragilee/NII-Research/Data/facetrack/nhknews7/nhknews7.facetrack.annotation.txt'

sftpURL   =  'per900a.hpc.vpl.nii.ac.jp'
sftpUser  =  'runzeli'
sftpPass  =  '#runzeli'

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
# automatically add keys without requiring human intervention
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )

ssh.connect(sftpURL, username=sftpUser, password=sftpPass)

ftp = ssh.open_sftp()
rootDir = ftp.listdir('/net/per610a/export/das11f/ledduy/Demo-MMWeb/video.archive/facetrack/nhknews7/nhk2002')

for fileRootDir in rootDir:
	# print(fileRootDir)
	if not fileRootDir.startswith('.'):
		secondDataPath = os.path.join(rootDataPath, fileRootDir)
		secondDir = ftp.listdir(secondDataPath)
		# print(secondDataPath)

		for fileSecondDir in secondDir:
			# print(fileSecondDir)
			if not fileSecondDir.startswith('.'):
				thirdDataPath = os.path.join(secondDataPath, fileSecondDir)
				thirdDir = ftp.listdir(thirdDataPath)
				# print(thirdDataPath)

				for fileThirdDir in thirdDir:
					# print(fileThirdDir)
					if not fileThirdDir.startswith('.'):
						fourthDataPath = os.path.join(thirdDataPath,fileThirdDir)
						print(fourthDataPath)

						with open(nameFilePath) as f:
							for line in f:
								line = line.strip()
								val = line.split(',')
								# print(val[1])
								if fileThirdDir == val[1]:
									directory = os.path.join(alignedDataPath,val[0])
									directory = directory.replace(' ','')
									# print(directory)
									if not os.path.exists(directory):
										os.makedirs(directory)
				 						# print(directory)
									fourthDir = ftp.listdir(fourthDataPath)
									# print(fourthDir)
									scp = SCPClient(ssh.get_transport())
									for file in fourthDir:
				 						imagepath = os.path.join(fourthDataPath,file)
				 						# print(imagepath)
										path = os.path.join(directory,file)
										# print(path)
										scp.get(imagepath, path)
									scp.close()
print('Finished.')
