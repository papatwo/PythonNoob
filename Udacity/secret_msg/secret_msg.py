import os

def rename_files():
	# 1. get file names from a folder
	file_list = os.listdir('../PythonPractice/Udacity/secret_msg/prank')
	saved_path = os.getcwd()
	print('current working dir is', saved_path)

	os.chdir('../PythonPractice/Udacity/secret_msg/prank')
	# 2. for each file, rename filename
	for filename in file_list:
		os.rename(filename, filename.translate(None, '0123456789'))

	os.chdir(saved_path)
rename_files()