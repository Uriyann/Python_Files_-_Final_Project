"""Final Project = Main Menu"""

import os

from Activity_Files import (
                    
                    Activity1, Activity2, Activity3, Activity4, Activity5, Activity6, 
                    Activity7, Activity8, Activity9, Activity10, Activity11, Activity12, 
                    Activity13, Activity14, Activity15, Activity16, Activity17, Activity18, 
                    Activity19, Activity20, Activity21, Activity22, Activity23, Activity24,
                    Activity25

                    )

from Code_Challenges_Files import (
                    
                    code_challenge1, code_challenge2, activity3_BAROTEA, code_challenge4,
                    code_challenge5, code_challenge6, code_challenge7, code_challenge8,
                    code_challenge9, code_challenge10, code_challenge11, code_challenge12,
                    code_challenge13, code_challenge14, code_challenge15, code_challenge16
                    
                    )

def Clear():

    os.system("cls")

def Main_Menu():
    while True:
        try:
            print(
                
                "\n\n\t| ======================================= |"
                "\n\t| ========= -Compiled Projects- ========= |"
                "\n\t| =============== ------- =============== |"
                "\n\t| ============= -Main Menu- ============= |"
                "\n\t| ======================================= |"
                
                "\n\n\t[ 1 ] - Python_Fundamentals: "
                "\n\t[ 2 ] - Activity_Project: "
                "\n\t[ 3 ] - Code_Challenges_Project: "
                "\n\t[ 0 ] - Terminate "

                  )
            
            num = int(input("\n\n\tSelect The Topic Of Your Choice: "))

            if num == 1:
                Clear()
                Fundamentals()
            elif num == 2:
                Clear()
                Activities()
            elif num == 3:
                Clear()
                Code_Chal()


            elif num == 0:
                Clear()
                choice = input("\n\t[The Final Project Menu Has Stopped.]"
                               "\n\n\tAre You Sure You Want To Continue: [Yes/No]: ").upper().strip()
                
                if choice == "NO":
                    Clear()
                    print("\n\t[The Final Project Menu will now continue.]")
                    continue
                elif choice == "YES":
                    Clear()
                    print("\n\t[The Final Project Menu will now be terminated.]\n")
                    break

            elif num < 0:
                Clear()
                print("\n\t[Error. Please Enter A Positive Number.]")
                continue
            elif num >= 5:
                Clear()
                print("\n\t[Error. Please Enter An Approriate Number Below.]")
                continue
            else:
                Clear()
                print("\n\t[Error. Wrong Input.]")
                continue
        
        except ValueError:
            Clear()
            print("\n\t[Error. Enter A Real Number.]")
            continue

