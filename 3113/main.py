"""3113 : กระต่ายน้อยกินราเมน"""

size, ramen_type = input().split()

if size == "S":
    if ramen_type == "R":
        BASE_PRICE = 60
    else:
        BASE_PRICE = 80
elif size == "M":
    if ramen_type == "R":
        BASE_PRICE = 80
    else:
        BASE_PRICE = 100
else:
    if ramen_type == "R":
        BASE_PRICE = 100
    else:
        BASE_PRICE = 120

topping_input = input().split()
topping_type = topping_input[0]

topping_price = 0
if topping_type != "N":
    count = int(topping_input[1])
    if topping_type == "P":
        topping_price = count * 15
    elif topping_type == "E":
        topping_price = count * 10

total_price = BASE_PRICE + topping_price
print(total_price)
