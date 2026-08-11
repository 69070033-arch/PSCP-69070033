"""3034: พอต"""

n, k = map(int, input().split())
all_people = [int(input()) for x in range(n)]
row =[]

for i in range(1,k+1):
    count = 0
    for j in all_people:
        if i == j:
            count+=1
    row.append(count)

ans = [x-min(row) for x in row]
print(sum(ans))