def Activities():
    while True:
        try:
            print(
                
                "\n\n\t| ======================================= |"
                "\n\t| ========= -Compiled Projects- ========= |"
                "\n\t| =============== ------- =============== |"
                "\n\t| =========== -Activity_Menu- =========== |"
                "\n\t| ======================================= |"
                
                "\n\n\t[ 1 ] - Activity_1  \t[ 14 ] - Activity_14"
                "\n\t[ 2 ] - Activity_2  \t[ 15 ] - Activity_15"
                "\n\t[ 3 ] - Activity_3  \t[ 16 ] - Activity_16"
                "\n\t[ 4 ] - Activity_4  \t[ 17 ] - Activity_17"
                "\n\t[ 5 ] - Activity_5  \t[ 18 ] - Activity_18"
                "\n\t[ 6 ] - Activity_6  \t[ 19 ] - Activity_19"
                "\n\t[ 7 ] - Activity_7  \t[ 20 ] - Activity_20"
                "\n\t[ 8 ] - Activity_8  \t[ 21 ] - Activity_21"
                "\n\t[ 9 ] - Activity_9  \t[ 22 ] - Activity_22"
                "\n\t[ 10 ] - Activity_10  \t[ 23 ] - Activity_23"
                "\n\t[ 11 ] - Activity_11  \t[ 24 ] - Activity_24"
                "\n\t[ 12 ] - Activity_12  \t[ 25 ] - Activity_25"
                "\n\t[ 13 ] - Activity_13  \t[ 0 ] - Terminate "
                  
                  )
            
            num = int(input("\n\n\tChoose A Number Of Your Choices: "))

            if num == 1:
                Clear()
                Activity1.Act1()
            elif num == 2:
                Clear()
                Activity2.Act2()
            elif num == 3:
                Clear()
                Activity3.Act3()
            elif num == 4:
                Clear()
                Activity4.Act4()
            elif num == 5:
                Clear()
                Activity5.Act5()
            elif num == 6:
                Clear()
                Activity6.Act6()
            elif num == 7:
                Clear()
                Activity7.Act7()
            elif num == 8:
                Clear()
                Activity8.Act8()
            elif num == 9:
                Clear()
                Activity9.Act9()
            elif num == 10:
                Clear()
                Activity10.Act10()
            elif num == 11:
                Clear()
                Activity11.Act11()
            elif num == 12:
                Clear()
                Activity12.Act12()
            elif num == 13:
                Clear()
                Activity13.Act13()
            elif num == 14:
                Clear()
                Activity14.Act14()
            elif num == 15:
                Clear()
                Activity15.Act15()
            elif num == 16:
                Clear()
                Activity16.Act16()
            elif num == 17:
                Clear()
                Activity17.Act17()
            elif num == 18:
                Clear()
                Activity18.Act18()
            elif num == 19:
                Clear()
                Activity19.Act19()
            elif num == 20:
                Clear()
                Activity20.Act20()
            elif num == 21:
                Clear()
                Activity21.Act21()
            elif num == 22:
                Clear()
                Activity22.Act22()
            elif num == 23:
                Clear()
                Activity23.Act23()
            elif num == 24:
                Clear()
                Activity24.Act24()
            elif num == 25:
                Clear()
                Activity25.Act25()

            elif num == 0:
                Clear()
                choice = input("\n\t[The Activity Project Menu Has Stopped.]"
                               "\n\n\tAre You Sure You Want To Continue: [Yes/No]: ").upper().strip()
                
                if choice == "NO":
                    Clear()
                    print("\n\t[The Activity Project Menu will now continue.]")
                    continue
                elif choice == "YES":
                    Clear()
                    print("\n\t[The Activity Project Menu will now be terminated.]\n")
                    break

            elif num < 0:
                Clear()
                print("\n\t[Error. Please Enter A Positive Number.]")
                continue
            elif num >= 5:
                Clear()
                print("\n\t[Error. Please Enter An Approriate Number Below.]")
                continue
            else:
                Clear()
                print("\n\t[Error. Wrong Input.]")
                continue
        
        except ValueError:
            Clear()
            print("\n\t[Error. Enter A Real Number.]")
            continue

def Code_Chal():
    while True:
        try:
            print(
                
                "\n\n\t| ======================================= |"
                "\n\t| ========= -Compiled Projects- ========= |"
                "\n\t| =============== ------- =============== |"
                "\n\t| ============= -Code_Menu- ============= |"
                "\n\t| ======================================= |"
                
                "\n\n\t[ 1 ] - Code_Challenge_1  \t[ 10 ] - Code_Challenge_10"
                "\n\t[ 2 ] - Code_Challenge_2  \t[ 11 ] - Code_Challenge_11"
                "\n\t[ 3 ] - Code_Challenge_3  \t[ 12 ] - Code_Challenge_12"
                "\n\t[ 4 ] - Code_Challenge_4  \t[ 13 ] - Code_Challenge_13"
                "\n\t[ 5 ] - Code_Challenge_5  \t[ 14 ] - Code_Challenge_14"
                "\n\t[ 6 ] - Code_Challenge_6  \t[ 15 ] - Code_Challenge_15"
                "\n\t[ 7 ] - Code_Challenge_7  \t[ 16 ] - Code_Challenge_16"
                "\n\t[ 8 ] - Code_Challenge_8  \t[ 0 ] - Terminate"
                "\n\t[ 9 ] - Code_Challenge_9"
                  
                  )
            
            num = int(input("\n\n\tChoose A Number Of Your Choices: "))

            if num == 1:
                Clear()
                code_challenge1.Code_Chal1()
            elif num == 2:
                Clear()
                code_challenge2.Code_Chal2()
            elif num == 3:
                Clear()
                activity3_BAROTEA.Code_Chal3()
            elif num == 4:
                Clear()
                code_challenge4.Code_Chal4()
            elif num == 5:
                Clear()
                code_challenge5.Code_Chal5()
            elif num == 6:
                Clear()
                code_challenge6.Code_Chal6()
            elif num == 7:
                Clear()
                code_challenge7.Code_Chal7()
            elif num == 8:
                Clear()
                code_challenge8.Code_Chal8()
            elif num == 9:
                Clear()
                code_challenge9.Code_Chal9()
            elif num == 10:
                Clear()
                code_challenge10.Code_Chal10()
            elif num == 11:
                Clear()
                code_challenge11.Code_Chal11()
            elif num == 12:
                Clear()
                code_challenge12.Code_Chal12()
            elif num == 13:
                Clear()
                code_challenge13.Code_Chal13()
            elif num == 14:
                Clear()
                code_challenge14.Code_Chal14()
            elif num == 15:
                Clear()
                code_challenge15.Code_Chal15()
            elif num == 16:
                Clear()
                code_challenge16.Code_Chal16()
            
            elif num == 0:
                Clear()
                choice = input("\n\t[The Code Challenge Project Menu Has Stopped.]"
                               "\n\n\tAre You Sure You Want To Continue: [Yes/No]: ").upper().strip()
                
                if choice == "NO":
                    Clear()
                    print("\n\t[The Code Challenge Project Menu will now continue.]")
                    continue
                elif choice == "YES":
                    Clear()
                    print("\n\n\t[The Code Challenge Project Menu will now be terminated.]\n")
                    break

            elif num < 0:
                Clear()
                print("\n\t[Error. Please Enter A Positive Number.]")
                continue
            elif num >= 17:
                Clear()
                print("\n\t[Error. Please Enter An Approriate Number Below.]")
                continue
            else:
                Clear()
                print("\n\t[Error. Wrong Input.]")
                continue
        
        except ValueError:
            Clear()
            print("\n\t[Error. Enter A Real Number.]"
                "\n")
            continue

