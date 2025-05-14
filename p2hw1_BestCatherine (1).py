# Catherine Best
# 3/12/2025
# P2HW1
# Vacation budget calculator
# Program Pseudocode (logic)

def main():
 
    print("This program calculates and displays travel expenses\n")
 
 
    budget = float(input("Enter Budget: "))
 
    destination = input("Enter your travel destination: ")
 
    gas = float(input("How much do you think you will spend on gas? "))
 
    accommodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
 
    food = float(input("Last, how much do you need for food? "))
 
 
    total_expenses = gas + accommodation + food
 
    remaining_balance = budget - total_expenses
 
 
    print("\n------------Travel Expenses------------")
 
    print(f"Location:\t\t{destination}")
 
    print(f"Initial Budget:\t${budget:.2f}")
 
    print(f"Fuel:\t\t${gas:.2f}")
 
    print(f"Accomodation:\t${accommodation:.2f}")
 
    print(f"Food:\t\t${food:.2f}")
 
    print("--------------------------------------")
 
    print(f"\nRemaining Balance:\t${remaining_balance:.2f}")
 
if __name__ == "__main__":
 
    main()