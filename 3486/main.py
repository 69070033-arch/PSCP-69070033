"""3486: ตำบลกระสุนตก"""

n = int(input())
shots = [tuple(map(int, input().split())) for _ in range(n)]

for tx in range(1001):
    for ty in range(1001):
        if all((tx - x) ** 2 + (ty - y) ** 2 == d ** 2 for x, y, d in shots):
            print(tx, ty)
            raise SystemExit