def Fundamentals():
    while True:
        try:
            print(
                
                "\n\n\t| ======================================= |"
                "\n\t| ========= -Compiled Projects- ========= |"
                "\n\t| =============== ------- =============== |"
                "\n\t| ========= -Fundamentals_Menu- ========= |"
                "\n\t| ======================================= |"
                
                "\n\n\t[ 1 ] - Print_Statements     \t[ 5 ] - Loops"
                  "\n\t[ 2 ] - Variables            \t[ 6 ] - List"
                  "\n\t[ 3 ] - Operators            \t[ 7 ] - Functions"
                  "\n\t[ 4 ] - Conditionals         \t[ 0 ] - Terminate"
                  
                  )
            
            num = int(input("\n\n\tChoose A Number Of Your Choices: "))

            if num == 1:
                Clear()
                Print()
            elif num == 2:
                Clear()
                Variables()
            elif num == 3:
                Clear()
                Operators()
            elif num == 4:
                Clear()
                Conditionals()
            elif num == 5:
                Clear()
                Loops()
            elif num == 6:
                Clear()
                List()
            elif num == 7:
                Clear()
                Functions()

            elif num == 0:
                Clear()
                choice = input("\n\t[The Fundamentals Menu Has Stopped.]"
                               "\n\n\tAre You Sure You Want To Continue: [Yes/No]: ").upper().strip()
                
                if choice == "NO":
                    Clear()
                    print("\n\t[The Fundamentals Menu will now continue.]")
                    continue
                elif choice == "YES":
                    Clear()
                    print("\n\n\t[The Fundamentals Menu will now be terminated.]\n")
                    break

            elif num < 0:
                Clear()
                print("\n\t[Error. Please Enter A Positive Number.]")
                continue
            elif num >= 13:
                Clear()
                print("\n\t[Error. Please Enter An Approriate Number Below.]")
                continue
            else:
                Clear()
                print("\n\t[Error. Wrong Input.]")
                continue
        
        except ValueError:
            Clear()
            print("\n\t[Error. Enter A Real Number.]"
                "\n")
            continue

