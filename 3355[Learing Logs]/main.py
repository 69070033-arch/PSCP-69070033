"""3355:[LEARNING LOGS] Shorten"""

numbers = []
value = int(input())

while value != -1:
    numbers.append(value)
    value = int(input())

if not numbers:
    print()
else:
    result = []
    start = previous = numbers[0]

    for number in numbers[1:]:
        if number != previous + 1:
            result.append(str(start) if start == previous
                          else f"{start}-{previous}")
            start = number
        previous = number

    result.append(str(start) if start == previous else f"{start}-{previous}")

    print(", ".join(result))
