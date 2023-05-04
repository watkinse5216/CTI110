# A math quiz game that asks the user addition and subtraction questions
# Date: 04/27/2023
# CTI-110 P5HW - Math Quiz
# Evan Watkins
#


import random

def add_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    answer = num1 + num2
    # Display the problem with correct formatting
    print('{:>5}'.format(num1))
    print('+{:>4}'.format(num2))
    print()
    
    # Prompt user for input
    print("Enter answer. ")
    guess = int(input())
    
    attempts = 1
    while guess != answer:
        if guess < answer:
            print("Sorry, guess too low." ) 
            print()
            guess = int(input("Try again: "))  # If the guess is too low
        else:
            print("Sorry, guess too high." )
            print()
            guess = int(input("Try again:")) # If the guess is too high
        attempts += 1
    
    # Use formatted string to display the number of attempts
    print(f"Congratulations!!! Your Answer is correct. ")
    print(f"Number of guesses: {attempts} ")
    print()
    
def subtract_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    answer = num1 - num2
    # Display the problem with correct formatting
    print('{:>5}'.format(num1))
    print('-{:>4}'.format(num2))
    
    # Prompt user for input
    print("Enter answer. ")
    guess = int(input())
    
    attempts = 1
    while guess != answer:
        if guess < answer:
            print("Sorry, guess too low." )
            print()
            guess = int(input("Try again: "))  # If the guess is too low
        else:
            print("Sorry, guess too high." )
            print()
            guess = int(input("Try again:")) # If the guess is too high
        attempts += 1
    
    # Use formatted string to display the number of attempts
    print(f"Congratulations!!! Your Answer is correct. ")
    print(f"Number of guesses: {attempts} ")
    print()

print("Welcome to Math Quiz")
print()
while True:
    print("MAIN MENU")
    print("--------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    print()
    choice = input("Please choose one of the menu options: ")
    
    
    if choice == "1":
        add_numbers()
        continue
        
    elif choice == "2":
        subtract_numbers()
        continue
        
    elif choice == "3":
        print("Thank you for playing...")
        print("Bye!!")
        break
        
    else:
        print("Invalid choice. Please try again.\n")
        continue