def Print():
    while True:
        try:
            print(

                "\n\n\tWelcome To Printing In Python"

                "\n\n\t\tPrint Menu"

                "\n\n\t[ 1 ] - Definition"
                  "\n\t[ 2 ] - Key Components"
                  "\n\t[ 0 ] - Terminate"

            )

            num = int(input("\n\n\tChoose A Number Of Your Choices: "))

            if num == 1:
                Clear()
                print(

                    "\n\n\t\t\t\tPRINTING DEFINITION"

                    "\n\n\tPrinting is the act of sending information (like strings, numbers, or variables)"
                    "\n\tto an output device, such as a console, where it can be displayed for the user to read."
                    "\n\n\tIn Python, printing is done using the print() function."
                    "\n\n\tTo use the print function, you simply type print() followed by the value(s) that you"
                    "\n\twant to print. "
                )

            elif num == 2:
                Clear()
                print(

                    "\n\n\t\tKEY COMPONENTS"

                    "\n\n\n\tBasic Usage:"
                    "\n\n\tprint('Hello, World!') \t\t\t# Output: Hello, World!"


                    "\n\n\n\tPrinting Multiple Values:"
                    "\n\n\tprint('Hello', 'World', 123) \t\t# Output: Hello World 123"

                    "\n\n\n\tCustom End:"
                    "\n\n\tprint('Hello', end=' ')"
                    "\n\tprint('World!') \t\t\t# Output: Hello World!"

                    "\n\n\n\tPrinting Variables:"
                    "\n\n\tname = 'Joshua!')"
                    "\n\tprint('Hello', name) \t\t\t# Output: Hello Joshua!"

                    "\n\n\n\tFormatted Strings:"
                    "\n\n\tage = 21)"
                    "\n\tprint(f'I am {age} years old.')\t\t# Output: I am 18 years old."

                    "\n\n\n\tEscape Sequence:"
                    "\n\n\tprint('Hello\\nWorld') \t\t\t# Output: Hello"
                    "\n\t\t\t\t\t\t\t  World"

                    "\n\n\tprint('Hello\\tWorld') \t\t\t# Output: Hellow      World"

                    "\n\n\tprint('Helloo\\bWorld') \t\t\t# Output: Hello World"
                )

            elif num == 0:
                Clear()
                choice = input("\n\t[The Print Menu Has Stopped.]"
                               "\n\n\tAre You Sure You Want To Continue: [Yes/No]: ").upper().strip()
                
                if choice == "NO":
                    Clear()
                    print("\n\t[The Print Menu will now continue.]")
                    continue
                elif choice == "YES":
                    Clear()
                    print("\n\n\t[The Print Menu will now be terminated.]\n")
                    break

            elif num < 0:
                Clear()
                print("\n\t[Error. Please Enter A Positive Number.]")
                continue
            elif num >= 3:
                Clear()
                print("\n\t[Error. Please Enter An Approriate Number Below.]")
                continue
            else:
                Clear()
                print("\n\t[Error. Wrong Input.]")
                continue
        
        except ValueError:
            Clear()
            print("\n\t[Error. Enter A Real Number.]"
                "\n")
            continue

def Variables():
    while True:
            try:
                print(

                    "\n\n\tWelcome To Variables In Python"

                    "\n\n\t\tVariable Menu"

                    "\n\n\t[ 1 ] - Definition"
                    "\n\t[ 2 ] - Key Components"
                    "\n\t[ 0 ] - Terminate"

                )

                num = int(input("\n\n\tChoose A Number Of Your Choices: "))

                if num == 1:
                    Clear()
                    print(

                        "\n\n\t\t\t\tVARIABLE DEFINITION"

                        "\n\n\tA variable is a name that refers to a value stored in memory. "
                        "\n\tIt allows you to store, retrieve, and manipulate data."
                        "\n\n\tVariables in programming are like named boxes that can store information."
                        "\n\tYou can use variables to store any type of data, such as numbers, strings, "
                        "\n\tlists, and objects."

                    )
                
                elif num == 2:
                    Clear()
                    print(

                        "\n\n\t\tKEY COMPONENTS"

                        "\n\n\n\tCreating Variables"
                        "\n\n\tname = 'Joshua' \t# String"
                        "\n\tage = 18 \t\t# Integer"
                        "\n\theight = 5.9 \t\t# Float"
                        "\n\tis_student = True \t# Boolean"

                        "\n\n\n\tChanging Values"
                        "\n\n\tage = 18"
                        "\n\tage = 19"
                        "\n\tprint(age) \t\t# Output: 19"

                    )
                
                elif num == 0:
                    Clear()
                    choice = input("\n\t[The Variable Menu Has Stopped.]"
                                "\n\n\tAre You Sure You Want To Continue: [Yes/No]: ").upper().strip()
                    
                    if choice == "NO":
                        Clear()
                        print("\n\t[The Variable Menu will now continue.]")
                        continue
                    elif choice == "YES":
                        Clear()
                        print("\n\n\t[The Variable Menu will now be terminated.]\n")
                        break

                elif num < 0:
                    Clear()
                    print("\n\t[Error. Please Enter A Positive Number.]")
                    continue
                elif num >= 3:
                    Clear()
                    print("\n\t[Error. Please Enter An Approriate Number Below.]")
                    continue
                else:
                    Clear()
                    print("\n\t[Error. Wrong Input.]")
                    continue
        
            except ValueError:
                Clear()
                print("\n\t[Error. Enter A Real Number.]"
                    "\n")
                continue

