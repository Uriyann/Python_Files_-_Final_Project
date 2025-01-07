flavors = {
    "PEPPERONI": 12,
    "HAWAIIAN": 10,
    "BOLOGNESE": 5,
    "OVERLOAD": 20
}

sizes = {
    "SMALL": 5,
    "MEDIUM": 7,
    "LARGE": 10,
    "EXTRA LARGE": 15
}

toppings = {
    "OLIVES": 2,
    "MUSHROOMS": 2,
    "EXTRA CHEESE": 2,
    "BACON": 2,
    "NONE": 0
}

price = 0

while True:
    pizza = input("\nWould you like to purchase/buy a pizza [Yes/No]: ").strip().upper()
    
    if pizza == "NO":
        print("\nThank you for using the machine")
        print(f"\nThe total price of the order is: ${price}")
        break

    elif pizza == "YES":
        flavor_pizz = input(f"\nChoose: {flavors}: ").strip()
        sizes_pizz = input(f"Choose: {sizes}: ").strip()
        topps_pizz = input(f"Choose: {toppings}: ").strip()

        calc = flavors[flavor_pizz.upper()] + sizes[sizes_pizz.upper()] + toppings[topps_pizz.upper()]
        price += calc

        print("\n\nOrder Summary: "
              f"\n\nFlavor: {flavor_pizz}"
              f"\nSize: {sizes_pizz}"
              f"\nToppings: {topps_pizz}"
              
              f"\n\nPrice: ${price}")
        
        pizza1 = input("\nWould you like to purchase/buy another pizza [Yes/No]: ").strip().upper()

        if pizza1 == "YES":
            continue

        elif pizza1 == "NO":
            print("\n\nThank you for ordering")
            print(f"\nThe total price of the order is: ${price}")
            break
        
        else:
            print("\nWe don't have pizza that you like")
            continue

    else:
        print("\nWe don't have pizza that you like")
        continue