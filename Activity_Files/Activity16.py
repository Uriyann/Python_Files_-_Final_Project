def Act16():
      for x in range(1, 11):
            for z in range(1, x + 1):
                  print(" ", end=" ")
            for y in range(11, x, -1):
                  print("*", end= " ")

            print()

Act16()