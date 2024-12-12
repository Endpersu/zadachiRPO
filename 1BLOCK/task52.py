def calculate_total_cost(candy_price, cookie_price, apple_price, x, y, z):
    total_cost = (candy_price * x) + (cookie_price * y) + (apple_price * z)
    return total_cost


candy_price = 500  
cookie_price = 300  
apple_price = 100  

x = 2  
y = 3  
z = 5  

total = calculate_total_cost(candy_price, cookie_price, apple_price, x, y, z)
print(f"Общая стоимость покупки: {total} рублей")