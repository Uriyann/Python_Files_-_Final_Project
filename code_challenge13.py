import os

os.system('cls')

print("\n\n\t\t\b\b|========================|\n\t\t\b\b|   By: Joshua Barotea   |\n\t\t\b\b|========================|\n\n")

for i in range(1, 9):
    for j in range(9, i, - 1):
        print(" ", end= " ")
    for k in range(i, 1, - 1):
        print(k, end= " ")
    for l in range(1, i + 1):
        print(l, end= " ")

    print()
    
for i in range(9, 0, -1):
    for j in range(9, i, - 1):
        print(" ", end= " ")
    for k in range(i, 1, - 1):
        print(k, end= " ")
    for l in range(1, i + 1):
        print(l, end= " ")

    print()

    