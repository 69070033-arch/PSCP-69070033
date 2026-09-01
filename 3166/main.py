"""3166: ผ่านหรือไม่ ค่าเฉลี่ยรายวิชา"""

n = int(input())
nums = 0
Check = True

for _ in range(n):
    Score = int(input())
    nums += Score
    if Score < 50:
        Check = False

if (nums/n) >= 60 and Check:
    print(f"{(nums/n):.1f}")
    print("PASS")
else:
    print(f"{(nums/n):.1f}")
    print("FAIL")
