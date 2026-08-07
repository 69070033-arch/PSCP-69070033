"""3036"""
import math
n = int(input())
numO = not n % 2
count = 1
j = 16
while j >= n:
    j -= 3+(1+int(j/5))
    print(f"{j, int(j/5)}")
    count += 1

print(count)