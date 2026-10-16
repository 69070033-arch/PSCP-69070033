"""3351: พูดจากภาษากระต่าย"""

message = input().lower()

if all(char in "it" for char in message):
    print("unknown", len(message))
else:
    error_at = -1

    for index, char in enumerate(message):
        if char not in "rabit":
            error_at = index
        elif char == "r" and message[index + 1:index + 2] != "a":
            error_at = index + 1
        elif char == "b" and message[index + 1:index + 2] not in ("i", "t"):
            error_at = index + 1
        elif char == "a" and message[index - 1:index] not in ("r", "a"):
            error_at = index

        if error_at != -1:
            print("no", error_at)
            break
    else:
        run = longest = 0

        for char in message:
            run = run + 1 if char == "a" else 0
            longest = max(longest, run)

        print("yes", longest)
