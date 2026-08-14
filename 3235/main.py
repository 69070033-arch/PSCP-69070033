"""3235: กระต่ายอ้วน"""

n = int(input())
a, b = [], []
count, rem = 0, 0
for i in range(n):
    name, weight = input().split()
    a.append(name)
    b.append(int(weight))
    if int(weight) > 15:
        count+=1

print(count)

for i in b:
    if i == max(b):
        break
    rem += 1

print(a[rem])
