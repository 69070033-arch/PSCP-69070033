"""3229: ระบบคิดคะแนนเกมออนไลน์"""

Score = int(input())
Bonus = int(input())
Days = int(input())
Total_Score, Code = 0, 0

if Days > 3:
    Total_Score = int((Score + Bonus)*(1.5))
else:
    Total_Score = Score + Bonus

if Total_Score >= 1500:
    Code = 5
elif Total_Score >= 1000:
    Code = 4
elif Total_Score >= 500:
    Code = 3
elif Total_Score >= 200:
    Code = 2
else:
    Code = 1

print(Total_Score)
print(Code)

if Code == 5 and Days >= 7:
    print(99)
elif Code == 4 and Bonus > 300:
    print(88)
else:
    print(0)
