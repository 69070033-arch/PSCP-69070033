"""3116 : นวัตกรรมงบประมาณโรงเรียน"""

school_name = input()
length = len(school_name)

first_char = school_name[0].upper()
last_char = school_name[-1].upper()

ascii_first = ord(first_char)
ascii_last = ord(last_char)

slots = [{"id": i, "val": i - 1} for i in range(1, 11)]

for slot in slots:
    if slot["id"] % 2:
        slot["val"] = ascii_first + slot["val"]
    else:
        slot["val"] = ascii_last - slot["val"]

for slot in slots:
    slot["val"] = slot["val"] % length
    if slot["val"] > 9:
        slot["val"] = slot["val"] % 10

selected_slots = slots[2:8]
PASSWORD = " ".join(str(slot["val"]) for slot in selected_slots)

print(PASSWORD)
