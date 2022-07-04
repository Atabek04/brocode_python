from ast import excepthandler
import os
import shutil

path = 'messages.py'

try:
	os.remove(path)  # can remove file
	# os.rmdir(path)	#can remove folder
	# shutil.rmtree(path)  #removing tree
except FileNotFoundError:
	print("The file was not found")
except PermissionError:
	print("You don't have access to file")
except OSError:
	print("The directory isn't empty")
else:
	print("File was successfully deleted")