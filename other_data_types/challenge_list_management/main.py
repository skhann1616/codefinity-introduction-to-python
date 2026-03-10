meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiments = ["Mustard", 1.99, 75, "Spicy"]
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]

#main list
deli_dept=[meat,cheese,condiments]
print("Initial Deli List: ",deli_dept)

if meat[0]=="Ham" and meat[2]<100:
    meat[2]=100

deli_dept.append(seasonal_meat)
deli_dept.remove(condiments)
deli_dept.sort()

print("Updated Deli List:", deli_dept)
