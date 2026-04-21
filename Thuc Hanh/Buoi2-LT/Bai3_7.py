
n = int(input("Nhập số nguyên dương n: "))


la_may_man = True
temp = n

if n <= 0:
    la_may_man = False
else:
    while temp > 0:
        chu_so = temp % 10

        if chu_so != 6 and chu_so != 8:
            la_may_man = False
            break

        temp //= 10


if la_may_man:
    print(f"{n} là số may mắn.")
else:
    print(f"{n} KHÔNG phải số may mắn.")