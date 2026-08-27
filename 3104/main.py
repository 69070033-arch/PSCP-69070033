"""3104: Ticket"""

input_data = input().split()
age = int(input_data[0])
day = input_data[1]

if age < 5:
    price = 0
elif age <= 18:
    price = 100
else:
    price = 150

if day == "Wed":
    price = int(price / 2)

print(price)
