# Catherine Best
# 4/4/2025
# P4LAB2
# Multiplication Table



def main():
    run_again = "yes"

    while run_again.lower() == "yes":
        try:
            num = int(input("Enter an integer: "))
            
            if num >= 0:
                print(f"\nMultiplication table for {num}:")
                for i in range(1, 13):
                    print(f"{num} x {i} = {num * i}")
            else:
                print("This program does not handle negative numbers.")
        
        except ValueError:
            print("This isn't a valid number, try again.")
            continue  
        
        run_again = input("\nWould you like to run the program again? (yes/no): ")

    print("Exiting program...")

main()