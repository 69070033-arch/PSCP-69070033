"""3477: [LEARNING LOGS] Pad Thai"""

INGREDIENTS = {
    "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp", "Bean Sprouts",
    "Noodle", "Chives", "Lime", "Egg", "Oil", "Peanuts",
}
TASTES = {"Sweet", "Sour", "Salty"}


def read_until(stop):
    """doc"""
    words = set()

    while True:
        line = input().strip()
        if line == stop:
            return words
        words.add(line)


used = read_until("Cook")
flavors = read_until("End")

if used - INGREDIENTS:
    answer = "This is not Pad Thai!!!"
elif INGREDIENTS - used:
    answer = "This is bad!"
elif flavors != TASTES:
    answer = "Not Bad..."
else:
    answer = "Delicious!"

print(answer)
