# Bài 4

# Hàm lambda kiểm tra số đồng nhất
# Số đồng nhất là số có tất cả các chữ số giống nhau, ví dụ: 1, 22, 333, 7777
KiemTraSoDongNhat = lambda n: len(set(str(n))) == 1


# Hàm lambda kiểm tra số hoàn thiện
# Số hoàn thiện là số có tổng các ước nhỏ hơn nó bằng chính nó
KiemTraSoHoanThien = lambda n: sum(i for i in range(1, n) if n % i == 0) == n


# Liệt kê các số đồng nhất từ 1 đến 10000
print("========== CAC SO DONG NHAT TU 1 DEN 10000 ==========")

for i in range(1, 10001):                       # Cho i chạy từ 1 đến 10000
    if KiemTraSoDongNhat(i):                    # Nếu i là số đồng nhất
        print(i, end=" ")                       # In i ra màn hình, nằm trên cùng một dòng


# Xuống dòng cho dễ nhìn
print("\n")


# Liệt kê các số hoàn thiện từ 1 đến 10000
print("========== CAC SO HOAN THIEN TU 1 DEN 10000 ==========")

for i in range(1, 10001):                       # Cho i chạy từ 1 đến 10000
    if KiemTraSoHoanThien(i):                   # Nếu i là số hoàn thiện
        print(i, end=" ")                       # In i ra màn hình, nằm trên cùng một dòng