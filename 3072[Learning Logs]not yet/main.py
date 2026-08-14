"""3072:[LEARNING LOGS] A-E-I-O-U"""

string = input().lower()
lit = list(string)

sara = ['a','e','i','o','u']
tomnac,count = 0, 0

for i in sara:
    for j in lit:
        if j == i:
            count += 1
    if count:
        print(f"{sara[tomnac]} : {count}")
    tomnac += 1
    count = 0
