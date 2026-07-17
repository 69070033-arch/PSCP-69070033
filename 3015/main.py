"""3015"""

x = int(input())
y = int(input())
a = int(input())
z = int(input())

count = z//x
minuspro = z*a
if count:
    minuspro = ((count*a)*y)+((z%x)*a)
print(minuspro)
