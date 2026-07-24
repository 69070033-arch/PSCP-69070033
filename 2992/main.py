"""2992"""

num = int(input())
char = input()
SWAP = str(num)[::-1]
if char == "+":
    print(f"{num} + {int(SWAP)} = {num+int(SWAP)}")
elif char == "*":
    print(f"{num} * {int(SWAP)} = {num*int(SWAP)}")
