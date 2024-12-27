amount = int(input("\nEnter the loan amount: "))
period = int(input("Enter the load period in years: "))

annual = 0.03
months = period * 12
interest = annual / 12
principal = amount / months

remaining_loan = amount

print("\n\n")

for headers in range(1):
    print("|\t\b\bMonth", end= "\t|")

    for monthly_pay_headers in range(1):
        print("\tMonthly Payment\t", end= "\t|")

    for interest_pay_headers in range(1):
        print("\tInterest", end= "\t|")

    for principal_headers in range(1):
        print("\tPrincipal", end= "\t|")

    for remaining_headers in range(1):
        print("\tRemaining Loan\t", end= "\t|")

    print()

for lines in range(129):
    print("-", end="")

print()

for month in range(1, months + 1):
    print(f"|\t{month}", end= "\t|")
    interest_payment = remaining_loan * interest

    monthly_payment = principal + interest_payment

    remaining_loan -= principal

    monthly_payment_str = f"{monthly_payment:.2f}"
    interest_payment_str = f"{interest_payment:.2f}"
    principal_str = f"{principal:.2f}"
    remaining_loan = abs(remaining_loan)
    remaining_loan_str = f"{remaining_loan:.2f}"

    for monthly_pay in range(1):
        print(f"\t    {monthly_payment_str}", end="\t\t|")
    
    for interest_pay in range(1):
        print(f"\t  {interest_payment_str}\t", end="\t|")

    for princ in range(1):
        print(f"\t  {principal_str}\t", end="\t|")

    for remaining in range(1):
        print(f"\t    {remaining_loan_str} \t", end="\t|")

    print()