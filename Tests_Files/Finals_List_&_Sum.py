even_num = []
odd_num = 0

while True:
    ask = int(input("Enter a number (type 0 to stop): ")) 

    if ask == 0:
        break

    elif ask % 2 == 0:
        even_num.append(ask)

    else:

        odd_num += ask


print(odd_num)
print(even_num)