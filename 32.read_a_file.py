try:
	with open("C:\\Users\\107\\Desktop\\texxt.txt") as file:
		print(file.read())
except FileNotFoundError:
	print("file was not found :(")