def calculate_total(price, percent):
    total = price + 0.01 * percent * price
    return total


calculate_total(20, 15)

my_price = 78.55
my_tip = 20
my_total = calculate_total(my_price, my_tip)
print(my_total)
