"""3023"""

n = int(input())

if n == 1:
    print(n)
else:
    operator = 0
    for i in range(len(str(n))):
        digit_n = 10**i
        operator += (n-digit_n+1)
    print(operator+n)
