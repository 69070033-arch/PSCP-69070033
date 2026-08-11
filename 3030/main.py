"""3030: ฉันจะเป็น Saitama ให้ได้เลย"""
import math

PushUp = int(input())
SitUp = int(input())
Squat = int(input())
Run = int(input())

NumP = int(input())
NumS = int(input())
NumR = int(input())
NumSq = int(input())

Days = max(math.ceil(PushUp / NumP), math.ceil(SitUp / NumS),
            math.ceil(Squat / NumSq), math.ceil(Run / NumR))
print(Days)
