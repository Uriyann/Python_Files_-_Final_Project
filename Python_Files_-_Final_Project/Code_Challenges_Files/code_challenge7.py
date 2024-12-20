def Code_Chal7():
    print("\n\n\t\t\b\b|========================|\n\t\t\b\b|   By: Joshua Barotea   |\n\t\t\b\b|========================|")

    try:

        groc = input("\n\n\tDid you buy a grocery (Yes/No): ").strip().upper()

        if groc == "YES":
            name = input("\n\tWhat is your name: ")
            age = int(input("\tAge: "))

            if age <= 0 or age > 150:
                print("\n\n\tEnter your real age\n\t ")
            else:

                item = input("\n\tName of the item: ")
                price = float(input("\tPrice of the item: "))

                if price <= 0:
                    print("\n\n\tEnter a real number on the Price given\n\t ")
                else:
                
                    amount = float(input("\n\tAmount Given: "))
                    
                    if amount <= 0:
                        print("\n\n\tEnter a real number on the Amount given\n\t ")
                    else:

                        calc1 = price * 0.123
                        calc2 = price + calc1
                        
                        calc3 = calc2 * 0.052
                        calc4 = calc2 - calc3
                                    
                        final1 = amount - calc2
                        final2 = amount - calc4

                        if age >= 1 and age <= 59:
                            if final1 < 0:
                                print(f"\n\n\tDear Customer, the amount you've entered is short by {round(final1, 2)}. Please try again\n\t ")
                            else:
                                print(f"\n\n\t\tHi customer {name}, you purchased a {item}, with a Price of {price} plus a 12.3% tax ({round(calc1, 2)}).\n\t\tTotal Cost: {round(calc2, 2)}\n\t\tAmount Given: {amount}\n\t\tChange: {round(final1, 2)}\n\t ")

                        elif age >= 60 and age <= 150:
                            if final2 < 0:
                                print(f"\n\n\tDear Senior Customer, the amount you've entered is short by {round(final2, 2)}. Please try again\n\t ")
                            else:
                                print(f"\n\n\t\tHi customer {name}, you purchased a {item}, with a Price of {price} plus a 12.3% tax ({round(calc1, 2)}), and since you are a senior at the age of {age}, you will get a 5.2% discount ({round(calc3, 2)}).\n\t\tTotal Cost: {round(calc4, 2)}\n\t\tAmount Given: {amount}\n\t\tChange: {round(final2, 2)}\n\t ")

        elif groc == "NO":
            print("\n\n\tThank you for coming to our store\n\t ")

        else:
            print("\n\n\tWrong Input\n\t ")

    except ValueError:
        print("\n\n\tError. Invalid Input\n\t ")