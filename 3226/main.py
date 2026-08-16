"""3226: [Recommend] Inflation"""

n = float(input())
k = int(input())

n = int(n * 100)
for _ in range(k):
    n += (n * 381) // 10000

print(f"{n // 100}.{n % 100:02d}")
