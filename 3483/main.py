"""3483: มาเป็นทีม"""

n, m = map(int, input().split())
scores = [list(map(int, input().split())) for _ in range(n)]

if not (1 <= n <= 10 and 1 <= m <= 20):
    print("Data Incorrect")
elif any(len(team) != m for team in scores) or any(
    score < 0 or score > 100 for team in scores for score in team
):
    print("Data Incorrect")
else:
    total = 0
    for i, team in enumerate(scores, start=1):
        total += sum(team)
        print(f"Team {i}: Average = {sum(team) / m:.2f}, Max = {max(team)}")
    print(f"Total Score of All Teams = {total}")
