name= input("Enter your name here:  ")
isStud = input ("Are you currently enrolled in DLL? [Yes or No]:  ").upper().strip()


if isStud == "YES":
	yearLev =input("What year are you currently enrolled? \nF- Freshmen \nS-Sophomore \nJ-Junior  \nR-Senior: \nPlease enter your answer here: ").upper().strip()
	
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