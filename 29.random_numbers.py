import random

x = random.randint(1,6)
y = random.random()
 
my_list= ['rock', 'paper', 'scissors']
z = random.choice(my_list)

card = [1,2,3,4,5,8,6,7,9,"J","Q", "K", "A"]
random.shuffle(card)

print(card)