def Act21():
    def Hallo(name):
        print(f"Hello {name}")

    def act2():
        num1 = int(input("Please enter a number:  "))
        num2 = int(input("Please enter another number:  "))
        answer = num1 + num2
        print(f"The sun of {num1} and {num2} is: {answer}")

    while True:
        ask = input("Please provide a name: ").upper().strip()
        if ask =="STOP":
            break

        else: 
             Hallo(ask)

