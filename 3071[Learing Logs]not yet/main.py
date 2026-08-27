"""3071: [LEARNING LOGS] จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""

a = int(input())
b = int(input())
d = int(input())
r = int(input())

count, start = 0, a

for i in range(a, b + 1):
    if i % d == r:
        break
    start += 1

if start <= b:
    for _ in range(start, b + 1, d):
        count += 1

print(count)
