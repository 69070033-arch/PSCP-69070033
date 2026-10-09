"""3599: SumOfNumber"""

n = int(input())
Total, k = 0, 0

while k != -1 and Total != n:
    k = int(input())
    if k > 0:
        Total += k

print(Total)
