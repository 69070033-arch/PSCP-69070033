"""3135: [LEARNING LOGS] ของขวัญและขโมย"""

N, K, T = map(int,input().split())
Count_lap, Diamond_pos = 0, 1

while True:
    while Diamond_pos > N:
        Diamond_pos -= N
    if Count_lap and Diamond_pos == 1 :
        print(Count_lap)
        break
    if T in (Diamond_pos,1):
        print(Count_lap+1)
        break
    Diamond_pos += K
    Count_lap += 1
