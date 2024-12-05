import os

def cc1():

    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t"
          "*\n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b"
          "* * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b"
          "* * * * *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b"
          "* * * * * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b"
          "* * * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b"
          "* * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t"
          "*")
    
def cc2():

    name = input("\n\n\t\t\tPlease enter your name: ")

    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t* \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b* * * "
        "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b* * * * * \n\t\t\t\t\t\t\t\t\t\t"
        "\t\t\t\b\b\b\b\b\b* *"+name+"* * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b"
        "* * * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b* * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t*")

def cc3():

    print("\n\tPersonal Bio Data Registration:")

    f_name = input("\n\t\tEnter Your First Name: ")
    m_name = input("\t\tEnter Your Middle Initial: ")
    l_name = input("\t\tEnter Your Last Name: ")

    age = int(input("\n\t\tEnter Your Age: "))
    gender = input("\t\tEnter Your Gender: ")

    birthdate_m = input("\n\t\tEnter Your Birth Month: ")
    birthdate_d = int(input("\t\tEnter Your Birth Day: "))
    birthdate_y = int(input("\t\tEnter Your Birth Year: "))
    birthplace = input("\t\tEnter Your Birth Place: ")

    weight = float(input("\n\t\tEnter Your Weight: "))
    height = float(input("\t\tEnter Your Height: "))

    civ_stat = input("\n\t\tEnter Your Civil Status: ")
    rel = input("\t\tEnter Your Type of Religion: ")
    citi = input("\t\tEnter Your Citizenship: ")
    lang = input("\t\tEnter Your Known Language: ")

    strt = input("\n\t\tEnter Your Street: ")
    brgy = input("\t\tEnter Your Barangay: ")
    city = input("\t\tEnter Your City: ")
    prvnc = input("\t\tEnter Your Province: ")

    num = int(input("\n\t\tEnter Your Phone No.: "))
    email = input("\t\tEnter Your Email: ")
    bsit = True

    print("\n\n\tPersonal Complete Bio Data:")

    print("\n\t\tHello "+f_name,m_name,l_name+"! You belong to the gender of "+gender+" and you are at the age of\b",
        age,". With your birthdate at "+birthdate_m,birthdate_d,birthdate_y,"and in the birthplace of "+
        birthplace+". You weight at an average of",weight,"kg, and with the height of",height,"cm. You are "+
        civ_stat+", belonging to the religion of "+rel+" with your citizenship of "+citi+" and you have known "+
        lang+" languages. You currently live in "+strt+", "+brgy+", "+city+", "+prvnc+". You currently use the phone number",
        num,"and the email "+email+". Lastly, you are a student of DLL from department of BSIT:",bsit)

def cc4():

    num1 = eval(input("\n\n\t\t\t\t\b\bEnter a Number: "))
    num2 = eval(input("\t\t\t\t\b\bEnter Another Number: "))

    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    mod = num1 % num2
    exp = num1 ** num2
    flr = num1 // num2

    print("\n\n\t\t\t\t\tThe Sum of",num1,"and",num2,"is",add,"\n\n\t\t\t\t\tThe Difference of",num1,"and"
        ,num2,"is",sub,"\n\n\t\t\t\t\tThe Product of",num1,"and",num2,"is",mul,"\n\n\t\t\t\t\tThe Quotient of"
        ,num1,"and",num2,"is",div,"\n\n\t\t\t\t\tThe Modulus of",num1,"and",num2,"is",mod,"\n\n\t\t\t\t\tThe Exponent of"
        ,num1,"and",num2,"is",exp,"\n\n\t\t\t\t\tThe Floor Division of",num1,"and",num2,"is",flr,"\n\n ")
    
def cc5():

    far = float(input("\n\n\tEnter the Rate of Temperature in Farehnheit: "))

    comp = (far - 32) * 5 / 9

    print(f"\n\tThe Degrees of Farehnheit {far} °F converted into Celcius is {round(comp, 2)} °C")

def cc6():

    name = input("\n\n\tEnter Your Name: ")

    pre = int(input("\n\n\tEnter Your Prelim Score: "))
    mid = int(input("\tEnter Your Midterm Score: "))
    senal = int(input("\tEnter Your Semi-Final Score: "))
    fin = int(input("\tEnter Your Final Score: "))
    quiz = int(input("\tEnter Your Quiz Score: "))
    proj = int(input("\tEnter Your Project Grade: "))


    fin_grade = (pre * 0.15) + (mid * 0.15) + (senal * 0.15) + (fin * 0.15) + (quiz * 0.25) + (proj * 0.15)

    print(f"\n\n\tHello {name}, Your Final Grade is: {fin_grade}")

    if fin_grade >= 100:
        print("\tDid You Entered Your Real Grade?")
    elif fin_grade >= 75:
        print("\tCongratulations, You Are Passed!")
    else:
        print("\tUnfortunately, You Are Failed.")

def cc7():

    try:

        groc = input("\n\n\tDid you buy a grocery (Yes/No): ").strip().upper()

        if groc == "YES":
            name = input("\n\tWhat is your name: ")
            age = int(input("\tAge: "))

            if age <= 0 or age > 150:
                print("\n\n\tEnter your real age\n\t ")
            else:

                item = input("\n\tName of the item: ")
                price = float(input("\tPrice of the item: "))

                if price <= 0:
                    print("\n\n\tEnter a real number on the Price given\n\t ")
                else:
                
                    amount = float(input("\n\tAmount Given: "))
                    
                    if amount <= 0:
                        print("\n\n\tEnter a real number on the Amount given\n\t ")
                    else:

                        calc1 = price * 0.123
                        calc2 = price + calc1
                        
                        calc3 = calc2 * 0.052
                        calc4 = calc2 - calc3
                                    
                        final1 = amount - calc2
                        final2 = amount - calc4

                        if age >= 1 and age <= 59:
                            if final1 < 0:
                                print(f"\n\n\tDear Customer, the amount you've entered is short by {round(final1, 2)}. Please try again\n\t ")
                            else:
                                print(f"\n\n\t\tHi customer {name}, you purchased a {item}, with a Price of {price} plus a 12.3% tax ({round(calc1, 2)}).\n\t\tTotal Cost: {round(calc2, 2)}\n\t\tAmount Given: {amount}\n\t\tChange: {round(final1, 2)}\n\t ")

                        elif age >= 60 and age <= 150:
                            if final2 < 0:
                                print(f"\n\n\tDear Senior Customer, the amount you've entered is short by {round(final2, 2)}. Please try again\n\t ")
                            else:
                                print(f"\n\n\t\tHi customer {name}, you purchased a {item}, with a Price of {price} plus a 12.3% tax ({round(calc1, 2)}), and since you are a senior at the age of {age}, you will get a 5.2% discount ({round(calc3, 2)}).\n\t\tTotal Cost: {round(calc4, 2)}\n\t\tAmount Given: {amount}\n\t\tChange: {round(final2, 2)}\n\t ")

        elif groc == "NO":
            print("\n\n\tThank you for coming to our store\n\t ")

        else:
            print("\n\n\tWrong Input\n\t ")

    except ValueError:
        print("\n\n\tError. Invalid Input\n\t ")

def cc8():

    sum = 0

    for i in range(10):
        num = int(input("\n\tEnter a number: "))
        sum += num

    print(f"\n\n\t\tThe sum of all numbers is: {sum}\n\n ")

def cc9():

    for i in range(10, 0, -1):
        for j in range(1, 11 - i):
            print(" ", end= " ")
        for k in range(1, i + 1):
            print("*", end= " ")
        print()