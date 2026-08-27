"""3115: [LEARNING LOGS] Arcade of Time: Store Check"""

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    num = int(input_data[0])
    check = int(input_data[1])

    timeline = [0] * 1442

    idx = 2
    for _ in range(num):
        start = int(input_data[idx])
        stop = int(input_data[idx + 1])
        timeline[start] += 1
        timeline[stop] -= 1
        idx += 2

    current_open = 0
    shop_count_at_minute = [0] * 1441
    for i in range(1441):
        current_open += timeline[i]
        shop_count_at_minute[i] = current_open

    results = []
    for _ in range(check):
        k = int(input_data[idx])
        results.append(str(shop_count_at_minute[k]))
        idx += 1

    print(" ".join(results))


if __name__ == "__main__":
    solve()
