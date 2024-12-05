num = int(input("Enter the number of right triangle: "))

for i in range(1, 6):
    for j in range(1, num + 1):
        for k in range(6, i, -1):
            print(" ", end= " ")
        for l in range(1, i + 1):
            print("*", end= " ")

    print()