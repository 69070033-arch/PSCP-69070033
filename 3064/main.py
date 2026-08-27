"""3064: วันเกิด"""

y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())

Ysum = y1 - y2
Msum = m1 - m2
Dsum = abs(d1 - d2)

#print(Ysum, Msum, Dsum)

if not Ysum:
    if not Msum:
        if 0 < Dsum <= 7:
            print(0)
        elif Dsum > 7:
            print(2)
        elif Dsum < 0:
            print(1)
    elif Msum > 0:
        print(2)
    elif Msum < 0:
        print(1)
elif Ysum < 0:
    print(1)
elif Ysum > 0:
    print(2)
