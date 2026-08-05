"""3022"""

n = float(input())
x = input()
y = input()

c = 0
if x == "C":
    c = n
elif x == "F":
    c = (n - 32) * 5 / 9
elif x == "K":
    c = n - 273.15
elif x == "R":
    c = (n * 5 / 9) - 273.15

result = {
    "C": c,
    "F": c * 9/5 + 32,
    "K": c + 273.15,
    "R": (c + 273.15) * 9/5
}

print(f"{result[y]:.2f}")
