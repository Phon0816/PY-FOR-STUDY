#Bảng Cửu Chương
def BangCuuChuong(a,b):         #gọi hàm
    if a > b :                          #nếu a > b
        a,b =b,a                        #thì thây a=b b=a
    for n in range(a, b + 1):           #Duyệt bảng cửu chương từ a -> b
        print(f'Bang cuu chuong {n}')   #in tiltle bảng cửu chương của n
        for i in range(1, 11):          #duyệt i từ 0-10 để in các dòng nhân ra terminal
            print(f'{n} x {i} = {n*i}') #in một phép nhân trong bảng cửu chương
        print()                         #in dòng trống để in các bản cửu chương

#Hàm kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(so):
    if so < 2:                          #Số nguyên tố chỉ chia hết cho 1 va chính nó, và phải > 1
        return False
    for i in range(2, int(so ** 0.5) + 1):#kiểm tra số đến căn bậc 2
        if so % i == 0:
            return False                 # Tìm thấy ước => không phải số nguyên tố
    return True

#Hàm tìm và liệt kê ra danh sách các số nguyên tố nhỏ hơn n
def liet_ke_nguyen_to_nho_hon_n(n):
    ket_qua = []                        # Tạo một danh sách rỗng
    for so in range(2, n):              #Vòng lập để chạy biên so từ 2 đến n
        if kiem_tra_so_nguyen_to(so):   #if dùng để kiểm tra so có phải là số nguyên tố hay không
            ket_qua.append(so)          #Nếu so là số nguyên tố thêm so vào Ket_qua
    return ket_qua

def Liet_Ke_Cac_Uoc_So_Cua_n(n):
    ket_qua = []                        #Tạo một danh sách rỗng
    for i in range(2, n):               #Vòng lập để chạy biến i từ 2 đến n
        if n % i == 0 and kiem_tra_so_nguyen_to(i):        # Phải thỏa mãn hai điều kiện : là ước của n và là số nguyên tố
            ket_qua.append(i)           #nếu i thõa mãn điều kiện thêm 1 vào danh sách
    return ket_qua


# Bảng cửu chương
print("========== BANG CUU CHUONG ==========")
dong = input("Nhap hai so a, b cach nhau boi dau phay:>? ")
a, b = dong.split(",")
a = int(a.strip())
b = int(b.strip())
BangCuuChuong(a, b)


# Liệt kê các số nguyên tố < n
print("\nCác số nguyên tố")
n2 = int(input("Nhập số nguyên dương n n:>? "))
ds = liet_ke_nguyen_to_nho_hon_n(n2)
if ds:
    print(f"Cac so nguyen to nho hon {n2}: {', '.join(map(str, ds))}")
else:
    print(f"Khong co so nguyen to nao nho hon {n2}")


# Ước số nguyên tố của n
print("\n========== UOC SO NGUYEN TO CUA N ==========")
n3 = int(input("Nhap so nguyen duong n:>? "))
ds_uoc = Liet_Ke_Cac_Uoc_So_Cua_n(n3)
if ds_uoc:
    print(f"Cac so vua la uoc cua {n3}, vua la so nguyen to: {', '.join(map(str, ds_uoc))}")
else:
    print(f"Khong co uoc so nao cua {n3} la so nguyen to")