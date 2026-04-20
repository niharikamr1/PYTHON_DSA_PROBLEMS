import math


distance = int(input("Enter the distance(in km):"))
truckMileage = int(input("Enter the truck mileage(km per litre):"))
fuelPrice=int(input("Enter Fuel price(per litre):"))
tollCharges=int(input("Enter the toll charges(one way):"))
dailyWage=int(input("Enter the Daily Wage of a driver:")) 
budget=int(input("Enter the budget planed for the trip:"))
days=int(input("Number of days planned for the trip:"))

fuelCost = (distance/truckMileage) * fuelPrice
days=math.ceil(distance/500) 
driverCost= dailyWage*days
totalTripCost= fuelCost+tollCharges+driverCost


print(f"{days}")
