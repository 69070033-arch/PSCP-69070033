"""3393: นักสำรวจถ้ำ (Cave Explorer)"""

input()
cave = list(map(int, input().split()))
moves = input().strip()

for move in moves:
    here = cave.index(1)
    there = here + (1 if move == "R" else -1)

    if not 0 <= there < len(cave):
        continue

    if cave[there] == 2:
        cave[here] = 0
        cave[there] = 1
        break

    cave[here], cave[there] = cave[there], cave[here]

print(*cave)
