from abc import ABC, abstractclassmethod, abstractmethod

class Vehicle(ABC):

	@abstractmethod
	def go(self):
		pass
	
	@abstractmethod
	def stop(self):
		pass

class Car(Vehicle):
	def go(self):
		print("You drive a car!")

	def stop(self):
		print("This car is stopped")

class Motorcycle:
	def go(self):
		print("YOu ride a Motorcycle!")

	def stop(self):
		print("this motorcycle is stopped!")

vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

car.go
motorcycle.go

car.stop()
motorcycle.stop()