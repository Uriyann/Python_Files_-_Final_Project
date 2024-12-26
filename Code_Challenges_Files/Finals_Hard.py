amount = int(input("Enter the loan amount: "))
period = int(input("Enter the load period in years: "))

annual = 0.03
months = period * 12
interest = annual / 12
principal = amount / months

remaining_loan = amount

print("\n\n")

for headers in range(1, 2):
    print("      Month", end= "\t|")

    for monthly_pay_headers in range(1):
        print("\tMonthly Payment\t", end= "\t|")

    for interest_pay_headers in range(1):
        print("\tInterest", end= "\t|")

    for principal_headers in range(1):
        print("\tPrincipal", end= "\t|")

    for remaining_headers in range(1):
        print("\tRemaining Loan\t", end= "\t|")

    print()

for month in range(1, months + 1):
    print(f"\t{month}", end= "\t|")

    interest_payment = remaining_loan * interest

    monthly_payment = principal + interest_payment

    remaining_loan -= principal

    monthly_payment = round(monthly_payment, 2)
    interest_payment = round(interest_payment, 2)
    principal = round(principal, 2)
    remaining_loan = abs(remaining_loan)
    remaining_loan = round(remaining_loan, 2)

    for monthly_pay in range(1):
        print(f"\t    {monthly_payment}", end="\t\t|")
    
    for interest_pay in range(1):
        print(f"\t  {interest_payment}\t", end="\t|")

    for princ in range(1):
        print(f"\t  {principal}\t", end="\t|")

    for remaining in range(1):
        print(f"\t    {remaining_loan}\t", end="\t|")

    print()