dep = 0

def create_account(name, deposit):
    
    while True:
        
        dep = 0

        dep += deposit



        try:

            if deposit < 0:
                print("\n\n\tError. Please Enter A Positive Number.")
                continue

            print(f"\n\n\t\tThe Account For {name} With A Initial Deposit Of ₱{dep} Have Been Created.")
            break
        
        except ValueError:
            print("\n\n\tError. Enter A Number.")

create_account(input("\tEnter Your Name: ").strip(), int(input("\n\tEnter Your Initial Deposit: ")))
print(dep)

def naot():
    print("Ilyyes")
#awefwaef#
# def denomination(amount):awdaw
#     ans1 = amount // 1000awdwadwa
#     num1 = amount % 1000

#     ans2 = num1 // 500
#     num2 = num1 % 500

#     ans3 = num2 // 200
#     num3 = num2 % 200

#     ans4 = num3 // 100
#     num4 = num3 % 100

#     ans5 = num4 // 50
#     num5 = num4 % 50

#     ans6 = num5 // 20
#     num6 = num5 % 20

#     ans7 = num6 // 10
#     num7 = num6 % 10

#     ans8 = num7 // 5
#     num8 = num7 % 5

#     ans9 = num8 // 1

#     print(f"\n\n\t\tThe Current Balance Of user is: ₱{amount}")
#     print(f"\n\n\t\t₱1000 - {ans1}"
#         f"\n\t\t₱500 - {ans2}"
#         f"\n\t\t₱200 - {ans3}"
#         f"\n\t\t₱100 - {ans4}"
#         f"\n\t\t₱50 - {ans5}"
#         f"\n\t\t₱20 - {ans6}"
#         f"\n\t\t₱10 - {ans7}"
#         f"\n\t\t₱5 - {ans8}"
#         f"\n\t\t₱1 - {ans9}")
    
# denomination()