"""3014: Milk"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

bottle = 0

while d >= a:
    d -= a
    bottle+=1
    if b and not bottle % b:
        bottle+=c

print(bottle)
