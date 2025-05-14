# CTI 110
# Catherine Best
# 3/29/2025
# P3HW1 debugging
# This program takes a number grade , determines average and displays letter grade for average.
# Enter grades for six months

mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# determine letter grade for average 
if avg >= 90:
 
    letter_grade = 'A'
elif avg >= 80:
 
    letter_grade = 'B'
elif avg >= 70:
 
    letter_grade = 'C'
elif avg >= 60:
 
    letter_grade = 'D'
else:
 
    letter_grade = 'F'

print("\nResults:")
print(f"Lowest Grade: {low}")
print(f"Highest Grade: {high}")
print(f"Sum of Grades: {total}")
print(f"Average Grade: {avg:.2f}")
print(f"Final Letter Grade: {letter_grade}")