"""3360: [LEARNING LOGS] หั่นขนมปัง"""

width, height, _, _ = map(int, input().split())

columns = [0] + list(map(int, input().split())) + [width]
lines = [0] + list(map(int, input().split())) + [height]

gaps_x = sorted(columns[i + 1] - columns[i] for i in range(len(columns) - 1))
gaps_y = sorted(lines[i + 1] - lines[i] for i in range(len(lines) - 1))

biggest = gaps_x[-1] * gaps_y[-1]
second = max(gaps_x[-1] * gaps_y[-2], gaps_x[-2] * gaps_y[-1])

print(max(biggest, second), min(biggest, second))
