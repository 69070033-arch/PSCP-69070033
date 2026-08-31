"""3160: [LEARNING LOGS] หาจำนวนเฉพาะ"""

n, k = map(int,input().split())
count = 0
num = []

for i in range(n,k+1):
    prime = True
    if i < 2:
        continue
    for j in range(2,int(i**0.5)+1):
        if not i % j:
            prime = False
            break
    if prime:
        num.append(str(i))
        count+=1
if num:
    print(" ".join(num))
print(f"Total primes: {count}")
