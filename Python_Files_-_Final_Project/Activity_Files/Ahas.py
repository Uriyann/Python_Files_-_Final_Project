even = 0
odd = 0
sum = 0

for i in range(10):
      num = int(input("Enter a number: "))
      if num %2 == 0:
            even += num
      else:
            odd += num

      sum += num

print(even)
print(odd)

print(sum)


