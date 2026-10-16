"""3357:[LEARNING LOGS] Giraffe"""

count = int(input())
heights = [int(input()) for _ in range(count)]

answer = 0

for index in range(count):
    taller_left = not index or heights[index] > heights[index - 1]
    taller_right = index == count - 1 or heights[index] > heights[index + 1]

    if taller_left and taller_right:
        answer += 1

print(answer)
