"""[LEARNING LOGS] BigFrame"""

str1 = input().rstrip()
str2 = input().rstrip()
str3 = input().rstrip()
str4 = input().rstrip()
str5 = input().rstrip()

str_total = [str1,str2,str3,str4,str5]
lenght = len(max(str_total, key=len))

print("*"*(lenght+4))
for _, senten in enumerate(str_total):
    print("* "+senten+" "*(lenght-(len(senten)-1))+"*")
print("*"*(lenght+4))
