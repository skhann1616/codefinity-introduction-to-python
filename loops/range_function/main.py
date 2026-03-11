# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for promoday in range(5):
    day = weekdays[promoday] 
    promo = daily_promotions[promoday]
    print(f"{day}: Promotion on {promo}")