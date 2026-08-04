"""3020"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())
SUM = 0

for i in range(1,d+1):
    if b and i != d and not i % b:
        SUM += c
    else:
        SUM += a
print(SUM)
