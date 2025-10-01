import math

a, b, c = map(float, input().split())

d1 = a + b - c
d2 = b + c - a
d3 = a + c - b

f1 = bool((abs(d1) > 1e-9) and (d1 > 0))
f2 = bool((abs(d2) - 0 > 1e-9) and (d2 > 0))
f3 = bool((abs(d3) - 0 > 1e-9) and (d3 > 0))

if (f1 and f2 and f3):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"{s:.2f}")
else:
    print("Khong phai 3 canh cua tam giac")