import os

source = "new_folder"
destination = "C:\\Users\\107\\Desktop\\new_folder"

try:
	if os.path.exists(destination):
		print("There is already a file!")
	else:
		os.replace(source, destination)
		print(source," was moved")
except FileNotFoundError:
	print("404")