def tong_binh_phuong_so_con(n):
    chuoi_n = str(n)
    chieu_dai = len(chuoi_n)
    tong = 0

    for i in range(chieu_dai):
        for j in range(i + 1, chieu_dai + 1):
            so_con = int(chuoi_n[i:j])
            tong += so_con ** 2

    return tong


print(tong_binh_phuong_so_con(2207))
print(tong_binh_phuong_so_con(54321))