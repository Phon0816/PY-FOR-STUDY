import math


def so_than_thien(a, b):
    danh_sach = []
    for i in range(a, b + 1):
        dao_nguoc = int(str(i)[::-1])
        if math.gcd(i, dao_nguoc) == 1:
            danh_sach.append(i)

    print(*danh_sach)
    print(len(danh_sach))


so_than_thien(10, 98)