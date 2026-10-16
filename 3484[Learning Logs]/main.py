"""3484: [LEARNING LOGS] หุ่นยนต์เคาะเสียงกระเบื้อง"""

size, rate = input().split()
size = int(size)
rate = float(rate)

grid = [list(map(int, input().split())) for _ in range(size)]

for row in grid:
    broken = sum(1 for value in row if value > 0)
    print(*row, broken, sum(row))

column_broken = [0] * size
column_points = [0] * size

for index in range(size):
    for value in [row[index] for row in grid]:
        if value > 0:
            column_broken[index] += 1
        column_points[index] += value

print(*column_broken)
print(*column_points)

total_broken = sum(column_broken)
total_points = sum(column_points)

print(total_broken, total_points, f"{total_points * rate:.2f}")
