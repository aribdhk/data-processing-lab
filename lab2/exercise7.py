def apply_discount(total):
    if total >= 2000:
        return total - total * 0.10
    return total


cart = [
    {"name": "Keyboard", "price": 800, "quantity": 1},
    {"name": "Mouse", "price": 450, "quantity": 2},
    {"name": "USB Cable", "price": 150, "quantity": 3},
    {"name": "Notebook", "price": 120, "quantity": 4},
]

total = 0
for item in cart:
    total += item["price"] * item["quantity"]

final_price = apply_discount(total)

print("Cart total       :", total)
print("Final price      :", final_price)
if final_price < total:
    print("10% discount applied.")
else:
    print("No discount applied.")