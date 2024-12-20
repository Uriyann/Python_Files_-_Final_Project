def Code_Chal11():
    print("\n\n\t\t\b\b|========================|\n\t\t\b\b|   By: Joshua Barotea   |\n\t\t\b\b|========================|\n\n")

    for i in range(1, 11):
        for j in range(1, 11 - i):
            print(" ", end= " ")
        for k in range(1, i + 1):
            print("*", end= " ")
        for l in range(2, i + 1):
            print("*", end= " ")

        print()

    for i in range(10, 0, -1):
        for j in range(0, 11 - i):
            print(" ", end= " ")
        for k in range(2, i + 1):
            print("*", end= " ")
        for l in range(3, i + 1):
            print("*", end= " ")

        print()