def tien_dien(num: int):
    res = 0
    if (num > 0):
        res += 1984 * min(50, num)
        num -= 50
    if (num > 0):
        res += 2050 * min(50, num)
        num -= 50
    if (num > 0):
        res += 2380 * min(100, num)
        num -= 100
    if (num > 0):
        res += 2998 * min(100, num)
        num -= 100
    if (num > 0):
        res += 3350 * min(100, num)
        num -= 100
    if (num > 0):
        res += 3460 * num
    return res   
    

ten = input("Ten chu ho: ")
disp1 = int(input("Chi so thang truoc: "))
disp2 = int(input("Chi so thang nay: "))
n = int(disp2 - disp1)

print("Ho va ten: ", ten)
print("Tien phai tra la: ", int(tien_dien(n) * 1.08))
