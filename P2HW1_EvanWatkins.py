# Adding onto a Program in IDLE

# 03/01/2023

# CTI-110 P2HW1 - Travel

# Evan Watkins

#
print('This program calculates and displays travel expenses')
tot_budget = float(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas_cost = float(input("How much do you think you will spend on gas? "))
print()
hotel_cost = float(input("Approximately, how much will you need for accommodation/hotel? "))
print()
food_cost = float(input("Last, how much do you need for food? "))
print()
print('------------Travel Expenses------------')
print('Location:', destination)
print('Initial Budget: $', format(tot_budget, ',.2f'))
print('Fuel: $', format(gas_cost, ',.2f'))
print('Accommodation: $', format(hotel_cost, ',.2f'))
print('Food: $', format(food_cost, ',.2f'))
print('---------------------------------------')
print()
print('Remaining Balance: $', format(tot_budget - gas_cost - hotel_cost - food_cost, ',.2f'))