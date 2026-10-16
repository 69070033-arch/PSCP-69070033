"""3476: [LEARNING LOGS] CuteCat CuteFox"""

DEFAULT_NAME = {"Cat": "Garfield", "Fox": "Fubuki"}
QUOTES = "'\""

total = int(input())
animals = {}
used_names = set()

for _ in range(total):
    line = input().strip().strip("{}")
    name, _, tag = line.partition(":")
    name = name.strip().strip(QUOTES)
    tag = tag.strip().strip(QUOTES)

    animals[tag] = name
    used_names.add(name)

groups = {"Cat": [], "Fox": []}

for tag, name in animals.items():
    groups[tag[:3]].append((int(tag[3:]), name, tag))

for kind, name in DEFAULT_NAME.items():
    numbers = [number for number, _, _ in groups[kind]]

    if 1 not in numbers and name not in used_names:
        groups[kind].append((1, name, kind + "01"))

for group in groups.values():
    group.sort()

print("Cat :", len(groups["Cat"]))
print("Fox :", len(groups["Fox"]))

for kind in ("Cat", "Fox"):
    for number, name, tag in groups[kind]:
        print(f"{name} : {tag}" if name else tag)