def Operators():
    while True:
            try:
                print(

                    "\n\n\tWelcome To Operators In Python"

                    "\n\n\t\tOperators Menu"

                    "\n\n\t[ 1 ] - Definition"
                    "\n\t[ 2 ] - Key Components"
                    "\n\t[ 0 ] - Terminate"

                )

                num = int(input("\n\n\tChoose A Number Of Your Choices: "))

                if num == 1:
                    Clear()
                    print(

                        "\n\n\t\t\t\tOPERATORS DEFINITION"

                        "\n\n\tOperators are symbols or keywords used to perform operations on variables and values."
                        "\n\n\tThese operators allow for various functionalities, from basic arithmetic operations "
                        "\n\tlike addition, subtraction, multiplication, and division to more complex comparisons "
                        "\n\tand logical operations."
                        "\n\n\tYou can use variables to store any type of data, such as numbers, strings, lists, and "
                        "\n\tobjects."
                        "\n\n\tPython provides several types of operators, including arithmetic operators for "
                        "\n\tmathematical calculations, comparison operators to compare values, and assignment operators"
                        "\n\tto assign values to variables."

                    )
                
                elif num == 2:
                    Clear()
                    print(

                        "\n\n\t\tKEY COMPONENTS"

                        "\n\n\n\tArithmetic Operators:"
                        "\n\n\tAddition = 5 + 3 \t\t# Output: 8"
                        "\n\tSubtraction = 5 - 3 \t\t# Output: 2"
                        "\n\tMultiplication = 5 * 3 \t\t# Output: 15"
                        "\n\tDivision = 5 / 2 \t\t# Output: 2.5"
                        "\n\tModulus_Remainder = 5 % 2 \t# Output: 1"
                        "\n\tExponentiation = 5 ** 2 \t# Output: 25"
                        "\n\tFloor_Division = 5 // 2 \t# Output: 2"

                        "\n\n\n\tAssignment Operators:"
                        "\n\n\tnum = 5 \t\t\t# Output: 5"
                        "\n\tnum += 2 \t\t\t# Output: 7"
                        "\n\tnum -= 4 \t\t\t# Output: 3"
                        "\n\tnum *= 10 \t\t\t# Output: 30"
                        "\n\tnum /= 5 \t\t\t# Output: 6.0"
                        "\n\tnum %= 6 \t\t\t# Output: 0"
                        "\n\tprint(num) \t\t\t# Output: 0"

                        "\n\n\n\tComparison Operators:"
                        "\n\n\tEqual = 5 == 5 \t\t\t# Output: True"
                        "\n\tNot_Equal = 5 != 3 \t\t# Output: True"
                        "\n\tGreater = 5 > 3 \t\t# Output: True"
                        "\n\tLesser = 5 < 2 \t\t\t# Output: False"
                        "\n\tGreater_or_Equal = 5 >= 5 \t# Output: True"
                        "\n\tLesser_or_Equal = 5 <= 5 \t# Output: False"

                        "\n\n\n\tLogical  Operators:"
                        "\n\n\tAnd = True and False \t\t# Output: False"
                        "\n\tOr = True or False \t\t# Output: True"
                        "\n\tNot = not False \t\t# Output: True"

                    )

                elif num == 0:
                    Clear()
                    choice = input("\n\t[The Operators Menu Has Stopped.]"
                                "\n\n\tAre You Sure You Want To Continue: [Yes/No]: ").upper().strip()
                    
                    if choice == "NO":
                        Clear()
                        print("\n\t[The Operators Menu will now continue.]")
                        continue
                    elif choice == "YES":
                        Clear()
                        print("\n\n\t[The Operators Menu will now be terminated.]\n")
                        break

                elif num < 0:
                    Clear()
                    print("\n\t[Error. Please Enter A Positive Number.]")
                    continue
                elif num >= 3:
                    Clear()
                    print("\n\t[Error. Please Enter An Approriate Number Below.]")
                    continue
                else:
                    Clear()
                    print("\n\t[Error. Wrong Input.]")
                    continue
        
            except ValueError:
                Clear()
                print("\n\t[Error. Enter A Real Number.]"
                    "\n")
                continue

