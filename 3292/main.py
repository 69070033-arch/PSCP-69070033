"""3292: Arrow"""

char = input()
n = int(input())

def right_arrow():
    """ลูกศรไปทางขวา"""
    space = 0
    for i in range(n):
        print(" "*space+"*"*(n-i))
        space += 2
    space -= 2
    for i in range(2,n+1):
        space -= 2
        print(" "*space+"*"*(i))

def left_arrow():
    """ลูกศรไปทางซ้าย"""
    space = n-1
    for i in range(n):
        print(" "*space+"*"*(n-i))
        space -= 1
    space = 0
    for i in range(2,n+1):
        space += 1
        print(" "*space+"*"*(i))

for pos, alphabet in enumerate(char):
    if alphabet.upper() == "L":
        left_arrow()
    elif alphabet.upper() == "R":
        right_arrow()
    if pos < len(char)-1:
        print()
