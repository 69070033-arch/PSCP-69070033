"""3068 : ปีอธิกสุรทิน"""

years = int(input())

if years < 1582:
    if not years % 4:
        print("yes")
    else:
        print("no")
else:
    if (not years % 400) or (not years % 4 and years % 100):
        print("yes")
    else:
        print("no")
