"""3232: [LEARNING LOGS] กบน้อยกระโดด"""

start, end = map(int, input().split())
count, cal = 0, 0

while start > 0:
    cal += start
    start -= 2
    count += 1
    if cal >= end:
        print(count)
        break

if cal < end:
    print(-1)
