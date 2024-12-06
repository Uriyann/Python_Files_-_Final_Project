pre = int(input("\n\n\tPrelim Score: "))
mid = int(input("\n\tMidterm Score: "))
semi = int(input("\n\tSemi-Final Score: "))
final = int(input("\n\tFinal Score: "))
quiz = int(input("\n\tQuiz Score: "))
proj = int(input("\n\tProject Score: " ))

fg = (pre * 0.15) + (mid * 0.15) + (semi * 0.15) + (final * 0.15) + (quiz * 0.25) + (proj * 0.15)


print(f"\n\n\tYour grade is {fg}")

if pre > 100:
	print("\n\tError. Wrong input")
elif fg >= 65:
	print("\n\tCongratulations! You have passed the course")
else:
	print("\n\tUnfortunately You Have Failed")



