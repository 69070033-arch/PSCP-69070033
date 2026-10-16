"""3473: FourDirections"""
arrows = {
    'U': ['  *  ', ' *** ', '* * *', '  *  ', '  *  '],
    'D': ['  *  ', '  *  ', '* * *', ' *** ', '  *  '],
    'L': ['  *  ', ' *   ', '*****', ' *   ', '  *  '],
    'R': ['  *  ', '   * ', '*****', '   * ', '  *  '],
}

code = ''
for letter in input():
    if letter in arrows:
        code = code + letter

for row in range(5):
    line = ''
    for letter in code:
        line = line + arrows[letter][row] + ' '
    print(line[:-1])
