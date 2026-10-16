"""3383: Difference"""
n = int(input())
m = int(input())

a = {int(input()) for _ in range(n)}
b = {int(input()) for _ in range(m)}

print(*sorted(a - b))
