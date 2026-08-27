"""3069 : ราศี"""

Date = int(input())
Month = int(input())

if (Date >= 20 and Month == 1) or (Date <= 18 and Month == 2):
    print("aquarius")
elif (Date >= 19 and Month == 2) or (Date <= 20 and Month == 3):
    print("pisces")
elif (Date >= 21 and Month == 3) or (Date <= 19 and Month == 4):
    print("aries")
elif (Date >= 20 and Month == 4) or (Date <= 20 and Month == 5):
    print("taurus")
elif (Date >= 21 and Month == 5) or (Date <= 21 and Month == 6):
    print("gemini")
elif (Date >= 22 and Month == 6) or (Date <= 22 and Month == 7):
    print("cancer")
elif (Date >= 23 and Month == 7) or (Date <= 22 and Month == 8):
    print("leo")
elif (Date >= 23 and Month == 8) or (Date <= 22 and Month == 9):
    print("virgo")
elif (Date >= 23 and Month == 9) or (Date <= 23 and Month == 10):
    print("libra")
elif (Date >= 24 and Month == 10) or (Date <= 21 and Month == 11):
    print("scorpio")
elif (Date >= 22 and Month == 11) or (Date <= 21 and Month == 12):
    print("sagittarius")
else:
    print("capricorn")
