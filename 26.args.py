# def add(num1, num2):
#     sum = num1 + num2
#     return sum


# print(add(5, 2))


def add(*stuff):
    sum = 0
    for i in stuff:
        sum += i
    return sum


print(add(5, 3, 4, 0, 5, 1, 2))
