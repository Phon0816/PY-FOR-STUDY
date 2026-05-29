# Bài 3

# Hàm kiểm tra n có chia hết cho 13 hoặc 19 hay không
def KiemTraChiaHet(n):                    # Gọi hàm và truyền vào số n
    if n % 13 == 0 or n % 19 == 0:                  # Nếu n chia hết cho 13 hoặc n chia hết cho 19
        return True                                 # Đúng thì trả về True
    else:                                           # Ngược lại nếu không chia hết
        return False                                # Trả về False


# Hàm kiểm tra 3 cạnh có tạo thành tam giác không
def KiemTraTamGiac(a, b, c):     # Gọi hàm và truyền vào 3 cạnh a, b, c
    if a + b > c and a + c > b and b + c > a:       # Điều kiện để 3 cạnh tạo thành 1 tam giác
        return True                                 # Nếu thỏa điều kiện thì là tam giác
    else:                                           # Nếu không thỏa điều kiện
        return False                                # Không phải tam giác


# Hàm kiểm tra loại tam giác
def KiemTraLoaiTamGiac(a, b, c):                    # Gọi hàm kiểm tra loại tam giác
    if KiemTraTamGiac(a, b, c) == False:            # Nếu 3 cạnh không tạo thành tam giác
        return "Không phải là tam giac"             # Trả về không phải tam giác
    if a == b and b == c:                           # Nếu 3 cạnh bằng nhau
        return "Tam giac đều"                       # Là tam giác đều
    elif a == b or a == c or b == c:                # Nếu có 2 cạnh bằng nhau
        return "Tam giac cân"                       # Là tam giác cân
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        # Kiểm tra định lý Pytago
        # Nếu bình phương 2 cạnh bằng bình phương cạnh còn lại
        return "Tam giac vuông"                     # Là tam giác vuông
    else:                                           # Nếu không rơi vào các trường hợp trên
        return "Tam giac thường"                    # Là tam giác thường


# Câu 1: Kiểm tra chia hết cho 13 hoặc 19
print("Kiểm tra chia hết")

n = int(input("Nhập số nguyên n:>? "))              # Nhập số nguyên n từ bàn phím

if KiemTraChiaHet(n):                               # Gọi hàm kiểm tra n có chia hết cho 13 hoặc 19 không
    print(f"{n} chia hết cho 13 hoặc 19")           # Nếu đúng thì in ra chia hết
else:                                               # Nếu sai
    print(f"{n} không chia hết cho 13 hoặc 19")     # In ra không chia hết


# Câu 2: Kiểm tra loại tam giác
print("\nKiểm tra tam giác")

a = float(input("Nhập cạch a:>? "))                 # Nhập cạnh a
b = float(input("Nhập cạch b:>? "))                 # Nhập cạnh b
c = float(input("Nhập cạch c:>? "))                 # Nhập cạnh c

ket_qua = KiemTraLoaiTamGiac(a, b, c)               # Gọi hàm kiểm tra loại tam giác và lưu

print("Kết quả:", ket_qua)                          # In kết quả ra terminal