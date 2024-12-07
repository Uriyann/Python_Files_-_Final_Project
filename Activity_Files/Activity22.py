def act1():
      print("\n\t\t\t\t\t\t\t\t\t\t\t\t\b\t*\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b* * *",
      "\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b\b\b* * * * *\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b\b\b\b\b* * * * * * *",
      "\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b\b\b* * * * *\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\b\b* * *",
      "\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b\t*\t \n\t\t\t\t\t\t\t\t\t\t\t\t\b")

def act2():
      num1 = int(input("Enter a number: "))
      num2 = int(input("Enter another number: "))

      print(num1, "\nFloor Divided to", num2 ,"=", num1 // num2)

def act3():
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

      print("\n\t\tHello "+f_name,m_name,l_name+"! You belong to the gender of "+gender+" and you are at the age of",age,
            ". With your birthdate at "+birthdate_m,birthdate_d,birthdate_y,"and in the birthplace of "+birthplace+
            ". You weight at an average of",weight,"kg, and with the height of",height,"cm. You are "+civ_stat+
            ", belonging to the religion of "+rel+" with your citizenship of "+citi+" and you have known "+lang+
            " languages. You currently live in "+strt+", "+brgy+", "+city+", "+prvnc+". You currently use the phone number"
            ,num,"and the email "+email+". Lastly, you are a student of DLL from department of BSIT:",bsit)

def act4():
      number1 = eval(input("\n\n\t\t\bEnter A Number: "))
      number2 = eval(input("\t\t\bEnter Another Number: "))

      add = number1 + number2
      sub = number1 - number2
      mul = number1 * number2
      div = number1 / number2
      flr_div = number1 // number2
      exp = number1 ** number2
      mod = number1 % number2


      print("\n\n\t\t\t\tThe sum of",number1,"and",number2,"in addition is",add,
      "\n\t\t\t\tThe sum of",number1,"and",number2,"in subtraction is",sub,"\n\t\t\t\tThe sum of",number1,
      "and",number2,"in multiplication is",mul,"\n\t\t\t\tThe sum of",number1,"and",number2,"in division is",div,
      "\n\t\t\t\tThe sum of",number1,"and",number2,"in floor division is",flr_div,"\n\t\t\t\tThe sum of",number1,"and",number2,
      "in exponentiation is",exp,"\n\t\t\t\tThe sum of",number1,"and",number2,"in modulus is",mod,"\n\n ")

def act5():
      temp = float(input("Enter Temperature in Farenheit: "))

      cel = (temp - 32) * 5/9

      print(f"The conversion of {temp} degrees Farenheit is {round(cel, 2)} degrees Celcius.")

def act6():
      x = 5
      print(x)

      x += 10
      print(x)

      x += 15
      print(x)

      x+= 10
      print(x)

def act7():
      gold = 0
      min = input("Hi, What is your name: ")

      isgold = input("Is the mineral Gold? [Yes / No]: ").upper().strip()

      if isgold == "YES":
            gold += 1
            print(f"Hi {min}, Your total number of Gold is: {gold}")

      elif isgold == "NO":
            print("Please input a Gold")

      else:
            print("Wrong Input")

def act8():
      pre = int(input("\n\n\tPrelim Score: "))
      mid = int(input("\n\tMidterm Score: "))
      semi = int(input("\n\tSemi-Final Score: "))
      final = int(input("\n\tFinal Score: "))
      quiz = int(input("\n\tQuiz Score: "))
      proj = int(input("\n\tProject Score: " ))

      fg = (pre * 0.15) + (mid * 0.15) + (semi * 0.15) + (final * 0.15) + (quiz * 0.25) + (proj * 0.15)


      print(f"\n\n\tYour grade is {fg}")

      if pre > 100:
            print("\n\tError. Wrong input")
      elif fg >= 65:
            print("\n\tCongratulations! You have passed the course")
      else:
            print("\n\tUnfortunately You Have Failed")

def act9():
      age = int(input("Enter your Age: "))

      if age > 130:
            print("Enter your Real Age")
      elif age >= 60 and age <= 130:
            print("You are a senior")
      elif age >= 46 and age <= 59:
            print("You are at Post Adulthood")
      elif age >= 32 and age <= 45:
            print("You are at Mid Adulthood")
      elif age >= 19 and age <= 31:
            print("You are at an Early Adulthood")
      elif age >= 14 and age <= 18:
            print("You are a Teenager")
      elif age >= 8 and age <= 13:
            print("You are at Pre-Teen")
      elif age >= 1 and age <= 7:
            print("You are a Todler")
      else:
            print("Enter a your Real Age")

def act10():
      name= input("Enter your name here:  ")
      isStud = input ("Are you currently enrolled in DLL? [Yes or No]:  ").upper().strip()


      if isStud == "YES":
            yearLev =input("What year are you currently enrolled? \nF- Freshmen \nS-Sophomore"
                        "\nJ-Junior  \nR-Senior: \nPlease enter your answer here: ").upper().strip()
            
            if yearLev == "F":
                  print(f"Hello Freshie {name}, and Welcome to DLL") 
            elif yearLev == "S":
                  print(f"Hello Sophomore {name}, and Welcome to DLL") 
            elif yearLev == "J":
                  print(f"Hello Junior {name}, and Welcome to DLL, konti na lang") 
            elif yearLev == "R":
                  print(f"Hello Senior {name}, Welcome to DLL and congrats pwede kanang humimlay")

      elif isStud == "NO":
            print("Thank you, Next")

      else:
            print("Wrong Input")

def act11():
      for i in range(1, 11):
            print("Hello World!")
            print("Happy Foundation")
            
            single = False

            print(f"{single}, That I'm Single")

def act12():
      for i in range(10, 1, -1):
            print(i)

def act13():
      sum = 0

      for i in range(4, 0, -1):
            i *= i
            sum += i


      print(i)
      print(sum)

def act14():
      for i in range(0,11):
            print(i, end="")
            for k in range(0,11):
                  print("*", end= (""))
            print()

def act15():
      for i in range(0, 11):
            print(i, end=" ")
            for k in range(0, i):
                  print("*", end= (" "))
            print()

def act16():
      for x in range(1, 11):
            for z in range(1, x + 1):
                  print(" ", end=" ")
            for y in range(11, x, -1):
                  print("*", end= " ")

            print()

def act17():
      for x in range(6, 0, -1):
            for y in range(1, x + 1):
                  print(" ", end= " ")

            for z in range(6, x, -1):
                  print("*", end= " ")

            for a in range(5, x, -1):
                  print("*", end= " ")

            print()

      for x in range(1, 6):
            for y in range(1, x + 2):
                  print(" ", end= " ")

            for z in range(5, x, -1):
                  print("*", end= " ")

            for a in range(4, x, -1):
                  print("*", end= " ")

            print()

def act18():
      num = int(input("Enter a number of right triangle: ")) 

      for i in range(1, 6):
            for r in range(1, num + 1):
                  print(" ", end= " ")
                  for j in range(1, i + 1):
                        print("*", end= " ")
                  for k in range(5, i, -1):
                        print(" ", end= " ") 

            print()

def act19():
      contin = True
      count = 0

      while contin == True:
            name = input("Enter a name: ").upper().strip()

            if name == "STOP":
                  print("The loop has now stopped")
                  print(f"You have entered {count} number of names")
                  break

            else:
                  count += 1
                  continue

def act20():
      isContinue = True
      no = 0
      while isContinue == True:
            ask = input("Would you like to add another triangle [Yes / No]: ").strip().upper()

            if ask == "no":
                  print("PROGRAM TERMINATED")
                  break
                  isContinue = False

            else:
                  no += 1
                  for x in range(1,5):
                        for r in range(1,no + 1):
                              for y in range(1,x + 1):
                                    print(" ", end= " ")
                        
                              for z in range(1, x, -1):
                                    print("*", end= " ")
                              print()    
                  continue

def act21():

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
                  Hallo(ask)

def act23():

      def add(num1, num2):
            """This function adds the first number and second number returnig sum value"""
            return print(f"The sum of the numbers are: {num1 + num2}")    

      add()

def act24():
      
      from Activity23 import add
      import Activity1

      add(21,21)
      Activity1

def act25():

      def list():

            courses = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]

            courses.remove("Delete w/o index")
            courses.pop()
            courses.append("DHRS")
            courses.insert(0, "ABELS")

            print(courses)

      list()


