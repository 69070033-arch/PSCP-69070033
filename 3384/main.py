"""3384: PickThem"""
import json

even = json.loads(input())
check = False

for i in even:
    if not i % 2:
        print(i)
        check = True

if not check:
    print("Nope")
