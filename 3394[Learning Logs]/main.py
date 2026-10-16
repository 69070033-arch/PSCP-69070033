"""3394:[LEARNING LOGS] ส่งต่อ"""

total, first = map(int, input().split())
forward = [0] + [int(input()) for _ in range(total)]

received = set()
current = first

while current and current not in received:
    received.add(current)
    current = forward[current]

print(len(received))
