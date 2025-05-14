# Catherine Best
# 3/30/2025
# P3HW2
# Employee Salary

# Pseudocode
# Ask user for an employee's name, amount of hours they worked, and their pay
# Define regular work hours and overtime pay rate 
# See if the hours they wored was more than the reg hours 
# Calculate overtime hours or set overtime to 0
# (reg hours * pay rate)
# (overtime hours * pay rate * 1.5)
# (regular pay + overtime pay) << gross pay 
# Show results 

def calculate_pay():
 
    name = input("Enter employee's name: ")
 
    hours_worked = float(input("Enter number of hours worked: "))
 
    pay_rate = float(input("Enter employee's pay rate: "))
 
 
    regular_hours = 40
 
    overtime_rate = 1.5
 
 
    if hours_worked > regular_hours:
 
        overtime_hours = hours_worked - regular_hours
 
    else:
 
        overtime_hours = 0
 
 
    regular_pay = min(hours_worked, regular_hours) * pay_rate
 
    overtime_pay = overtime_hours * (pay_rate * overtime_rate)
 
    gross_pay = regular_pay + overtime_pay
 
 
    print("--------------------------------------")
 
    print(f"Employee name: {name}")
 
    print(" ")
 
    print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<10}")
 
    print("---------------------------------------------------------------------------")
 
    print(f"{hours_worked:<15.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}{overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<10.2f}")

calculate_pay()