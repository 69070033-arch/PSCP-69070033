"""3002"""

name = input()
surname =input()
age = int(input())

if len(name) >= 5 and len(surname) >= 5:
    print(f"{name[:2]}{surname[-1]}{age%10}")
else:
    print(f"{name[0]}{age}{surname[-1]}")
