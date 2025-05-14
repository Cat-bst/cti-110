# Catherine Best
# 4/30/2025
# P3LAB
# Amount of change calculator

amount = float(input("Enter the amount of money as a float: "))

cents = int(round(amount * 100))

if cents == 0:
    print("No change")
else:
    dollars = cents // 100
    cents -= dollars * 100

    quarters = cents // 25
    cents -= quarters * 25

    dimes = cents // 10
    cents -= dimes * 10

    nickels = cents // 5
    cents -= nickels * 5

    pennies = cents

if dollars == 1:
    print("1 dollar")
elif dollars > 1:
    print(f"{dollars} dollars")

if quarters == 1:
    print("1 quarter")
elif quarters > 1:
    print(f"{quarters} quarters")

if dimes == 1:
    print("1 dime")
elif dimes > 1:
    print(f"{dimes} dimes")

if nickels == 1:
    print("1 nickel")
elif nickels > 1:
    print(f"{nickels} nickels")

if pennies == 1:
    print("1 penny")
elif pennies > 1:
    print(f"{pennies} pennies")
