"""3363: ไข้หวัดกระต่ายสายพันธุ์ใหม่"""
risk_levels = (100, 60, 20)

rows, cols = map(int, input().split())
my_row, my_col = map(int, input().split())
n = int(input())

risk = {}
for _ in range(n):
    row, col = map(int, input().split())
    for i in range(row - 2, row + 3):
        if not 0 <= i < rows:
            continue
        for j in range(col - 2, col + 3):
            if not 0 <= j < cols:
                continue
            level = risk_levels[max(abs(i - row), abs(j - col))]
            if level > risk.get((i, j), 0):
                risk[(i, j)] = level

unsafe = sum(1 for level in risk.values() if level > 0)
print(rows * cols - unsafe)
print(f"{risk.get((my_row, my_col), 0)}%")
