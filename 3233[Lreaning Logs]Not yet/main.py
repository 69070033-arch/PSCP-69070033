"""3233: [LEARNING LOGS] สลากกินแบ่ง"""

example = input().split()
ticket = input().split()

if example == ticket:
    print(1000000)
elif example[1] == ticket[1]:
    print(100000)
elif example[0] == ticket[0]:
    if example[1][2:] == ticket[1][2:]:
        print(2000)
    elif example[1][3:] == ticket[1][3:]:
        print(1000)
    else:
        print(20)
elif not example[0] == ticket[0]:
    if example[1][2:] == ticket[1][2:]:
        print(200)
    elif example[1][3:] == ticket[1][3:]:
        print(100)
    else:
        print(0)
