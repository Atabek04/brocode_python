text = "\nHave a nice day!\nSee ya"


with open("C:\\Users\\107\\Desktop\\text.stxt", "a") as file: #mode "a" for append; "w" for overwrite
	file.write(text)