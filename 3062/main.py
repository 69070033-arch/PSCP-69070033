"""3062: ค่าตั๋ว"""

age = int(input())
char = input().lower()

if char == "s" or age < 18:
    print(20)
else:
    print(50)
