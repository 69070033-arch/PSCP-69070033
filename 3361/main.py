"""3361: ขายรถยนต์"""

n = int(input())
cars = [tuple(map(int, input().split())) for _ in range(n)]

best = 0
answer = 0
for _, value in reversed(cars):
    if value < best:
        answer += 1
    else:
        best = value

print(answer)
