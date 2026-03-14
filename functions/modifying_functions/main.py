def apply_discount(price, discount=0.05):
    price = price * (1 - discount)
    return price

def apply_tax(price, tax=0.07):
    price = price * (1 + tax)
    return price

def calculate_total(price, discount=0.05, tax=0.07):
    disc = apply_discount(price,discount)
    total = apply_tax(disc,tax)
    return total

print(f"Total cost with default discount and tax: ${calculate_total(120)}")
print(f"Total cost with custom discount and tax: ${calculate_total(100, discount=0.10, tax=0.08)}")

calculate_total(120)
calculate_total(100, discount=0.10, tax=0.08)