import argparse

parser = argparse.ArgumentParser(description='Fuel efficiency calculator has two functions defined in the MPG class. The fuel efficiency function\
			divides the miles by the gallons and returns the result rounded to two decimal places. The fuel cost per mile function returns the\
			result of dividing fuel efficiency by the price paid per gallon, also rounded to two decimal places.')

parser.add_argument('user_price_per_gallon', metavar='', type=float, help='Enter the price paid per gallon of fuel as type <float/int>')
parser.add_argument('user_gallons_purchased', metavar='', type=float,  help='Enter the number of gallons purchased as type <float/int>')
parser.add_argument('user_miles_travelled', metavar='', type=float,  help='Enter the number of miles traveled as type <float/int>')

group = parser.add_mutually_exclusive_group()
group.add_argument('-q','--quiet',action='store_true')
group.add_argument('-v','--verbose',action='store_true')

args = parser.parse_args()

class Mpg:
	""" FUEL EFFICIENCY AND FUEL COST PER MILE FUNCTIONS"""	
	def __init__(self, user_price_per_gallon, user_gallons_purchased, user_miles_travelled):
		self.price = user_price_per_gallon 
		self.gallons = user_gallons_purchased
		self.miles = user_miles_travelled
	
	def fuel_efficiency(self):
		efficiency = self.miles / self.gallons
		return round(efficiency, 2)
		 
		
	def fuel_cost_per_mile(self):
		fuel_cost = self.price / (self.miles / self.gallons)
		return round(fuel_cost, 2)
		
my_car = Mpg(args.user_price_per_gallon, args.user_gallons_purchased, args.user_miles_travelled)	

if args.verbose:
	print (f"\nYour fuel efficiency is {my_car.fuel_efficiency()}")
	print(f"\nYour fuel cost is ${my_car.fuel_cost_per_mile()} per mile")

