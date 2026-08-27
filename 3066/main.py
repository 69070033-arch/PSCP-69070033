"""3066 : เหมือนกันหมด"""

x = int(input())
y = int(input())
z = int(input())

if x == y == z and x == z:
    print("all the same")
elif x != y != z and x != z:
    print("all different")
else:
    print("neither")
