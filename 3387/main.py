"""3387: Tuple's Sad life"""
data = tuple(input().split())
target = input()

first = data.index(target)
size = data.count(target)

for _ in range(size):
    print(' '.join([str(first)] * size))
