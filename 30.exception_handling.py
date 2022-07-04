try:
	numerator = int(input("Enter the numerator: "))
	denominator = int(input("Enter the denominator: "))
	result = numerator / denominator


except ZeroDivisionError as e:
	print(e)
	print("The denominator can't be zero!")
except ValueError as e:
	print(e)
	print("Enter only numbers!")
except Exception as e:
	print(e)
	print("Something went wrong!")

else:
	print(result)
