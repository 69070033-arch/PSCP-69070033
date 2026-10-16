"""3481: ลอดสะพาน"""
length, n = map(int, input().split())

bridges = []
for _ in range(n):
    a, b = map(int, input().split())
    bridges.append((a, b))

best = 0

for spot in range(length):
    count = 0
    for bridge in bridges:
        if bridge[0] <= spot < bridge[1]:
            count += 1
    if count > best:
        best = count

print(best)
