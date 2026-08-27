"""3101 : สถานะน้ำ"""

temp = int(input())
unit = input().upper()

if unit == "F":
    temp_c = (temp - 32) * 5 / 9
else:
    temp_c = temp

if temp_c <= 0:
    print("solid")
elif temp_c >= 100:
    print("gas")
else:
    print("liquid")
