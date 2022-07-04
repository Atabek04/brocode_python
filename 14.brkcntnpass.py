#Loop controllers

"""
-----------break-----------
while True:
    name = input("What's your name?")
    if name != "":
        print(name)
        break
---------------------------
"""

"""
-----------continue-----------
phone_number = "124-231-132"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")
------------------------------
"""

friends = ["Mark ", "Python ", "Mini ", "Sony ", "John "]
for i in friends:
    if i == "Sony ":
        pass
    else:
        print(i, end="")
