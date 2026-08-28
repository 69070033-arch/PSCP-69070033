"""3135: [LEARNING LOGS] ของขวัญและขโมย"""

N, K, T = map(int,input().split())
count_lap, lap= 1, 1

while True:
    lap += K
    while lap > N:
        lap -= N
    if lap == 1:
        print(count_lap)
        break
    elif lap == T:
        print(count_lap+1)
        break
    count_lap += 1
