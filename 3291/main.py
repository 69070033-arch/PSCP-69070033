"""3291: Right Arrow"""
import math

k = int(input())
n = int(input())
space1, space2 = 0, n//2

for _ in range(math.ceil(n/2)-1):
    print(" "*(space1)+"*"*k)
    space1 += 1

for _ in range(math.ceil(n/2)):
    print(" "*(space2)+"*"*k)
    space2 -= 1
