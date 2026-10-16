"""3390: Array 2D ตรวจสอบ"""
grid = [list(map(int, input().split())) for _ in range(5)]

row = -1
for index in range(5):
    if sum(grid[index]) % 2 == 1:
        row = index
        break

col = -1
for index in range(5):
    if sum(grid[i][index] for i in range(5)) % 2 == 1:
        col = index
        break

print(row, col)
