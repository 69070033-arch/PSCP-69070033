"""3353: PickThemAgain"""

array = list(map(int, input().split()))
array = array[::-1]
check = False

for _, value in enumerate(array):
    if not value % 3 or not value % 5:
        print(value)
        check = True
    else:
        pass

if not check:
    print("Nope")
