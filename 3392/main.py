"""3392: Array ฮาเฮ"""
numbers = []
for index in range(1, 4):
    numbers.append(int(input()))
    print(f"Input number {index} stored.")

menu = int(input())
while menu:
    if menu == 1:
        print('Original order:', *numbers)
    elif menu == 2:
        print('Descending order:', *sorted(numbers, reverse=True))
    elif menu == 3:
        print('Ascending order:', *sorted(numbers))
    menu = int(input())
