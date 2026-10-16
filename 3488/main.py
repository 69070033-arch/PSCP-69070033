"""3488: ไฟส่อง"""

n = int(input())

diff = [0] * 361

for _ in range(n):
    a, b = map(int, input().split())
    if a < b:
        diff[a] += 1
        diff[b] -= 1
    else:
        diff[a] += 1
        diff[360] -= 1
        diff[0] += 1
        diff[b] -= 1

lit = 0
coverage = []

for angle in range(360):
    lit += diff[angle]
    coverage.append(1 if lit > 0 else 0)

best = current = 0

for angle in range(720):
    if coverage[angle % 360]:
        current = min(current + 1, 360)
        best = max(best, current)
    else:
        current = 0

print(best)
