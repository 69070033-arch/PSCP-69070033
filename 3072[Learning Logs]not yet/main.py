"""3072:[LEARNING LOGS] A-E-I-O-U"""

string = input().lower()
sara = ['a','e','i','o','u']

for i in sara:
    check = string.count(i)
    if check:
        print(f"{i} : {check}")
