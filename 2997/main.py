"""2997"""

a = int(input())
b = int(input())
char = input()

if char == "A":
    ans = 1/(1+10**((b-a)/400))
    print(f"{ans:.2f}")
elif char == "B":
    ans = 1/(1+10**((a-b)/400))
    print(f"{ans:.2f}")
