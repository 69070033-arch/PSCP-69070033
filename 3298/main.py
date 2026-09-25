"""3298: กระต่ายน้อยรัก BUU"""

def main(sating):
    """Working Place"""
    MAX_COUNT = 0
    COUNT = 0
    TEXT = ""
    REM = False
    LOWER_SATING = sating.lower()
    if "buu" in LOWER_SATING:
        i = 0
        while i < len(sating):
            if LOWER_SATING[i] == 'b':
                COUNT = 0
                i += 1
                while i < len(sating) and LOWER_SATING[i] == 'u':
                    COUNT += 1
                    i += 1
                if COUNT > MAX_COUNT:
                    MAX_COUNT = COUNT
            else:
                i += 1
        print(f"Yes {MAX_COUNT}")
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
