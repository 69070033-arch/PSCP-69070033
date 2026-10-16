"""3391: สะสมเหรียญเวทย์มนตร์"""
n = int(input())
fire = water = earth = 0

for _ in range(n):
    coins = list(map(int, input().split()))
    fire += max(coins[0], coins[3])
    water += max(coins[1], coins[4])
    earth += max(coins[2], coins[5])

total = fire + water + earth
print(f"Total: {total}")
print(f"Fire: {fire}\nWater: {water}\nEarth: {earth}")
print(f"Bonus: {'YES' if fire > water + earth else 'NO'}")
