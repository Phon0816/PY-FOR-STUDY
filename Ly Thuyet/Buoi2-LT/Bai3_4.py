n = int(input("Nhap Số Nguyên Duong"))

chan = 0
le = 0

temp = n

if n==0 :
    chan=1
else:
    while temp > 0 :
        chu_so = temp % 10
        if chu_so % 2 == 0:
            chan += 1
        else :
            le += 1
        temp//= 10

print(f"So Luong So Le : {le}, So Luong So Chan : {chan}")


