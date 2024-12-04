import os

def cc1():

    os.system('cls')

    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t* \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b"
            "* * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b* * * * * "
            "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b* * * * * * * "
            "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b* * * * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b"
            "* * * \n\t\t\t\t\t\t\t\t\t\t\t\t\t*")
    
def cc2():

    os.system('cls')

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

    os.system('cls')

    print("\n\n\tPersonal Complete Bio Data:")

    print("\n\t\tHello "+f_name,m_name,l_name+"! You belong to the gender of "+gender+" and you are at the age of\b",
        age,". With your birthdate at "+birthdate_m,birthdate_d,birthdate_y,"and in the birthplace of "+
        birthplace+". You weight at an average of",weight,"kg, and with the height of",height,"cm. You are "+
        civ_stat+", belonging to the religion of "+rel+" with your citizenship of "+citi+" and you have known "+
        lang+" languages. You currently live in "+strt+", "+brgy+", "+city+", "+prvnc+". You currently use the phone number",
        num,"and the email "+email+". Lastly, you are a student of DLL from department of BSIT:",bsit)

def cc4():

    os.system('cls')

    num1 = eval(input("\n\n\t\t\t\t\b\bEnter a Number: "))
    num2 = eval(input("\t\t\t\t\b\bEnter Another Number: "))

    os.system('cls')

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

    os.system('cls')

    far = float(input("\n\n\tEnter the Rate of Temperature in Farehnheit: "))

    comp = (far - 32) * 5 / 9

    print(f"\n\tThe Degrees of Farehnheit {far} °F converted into Celcius is {round(comp, 2)} °C")

def cc6():

    os.system('cls')

    name = input("\n\n\tEnter Your Name: ")

    pre = int(input("\n\n\tEnter Your Prelim Score: "))
    mid = int(input("\tEnter Your Midterm Score: "))
    senal = int(input("\tEnter Your Semi-Final Score: "))
    fin = int(input("\tEnter Your Final Score: "))
    quiz = int(input("\tEnter Your Quiz Score: "))
    proj = int(input("\tEnter Your Project Grade: "))


    fin_grade = (pre * 0.15) + (mid * 0.15) + (senal * 0.15) + (fin * 0.15) + (quiz * 0.25) + (proj * 0.15)

    os.system('cls')

    print(f"\n\n\tHello {name}, Your Final Grade is: {fin_grade}")

    if fin_grade >= 100:
        print("\tDid You Entered Your Real Grade?")
    elif fin_grade >= 75:
        print("\tCongratulations, You Are Passed!")
    else:
        print("\tUnfortunately, You Are Failed.")