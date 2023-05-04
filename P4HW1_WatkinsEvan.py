# CTI-110
# P4HW1 - Score List
# Evan Watkins
# 04/04/2023

# Ask user to enter number of scores they would like to enter
num_scores = int(input("Enter the number of scores you would like to enter: "))
print()

# Create a loop to collect the number of scores the user wants to enter
scores = []
for i in range(num_scores):
    # Note every time a score is entered, check if it is valid
    while True:
        score = float(input(f"Enter score #{i+1}: "))
        if score < 0 or score > 100:
            print()
            print("Invalid score. Please enter a score between 0 and 100.")
        else:
            scores.append(score)
            break
print()
print()
print('--------------Results--------------')
# Find the lowest score entered
lowest_score = min(scores)
print("Lowest score entered:", lowest_score)

# Remove the lowest score from the list
scores.remove(lowest_score)
print("Score list after dropping lowest score:", scores)

# Find the average of the modified score list
average = sum(scores) / len(scores)
print("Average of scores in modified list:", average)

# Determine the letter grade for the calculated average and display it to user
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
print("Letter grade for the calculated average:", letter_grade)
print('----------------------------------')
