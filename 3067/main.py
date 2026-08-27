"""3067 : การเพิ่ม/ลด"""

x = float(input())
y = float(input())
z = float(input())

if x < y < z:
    print("increasing")
elif x > y > z:
    print("decreasing")
else:
    print("neither")
