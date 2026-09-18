"""3292: Arrow"""

char = input()
n = int(input())
space = 0

for i in range((n*2)+1):
    if i > n:
        print(" "*space+"*"*((i-n)))
        space -= 2
        # print("if")
    elif i < n:
        print(" "*space+"*"*(n-i))
        space += 2
        # print("elif")
    # print(i)
    # print(space)
    

