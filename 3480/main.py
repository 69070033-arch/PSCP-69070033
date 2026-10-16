"""3480: นก"""
n = int(input())
heights = list(map(int, input().split()))

nests = 0

for i in range(n):
    good = True
    if i > 0 and heights[i - 1] > heights[i]:
        good = False
    if i + 1 < n and heights[i + 1] > heights[i]:
        good = False
    if good:
        nests += 1

print(nests)
