"""
MIT Intro to CS with Python
Unit 1 Assignment 1
"""

"""
Formulas
minimum_monthly_payment = minrate * balance
monthly_interest = intrate/12 * balance
principal_paid = minimum_monthly_payment - monthly_interest
balance -= principal_paid
"""
"""
# Problem 1
# Note: instead of using a for loop, we could also have used a while loop
# While months < 12, adding 1 to months at the end of each iteratation
balance = float(raw_input("Enter the outstanding balance on your credit card: "))
intrate = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
minrate = float(raw_input("Enter the minimum monthly payment rate as ad decimal: "))
Total = 0
for x in range(1, 13):
    monthint = intrate/12 * balance
    minpay = minrate * balance
    princpay = minpay - monthint
    balance -= princpay
    Total += minpay

    print "Month:",x
    print "Minimum Monthly Payment: $" + str(round(minpay,2))
    print "Principle Paid: $" + str(round(princpay,2))
    print "Remaining Balance: $" + str(round(balance,2))

print "RESULT"
print "Total amount paid: $" + str(round(Total,2))
print "Remaining balance: $" + str(round(balance,2))
"""
# Problem 2
"""
Formulas
Month_Int = interest / 12
New_Bal = balance * (1 + Month_Int) - MinPay
"""

"""
balance = float(raw_input("Enter the outstanding balance on your credit card: "))
interest = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
Mon_Int = interest/12
new_bal = balance
for x in range(10,int(balance),10):
    if new_bal <= 0:
        break
    else:
        new_bal = balance
        for y in range(1,13):
            new_bal = round(new_bal * (1 + Mon_Int) - x,2)
            if new_bal <= 0:
                print "RESULT"
                print "Monthly payment to pay off debt in 1 year:",x
                print "Number of months needed:",y
                print "Balance:",new_bal
                break
"""
# Problem 3

"""
Formulas
New_Bal = balance * (1 + Month_Int) - MinPay
Low = balance/12
High = balance * (1 + (Month_Int) ** 12) / 12 
"""
"""
balance = float(raw_input("Enter the outstanding balance on your credit card: "))
interest = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
Month_Int = interest/12
Low = balance/12
High = (balance * ((1 + Month_Int) ** 12)) / 12
New_Bal = balance
while New_Bal > 0:
    New_Bal = balance
    Guess = round((Low + High)/2,2)
    for x in range(1,13):
        New_Bal = round(New_Bal * (1 + Month_Int) - Guess,2)
        if New_Bal <= 0 and x < 12:
            High = Guess
            New_Bal = balance
            break
        if New_Bal <= 0:
            print "RESULT"
            print "Monthly payment to pay off debt in 1 year:",Guess
            print "Number of months needed: 12"
            print "Balance:",New_Bal
            break
    else: Low = Guess
"""

























