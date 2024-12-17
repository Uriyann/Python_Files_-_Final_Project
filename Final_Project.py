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
                  
                  "\n\n\t[ 1 ] - Activity_Project: "
                  "\n\t[ 2 ] - Code_Challenges_Project: "
                  "\n\t[ 3 ] - Python Fundamentals: "
                  "\n\t[ 0 ] - Terminate "

                  )
            
            num = int(input("\n\n\tSelect The Topic Of Your Choice: "))

            if num == 1:
                Clear()
                Activities()
            elif num == 2:
                Clear()
                Code_Chal()
            elif num == 3:
                Clear()
                Fundamentals()


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
                print("\n\t[Error. Please Enter An Approriate Number.]")
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
                print("\n\t[Error. Please Enter An Approriate Number.]")
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
                print("\n\t[Error. Please Enter An Approriate Number.]")
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
                
                "\n\n\t[ 1 ] - Print_Statements     \t[ 10 ] - Loops"
                  "\n\t[ 2 ] - Variables            \t[ 11 ] - List"
                  "\n\t[ 3 ] - Operators            \t[ 12 ] - Functions"
                  "\n\t[ 4 ] - Conditionals         \t[ 0 ] - Terminate"
                  
                  )
            
            num = int(input("\n\n\tChoose A Number Of Your Choices: "))

            if num == 1:
                Clear()
                Print()
            elif num == 2:
                Clear()
                Variables()

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
                print("\n\t[Error. Please Enter An Approriate Number.]")
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

                "\n\tWelcome To Printing In Python"

                "\n\n\t\tPrint Menu"

                "\n\n\t[ 1 ] - Definition"
                  "\n\t[ 2 ] - Key Components"
                  "\n\t[ 0 ] - Terminate"

            )

            num = int(input("\n\n\tChoose A Number Of Your Choices: "))

            if num == 1:
                print(

                    "\n\t\t\t\tPRINTING DEFINITION"

                    "\n\n\tPrinting is the act of sending information (like strings, numbers, or variables)"
                    "\n\tto an output device, such as a console, where it can be displayed for the user to read."
                    "\n\n\tIn Python, printing is done using the print() function."
                    "\n\n\tTo use the print function, you simply type print() followed by the value(s) that you want to print. "
                )
            elif num == 2:
                print(

                    "\n\t\tKEY COMPONENTS"

                    "\n\n\n\tBasic Usage:"
                    "\n\n\n\tprint('Hello, World!')"
                    "\n\t# Output: Hello, World!"

                    "\n\n\n\tPrinting Multiple Values:"
                    "\n\n\n\tprint('Hello', 'World', 123)"
                    "\n\t# Output: Hello World 123"

                    "\n\n\n\tCustom End:"
                    "\n\n\n\tprint('Hello', end=' ')"
                    "\n\tprint('World!')"
                    "\n\t# Output: Hello World!"

                    "\n\n\n\tPrinting Variables:"
                    "\n\n\n\tname = 'Joshua!')"
                    "\n\tprint('Hello', name)"
                    "\n\t# Output: Hello Joshua!"

                    "\n\n\n\tFormatted Strings:"
                    "\n\n\n\tage = 21)"
                    "\n\tprint(f'I am {age} years old.')"
                    "\n\t# Output: I am 18 years old."

                    "\n\n\n\tEscape Sequence:"
                    "\n\n\n\tprint('Hello\\nWorld')"
                    "\n\t# Output: Hello"
                    "\n\t          World"

                    "\n\n\n\tprint('Hello\\tWorld')"
                    "\n\t# Output: Hellow      World"

                    "\n\n\n\tprint('Helloo\\bWorld')"
                    "\n\t# Output: Hello World"
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
                print("\n\t[Error. Please Enter An Approriate Number.]")
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

                    "\n\tWelcome To Variables In Python"

                    "\n\n\t\tVariable Menu"

                    "\n\n\t[ 1 ] - Definition"
                    "\n\t[ 2 ] - Key Components"
                    "\n\t[ 0 ] - Terminate"

                )

                num = int(input("\n\n\tChoose A Number Of Your Choices: "))

                if num == 1:
                    print(

                        "\n\t\t\t\tVARIABLE DEFINITION"

                        "\n\n\tA variable is a name that refers to a value stored in memory. "
                        "\n\tIt allows you to store, retrieve, and manipulate data."
                        "\n\n\tVariables in programming are like named boxes that can store information."
                        "\n\tYou can use variables to store any type of data, such as numbers, strings, lists, and objects."

                    )
                
                elif num == 2:
                    print(

                        "\n\t\tKEY COMPONENTS"

                        "\n\n\n\tCreating Variables"
                        "\n\n\tname = 'Joshua' \t# String"
                        "\n\tage = 18 \t# Integer"
                        "\n\theight = 5.9 \t# Float"
                        "\n\tis_student = True \t# Boolean"

                        "\n\n\n\tChanging Values"
                        "\n\n\tage = 18"
                        "\n\tage = 19"
                        "\n\tprint(age)"
                        "\n\t# Output: 19"

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
                    print("\n\t[Error. Please Enter An Approriate Number.]")
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

                    "\n\tWelcome To Operators In Python"

                    "\n\n\t\tOperators Menu"

                    "\n\n\t[ 1 ] - Definition"
                    "\n\t[ 2 ] - Key Components"
                    "\n\t[ 0 ] - Terminate"

                )

                num = int(input("\n\n\tChoose A Number Of Your Choices: "))

                if num == 1:
                    print(

                        "\n\t\t\t\tOPERATORS DEFINITION"

                        "\n\n\tOperators are symbols or keywords used to perform operations on variables and values."
                        "\n\n\tThese operators allow for various functionalities, from basic arithmetic operations "
                        "\n\tlike addition, subtraction, multiplication, and division to more complex comparisons and logical operations."
                        "\n\tYou can use variables to store any type of data, such as numbers, strings, lists, and objects."
                        "\n\n\tPython provides several types of operators, including arithmetic operators for mathematical calculations, "
                        "\n\tcomparison operators to compare values, and assignment operators to assign values to variables."

                    )
                
                elif num == 2:
                    print(

                        "\n\t\tKEY COMPONENTS"

                        "\n\n\n\tArithmetic Operators"
                        "\n\n\tAddition = 5 + 3 \t# Output: 8"
                        "\n\tSubtraction = 5 - 3 \t# Output: 2"
                        "\n\tMultiplication = 5 * 3 \t# Output: 15"
                        "\n\tDivision = 5 / 2 \t# Output: 2.5"
                        "\n\tModulus_Remainder = 5 % 2 \t# Output: 1"
                        "\n\tExponentiation = 5 ** 2 \t# Output: 25"
                        "\n\tFloor_Division = 5 // 2 \t# Output: 2"

                        "\n\n\n\tAssignment Operators"
                        "\n\n\tnum = 5 \t# Output: 5"
                        "\n\tnum += 2 \t# Output: 7"
                        "\n\tnum -= 4 \t# Output: 3"
                        "\n\tnum *= 10 \t# Output: 30"
                        "\n\tnum /= 5 \t# Output: 6.0"
                        "\n\tnum %= 6 \t# Output: 0"
                        "\n\tprint(num)"
                        "\n\t# Output: 0"

                        "\n\n\n\tComparison Operators"
                        "\n\n\tEqual = 5 == 5 \t# Output: True"
                        "\n\tNot_Equal = 5 != 3 \t# Output: True"
                        "\n\tGreater = 5 > 3 \t# Output: True"
                        "\n\tLesser = 5 < 2 \t# Output: False"
                        "\n\tGreater_or_Equal = 5 >= 5 \t# Output: True"
                        "\n\tLesser_or_Equal = 5 <= 5 \t# Output: False"

                        "\n\n\n\tLogical  Operators"
                        "\n\n\tAnd = True and False \t# Output: False"
                        "\n\tOr = True or False \t# Output: True"
                        "\n\tNot = not False \t# Output: True"

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
                    print("\n\t[Error. Please Enter An Approriate Number.]")
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

if __name__ == "__main__":
    Main_Menu()

"""Unfinished"""