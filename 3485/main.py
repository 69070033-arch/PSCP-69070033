"""3485: รหัสต้องไม่ซ้ำกัน"""

n = int(input())
codes = list(map(int, input().split()))
codes = codes[:n]

count = {}
for code in codes:
    count[code] = count.get(code, 0) + 1

rare = sorted(code for code, times in count.items() if times == 1)

print(*rare)
