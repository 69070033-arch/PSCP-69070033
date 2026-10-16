"""3356: Bus Seat"""

rows = int(input())
seats_per_row = int(input())
my_seat = int(input())

column = (my_seat - 1) // rows + 1
my_row = rows - (my_seat - 1) % rows

for row in range(1, rows + 1):
    line = ""
    for seat in range(1, seats_per_row + 1):
        number = (seat - 1) * rows + rows - row + 1
        if seat == column and row == my_row:
            line += "XX "
        else:
            line += f"{number:02d} "
    print(line.rstrip())
    if row % 2 == 0 and row != rows:
        print()
