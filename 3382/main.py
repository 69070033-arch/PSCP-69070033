"""3382: Day08-0_02-Backward"""

Item = input()
array = []

while Item != "NULL":
    array.append(Item)
    Item = input()

array.reverse()

for i in array:
    print(i)
