"""four direction"""
order = input()

print("  *   " * len(order))

line2 = {
    "U": " * ", "D": "  *  ",
    "L": " *   ", "R": "   * "
}

line3 = {
    "U": "* * ", "D": " * *",
    "L": "***", "R": "***"
}

line4 = {
    "U": "  *  ", "D": " * ",
    "L": " *   ", "R": "   * "    
}

line = [line2, line3, line4]

for i in range(3): #each line
    for word in order:
        print(line[i].get(word), end=" ")
    print()

print("  *   " * len(order))