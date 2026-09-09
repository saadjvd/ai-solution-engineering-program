print("===== IMTIAZ SUPER MARKET =====")

name = input("Enter your name: ")
product = input("Enter the product name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item (PKR): "))

total = quantity * price

print("\n===== ORDER SUMMARY =====")
print(f"Customer: {name}")
print(f"Product: {product}")
print(f"Quantity: {quantity}")
print(f"Price per item: PKR {price}")
print(f"Total: PKR {total}")

print(f"\nThank you for shopping with Imtiaz Super Market, {name}!")