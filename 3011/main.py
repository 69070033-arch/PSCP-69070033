"""3011"""
x = input()
y = input()

if (x == "Red" or x == "Yellow") and (y == "Yellow" or y == "Red"):
    print("Orange")
elif (x == "Red" or x == "Blue") and (y == "Blue" or y == "Red"):
    print("Violet")
elif (x == "Blue" or x == "Yellow") and (y == "Yellow" or y == "Blue"):
    print("Green")
else:
    print("Error")