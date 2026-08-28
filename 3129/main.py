"""3129: วิเคราะห์ยอดขายร้านกาแฟ"""

n = int(input())
mx, mn, total = 0, 0, 0

for i in range(n):
    num = int(input())
    if num > mx or not i:
        mx = num
    if num < mn or not i:
        mn = num
    total += num

print(total)
print(mx)
print(mn)
print(f"{total/n:.1f}")
