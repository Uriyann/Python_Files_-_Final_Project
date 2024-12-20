def Act7():
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
