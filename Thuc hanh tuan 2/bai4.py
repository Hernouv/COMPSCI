c = input()
ac = int(ord(c))

# print(ac) 65->90 and 97->122

if ((65 <= ac and ac <= 90) or (97 <= ac and ac <= 122)):
    print(f"{c} la ki tu alphabet")
else:
    print(f"{c} khong phai la ki tu alphabet")