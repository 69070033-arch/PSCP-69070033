"""3238: Elon Musk (X-shape)"""

def main():
    """3238"""
    num, char = input().split()
    num = int(num)
    asciichar = ord(char)
    half = num // 2

    for i in range(num):
        for j in range(num):
            if i == j or i + j == num - 1:
                if char == "#":
                    print(char, end="")
                else:
                    print(chr(asciichar + abs(i - half)), end="")
            else:
                print("-", end="")
        print()

main()
