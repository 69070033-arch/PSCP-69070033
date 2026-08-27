"""3111: [LEARNING LOGS] สหกรณ์โรงเรียน"""

from decimal import Decimal, ROUND_HALF_UP

status = input().strip().upper()
n = int(input())

total_price = Decimal("0.0")
for _ in range(n):
    total_price += Decimal(input().strip())

if status == "Y":
    net_price = total_price * Decimal("0.95")
elif status == "N" and total_price >= Decimal("500"):
    net_price = total_price * Decimal("0.97")
else:
    net_price = total_price

result = net_price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(f"{result:.2f}")
