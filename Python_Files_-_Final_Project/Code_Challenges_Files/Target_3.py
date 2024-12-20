import os

num = int(input("Enter the number of column: "))

os.system("cls")

for i in range(1, 11):
    for j in range(1, num + 1):
        print(i * j, end= "\t")

    print()