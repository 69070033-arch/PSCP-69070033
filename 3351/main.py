"""3351: พูดจากภาษากระต่าย"""
word = input().strip().upper()

if not any(letter in 'RAB' for letter in word):
    print('unknown', len(word))
else:
    bad = None

    for index, letter in enumerate(word):
        if letter not in 'RABIT':
            bad = index
            break
        elif letter == 'A' and (index == 0 or word[index - 1] not in 'RA'):
            bad = index
            break
        elif letter == 'R' and word[index + 1:index + 2] != 'A':
            bad = index
            break
        elif letter == 'B' and word[index + 1:index + 2] not in ('I', 'T'):
            bad = index
            break

    if bad is not None:
        print('no', bad)
    else:
        longest = 0
        run = 0

        for letter in word:
            if letter == 'A':
                run += 1
            else:
                run = 0
            longest = max(longest, run)

        print('yes', longest)
