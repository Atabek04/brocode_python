class Animal:

	alive = True

	def eat(self):
		print("This animal is eating")
	
	def sleep(self):
		print("This animal is sleeping")


class Rabbit(Animal): #Rabbit is child class, Animal is a parent class
	def run(self):
		print("The rabbit is running")

class Fish(Animal):
	def swim(self):
		print("The fish is swimming")

class Hawk(Animal):
	def fly(self):
		print("This hawk is flying")

rabbit = Rabbit()
fish  = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()