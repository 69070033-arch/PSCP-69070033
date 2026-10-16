"""3475: Muddled Menu"""

menu = []

while True:
    line = input().strip()

    if line == "DONE":
        break

    if line == "CLOSED":
        menu.clear()
        break

    if line == "SOMETHING'S WRONG":
        menu.clear()
        continue

    if line.startswith("Can't do:"):
        name = line[len("Can't do:"):].strip()
        if name in menu:
            menu.remove(name)
        continue

    name, _, pos = line.rpartition("#")
    name = name.strip()
    pos = pos.strip()

    if pos in ("N", ""):
        menu.append(name)
    else:
        idx = int(pos) - 1
        if 0 <= idx <= len(menu):
            menu.insert(idx, name)

print("Full Course:", menu, "Reversed:", menu[::-1])
