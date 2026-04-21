n = int(input("Nhập số nguyên dương n: "))

tong = 0
tich = 1
temp = n

if n == 0:
    tong = 0
    tich = 0
else:
    while temp > 0:
        chu_so = temp % 10
        tong += chu_so
        tich *= chu_so
        temp //= 10

print(f"Tổng = {tong}, Tích = {tich}")