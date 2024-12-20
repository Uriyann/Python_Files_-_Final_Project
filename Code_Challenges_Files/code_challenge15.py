def Code_Chal15():
    print("\n\n\t\t\b\b|========================|\n\t\t\b\b|   By: Joshua Barotea   |\n\t\t\b\b|========================|")

    count = True
    num = 0

    while count == True:

        triangle = input("\n\tDo you want to increase the number of Right Triangle? [Yes / No]: ").upper().strip()

        if triangle == "NO":
            print("\n\t\tThe loop has stopped")

            question = input("\n\tDo you still want to continue? [Yes / No]: ").upper().strip()
            
            
            if question == "YES":
                print("\n\t\tThe system has stopped")
                print(f"\n\t\tThe sum of all Right Triangle created is {num}\n")
                break
            
            elif question == "NO":
                print("\n\t\tThe loop will now continue")
                continue
            
            
        elif triangle == "YES":
            num += 1

            for i in range(1, 6):
                for j in range(1, num + 1):
                    for k in range(1, i + 1):
                        print(k, end= " ")
                    for l in range(6, i, -1):
                        print(" ", end= " ")

                print()

            continue

        else:
            print("\n\tInvalid Input. Only Answer in [Yes / No]\n")
            continue