import os

os.system('cls')

print("\n\n\t\t\b\b|========================|\n\t\t\b\b|   By: Joshua Barotea   |\n\t\t\b\b|========================|")


far = float(input("\n\n\tEnter the Rate of Temperature in Farehnheit: "))

comp = (far - 32) * 5 / 9

print(f"\n\tThe Degrees of Farehnheit {far} °F converted into Celcius is {round(comp, 2)} °C")