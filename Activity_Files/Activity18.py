def Act18():
      num = int(input("Enter a number of right triangle: ")) 

      for i in range(1, 6):
            for r in range(1, num + 1):
                  print(" ", end= " ")
                  for j in range(1, i + 1):
                        print("*", end= " ")
                  for k in range(5, i, -1):
                        print(" ", end= " ") 

            print()

Act18()