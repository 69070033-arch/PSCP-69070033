"""3352: LastStand"""
import json

array = json.loads(input())

for pos, value in enumerate(array):
    print(str(value)[-1])
