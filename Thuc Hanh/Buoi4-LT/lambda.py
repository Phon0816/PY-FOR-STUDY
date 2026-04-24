import math

#a) Hàm nhận một đối số là số nguyên n trả về giá trị tuyệt đối của n
cau_a = lambda n :abs(n)

#b) Hàm nhận một đối số là số nguyên n và trả về giá trị của n + 15
cau_b = lambda n : n + 15

#c) Hàm nhận hai đối số là số nguyên (x,y), trả về tích của x và y
cau_c = lambda x,y : x * y

#d) Hàm nhận một đối số nguyên là n Cho biết n có bội số của 13 hoặc 19  hay không
cau_d = lambda n : n % 13 == 0 or n % 19 == 0

#e) Hàm nhận một đối số là số thực r là bán kính của hifnh tròn. Cho biết diện tích hình tròn
cau_e = lambda r : math.pi * (r ** 2)

#f) Hàm nhận 2 đối số là ố thực d, r là chiều dài và chiều rộng hình chữ nhật . Cho biết chu vi hình chữ nhật
cau_f = lambda d,r : 2 * (d + r)

#g) Kiểm tra số chính phương
cau_g = lambda n : n > 0 and (n ** 0.5).is_integer()

#h) Kiểm tra số nguyên tố
cau_h = lambda n : n > 1 and all(n % i == 0 for i in range(2, int(n ** 0.5) + 1))

# i) Kiểm tra và phân loại tam giác (Dùng toán tử 3 ngôi lồng nhau)
cau_i = lambda a, b, c: (
    "Không phải tam giác" if not (a + b > c and a + c > b and b + c > a)
    else "Tam giác đều" if a == b == c
    else "Tam giác vuông cân" if (a == b or b == c or a == c) and (a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a)
    else "Tam giác cân" if a == b or b == c or a == c
    else "Tam giác vuông" if (a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a)
    else "Tam giác thường"
)

print(f"a) Trị tuyệt đối của -5 là: {cau_a(-5)}")
print(f"d) 38 có là bội của 13 hoặc 19 không? {cau_d(38)}")
print(f"g) 16 có phải số chính phương? {cau_g(16)}")
print(f"h) 17 có phải số nguyên tố? {cau_h(17)}")
print(f"i) 3 cạnh (3, 4, 5) là: {cau_i(3, 4, 5)}")
print(f"i) 3 cạnh (2, 2, 5) là: {cau_i(2, 2, 5)}")