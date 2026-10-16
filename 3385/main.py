"""3385: BusStop I"""
p = int(input())
n = int(input())

stops = {}
for _ in range(n):
    data = list(map(int, input().split()))
    stops[data[0]] = data[1:]

bus = []
boarded = 0
for sign in range(1, n + 1):
    bus = [dest for dest in bus if dest != sign]
    for dest in stops.get(sign, []):
        if len(bus) == p:
            break
        if dest > sign:
            bus.append(dest)
            boarded += 1

print(boarded - len(bus))
