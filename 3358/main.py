"""3358: Pig"""

n = int(input())
pig = list(map(int, input().split()))
duel = len(pig) // n
present_value, next_value, sum_num, total_list = 0, 0, 0, []

for _ in range(len(pig) // duel):
    next_value = present_value + duel
    total_list.append(str(max(pig[present_value:next_value])))
    sum_num += max(pig[present_value:next_value])
    present_value += duel

if len(pig) > 2:
    print(" + ".join(total_list), f"= {sum_num}")
else:
    print(sum_num)
