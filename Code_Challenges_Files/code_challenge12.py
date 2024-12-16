def Code_Chal12():
    print("\n\n\t\t\b\b|========================|\n\t\t\b\b|   By: Joshua Barotea   |\n\t\t\b\b|========================|\n\n")

    for i in range(11, 0, -1):
        for j in range(1, i + 1):
            print(" ", end= " ")
        for k in range(11, i, -1):
            print("*", end= " ")
        for l in range(11, i, -1):
            print("*", end= " ")
        
        print()

    for i in range(1, 11):
        for j in range(1, 9):
            print(" ", end= " ")
        for k in range(1, 7):
            print("*", end= " ")

        print()