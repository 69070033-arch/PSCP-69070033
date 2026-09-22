"""3294: Teaching schedule"""

n = int(input())
a = int(input())

seconds = n*a
hours = (seconds*60)//3600
minutes = ((seconds*60) % 3600) // 60

mix_text = []
if hours:
    mix_text.append(f"{hours} hours")
if minutes:
    mix_text.append(f"{minutes} minute")

if mix_text:
    print(" ".join(mix_text))
else:
    print("No teaching")
