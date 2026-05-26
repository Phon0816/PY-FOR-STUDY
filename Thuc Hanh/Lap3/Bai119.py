limit = 1000000
is_p = [True] * limit
is_p[0] = is_p[1] = False
for i in range(2, int(limit ** 0.5) + 1):
    if is_p[i]:
        for j in range(i * i, limit, i):
            is_p[j] = False

std_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
ext_map = {'0': '0', '1': '1', '2': '2', '5': '5', '6': '9', '8': '8', '9': '6'}

a, b, c, d, e = [], [], [], [], []

for i in range(limit):
    s = str(i)

    rot_std = ""
    for ch in reversed(s):
        if ch in std_map:
            rot_std += std_map[ch]
        else:
            rot_std = None
            break

    rot_ext = ""
    for ch in reversed(s):
        if ch in ext_map:
            rot_ext += ext_map[ch]
        else:
            rot_ext = None
            break

    if rot_std == s:
        a.append(i)
        if is_p[i]:
            b.append(i)

    if rot_ext == s:
        c.append(i)
        if is_p[i]:
            d.append(i)

    if rot_std is not None and rot_std != s and not is_p[i]:
        if is_p[int(rot_std)]:
            e.append(i)

print("a.- Các số strobogrammatic nhỏ hơn 1 triệu:\n" + ", ".join(map(str, a)) + "\n")
print("b.- Các số nguyên tố strobogrammatic nhỏ hơn 1 triệu:\n" + ", ".join(map(str, b)) + "\n")
print("c.- Các số strobogrammatic mở rộng nhỏ hơn 1 triệu:\n" + ", ".join(map(str, c)) + "\n")
print("d.- Các số nguyên tố strobogrammatic mở rộng nhỏ hơn 1 triệu:\n" + ", ".join(map(str, d)) + "\n")
print("e.- Các số thỏa mãn yêu cầu e:\n" + ", ".join(map(str, e)))