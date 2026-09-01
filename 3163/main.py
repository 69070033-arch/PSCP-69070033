"""3163: สินค้าส่งออก"""

n = int(input())
nums = [int(input()) for _ in range(n)]
count_even, count_odd = 0, 0

for i in nums:
    if not i % 2:
        count_even += 1
    else:
        count_odd += 1

print(f"SUM {sum(nums)}")
print(f"EVEN {count_even}")
print(f"ODD {count_odd}")
