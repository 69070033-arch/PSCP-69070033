"""3482: นักล่าอสูร

จำจุดตายของอสูรที่เคยสังหารสำเร็จ ถ้ายังไม่รู้ก็ไล่ลอง 1, 2, 3
จนกว่าจะฆ่าได้ครบ 5 ตน
"""

killed = 0
attacks = 0
learned = {}  # ชื่ออสูร -> จุดตาย
tried = {}  # ชื่ออสูร -> จุดตายที่เคยลองแล้ว

while killed < 5:
    demon = input().strip()

    if demon in learned:
        guess = learned[demon]
    else:
        guess = 1
        for value in tried.get(demon, []):
            guess = value + 1
        if guess > 3:
            guess = 1
        tried.setdefault(demon, []).append(guess)

    print(guess)
    attacks += 1

    result = input().strip()
    if result == "kill":
        learned[demon] = guess
        killed += 1

print(attacks)
