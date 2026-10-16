"""3478: Easy Histogram"""
text = input()

lower_counts = [0] * 26
upper_counts = [0] * 26

for char in text:
    if 'a' <= char <= 'z':
        lower_counts[ord(char) - ord('a')] += 1
    elif 'A' <= char <= 'Z':
        upper_counts[ord(char) - ord('A')] += 1

for i in range(26):
    if lower_counts[i] > 0:
        print(chr(ord('a') + i), '=', lower_counts[i])
    if upper_counts[i] > 0:
        print(chr(ord('A') + i), '=', upper_counts[i])
