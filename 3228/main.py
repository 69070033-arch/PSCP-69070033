"""3228: การนับสระ"""

text = input().lower()
sara = ["a","e","i","o","u"]
count = 0

for _, char in enumerate(text):
    if char in sara:
        count+=1

print(count)
