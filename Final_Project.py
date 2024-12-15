import os

from Activity_Files import (
                    
                    Activity1, Activity2, Activity3, Activity4, Activity5, Activity6, 
                    Activity7, Activity8, Activity9, Activity10, Activity11, Activity12, 
                    Activity13, Activity14, Activity15, Activity16, Activity17, Activity18, 
                    Activity19, Activity20, Activity21, Activity22, Activity23, Activity24,
                    Activity25

                    )

from Code_Challenges_Files import (
                    
                    Code_Challenges_Compilation
                    
                    )

from Personal_Project_Files import (

                    Drawing_Boat, Drawing_Heart, Drawing_Rhombus,
                    Lyrics_Ver1, Lyrics_Ver2

                    )

def Clear():

    os.system("cls")

def Main_Menu():
    try:
        while True:
            print("\n\n\t| ======================================= |"
                  "\n\t| ========= -Compiled Projects- ========= |"
                  "\n\t| =============== ------- =============== |"
                  "\n\t| ============= -Main Menu- ============= |"
                  "\n\t| ======================================= |"
                  
                  "\n\n\t[ 1 ] - Activity_Project: "
                  "\n\t[ 2 ] - Code_Challenges_Project: "
                  "\n\t[ 3 ] - Personal_Project: "
                  "\n\t[ 4 ] - Test_Project: "
                  "\n\t[ 0 ] - Terminate ")
            
            num = int(input("\n\n\tChoose A Number: "))

            if num == 1:
                pass
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

# def Activities():
#     try:
#         while True:


if __name__ == "__main__":
    Main_Menu()