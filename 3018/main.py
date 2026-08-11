"""3018: RectangleArea"""

x1, y1, w1, h1 = map(int, input().split())
x2, y2, w2, h2 = map(int, input().split())

w = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
h = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))

if w and h:
    print(w * h)
else:
    print("no overlapping")
