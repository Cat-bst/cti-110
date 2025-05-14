# Catherine Best
# 3/6/2025
# P2LAB2
# Create a dictionary
vehicles_mpg = {
 
    "Camaro": 18.21,
 
    "Prius": 52.36,
 
    "Model S": 110,
 
    "Silverado": 26
}
keys = vehicles_mpg.keys()
print("Available vehicles:", list(keys))
vehicle = input("Enter a vehicle to see it's mpg: ")
if vehicle in vehicles_mpg:
 
    mpg = vehicles_mpg[vehicle]
 
    print(f"The {vehicle} gets {mpg} MPG.")
 
    miles = float(input("How many miles will you drive this vehicle? "))
 
    gallons_needed = miles / mpg
 
    print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")