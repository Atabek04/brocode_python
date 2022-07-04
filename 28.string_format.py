'''
====================================
animal = "cow"
item = "moon"

# print("The ", animal, " jumped over the", item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item))  # positional arguments
# print("The {animal} jumped over the {animal}".format(animal="cow", item="moon")) #keyword argument

# text = "The {} jumped over the {}"
# print(text.format(animal,item))
====================================
'''

'''
====================================
name = "Bro"
print("Hello my name is {}".format(name))
print("Hello my name is {:10}.Nice to meet you".format(name)) #adding a padding
print("Hello my name is {:<10}.Nice to meet you".format(name)) #left aligning
print("Hello my name is {:>10}.Nice to meet you".format(name)) #Right aligning
print("Hello my name is {:^10}.Nice to meet you".format(name)) #Centre aligning
====================================
'''


pi = 3.14159
number = 1000000

print("The number pi is {:.2f}".format(pi)) #float point
print("The number is {:,}".format(number))  #adding coma after 3 zeros
print("The number is {:b}".format(number))  #converting to binary system
print("The number is {:o}".format(number))  #converting to octal system
print("The number is {:x}".format(number))  #converting to hexadecimal system
print("The number is {:e}".format(number))  #converting to scientific notion 