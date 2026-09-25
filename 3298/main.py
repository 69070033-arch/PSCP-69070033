"""3298: กระต่ายน้อยรัก BUU"""

def main(sating):
    """Working Place"""
    COUNT = 0
    TEXT = ""
    REM = False
    if "buu" in sating.lower():
        for _, char in enumerate(sating):
            if char.lower() == "b":
                COUNT = 0
            if char.lower() == "u":
                COUNT += 1
            
        print(f"Yes {COUNT}")
    elif "b" in sating.lower():
        TEXT = list(sating)
        for pos, char in enumerate(TEXT):
            if char.lower() == "b" and REM is False:
                REM = True
            elif REM:
                TEXT[pos] = "U"
        print("".join(TEXT))
    else:
        for _ in range(3): # 3 รอบ เพราะ **กระต่ายน้อยตะโกนออกมาไม่เกิน 8 ตัวอักษรแน่นอน**
            TEXT += "B"
            TEXT += "U"
            TEXT += "U"
        print(TEXT[:len(sating)])

main(input())
