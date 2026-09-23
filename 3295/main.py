"""3295: Electric_Using"""
from decimal import Decimal, ROUND_HALF_UP

elec_using = int(input())
ft = elec_using * 0.5
price = 0

while elec_using > 0:
    if elec_using > 200:
        elec = elec_using - 200
        price += 15 * elec
        elec_using = 200
    elif elec_using > 100:
        elec = elec_using - 100
        price += 12 * elec
        elec_using = 100
    elif elec_using > 50:
        elec = elec_using - 50
        price += 10 * elec
        elec_using = 50
    elif elec_using > 10:
        elec = elec_using - 10
        price += 7 * elec
        elec_using = 10
    else:
        price += 5 * elec_using
        elec_using = 0

vat = (price / 100) * 7
total = price + vat + ft
final_price = Decimal(str(total)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
print(final_price)
