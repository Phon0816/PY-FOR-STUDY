n = int(input("Nhập số nguyên dương n: "))

max_val = 0
temp = n

if n == 0:
    max_val = 0
else:
    while temp > 0:
        chu_so = temp % 10

        if chu_so > max_val:
            max_val = chu_so

        temp //= 10

print(f"Số lớn nhất là: {max_val}")