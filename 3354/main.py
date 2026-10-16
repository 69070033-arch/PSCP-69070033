"""3354: Hint"""

hints = []
for _ in range(3):
    op, value = input().split()
    hints.append((op, int(value)))

for number in range(1000):
    digits = [number % 10, number // 10 % 10, number // 100]
    ok = True
    for (op, value), digit in zip(hints, digits):
        if op == ">":
            ok = digit > value
        elif op == ">=":
            ok = digit >= value
        elif op == "<":
            ok = digit < value
        elif op == "<=":
            ok = digit <= value
        elif op == "!=":
            ok = digit != value
        else:
            ok = digit == value
        if not ok:
            break
    if ok:
        print(f"{number:03d}")
