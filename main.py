

# Pay Program

try:
    hours_worked = float(input("Enter number of hours worked: "))
    rate = float(input("Enter rate: ")) * 1.5
    total_pay = hours_worked * rate
    if hours_worked > 40:
        total_pay = hours_worked * rate
    else:
        total_pay = hours_worked * 10
    print("Pay: " + str(total_pay))

except:
    print("Please start over and enter a number")



