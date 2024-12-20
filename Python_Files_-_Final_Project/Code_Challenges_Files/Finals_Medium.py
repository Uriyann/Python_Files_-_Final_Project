flavors = {
    "Pepperoni": 200,
    "Hawaiian": 250,
    "Supreme": 300,
    "Cheese": 180
}

sizes = {
    "Small": 50,
    "Medium": 100,
    "Large": 150,
    "Extra Large": 200
}

toppings = {
    "Olives": 30,
    "Mushrooms": 40,
    "Extra Cheese": 50,
    "Bacon": 60,
    "None": 0
}

price = 0

while True:
    pizza = input("Would you like to purchase/buy a pizza: ").strip().upper()
    
    if pizza == "NO":
        break

    elif pizza == "YES":
        flavor_pizz = input(f"Choose: {flavors}: ").strip()
        sizes_pizz = input(f"Choose: {sizes}: ").strip()
        topps_pizz = input(f"Choose: {toppings}: ").strip()

        calc = flavors[flavor_pizz] + sizes[sizes_pizz] + toppings[topps_pizz]
        price += calc

        print("Order Summary: "
              f"\nFlavor: {flavor_pizz}"
              f"\nSize: {sizes_pizz}"
              f"\nToppings: {topps_pizz}"
              
              f"\n\nPrice: {price}")
        
        pizza1 = input("Would you like to purchase/buy another pizza: ").strip().upper()

        if pizza1 == "YES":
            pizza

        elif pizza1 == "NO":
            break
        

    else:
        print("We don't have pizza that you like")
        continue

        