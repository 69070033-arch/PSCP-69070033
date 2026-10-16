"""3473: FourDirection"""

directions = input().strip()

print("  *   " * len(directions))

TOP = {
    "U": " *** ", "D": "  *  ",
    "L": " *   ", "R": "   * "
}

MIDDLE = {
    "U": "* * *", "D": "* * *",
    "L": "*****", "R": "*****"
}

BOTTOM = {
    "U": "  *  ", "D": " *** ",
    "L": " *   ", "R": "   * "
}

ROWS = [TOP, MIDDLE, BOTTOM]

for row in ROWS:
    for direction in directions:
        print(row.get(direction), end=" ")
    print()

print("  *   " * len(directions))
