"""3036"""
import math

n = int(input())
r = math.ceil(math.sqrt(n))
k = n - (r - 1)**2
wall = 0

if not k % 2:
    wall = (2*r) - 3
else:
    wall = (2*r) - 2

print(wall)
