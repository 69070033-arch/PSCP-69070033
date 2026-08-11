"""3039: ค่าน้อยที่สุด (4 ค่า)"""

n = int(input())
Answer = 0
for i in range(n):
    num = int(input())
    if not i:
        Answer = num
    if num < Answer:
        Answer = num

print(Answer)
