"""3381:[LEARNING LOGS] Point Sorting"""

cases = int(input())

for _ in range(cases):
    total = int(input())
    points = [tuple(map(int, input().split())) for _ in range(total)]

    points.sort(key=lambda point: (point[0] + point[1], -point[1]))

    for x, y in points:
        print(x, y)
