"""3035: ฟิลเตอร์ AR TikTok"""

r, x, y = map(float, input().split())

if r**2 > (x**2)+(y**2):
    print("IN")
elif r**2 < (x**2)+(y**2):
    print("OUT")
else:
    print("ON")
