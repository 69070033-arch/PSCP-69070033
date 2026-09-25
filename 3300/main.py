"""3300: สมดุลย์ชีวิต"""

N = int(input())
H = [int(input()) for _ in range(N)]

heavy = 0
for time in H:
    if time > 18:
        heavy += 1

normal = N - heavy

if not heavy:
    print(N)
else:
    extra_days = (heavy - 1) - normal
    if extra_days < 0:
        extra_days = 0
    print(N + extra_days)
