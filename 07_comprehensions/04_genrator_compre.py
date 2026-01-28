daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]
#this will not make a memory they will keep in streams ()
total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)