"""3230: โรงแรมกลางกรุง ไม่มีชั้น 13"""

text = input()
text_ans = ""
total_plus, total_times = 0, 1

for pos, char in enumerate(text):
    if int(char) > 5:
        if pos < 4:
            text_ans += str(9 + pos)
        else:
            text_ans += "14"
        break
if not text_ans:
    text_ans = "13"

if text == text[::-1]:
    if int(text[0]) + int(text[4]) > 5:
        text_ans += "1"
    elif int(text[1]) * int(text[3]) > 5:
        text_ans += "2"
    else:
        text_ans += "0"
else:
    try:
        if int(text[0]) // int(text[4]) > 5:
            text_ans += "1"
        elif int(text[1]) - int(text[4]) > 5:
            text_ans += "2"
        else:
            text_ans += "0"
    except ZeroDivisionError:
        if int(text[1]) - int(text[4]) > 5:
            text_ans += "2"
        else:
            text_ans += "0"

for _, char in enumerate(text):
    total_plus += int(char)
    total_times *= int(char)

if total_plus > 25:
    text_ans += "1"
elif total_times > 55:
    text_ans += "2"
else:
    text_ans += "0"

print(text_ans)
