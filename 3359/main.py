"""3359: กองชาม"""

n = int(input())
counts = [0] * 301
for _ in range(n):
    counts[int(input())] += 1
print(max(counts))
