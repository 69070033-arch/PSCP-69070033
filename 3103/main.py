"""3103: จำนวนสระ"""

n = int(input())
VOWELS = "AEIOU"
count = 0

for _ in range(n):
    char = input()
    if char in VOWELS:
        count += 1

print(count)
