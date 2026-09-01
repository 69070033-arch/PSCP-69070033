"""3165: เดินเล่นในงานเทศกาล"""

walk = input()
x, y = 0, 0

for _, text in enumerate(walk):
    if text == "N":
        y += 1
    elif text == "S":
        y -= 1
    elif text == "E":
        x += 1
    elif text == "W":
        x -= 1

print(x, y, abs(x) + abs(y))
