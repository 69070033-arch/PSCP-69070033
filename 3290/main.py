"""3290: Left Arrow"""
import math

k = int(input())
n = int(input())
space1, space2 = n//2, 0

for _ in range(math.ceil(n/2)-1):
    print(" "*(space1)+"*"*k)
    space1 -= 1

for _ in range(math.ceil(n/2)):
    print(" "*(space2)+"*"*k)
    space2 += 1
