"""3012: ภาษีรถยนต์"""

year = int(input())
cc = int(input())

if year <= 1990:
    if cc <= 1500:
        TAX = 1250
    elif cc <= 2000:
        TAX = 1400
    else:
        TAX = 2000
elif year <= 1999:
    if cc <= 1500:
        TAX = 1100
    elif cc <= 2000:
        TAX = 1300
    else:
        TAX = 1700
else:
    if cc <= 1500:
        TAX = 1000
    elif cc <= 2000:
        TAX = 1200
    else:
        TAX = 1500

print(TAX)
