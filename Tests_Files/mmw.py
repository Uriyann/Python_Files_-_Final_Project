import os

while True:
    try:
        var= int(input("Enter x: --> "))
        os.system("cls")

        compute = ((7 * var) + 4) % 26


        print(compute)
    except ValueError:
        print("Enter a number")
        continue

"""This Program Will Determine The Number For Cryptograph"""