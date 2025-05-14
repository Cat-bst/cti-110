# Catherine Best
# 4/20/2025
# P5LAB
# Self checkout 

import random

def disperse_change(change):
    cents = round(change * 100)

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    print(f"{dollars} Dollars")
    print(f"{quarters} Quarters")
    print(f"{dimes} Dimes")
    print(f"{nickels} Nickels")
    print(f"{pennies} Pennies")

def main():
    
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed}")

    cash_given = float(input("How much cash will you put in the self-checkout? "))

    change = round(cash_given - total_owed, 2)
    print(f"Change is: ${change}")

    disperse_change(change)

main()