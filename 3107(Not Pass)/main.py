"""3107: Bonus"""

position, year, salary = input().split()
position = position.upper()
year = int(year)
salary = int(salary)

if position == "M":
    base_bonus = 1500
    if year < 5:
        percent = 6
    elif year <= 10:
        percent = 8
    else:
        percent = 10
elif position == "B":
    base_bonus = 1000
    if year < 5:
        percent = 5
    elif year <= 10:
        percent = 6
    else:
        percent = 7
else:
    base_bonus = 500
    if year < 5:
        percent = 4
    elif year <= 10:
        percent = 5
    else:
        percent = 6

computed_bonus = (salary * percent) // 100
total_bonus = base_bonus + computed_bonus

print(total_bonus)
