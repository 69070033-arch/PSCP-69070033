"""3024"""

Score_Total = float(input())
Max_Score = float(input())

TwoScore = Score_Total - Max_Score
MinScore = max(0,TwoScore - Max_Score)

if  Max_Score - MinScore > 2:
    print("Surprising")
else:
    print("Not surprising")
