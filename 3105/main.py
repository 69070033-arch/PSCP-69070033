"""3105: คำนวณค่าแท็กซี่เบื้องต้น"""

distance = int(input())

if distance <= 0:
    FARE = 0
elif distance <= 1:
    FARE = 35
elif distance <= 10:
    FARE = 35 + (distance - 1) * 5
else:
    FARE = 35 + 45 + (distance - 10) * 8

print(FARE)
