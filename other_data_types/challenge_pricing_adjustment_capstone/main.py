grocery_inventory = { 
"Milk": ("Dairy", 3.50, 8),
"Eggs": ("Dairy", 5.50, 30),
"Bread": ("Bakery", 2.99, 15),
"Apples": ("Produce", 1.50, 50)
}

price_eggs = grocery_inventory.get("Eggs")

if price_eggs[1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory.update({"Eggs":("Dairy",4.50,30)})
else:
    print("Eggs price is resonable")

grocery_inventory["Tomatoes"] = ("Produce",1.20,30)
print("Inventory after adding tomatoes:",grocery_inventory)

if grocery_inventory["Milk"][2] <10:
    print("milk needs to be restocked. increasing stock by 20 units.")
    old_category, old_price, old_stock = grocery_inventory["Milk"]
    grocery_inventory["Milk"] = (old_category, old_price, old_stock + 20)

else:
    print("Milk has sufficient stock")

if grocery_inventory["Apples"][1] >2:
    grocery_inventory.pop("Milk")
    print("Apples removed from inventory due to high price.")

print("Updated Inventory:", grocery_inventory)