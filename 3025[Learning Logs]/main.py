"""3025"""

x = int(input())
y = int(input())

if not x % 3 and y >= 21:
    x+=1
if x > 12:
    x-=12

if x <= 3:
    print("winter")
elif x <= 6:
    print("spring")
elif x <= 9:
    print("summer")
elif x <= 12:
    print("fall")
