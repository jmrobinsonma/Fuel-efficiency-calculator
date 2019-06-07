##################################################### MPG  CALCULATOR ##########################################################################

print("What is the price per gallon?")
user_price_per_gallon = float(input("$"))

print("How many gallons were purchased?")
user_gallons_purchased = float(input(">"))

print("How many miles were traveled?")
user_miles_travelled = float(input(">"))


class Mpg:
	
	def __init__(self, user_price_per_gallon, user_gallons_purchased, user_miles_travelled):
		self.price = user_price_per_gallon 
		self.gallons = user_gallons_purchased
		self.miles = user_miles_travelled
	
	def fuel_efficiency(self):
		efficiency = self.miles / self.gallons
		rounded_fuel_efficiency = round(efficiency, 2)
		final_statement = print("\nYour fuel efficiency is {} Miles Per Gallon".format(rounded_fuel_efficiency))
		return final_statement
		
	def fuel_cost_per_mile(self):
		fuel_cost = self.price / (self.miles / self.gallons)
		rounded_fuel_cost = round(fuel_cost, 2)
		final_statement0 = print("Your fuel cost is ${} per mile".format(rounded_fuel_cost))
		return final_statement0
		

my_car = Mpg(user_price_per_gallon, user_gallons_purchased, user_miles_travelled)	

print (Mpg.fuel_cost_per_mile(my_car))
print(my_car.fuel_efficiency())


