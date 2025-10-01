a1, b1, c1, a2, b2, a3 = map(int, input().split())
avg = (a1 + b1 + c1) + (a2 + b2) * 2 + a3 * 3
avg /= 10
print("{:.1f}".format(avg))