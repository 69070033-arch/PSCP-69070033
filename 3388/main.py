"""3388: 113"""

txt = input()
total = ""

for i in txt:
    total += i
    if "113" in total:
        total = total.replace("113","")

print(total)
