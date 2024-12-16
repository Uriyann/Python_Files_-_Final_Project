def Code_Chal16():
    print("\n\n\t\t\b\b|========================|\n\t\t\b\b|   By: Joshua Barotea   |\n\t\t\b\b|========================|\n\n")


    account = {}

    def create_account():
        name = input("\tEnter Your Name: ").strip()

        if name in account:
            print("\n\n\tThis Account Already Exist.")
            return
        
        while True:
            try:

                deposit = int(input("\n\tEnter Your Initial Deposit: "))

                if deposit < 0:
                    print("\n\n\tError. Please Enter A Positive Number.")
                    continue
                
                account[name] = deposit

                print(f"\n\n\t\tThe Account For {name} With A Initial Deposit Of ₱{deposit} Have Been Created.")
                break
            
            except ValueError:
                print("\n\n\tError. Enter A Number.")

    def deposit_amount():
        name = input("\n\tEnter Your Name: ").strip()

        if name not in account:
            print("\n\n\tThis Account Does Not Exist.")
            return
        
        while True:
            try:

                deposit = int(input("\n\tEnter Your Amount To Deposit: "))

                if deposit < 0:
                    print("\n\n\tError. Please Enter A Positive Number.")
                    continue

                account[name] += deposit

                print(f"\n\n\t\tThe Account For {name} With A Deposit Of ₱{deposit} Have Been Added Into Account.")
                print(f"\n\n\t\tThe Current Balance Of {name} is: ₱{account[name]}")
                break

            except ValueError:
                print("\n\n\tError. Enter A Number.")
            
    def withraw_amount():
        name = input("\n\tEnter Your Name: ").strip()

        if name not in account:
            print("\n\n\tThis Account Does Not Exist.")
            return

        while True:
            try:

                withrawal = int(input("\n\tEnter Your Amount To Withraw: "))

                if withrawal < 0:
                    print("\n\n\tError. Please Enter A Positive Number.")
                    continue

                elif withrawal > account[name]:
                    print("\n\n\tError. Insufficient Amount")
                    continue

                account[name] -= withrawal

                print(f"\n\n\t\tThe Account for {name} With A Withrawal Of ₱{withrawal} Has Been Removed From Account")
                print(f"\n\n\t\tThe Current Balance Of {name} is: ₱{account[name]}")
                break
            
            except ValueError:
                print("\n\n\tError. Enter A Number.")

    def balance_amount():
        name = input("\n\tEnter Your Name: ").strip()

        if name not in account:
            print("\n\n\tThis Account Does Not Exist.")
            return

        print(f"\n\n\t\tThe Current Balance Of {name} is: ₱{account[name]}")


        while True:

            desicion = input("\n\tDo You Want To Denominate Your Current Balance? [Yes / No]: ").strip().upper()

            if desicion == "YES":

                ans1 = account[name] // 1000
                num1 = account[name] % 1000

                ans2 = num1 // 500
                num2 = num1 % 500

                ans3 = num2 // 200
                num3 = num2 % 200

                ans4 = num3 // 100
                num4 = num3 % 100

                ans5 = num4 // 50
                num5 = num4 % 50

                ans6 = num5 // 20
                num6 = num5 % 20

                ans7 = num6 // 10
                num7 = num6 % 10

                ans8 = num7 // 5
                num8 = num7 % 5

                ans9 = num8 // 1

                print(f"\n\n\t\tThe Current Balance Of {name} is: ₱{account[name]}")
                print(f"\n\n\t\t₱1000 - {ans1}"
                    f"\n\t\t₱500 - {ans2}"
                    f"\n\t\t₱200 - {ans3}"
                    f"\n\t\t₱100 - {ans4}"
                    f"\n\t\t₱50 - {ans5}"
                    f"\n\t\t₱20 - {ans6}"
                    f"\n\t\t₱10 - {ans7}"
                    f"\n\t\t₱5 - {ans8}"
                    f"\n\t\t₱1 - {ans9}")
                
                break

            elif desicion == "NO":
                print("\n\tDenomination Cancelled.")
                return

            else:
                print("\n\n\tError. Wrong Input.")
                continue

    while True:

        print("\n\tSelect an Option:"
            "\n\n\t1. [Create an Account]"
            "\n\t2. [Deposit]"
            "\n\t3. [Withraw]"
            "\n\t4. [Balance]"
            "\n\t5. [Exit]")

        try:

            choice = int(input("\n\nEnter Your Option: "))


            if choice == 1:
                create_account()
            elif choice == 2:
                deposit_amount()
            elif choice == 3:
                withraw_amount()
            elif choice == 4:
                balance_amount()
            elif choice == 5:
                print("\n\tThe System Will Now Terminate\n")
                break

            else:
                print("\n\n\tError. Wrong Input.")
                continue

        except ValueError:
            print("\n\n\tError. Enter A Number.")