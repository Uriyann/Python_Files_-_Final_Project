isContinue = True

def denomination(amount):

      one_thou = amount // 1000 
      ans_thou = 1000 % amount

      five_h = 500 // ans_thou
      ans_fiveh = 500 % ans_thou

      two_h = 200 // ans_fiveh
      ans_twoh = 200 % ans_fiveh
      
      one_h = 100 // ans_twoh
      ans_oneh = 100 % ans_twoh

      fifty = 50 // ans_oneh
      ans_fifty = 50 % ans_oneh

      twenty = 20 // ans_fifty
      ans_twenty = 20 % ans_fifty

      ten = 10 // ans_twenty
      ans_ten = 10 % ans_twenty

      five = 5 // ans_ten
      ans_five = 5 % ans_ten

      ans_one = 1 // ans_five


      print(f"1000 - {one_thou} "
      f"1000 - {five_h} "
      f"1000 - {two_h} "
      f"1000 - {one_h} "
      f"1000 - {fifty} "
      f"1000 - {twenty} "
      f"1000 - {ten} "
      f"1000 - {five} "
      f"1000 - {ans_one} "
      )

denomination(int(input("Enter a number: ")))