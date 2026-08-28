"""3157: [LEARNING LOGS] เกมสะสมแต้ม"""

mem = 0

for _ in range(int(input())):
    char = input()
    if char == "+":
        mem += 10
    else:
        mem -= 5

print(mem)
