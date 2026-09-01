"""3164: ผลรวมของค่าที่มากกว่า"""

n = int(input())
nums = []
total = 0

for _ in range(n):
    num1 = int(input())
    num2 = int(input())
    total += max(num1,num2)
    nums.append(max(num1,num2))

if len(nums) > 1:
    print(" + ".join(map(str,nums)),end=" = ")
print(total)
