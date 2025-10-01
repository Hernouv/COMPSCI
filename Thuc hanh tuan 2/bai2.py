a, b = map(float, input().split())
r = min(a, b) / 2
s = r ** r * 3.14
print(f"{(a * b - s):.2f}")
