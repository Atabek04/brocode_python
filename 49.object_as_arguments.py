class Car:

	color = None

class Motorcycle:
	
	color = None

def change_color(vehicle, color):

	vehicle.color = color


bike_1 = Motorcycle()

car_1 = Car()
car_2 = Car()
car_3 = Car()


change_color(car_1, "red")
change_color(car_2, "blue")
change_color(car_3, "silver")

change_color(bike_1, "gold")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)

