# CTI-110

   # P2HW2 - List

   # Watkins Evan

   # 03/09/2023

   #
#Grades List
mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))
print()
print("------------Results------------")
#List of Grades
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
#Grade Sum
sum_grades =mod_1 + mod_2 + mod_3 + mod_4 + mod_5 + mod_6
#Finding the Average of Grades
results = sum_grades / 6
#Finding the Highest Grade
highest = max(grades)
#Finding the Lowest Grade
lowest = min(grades)
print('Lowest Grade', format(lowest, ',.1f'))
print('Highest Grade', format(highest, ',.1f'))
print('Sum of Grades:', format(sum_grades, ',.1f'))
print('Average:', format(results, ',.2f'))
print('----------------------------------------')