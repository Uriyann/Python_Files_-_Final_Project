name = input("\n\n\tEnter your Name: ")
amount = int(input("\tEnter your Deposited Amount: "))

print("\n\t--------------------------------------------------------")

ans1 = amount // 1000
num1 = amount % 1000

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


print(f"\n\n\t\tHello! {name}, you have deposited the amount of {amount}, the organized bill is as follow:\n\n\t\t\t{ans1} - 1000\n\t\t\t{ans2} - 500\n\t\t\t{ans3} - 200\n\t\t\t{ans4} - 100\n\t\t\t{ans5} - 50\n\t\t\t{ans6} - 20\n\t\t\t{ans7} - 10\n\t\t\t{ans8} - 5\n\t\t\t{ans9} - 1\n")