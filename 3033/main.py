"""3033: กระดาษห่อของขวัญ"""
r, y, z = map(float, input().split())

Length = (2*3.14*r) + z
Width = (r * 2) + y

print(f"{Width:.2f} {Length:.2f}")
