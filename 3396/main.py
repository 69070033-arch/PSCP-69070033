"""3396: แซงรอบ"""
n, k = map(int, input().split())
times = []
for _ in range(n):
    times.append(int(input()))

best = 10 ** 9
for t in times:
    if t < best:
        best = t

if k == 1:
    print(n)
else:
    survivors = 0
    for t in times:
        if (k - 1) * t < k * best:
            survivors += 1
    print(survivors)