def Conditionals():
    while True:
            try:
                print(

                    "\n\n\tWelcome To Conditionals In Python"

                    "\n\n\t\tConditionals Menu"

                    "\n\n\t[ 1 ] - Definition"
                    "\n\t[ 2 ] - Key Components"
                    "\n\t[ 0 ] - Terminate"

                )

                num = int(input("\n\n\tChoose A Number Of Your Choices: "))

                if num == 1:
                    Clear()
                    print(

                        "\n\n\t\t\t\tCONDITIONALS DEFINITION"

                        "\n\n\tConditionals allow you to make decisions in your code based on whether a condition is "
                        "\n\tTrue or False. "
                        "\n\n\tThey use if-else statements to control the flow of execution."
                        "\n\n\tThe condition can be any expression that evaluates to a Boolean value (True or False). "
                        "\n\n\tIf the condition is True, the code block indented below the if statement will be executed. "
                        "\n\n\tIf the condition is False, the code block will be skipped."

                    )
                
                elif num == 2:
                    Clear()
                    print(

                    "\n\n\t\tKEY COMPONENTS"

                    "\n\n\n\tBasic Syntax:"
                    "\n\n\tif condition: \n\t\t# Code used to execute if the condition is True"
                    "\n\n\telif another_condition: \n\t\t# Code used to execute if the first condition is False, but another_condition is True"
                    "\n\n\telse: \n\t\t# Code to execute if all conditions are False"

                    "\n\n\n\tif Statement:"
                    "\n\n\tage = 18"
                    "\n\tif age >= 18:"
                    "\n\t\tprint('You are an adult.') \n\t\t# Output: You are an adult."

                    "\n\n\n\tif_else Statement:"
                    "\n\n\tage = 15"
                    "\n\tif age >= 18:"
                    "\n\t\tprint('You are an adult.')"
                    "\n\telse:"
                    "\n\t\tprint('You are a minor.') \n\t\t# Output: You are a minor."

                    "\n\n\n\tif_elif_else Statement:"
                    "\n\n\tage = 15"
                    "\n\n\tif age >= 18:"
                    "\n\t\tprint('You are an adult.')"
                    "\n\tif age >= 50:"
                    "\n\t\tprint('You are a senior.')  \n\t\t# Output: You are a senior."
                    "\n\telse:"
                    "\n\t\tprint('You are a minor.')"
                    

                    "\n\n\n\tNested Conditionals:"
                    "\n\n\tage = 18"
                    "\n\tif age >= 18:"
                    "\n\t\tif age <= 30:"
                    "\n\t\t\tprint('You are a young adult.') \n\t\t\t# Output: You are a young adult."

                    )
                
                elif num == 0:
                    Clear()
                    choice = input("\n\t[The Conditionals Menu Has Stopped.]"
                                "\n\n\tAre You Sure You Want To Continue: [Yes/No]: ").upper().strip()
                    
                    if choice == "NO":
                        Clear()
                        print("\n\t[The Conditionals Menu will now continue.]")
                        continue
                    elif choice == "YES":
                        Clear()
                        print("\n\n\t[The Conditionals Menu will now be terminated.]\n")
                        break

                elif num < 0:
                    Clear()
                    print("\n\t[Error. Please Enter A Positive Number.]")
                    continue
                elif num >= 3:
                    Clear()
                    print("\n\t[Error. Please Enter An Approriate Number Below.]")
                    continue
                else:
                    Clear()
                    print("\n\t[Error. Wrong Input.]")
                    continue
        
            except ValueError:
                Clear()
                print("\n\t[Error. Enter A Real Number.]"
                    "\n")
                continue

