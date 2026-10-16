"""3395: เข้าแถว"""
n, l = map(int, input().split())
heights = list(map(int, input().split()))
customers = list(map(int, input().split()))

tallest = [0] * (n + 1)
for i in range(1, n + 1):
    tallest[i] = heights[i - 1]
    if tallest[i - 1] > tallest[i]:
        tallest[i] = tallest[i - 1]

for a in customers:
    chair = tallest[a - 1] + 1 - heights[a - 1]
    if chair < 0:
        chair = 0
    print(chair)
