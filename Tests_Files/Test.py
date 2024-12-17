import os

from Personal_Project_Files import (

                    Drawing_Boat, Drawing_Heart, Drawing_Rhombus,
                    Lyrics_Ver1, Lyrics_Ver2

                    )

def Clear():

    os.system("cls")

def Per_Project():
    while True:
        try:
            print(
                
                "\n\n\t| ======================================= |"
                  "\n\t| ========= -Compiled Projects- ========= |"
                  "\n\t| =============== ------- =============== |"
                  "\n\t| =========== -Personal_Menu- =========== |"
                  "\n\t| ======================================= |"
                
                "\n\n\t[ 1 ] - Personal_Proj_1  \t[ 4 ] - Personal_Proj_4"
                  "\n\t[ 2 ] - Personal_Proj_2  \t[ 5 ] - Personal_Proj_5"
                  "\n\t[ 3 ] - Personal_Proj_3  \t[ 0 ] - Terminate"
                  
                  )
            
            num = int(input("\n\n\tChoose A Number: "))

            if num == 1:
                Drawing_Boat.Boat()
            elif num == 2:
                Drawing_Heart.Heart()
            elif num == 3:
                Drawing_Rhombus.Rhombus()
            elif num == 4:
                Lyrics_Ver1.Lyrics_v1()
            elif num == 5:
                Lyrics_Ver2.Lyrics_v2()

            elif num == 0:
                Clear()
                choice = input("\n\t[The Personal Project Menu Has Stopped.]"
                               "\n\n\tAre You Sure You Want To Continue: [Yes/No]: ").upper().strip()
                
                if choice == "NO":
                    Clear()
                    print("\n\t[The Personal Project Menu will now continue.]")
                    continue
                elif choice == "YES":
                    Clear()
                    print("\n\n\t[The Personal Project Menu will now be terminated.]\n")
                    break

            elif num < 0:
                Clear()
                print("\n\t[Error. Please Enter A Positive Number.]")
                continue
            elif num >= 6:
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

Per_Project()