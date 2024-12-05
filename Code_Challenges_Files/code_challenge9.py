import os

os.system('cls')

print("\n\n\t\t\b\b|========================|\n\t\t\b\b|   By: Joshua Barotea   |\n\t\t\b\b|========================|\n\n")

for i in range(10, 0, -1):
    for j in range(1, 11 - i):
        print(" ", end= " ")
    for k in range(1, i + 1):
        print("*", end= " ")
    print()