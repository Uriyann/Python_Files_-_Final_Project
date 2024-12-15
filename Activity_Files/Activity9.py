def Act9():
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