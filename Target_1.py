for i in range(1,6):
    for j in range(1, 7):
        print(" ", end= " ")
    for k in range(6, i, -1):
        print("*", end= " ")
    
    print()

for i in range(1, 6):
    for j in range(6, i, -1):
        print(" ", end= " ")
    for k in range(1, i + 1):
        print("*", end= " ")
    
    print()