  # CTI-110

   # P4HW2 - Salary Calculator

   # Evan Watkins

   # 04/17/2023


#Initialize variables
num_employees = 0
overtime_total = 0
regular_pay_total = 0
gross_pay_total = 0

#Get Input
while True:
    employee_name = input("Enter employee name or 'Done' to terminate: ")
    if employee_name == "Done":
        break
        print()
    num_employees += 1
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    print()
    
    #calculate overtime pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = (overtime_hours * 1.5) * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
    
    #calculate pay for hours worked
    regular_pay = (hours_worked - overtime_hours) * pay_rate
    #calculate gross pay
    gross_pay = overtime_pay + regular_pay

    #add up totals
    overtime_total += overtime_pay
    regular_pay_total += regular_pay
    gross_pay_total += gross_pay
    
    #display results for individual employee
    print("Employee name:", employee_name)
    print()
    print("Hours Worked     Pay rate         OverTime       OverTime Pay        RegHour Pay         Gross Pay", )
    print("---------------------------------------------------------------------------------------------------")
    print(f'{hours_worked:<20.2f}{pay_rate:<15.2f}{overtime_hours:<15.2f}{overtime_pay:<20.2f}${regular_pay:<20.2f}${gross_pay:<15.2f}')
    print()
    
#display totals for all employees
print("Total number of employees entered:", num_employees)
print("Total amount paid for overtime: $",overtime_total)
print("Total amount paid for regular hours: $",regular_pay_total)
print("Total amount paid in gross: $",gross_pay_total)