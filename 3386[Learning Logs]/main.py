"""3386:[LEARNING LOGS] Duplicate I"""

first_size = int(input())
second_size = int(input())

first_group = {int(input()) for _ in range(first_size)}
second_group = {int(input()) for _ in range(second_size)}

duplicates = first_group & second_group

if duplicates:
    for student in sorted(duplicates, reverse=True):
        print(student)
else:
    print("Nope")
