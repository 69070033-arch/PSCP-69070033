"""3065 :ตัวเลขโรมันแบบง่าย"""

n = int(input())
symbol = ""

roman = {
    "IX":9,
    "V":5,
    "IV":4,
    "I":1,
}

if n < 0:
    symbol = "Error : Please input positive number"
elif not n or n > 9:
    symbol = "Error : Out of range"
else:
    for Sym, Val  in roman.items():
        while n >= Val:
            symbol += Sym
            n -= Val

print(symbol)