def Loops():
    while True:
            try:
                print(

                    "\n\n\tWelcome To Loops In Python"

                    "\n\n\t\tLoop Menu"

                    "\n\n\t[ 1 ] - Definition"
                    "\n\t[ 2 ] - Key Components"
                    "\n\t[ 0 ] - Terminate"

                )

                num = int(input("\n\n\tChoose A Number Of Your Choices: "))

                if num == 1:
                    Clear()
                    print(

                        "\n\n\t\t\t\tLOOPS DEFINITION"

                        "\n\n\tLoops are used to execute a block of code repeatedly based on a condition or a "
                        "\n\tsequence of items."
                        "\n\n\tPython provides two primary types of loops: for loops and while loops."
                        "\n\n\tA for loop is used to iterate over a sequence (like a list, string, or range). "
                        "\n\tIt executes the block of code for each item in the sequence."
                        "\n\n\tA while loop repeats as long as the condition is True. It checks the condition "
                        "\n\tbefore each iteration."

                    )
                
                elif num == 2:
                    Clear()
                    print(

                        "\n\n\t\tKEY COMPONENTS"

                        "\n\n\n\tfor Loop:"
                        "\n\n\tfor i in range(5): \n\t# Iterates over the range 0 to 4"
                        "\n\t\tprint(i) \n\t\t# Output: 0 1 2 3 4"
                        "\n\n\tfor i in range(2, 10, 2): \n\t# Start at 2, end before 10, step by 2"
                        "\n\t\tprint(i) \n\t\t# Output: 0 2 4 6 8"
                        "\n\n\tfor i in range(10, 0, -1): \n\t# Start at 10, ending before 0"
                        "\n\t\tprint(i) \n\t\t# Output: 10 9 8 7 6 5 4 3 2 1"

                        "\n\n\n\twhile Loop:"
                        "\n\n\tcount = 0"
                        "\n\twhile count < 5:"
                        "\n\t\tprint(count) \n\t\t# Output: 0 1 2 3 4"
                        "\n\t\tcount += 1"

                        "\n\n\n\tNested Loops:"
                        "\n\n\tfor i in range(3):"
                        "\n\t\tfor j in range(3):"
                        "\n\t\t\tprint(i * j) \n\t\t\t# Output: 1 2 3, 2 4 6, 3 6 9"

                        "\n\n\n\tbreak and continue Statements:"
                        "\n\n\tfor i in range(10):"
                        "\n\t\tif i == 5:"
                        "\n\t\t\tbreak \n\t\t\t# Exit the loop when i equals 5"
                        "\n\t\tprint(i)  \n\t\t# Output: 0 1 2 3 4"

                        "\n\n\tfor i in range(5):"
                        "\n\t\tif i == 2:"
                        "\n\t\t\tcontinue \n\t\t\t# Skip the iteration when i equals 2"
                        "\n\t\tprint(i)  \n\t\t# Output: 0 1 3 4"

                        "\n\n\n\tInfinite Loops:"
                        "\n\n\twhile True:"
                        "\n\t\tprint('This will run forever unless stopped.')"
                        "\n\t\t# You can add a break condition to exit the loop."

                    )
                
                elif num == 0:
                    Clear()
                    choice = input("\n\t[The Loop Menu Has Stopped.]"
                                "\n\n\tAre You Sure You Want To Continue: [Yes/No]: ").upper().strip()
                    
                    if choice == "NO":
                        Clear()
                        print("\n\t[The Loop Menu will now continue.]")
                        continue
                    elif choice == "YES":
                        Clear()
                        print("\n\n\t[The Loop Menu will now be terminated.]\n")
                        break

                elif num < 0:
                    Clear()
                    print("\n\t[Error. Please Enter A Positive Number.]")
                    continue
                elif num >= 3:
                    Clear()
                    print("\n\t[Error. Please Enter An Approriate Number Below.]")
                    continue
                else:
                    Clear()
                    print("\n\t[Error. Wrong Input.]")
                    continue
        
            except ValueError:
                Clear()
                print("\n\t[Error. Enter A Real Number.]"
                    "\n")
                continue

def List():
    while True:
            try:
                print(

                    "\n\n\tWelcome To List In Python"

                    "\n\n\t\tList Menu"

                    "\n\n\t[ 1 ] - Definition"
                    "\n\t[ 2 ] - Key Components"
                    "\n\t[ 0 ] - Terminate"

                )

                num = int(input("\n\n\tChoose A Number Of Your Choices: "))

                if num == 1:
                    Clear()
                    print(

                        "\n\n\t\t\t\tLIST DEFINITION"

                        "\n\n\tA list is a collection of items in a specific order, and it is one of Python's "
                        "\n\tmost versatile and commonly used data structures. Lists are mutable, meaning "
                        "\n\ttheir content can be changed after creation."
                        "\n\n\tLists are also a type of built-in data structure in Python (along with tuples, "
                        "\n\tsets and dictionaries), which is a specified way of storing and formatting data."

                    )
                
                elif num == 2:
                    Clear()
                    print(

                        "\n\n\t\tKEY COMPONENTS"

                        "\n\n\n\tCreating a List:"
                        "\n\n\tnumbers = [1, 2, 3, 4, 5]"
                        "\n\tfruits = ['apple', 'banana', 'cherry']"
                        "\n\tmixed = [1, 'apple', 3.14, True]"
                        "\n\tprint(numbers) \t\t\t\t\t# Output: [1, 2, 3, 4, 5]"

                        "\n\n\n\tAccessing List Elements:"
                        "\n\n\tfruits = ['apple', 'banana', 'cherry']"
                        "\n\tprint(fruits[2]) \t\t\t\t# Output: cherry"

                        "\n\n\n\tModifying a List:"
                        "\n\n\tmixed = [1, 'apple', 3.14, True]"
                        "\n\tmixed[1] = 'pineapple'"
                        "\n\tprint(mixed) \t\t\t\t\t# Output: [1, 'pineapple', 3.14, True]"

                        "\n\n\tmixed.append('orange') \t\t\t\t# Output: [1, 'pineapple', 3.14, True, 'orange']"
                        "\n\tmixed.insert(1, 'men') \t\t\t\t# Output: [1, 'men', 'pineapple', 3.14, True, 'orange']"

                        "\n\n\tmixed.remove('men') \t\t\t\t# Removes 'men"
                        "\n\tlast_item = mixed.pop() \t\t\t# Removes 'orange"
                        "\n\tdel fruits[0]  \t\t\t\t\t# Removes 1"
                        "\n\tprint(fruits) \t\t\t\t\t# Output: ['pineapple', 3.14, True]"

                    )
                
                elif num == 0:
                    Clear()
                    choice = input("\n\t[The List Menu Has Stopped.]"
                                "\n\n\tAre You Sure You Want To Continue: [Yes/No]: ").upper().strip()
                    
                    if choice == "NO":
                        Clear()
                        print("\n\t[The List Menu will now continue.]")
                        continue
                    elif choice == "YES":
                        Clear()
                        print("\n\n\t[The List Menu will now be terminated.]\n")
                        break

                elif num < 0:
                    Clear()
                    print("\n\t[Error. Please Enter A Positive Number.]")
                    continue
                elif num >= 3:
                    Clear()
                    print("\n\t[Error. Please Enter An Approriate Number Below.]")
                    continue
                else:
                    Clear()
                    print("\n\t[Error. Wrong Input.]")
                    continue
        
            except ValueError:
                Clear()
                print("\n\t[Error. Enter A Real Number.]"
                    "\n")
                continue

