"""3042"""

n = int(input())

for i in range(n,-1,-1):
    if not i % 10:
        print(i, end=" ")
