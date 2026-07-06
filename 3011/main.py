"""3011"""
x = input()
y = input()

if (x in {"Red","Yellow","Blue"}) and (y in {"Red","Yellow","Blue"}):
    if (x == "Red" and y == "Yellow") or (x == "Yellow" and y == "Red"):
        print("Orange")
    elif (x == "Red" and y == "Blue") or (x == "Blue" and y == "Red"):
        print("Violet")
    elif (x == "Blue" and y == "Yellow") or (x == "Yellow" and y == "Blue"):
        print("Green")
    elif x == y:
        print(x)
else:
    print("Error")
