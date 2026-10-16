"""3487: ติดตั้งหลอดไฟ"""

n = int(input())
heights = sorted(int(input()) for _ in range(n))

distance = 2 * sum(height * (n - i) for i, height in enumerate(heights))

print(distance)
