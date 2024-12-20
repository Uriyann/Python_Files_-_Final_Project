def Act5():
    temp = float(input("Enter Temperature in Farenheit: "))

    cel = (temp - 32) * 5/9

    print(f"The conversion of {temp} degrees Farenheit is {round(cel, 2)} degrees Celcius.")
