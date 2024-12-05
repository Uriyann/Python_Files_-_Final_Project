import os


print("\n\n\t\t\b\b|========================|\n\t\t\b\b|   By: Joshua Barotea   |\n\t\t\b\b|========================|")

count = True
num = 0


while count == True:
    
    number = int(input("\n\tEnter a number: "))

    os.system('cls')

    if number == 0:
        print("\n\t\tThe loop has now stopped")

        question = input("\n\tDo you still want to continue? [Yes / No]: ").upper().strip()

        if question == "YES":
            print("\n\t\tThe system has stopped")
            print(f"\n\t\tThe sum of all number is {num}\n")
            break

        elif question == "NO":
            print("\n\t\tThe loop will now continue")
            continue
        
        else:
            print("\n\tInvalid Input. Only Answer in [Yes / No]\n")
            continue

    elif number < 0:
        print("\n\t\tInvalid Input. Try Again")
        continue

    else:
        num += number
        continue