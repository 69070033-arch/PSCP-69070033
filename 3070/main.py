"""3070 : นับเลขคู่และเลขคี่"""

even = 0
odd = 0

for _ in range(3):
    n = int(input())
    if not n % 2:
        even += 1
    else:
        odd += 1

print(f"{even}\n{odd}")
