# Catherine Best
# 4/13/2025
# P4HW2
# Salary Calculator

# Creat variables for overtime pay, regular pay, gross pay, and number of employees.
# Make a loop to ask for employee name, hours worked, and pay rate and keep going until "Done" is typed.
# Calculate overtime hours and regular hours based on the hours worked.
# 1.5x pay rate for overtime hours.
# Gross pay is sum of regular pay and overtime pay.
# Display the pay info.
# When loops ends, display total number of employees, total overtime pay, total regular pay, and total gross pay.

total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

while True:
    employee_name = input("Enter employee's name or \"Done\" to terminate: ")
    
    if employee_name == "Done":
        break

    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
    else:
        overtime_hours = 0

    regular_hours = hours_worked - overtime_hours
    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    print("\nEmployee name:\t", employee_name)
    print()
    print("Hours Worked  Pay Rate  OverTime  OverTime Pay  RegHour Pay  Gross Pay")
    print("----------------------------------------------------------------------")
    print(f"{hours_worked:<13}{pay_rate:<10}{overtime_hours:<10}{overtime_pay:<14.2f}{regular_pay:<13.2f}{gross_pay:<.2f}")
    print()

    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

print(f"\nTotal number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")