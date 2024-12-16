def Code_Chal5():
	print("\n\n\t\t\b\b|========================|\n\t\t\b\b|   By: Joshua Barotea   |\n\t\t\b\b|========================|")

	name = input("\n\n\tEnter Your Name: ")

	pre = int(input("\n\n\tEnter Your Prelim Score: "))
	mid = int(input("\tEnter Your Midterm Score: "))
	senal = int(input("\tEnter Your Semi-Final Score: "))
	fin = int(input("\tEnter Your Final Score: "))
	quiz = int(input("\tEnter Your Quiz Score: "))
	proj = int(input("\tEnter Your Project Grade: "))


	fin_grade = (pre * 0.15) + (mid * 0.15) + (senal * 0.15) + (fin * 0.15) + (quiz * 0.25) + (proj * 0.15)
	

	print(f"\n\n\tHello {name}, Your Final Grade is: {fin_grade}")

	if fin_grade >= 100:
		print("\tDid You Entered Your Real Grade?")
	elif fin_grade >= 75:
		print("\tCongratulations, You Are Passed!")
	else:
		print("\tUnfortunately, You Are Failed.")