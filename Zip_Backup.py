import os, zipfile

def backupZip(folder):
	# get the absolute path of the folder
	folder = os.path.abspath(folder)
	# file_nameing purpose
	number = 1
	while True:
		# creating the zip filename
		zipFileName = folder + '_' + str(number) + '.zip'
		# check the zip filename exists or not
		# if not means brak the loop / exists means increase the number count
		if not os.path.exists(zipFileName):
			break
		number = number + 1
	print(f"Creating {zipFileName}")
	# opening the zipfile in writting mode
	file = zipfile.ZipFile(zipFileName, 'w')
	# looping through folders, subfolders and files in directory
	for foldername, subfolders, filenames in os.walk(folder):
		print(f"addinf file {foldername}")
		# setting the basedirectory folder in zip
		file.write(foldername)

		for filename in filenames:
			current_base = os.path.basename(folder)
			# if an existing zip exists it eliminates
			# You can remove condition " if needed "
			if filename.endswith('.zip'):
				continue
			# combine the folder path and the filepath
			file.write(os.path.join(foldername,filename))
	file.close()

backupZip('D:\\base')