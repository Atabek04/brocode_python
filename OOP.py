#Differences between class variables and variables

class Car:

	wheels = 4 #class variables

	def __init__(self, make, model, year, color): # <=This is a constructor 
		self.make = make
		self.model = model
		self.year = year
		self.color = color

	def drive(self):
		print("This "+self.model+" is Driving")
	
	def stop(self):
		print("This "+self.model+" is stopped")

#new line
	def crash(self):
		print("The car is crashed")