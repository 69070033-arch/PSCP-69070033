"""3474: Resistor"""
digit_colors = ['black', 'brown', 'red', 'orange', 'yellow',
                'green', 'blue', 'purple', 'grey', 'white']
multiplier_colors = ['black', 'brown', 'red', 'orange', 'yellow',
                     'green', 'blue', 'purple', 'gold', 'silver']
multiplier_values = [1, 10, 100, 1000, 10000,
                     100000, 1000000, 10000000, 0.1, 0.01]
tolerance_colors = ['brown', 'red', 'green', 'blue',
                    'purple', 'grey', 'gold', 'silver']
tolerance_values = [0.01, 0.02, 0.005, 0.0025, 0.001, 0.0005, 0.05, 0.1]

band1 = input().strip().lower()
band2 = input().strip().lower()
band3 = input().strip().lower()
band4 = input().strip().lower()

first = -1
second = -1
multiplier = -1
tolerance = -1

for i, color in enumerate(digit_colors):
    if color == band1:
        first = i
    if color == band2:
        second = i

for i, color in enumerate(multiplier_colors):
    if color == band3:
        multiplier = i

for i, color in enumerate(tolerance_colors):
    if color == band4:
        tolerance = i

if first < 0 or second < 0 or multiplier < 0 or tolerance < 0:
    print('Error')
else:
    ohms = (first * 10 + second) * multiplier_values[multiplier]
    low = ohms * (1 - tolerance_values[tolerance])
    high = ohms * (1 + tolerance_values[tolerance])
    print(f"{low:.4f}")
    print(f"{high:.4f}")
