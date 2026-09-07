"""3231: เกมทายลูกเต๋า"""

g = int(input())
r = int(input())

if g > r or 1 < g > 6 or 1 < r > 6:
    print("Invalid")
elif g == r:
    print("Correct!")
else:
    print("Wrong!")
