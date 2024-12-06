name = input("Enter your Name: ")
deposit = int(input("Enter your Deposit Amount: "))

ans1 = deposit // 1000
num1 = deposit % 500

ans2 = num1 // 500
num2 = num1 % 200

ans3 = num2 // 200
num3 = num2 % 100

ans4 = num3 // 100
num4 = num3 % 50

ans5 = num4 // 50
num5 = num4 % 20

ans6 = num5 // 20
num6 = num5 % 10

ans7 = num6 // 10
num7 = num6 % 5

ans8 = num7 // 5
num8 = num7 % 1

ans9 = num8 // 1

print(f"\n\n\tHello! {name}, you have deposited the amount of: {deposit}.\n\n\t\t{ans1} - 1000\n\t\t{ans2} - "
      "500\n\t\t{ans3} - 200\n\t\t{ans4} - 100\n\t\t{ans5} - 50\n\t\t{ans6} - 20\n\t\t{ans7} - 10\n\t\t{ans8} "
      "- 5\n\t\t{ans9} - 1\n\t\t")