import os, shutil

def copy_program(folder):
	# setting destination folder to copy 
	destination_location = 'D:\\FFOutput'
	# sorce folder absolute path loaction
	folderpath = os.path.abspath(folder)
	# looping through each folder, subfolder and filnames
	for foldername, subfolders, filenames in os.walk(folder):
		for filename in filenames:
			# if filename extension
			if filename.endswith('.png'):
				print(f"Copying {filename}...")
				file_location = (os.path.join(foldername,filename))
				# copy command
				shutil.copy(file_location, destination_location)

copy_program(r'D:\User\brouchuers')