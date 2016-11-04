# get balance after one year of making minimum monthly payments

balance = int(raw_input("Enter your outstanding balance: "))
annual_interest = float(raw_input("Enter the annual interest rate: "))
monthly_pay_rate = float(raw_input("Enter the minimum monthly payment rate: "))

monthly_interest_rate = annual_interest/12
print monthly_interest_rate

total_paid = 0.0

for month in range(1,13):

	monthly_payment = round(monthly_pay_rate * balance,2)
	interest = round(monthly_interest_rate * balance,2)
	principal_paid = monthly_payment - interest
	balance -= principal_paid
	total_paid += monthly_payment

	print "Month:",month
	print "Minimum Monthly Payment:","$"+str(monthly_payment)
	print "Principle Paid:","$"+str(principal_paid)
	print "Remaining Balance:","$"+str(balance)

print "RESULT"
print "Total Amount Paid:","$"+str(total_paid)
print "Remaining Balance:""$"+str(balance)

# incrementing by 10, get the minimum fixed monthly payment required to pay off balance in a year. must be a multiple of 10.

Balance = int(raw_input("Enter your outstanding balance: "))
annual_interest = float(raw_input("Enter your annual interest rate: "))

monthly_interest_rate = annual_interest / 12
fixed_payment = 0
not_paid_off = True
balance = None
months_needed = None

while not_paid_off:
	balance = Balance
	fixed_payment += 10
	for month in range(1,13):
		interest = round(monthly_interest_rate * balance,2)
		principal_paid = fixed_payment - interest
		balance -= principal_paid
		if balance <= 0.0:
			not_paid_off = False
			months_needed = month 
			break		


print "RESULT"
print "Monthly payment need to pay off debt in one year:","$"+str(fixed_payment)
print "Number of months needed:",months_needed
print "Balance:",balance

# using bisection search, get the minimum fixed monthly payment required to pay off balance in a year, to the nearest cent

Balance = int(raw_input("Enter your outstanding balance: "))
annual_interest = float(raw_input("Enter your annual interest rate: "))

monthly_interest_rate = annual_interest / 12
lower_bound = round(Balance / 12.0,2)
upper_bound = round((Balance * (1+monthly_interest_rate)**12) / 12.0,2)
fixed_payment = round((lower_bound + upper_bound) / 2.0,2)
solution_not_found = True
balance = None
months_needed = None
smallest_sufficient = upper_bound
largest_insufficient = lower_bound

while solution_not_found:
	balance = Balance
	for month in range(1,13):
		interest = round(monthly_interest_rate * balance,2)
		principal_paid = round(fixed_payment - interest,2)
		balance = round(balance-principal_paid,2)
		if balance <= 0.0:
			smallest_sufficient = fixed_payment
			if round(smallest_sufficient - largest_insufficient,2) == .01:
				solution_not_found = False
				months_needed = month
			else:
				upper_bound = fixed_payment
				fixed_payment = round((upper_bound + lower_bound) / 2.0,2)
			break
	else:
		largest_insufficient = fixed_payment
		if round(smallest_sufficient - largest_insufficient,2) == .01:
			solution_not_found = False
			months_needed = month 
		else:
			lower_bound = fixed_payment
			fixed_payment = round((upper_bound + lower_bound) / 2.0,2)



print "RESULT"
print "Monthly payment need to pay off debt in one year:","$"+str(smallest_sufficient)
print "Number of months needed:",months_needed
print "Balance:","$"+str(balance)













