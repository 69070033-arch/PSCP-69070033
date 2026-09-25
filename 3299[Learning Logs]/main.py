"""3299: [LEARNING LOGS] แปลงดอกไม้"""
L, N = map(int, input().split())

target = 2 * N
X = 1

while X * (X + 1) < target:
    X += 1

k = (X + L - 1) // L
print(k)
