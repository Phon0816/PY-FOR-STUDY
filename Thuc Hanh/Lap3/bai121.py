def get_strobogrammatic(n, target_length, pairs):
    if n == 0:
        return [""]
    if n == 1:
        return [k for k, v in pairs.items() if k == v]

    centers = get_strobogrammatic(n - 2, target_length, pairs)
    res = []

    for center in centers:
        for left, right in pairs.items():
            if left == '0' and n == target_length:
                continue
            res.append(left + center + right)

    return res


n = int(input("Nhập n (2 <= n <= 10): "))

if 2 <= n <= 10:
    std_pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    ext_pairs = {'0': '0', '1': '1', '2': '2', '5': '5', '6': '9', '8': '8', '9': '6'}

    std_nums = sorted(get_strobogrammatic(n, n, std_pairs))
    ext_nums = sorted(get_strobogrammatic(n, n, ext_pairs))

    print(f"a.- Tất cả các số strobogrammatic gồm {n} chữ số:")
    print(", ".join(std_nums))

    print(f"\nb.- Tất cả các số strobogrammatic mở rộng gồm {n} chữ số:")
    print(", ".join(ext_nums))
else:
    print("Vui lòng nhập n trong khoảng từ 2 đến 10.")