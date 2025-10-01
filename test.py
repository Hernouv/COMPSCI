a, b, c = map(int, input().split())
max_num = a if a > b and b > c else (b if b > c else c)
print(max_num)