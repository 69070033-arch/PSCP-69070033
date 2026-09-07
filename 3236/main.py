"""3236: รหัสแฝดเทค"""

n = int(input())
num1 = input()
num2 = input()
count = 0

for i in range(n):
    if int(num1[i]) + int(num2[i]) != 9:
        count += 1

if not count:
    print("YES")
else:
    print("NO", count)
