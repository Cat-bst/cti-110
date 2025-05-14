# Catherine Best
# 4/12/2025
# P4HW1
# Grade Calculator

# Ask user how many scores they want to enter
# Initialize an empty list to store valid scores
# Repeat until required number of valid scores is collected:
#    Ask user to enter a score
#    If the score is between 0 and 100, add it to the list
#    Else, show error and ask again for the same score
# Remove the lowest score from the list
# Calculate average of remaining scores and determine the grade
# Display the results: lowest score, modified list, average, and grade

scores = []

try:
    num_scores = int(input("How many scores do you want to enter? "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

i = 0
while i < num_scores:
    try:
        score = float(input(f"Enter score #{i+1}: "))
        if 0 <= score <= 100:
            scores.append(score)
            i += 1
        else:
            print("\nINVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            print(f"Enter score #{i+1} again: ", end="")
    except ValueError:
        print("Please enter a valid number.")

lowest = min(scores)
scores.remove(lowest)

print("\n----------------Results------------")
print(f"Lowest Score  : {lowest:.1f}")
print(f"Modified List : {[round(s, 1) for s in scores]}")

average = sum(scores) / len(scores)
print(f"Scores Average: {average:.2f}")

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade         : {grade}")
print("----------------------------------")