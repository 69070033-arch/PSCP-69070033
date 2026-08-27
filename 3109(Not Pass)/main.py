"""3109: ชานมไข่มุก"""

line1 = input().split()
if len(line1) == 2:
    pearl_type = line1[0]
    pearl_weight = int(line1[1])
else:
    pearl_type = line1[0]
    pearl_weight = int(input())

line2 = input().split()
if len(line2) == 3:
    tea_type = line2[0]
    sweetness = int(line2[1])
    tea_volume = int(line2[2])
else:
    tea_type = line2[0]
    sweetness = int(input())
    tea_volume = int(input())

if pearl_type == "H":
    pearl_energy = pearl_weight * 5
elif pearl_type == "O":
    pearl_energy = pearl_weight * 3
else:
    pearl_energy = pearl_weight * 2

if tea_type == "R":
    if sweetness == 1:
        tea_rate = 12
    elif sweetness == 2:
        tea_rate = 18
    else:
        tea_rate = 25
elif tea_type == "T":
    if sweetness == 1:
        tea_rate = 15
    elif sweetness == 2:
        tea_rate = 20
    else:
        tea_rate = 30
else:
    if sweetness == 1:
        tea_rate = 10
    elif sweetness == 2:
        tea_rate = 15
    else:
        tea_rate = 20

tea_energy = tea_volume * tea_rate
total_energy = pearl_energy + tea_energy

print(total_energy)
