name = "Bro"    # global scope (available inside & outside functions)


def display_name():
    name = "Code"  # local scope (available inly inside this function)
    print(name)


print(name)
display_name()
