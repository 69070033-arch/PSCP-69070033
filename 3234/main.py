"""3234: ไฟคริสตมาส"""

char, n = input().split()
color = ["Red", "Green", "Blue"]
ans ,k = [], 0

if char == "B":
    k = 2
elif char == "G":
    k = 1

for i in range(k,int(n)+k):
    index = i % 3
    ans.append(color[index])

print(" ".join(ans))
