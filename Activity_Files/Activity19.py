def Act19():
      contin = True
      count = 0

      while contin == True:
            name = input("Enter a name: ").upper().strip()

            if name == "STOP":
                  print("The loop has been terminated")
                  print(f"You have entered {count} number of names")
                  break

            else:
                  print(f"Hi {name}")
                  count += 1
                  continue

Act19()