"""3362: บุพเพสันนิวาส"""

first = input().strip()
second = input().strip()

while len(first) < len(second):
    first += first[0]
while len(second) < len(first):
    second += second[0]

talisman = ''
for a, b in zip(first, second):
    if a.lower() in 'love' or b.lower() in 'love':
        talisman += 'w'
    else:
        talisman += '$'

run = 0
longest = 0
for symbol in talisman:
    if symbol == 'w':
        run += 1
        longest = max(longest, run)
    else:
        run = 0

if talisman.count('w') % 2 == 1:
    talisman += str(longest)
elif longest < 2:
    talisman += '#'

print(talisman)
