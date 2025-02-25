# mortgage.py
#
# Exercise 1.7

principal = 500_000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1_000
months = 0

while principal > 0:
    months += 1
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    if months >= extra_payment_start_month and months <= extra_payment_end_month: 
    	principal = principal - extra_payment
    	total_paid = total_paid + extra_payment
    print(f'{months:>3}, {round(total_paid, 2):>10}, {round(principal, 2):>10}')

print(f'Total paid {round(total_paid, 2):>16}')
print(f'Months {months:>20}')

