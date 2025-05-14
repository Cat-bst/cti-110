# Catherine Best
# 2/27/2025
# P1HW2
# Vacation budget calculator
# Program Pseudocode (logic)

def main():
 
 
    budget = float(input("Enter budget: $"))
 
    destination = input("Enter your travel destination: ")
 
    gas = float(input("How much do you will spend on gas: $"))
 
    accommodation = float(input("Approximately, how much will you need for accomdation/hotel? $"))
 
    food = float(input("Last, how much do you need for food? $"))
 
 
 
    total_expenses = gas + accommodation + food
 
    remaining_budget = budget - total_expenses
 
 
 
    print("\nTravel Expenses:")
 
    print(f"Location: {destination}")
 
    print(f"Initial budget: ${budget:.2f}")
 
    print(f"Fuel: ${gas}")
 
    print(f"Accommodation: ${accommodation}")
 
    print(f"Food: ${food}")
 
    print(f"Remaining Balance: ${remaining_budget:.2f}")
 
 
    if remaining_budget < 0:
 
        print("You don't have enough, sorry!!!")
 
    else:
 
        print("Have a nice vacation! :)")
if __name__ == "__main__":
 
    main()