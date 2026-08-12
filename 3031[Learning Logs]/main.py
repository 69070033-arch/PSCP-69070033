"""3031: [LEARNING LOGS] Ink"""
import math

s, n = map(int, input().split())

for _ in range(n):
    x, y = map(int, input().split())
    d = math.ceil((3.1416*((x**2) + (y**2)))/s)
    print(d)
