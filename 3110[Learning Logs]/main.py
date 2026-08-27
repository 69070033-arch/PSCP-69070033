"""3110: [LEARNING LOGS] สงคราม...ส่งด่วน"""

route_input = input().split()
weight = float(input())

origin = route_input[0]
destination = route_input[1]

base = 0
rate = 0
found = False

if origin == "BKK" and destination == "CNX":
    base, rate = 10, 30
    found = True
elif origin == "CNX" and destination == "UBP":
    base, rate = 15, 40
    found = True
elif origin == "UBP" and destination == "BKK":
    base, rate = 20, 40
    found = True
elif origin == "BKK" and destination == "PKT":
    base, rate = 25, 50
    found = True
elif origin == "PKT" and destination == "CNX":
    base, rate = 30, 60
    found = True
elif origin == "UBP" and destination == "PKT":
    base, rate = 40, 70
    found = True

if found:
    total_cost = base + (weight * rate)
    # เปลี่ยนมาแสดงผลเป็นทศนิยม 2 ตำแหน่ง
    print(f"{total_cost:.2f}")
else:
    print("Error")
