# This is a program that displays letter grades but needs to be debugged.
# Watkins
# This program takes a number grade , determines average and displays letter grade for average.
# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))
print()
# add grades entered to a list
print("------------Results------------")
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades
low = min(grades)
high = max(grades)
sum = sum(grades)
avg = sum / len(grades)
print('Lowest Grade', format(low, ',.1f'))
print('Highest Grade', format(high, ',.1f'))
print('Sum of Grades:', format(sum, ',.1f'))
print('Average:', format(avg, ',.2f'))
print('----------------------------------------')
# determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
       print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F') # TO DO: finish this