try:
      compile = True

      while compile:

            print("\n\tSELECT FROM THE FOLLOWING PROGRAMS BELOW \n\t"
                  "\n\tActivity 1 - [1]", "\tActivity 9 - [9]", "\tActivity 17 - [17]"
                  "\n\tActivity 2 - [2]", "\tActivity 10 - [10]", "\tActivity 18 - [18]"
                  "\n\tActivity 3 - [3]", "\tActivity 11 - [11]", "\tActivity 20 - [20]"
                  "\n\tActivity 4 - [4]", "\tActivity 12 - [12]", "\tActivity 21 - [21]"
                  "\n\tActivity 5 - [5]", "\tActivity 13 - [13]", "\tActivity 23 - [23]"
                  "\n\tActivity 6 - [6]", "\tActivity 14 - [14]", "\tActivity 24 - [24]"
                  "\n\tActivity 7 - [7]", "\tActivity 15 - [15]", "\tActivity 25 - [25]"
                  "\n\tActivity 8 - [8]", "\tActivity 16 - [16]", )

            num = int(input("\n\n\tSelect a Program: "))

            if num == 1:
                  act1()
                  continue

            elif num == 2:
                  act2()
                  continue

            elif num == 3:
                  act3()
                  continue

            elif num == 4:
                  act4()
                  continue

            elif num == 5:
                  act5()
                  continue

            elif num == 6:
                  act6()
                  continue
            
            elif num == 7:
                  act7()
                  continue

            elif num == 8:
                  act8()
                  continue

            elif num == 9:
                  act9()
                  continue

            elif num == 10:
                  act10()
                  continue

            elif num == 11:
                  act11()
                  continue

            elif num == 12:
                  act12()
                  continue

            elif num == 13:
                  act13()
                  continue

            elif num == 14:
                  act14()
                  continue
                  
            elif num == 15:
                  act15()
                  continue

            elif num == 16:
                  act16()
                  continue

            elif num == 17:
                  act17()
                  continue
            
            elif num == 18:
                  act18()
                  continue

            elif num == 19:
                  act19()
                  continue

            elif num == 20:
                  act20()
                  continue

            elif num == 21:
                  act21()
                  continue

            elif num == 23:
                  act23()
                  continue

            elif num == 24:
                  act24()
                  continue

            elif num == 25:
                  act25()
                  continue
            
            elif num < 0:
                  print("Wrong Input. Must Be A Positive Number.")
                  continue

            else:
                  print("Thank You For Using Our Program.")
                  break

except ValueError:

      print("Wrong Input. Must Be A Number.")