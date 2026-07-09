"""3017"""

money = int(input())
per10 = (10/100)*money

if per10 < 50:
    per10 = 50
elif per10 > 1000:
    per10 = 1000

vat = (7/100)*(money+per10)
print(f"{money+per10+vat:.2f}")
