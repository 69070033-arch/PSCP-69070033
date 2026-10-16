"""3393: นักสำรวจถ้ำ (Cave Explorer)"""

n = int(input())
cave = list(map(int, input().split()))
commands = input().strip()

start = 0
treasure = 0
for i in range(n):
    if cave[i] == 1:
        start = i
    elif cave[i] == 2:
        treasure = i

hero = start
stopped = False

for command in commands:
    if command == 'R':
        target = hero + 1
    else:
        target = hero - 1

    if target < 0 or target >= n:
        continue

    hero = target
    if hero == treasure:
        stopped = True
        break

cave[start] = 0
cave[treasure] = 0
cave[hero] = 1

print(*cave)
