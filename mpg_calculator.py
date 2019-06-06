#################################################MPG####CALCULATOR###############################################################################

print("What is the price per gallon?")
user_price_per_gallon = float(input("$"))

print("How many gallons were purchased?")
user_gallons_purchased = float(input(">"))

print("How many miles were traveled?")
user_miles_travelled = float(input(">"))


def fuel_efficiency(a, b): 
    c = a / b
    return c


def fuel_cost_per_mile(d, e, f):
    g = d / (e / f)
    return g

efficiency = fuel_efficiency(user_miles_travelled, user_gallons_purchased)
cost = fuel_cost_per_mile(user_price_per_gallon, user_miles_travelled, user_gallons_purchased)

efficiency_rounded = round(efficiency, 2)
cost_rounded = round(cost, 2)

print(f"Your fuel efficiency is ", (efficiency_rounded), "Mpg")
print(f"Your fuel cost per mile is $", (cost_rounded), " ")

