"""3106: Basic ATM"""

amount = int(input())

if amount < 100 or amount > 20000 or amount % 100:
    print("ERROR")
else:
    b1000 = amount // 1000
    amount = amount % 1000

    b500 = amount // 500
    amount = amount % 500

    b100 = amount // 100

    if b1000 > 0:
        print(f"1000 = {b1000}")
    if b500 > 0:
        print(f"500 = {b500}")
    if b100 > 0:
        print(f"100 = {b100}")
