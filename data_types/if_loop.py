weight = float(input("Enter the weight of the package in Kg: "))

if weight <= 0:
    print("Invalid weight. Please enter a positive value.")
elif weight <= 2:
    shipping_cost = 10.00
elif weight <= 5:
    shipping_cost = 15.00
elif weight <= 10:
    shipping_cost = 20.00
else:
    shipping_cost = 25.00

if weight > 0:
    print(f"The shipping cost for a {weight} kg package is ${shipping_cost:.2f}.")