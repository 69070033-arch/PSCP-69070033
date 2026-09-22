"""3297: ตั๋วหนังสุดป่วน"""

n = int(input())
price = []
ticket = []

while n > 0:
    a, b = map(int, input().split())
    n -= b

    if a < 15:
        n += b
        price.append(-1)
        ticket.append(0)
    elif n < 0:
        n += b
        price.append(-2)
        ticket.append(0)
    elif 15 < a <= 22:
        price.append(int((b*150)-(((b*150)/100)*20)))
        ticket.append(n)
    elif a >= 60:
        price.append(int((b*150)/2))
        ticket.append(n)
    else:
        price.append(b*150)
        ticket.append(n)

for pos, items in enumerate(price):
    if items > 0:
        print(items, ticket[pos])
    else:
        print(items)
