amount = int(input("Enter the loan amount: "))
period = int(input("Enter the load period in years: "))

annual = 0.03
months = period * 12
interest = annual / 12
principal = amount / months

remaining_loan = amount



for month in range(1, months + 1):
    print(f"\t{month}", end= " ")
    
    for line_1 in range(1):
        print("\t|", end= " ")

    for monthly_pay in range(1):
        interest_payment = remaining_loan * interest

        monthly_payment = principal + interest_payment

        remaining_loan -= principal

        monthly_payment = round(monthly_payment, 2)
        interest_payment = (interest_payment, 2)
        principal = round(principal, 2)
        remaining_loan = round(remaining_loan, 2)

        print(f"\t{monthly_payment}", end=" ")

    for line_2 in range(1):
        print("\t|", end= " ")
    
    for interest_pay in range(1):
        print(f"\t{interest_payment}", end=" ")

    for line_3 in range(1):
        print("\t|", end= " ")

    for princ in range(1):
        print(f"\t{principal}", end=" ")

    for line_4 in range(1):
        print("\t|", end= " ")

    for remaining in range(1):
        print(f"\t{remaining_loan}", end=" ")

    for line_5 in range(1):
        print("\t|", end= " ")

    print()