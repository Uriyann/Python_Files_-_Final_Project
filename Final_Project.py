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

# from Personal_Project_Files import (

#                     Drawing_Boat, Drawing_Heart, Drawing_Rhombus,
#                     Lyrics_Ver1, Lyrics_Ver2

#                     )

def Clear():

    os.system("cls")

def Main_Menu():
    try:
        while True:
            print(
                
                "\n\n\t| ======================================= |"
                  "\n\t| ========= -Compiled Projects- ========= |"
                  "\n\t| =============== ------- =============== |"
                  "\n\t| ============= -Main Menu- ============= |"
                  "\n\t| ======================================= |"
                  
                  "\n\n\t[ 1 ] - Activity_Project: "
                  "\n\t[ 2 ] - Code_Challenges_Project: "
                  "\n\t[ 3 ] - Personal_Project: "
                  "\n\t[ 4 ] - Test_Project: "
                  "\n\t[ 0 ] - Terminate "

                  )
            
            num = int(input("\n\n\tChoose A Number: "))

            if num == 1:
                Activities()
            elif num == 2:
                pass
            elif num == 3:
                pass
            elif num == 4:
                pass

            elif num == 0:
                print("\n\t[The Final Project will now be terminated.]"
                      "\n")
                break
            elif num < 0:
                print("\n\t[Error. Please Enter A Positive Number.]")
            elif num >= 5:
                print("\n\t[Error. Please Enter An Approriate Number.]")
            else:
                print("\n\t[Error. Wrong Input.]")
        
    except ValueError:
        print("\n\t[Error. Enter A Real Number.]"
              "\n")

def Activities():
    try:
        while True:
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
            
            num = int(input("\n\n\tChoose A Number: "))

            if num == 1:
                Activity1.Act1()
            elif num == 2:
                Activity2.Act2()
            elif num == 3:
                Activity3.Act3()
            elif num == 4:
                Activity4.Act4()
            elif num == 5:
                Activity5.Act5()
            elif num == 6:
                Activity6.Act6()
            elif num == 7:
                Activity7.Act7()
            elif num == 8:
                Activity8.Act8()
            elif num == 9:
                Activity9.Act9()
            elif num == 10:
                Activity10.Act10()
            elif num == 11:
                Activity11.Act11()
            elif num == 12:
                Activity12.Act12()
            elif num == 13:
                Activity13.Act13()
            elif num == 14:
                Activity14.Act14()
            elif num == 15:
                Activity15.Act15()
            elif num == 16:
                Activity16.Act16()
            elif num == 17:
                Activity17.Act17()
            elif num == 18:
                Activity18.Act18()
            elif num == 19:
                Activity19.Act19()
            elif num == 20:
                Activity20.Act20()
            elif num == 21:
                Activity21.Act21()
            elif num == 22:
                Activity22.Act22()
            elif num == 23:
                Activity23.Act23()
            elif num == 24:
                Activity24.Act24()
            elif num == 25:
                Activity25.Act25()

            elif num == 0:
                print("\n\t[The Activity Project will now be terminated.]"
                      "\n")
                Main_Menu()
                break
            elif num < 0:
                print("\n\t[Error. Please Enter A Positive Number.]")
            elif num >= 26:
                print("\n\t[Error. Please Enter An Approriate Number.]")
            else:
                print("\n\t[Error. Wrong Input.]")

    except ValueError:
        print("\n\t[Error. Enter A Real Number.]"
              "\n")
        
def Code_Chal():
    try:
        while True:
            print("\n\n\t| ======================================= |"
                  "\n\t| ========= -Compiled Projects- ========= |"
                  "\n\t| =============== ------- =============== |"
                  "\n\t| ============= -Code_Menu- ============= |"
                  "\n\t| ======================================= |"
                
                "\n\n\t[ 1 ] - Code_Challenge_1  \t[ 10 ] - Code_Challenge_1"
                  "\n\t[ 2 ] - Code_Challenge_2  \t[ 11 ] - Code_Challenge_1"
                  "\n\t[ 3 ] - Code_Challenge_3  \t[ 12 ] - Code_Challenge_1"
                  "\n\t[ 4 ] - Code_Challenge_4  \t[ 13 ] - Code_Challenge_1"
                  "\n\t[ 5 ] - Code_Challenge_5  \t[ 14 ] - Code_Challenge_1"
                  "\n\t[ 6 ] - Code_Challenge_6  \t[ 15 ] - Code_Challenge_1"
                  "\n\t[ 7 ] - Code_Challenge_7  \t[ 16 ] - Code_Challenge_1"
                  "\n\t[ 8 ] - Code_Challenge_8  \t[ 0 ] - Terminate"
                  "\n\t[ 9 ] - Code_Challenge_9"
                  
                  )
            
            num = int(input("\n\n\tChoose A Number: "))

            if num == 1:
                code_challenge1
            elif num == 2:
                Activity2.Act2()
            elif num == 3:
                Activity3.Act3()
            elif num == 2:


if __name__ == "__main__":
    Main_Menu()

"""Unfinished"""