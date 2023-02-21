# Creating a Program in IDLE

# 02/16/2023

# CTI-110 P1HW2 - Travel Expense

# Evan Watkins

#
tot_budget = int(input("Enter Budget:"))
print()
destination= input("Enter your travel destination:")
print()
gas_cost = int(input("How much do you think you will spend on gas?"))
print()
hotel_cost = int(input("Approximately, how much will you need for accomodation/hotel?"))
print()
food_cost = int(input("Last, how much do you need for food?"))
print()
print('------------Travel Expenses------------')
print('Location:', destination)
print('Initial Budget:', tot_budget)
print()
print('Fuel:', gas_cost)
print('Accomodation:', hotel_cost)
print('Food', food_cost)
print()
print('Remaining Balance:', tot_budget - gas_cost - hotel_cost - food_cost)
