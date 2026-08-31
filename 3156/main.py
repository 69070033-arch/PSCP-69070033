"""3156: Conan"""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
Password = input()
shift = int(input())
Key = ""

for _, CharPass in enumerate(Password):
    for j, CharAlpha in enumerate(ALPHABET):
        if CharPass == CharAlpha:
            slide = shift + j
            while slide >= len(ALPHABET):
                slide -= len(ALPHABET)
            Key += ALPHABET[slide]
print(Key)
