flavors = {
    "Pepperoni": 12,
    "Hawaiian": 10,
    "Bolognese": 5,
    "Overload": 20
}

sizes = {
    "Small": 5,
    "Medium": 7,
    "Large": 10,
    "Extra Large": 15
}

toppings = {
    "Olives": 2,
    "Mushrooms": 2,
    "Extra Cheese": 2,
    "Bacon": 2,
    "None": 0
}

price = 0

while True:
    pizza = input("\nWould you like to purchase/buy a pizza [Yes/No]: ").strip().upper()
    
    if pizza == "NO":
        print("\nThank you for using the machine")
        break

    elif pizza == "YES":
        flavor_pizz = input(f"\nChoose: {flavors}: ").strip()
        sizes_pizz = input(f"Choose: {sizes}: ").strip()
        topps_pizz = input(f"Choose: {toppings}: ").strip()

        calc = flavors[flavor_pizz] + sizes[sizes_pizz] + toppings[topps_pizz]
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