"""3040: แลกเปลี่ยนเงิน"""

n = int(input())

ten, n = n // 10, n % 10
five, n = n // 5, n % 5
two, one = n // 2, n % 2

print(f"10 = {ten}\n5 = {five}\n2 = {two}\n1 = {one}")
