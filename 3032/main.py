"""3032: คะแนนสอบ"""

n = int(input())
Num = 0
j = 0
while j < n:
    Score = int(input())
    if Num < Score:
        Num = Score
        COUNT = 1
    elif Num == Score:
        COUNT += 1
    j+=1

print(Num)
print(COUNT)