def Functions():
    while True:
            try:
                print(

                    "\n\n\tWelcome To Functions In Python"

                    "\n\n\t\tFunction Menu"

                    "\n\n\t[ 1 ] - Definition"
                    "\n\t[ 2 ] - Key Components"
                    "\n\t[ 0 ] - Terminate"

                )

                num = int(input("\n\n\tChoose A Number Of Your Choices: "))

                if num == 1:
                    Clear()
                    print(

                        "\n\n\t\t\t\tFUNCTIONS DEFINITION"

                        "\n\n\tA function is a reusable block of code that performs a specific task. "
                        "\n\n\tIt allows you to organize code, avoid repetition, and make your programs easier to manage and debug."
                        "\n\n\tA function is a block of organized, reusable code that is used to perform a single, related action."
                        "\n\n\tFunction blocks begin with the keyword def followed by the function name and parentheses"

                    )
                
                elif num == 2:
                    Clear()
                    print(

                        "\n\n\t\tKEY COMPONENTS"

                        "\n\n\n\tCreating Functions:"
                        "\n\n\tdef function_name(parameters):"
                        "\n\t\t\t\t\t\t# Code block (body of the function)"
                        "\n\t\treturn result \t\t\t# Optional: returns a value"

                        "\n\n\tdef greet():"
                        "\n\n\t\tprint('Hello, world!')"
                        "\n\tgreet() \t\t\t\t# Output: Hello, world!"

                        "\n\n\n\tParameters and Arguments:"
                        "\n\n\tdef greet(name):"
                        "\n\t\tprint(f'Hello, {name}!')"
                        "\n\tgreet('Alice') \t\t\t\t# Output: Hello, Alice!"

                        "\n\n\n\tReturn Statement:"
                        "\n\n\tdef add(a, b):"
                        "\n\t\treturn a + b"
                        "\n\tresult = add(3, 5)"
                        "\n\tprint(result)  \t\t\t\t# Output: 8"

                        "\n\n\n\tVariable Scope:"
                        "\n\n\tx = 10  \t\t\t\t# Global variable"
                        "\n\tdef show_value():"
                        "\n\t\tx = 20  \t\t\t# Local variable"
                        "\n\t\tprint(x)"
                        "\n\tshow_value()  \t\t\t\t# Output: 20"
                        "\n\tprint(x)      \t\t\t\t# Output: 10"

                        "\n\n\n\tReturn Statement:"
                        "\n\n\tdef add(a, b):"
                        "\n\t\treturn a + b"
                        "\n\tresult = add(3, 5)"
                        "\n\tprint(result)  \t\t\t\t# Output: 8"

                    )
                
                elif num == 0:
                    Clear()
                    choice = input("\n\t[The Function Menu Has Stopped.]"
                                "\n\n\tAre You Sure You Want To Continue: [Yes/No]: ").upper().strip()
                    
                    if choice == "NO":
                        Clear()
                        print("\n\t[The Function Menu will now continue.]")
                        continue
                    elif choice == "YES":
                        Clear()
                        print("\n\n\t[The Function Menu will now be terminated.]\n")
                        break

                elif num < 0:
                    Clear()
                    print("\n\t[Error. Please Enter A Positive Number.]")
                    continue
                elif num >= 3:
                    Clear()
                    print("\n\t[Error. Please Enter An Approriate Number Below.]")
                    continue
                else:
                    Clear()
                    print("\n\t[Error. Wrong Input.]")
                    continue
        
            except ValueError:
                Clear()
                print("\n\t[Error. Enter A Real Number.]"
                    "\n")
                continue

Main_Menu()