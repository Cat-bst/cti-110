# Catherine Best
# 3/12/2025
# P2HW2
# Module grade calculator
# Program Pseudocode (detail algorithm)

# Pseudocode:
# 1. Make an empty list named 'grades' to store the module scores.
# 2. Prompt the user to enter a grade for Module 1-6 and store it in the list.
# 3. min() will calculate the lowest grade. 
# 4. max() will calculate the highest grade.
# 5. sum() will calculate the sum of the grades.
# 6. Calculate the average grade by dividing the total sum by the number of grades.
# 7. Display the results.

grades = []
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

lowest_grade = min(grades)
highest_grade = max(grades)
total_sum = sum(grades)
average_grade = total_sum / len(grades)

print("\n----------------Results----------------")
print(f"Lowest Grade:\t {lowest_grade:.1f}")
print(f"Highest Grade:\t {highest_grade:.1f}")
print(f"Sum of Grades:\t {total_sum:.1f}")
print(f"Average:\t {average_grade:.1f}")
print("----------------------------------------")