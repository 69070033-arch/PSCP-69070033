"""3237: [Recommend] สามเหลี่ยม"""

n = int(input())
for i in range(1,n+1):
    if i >= 3  and i != n:
        print("0"+"1"*(i-2)+"0")
    elif i and i == n :
        print("0"*i)
    else:
        print("0"*i)
