from datetime import datetime, timedelta

def bai_i():
    now = datetime.now()
    print("--- BÀI i ---")
    print(f"{'Năm hiện tại':<55} | {now.year}")
    print(f"{'Tháng hiện tại bằng chữ':<55} | {now.strftime('%B')}")
    print(f"{'Tuần hiện tại là tuần thứ mấy trong năm':<55} | {now.strftime('%W')}")
    print(f"{'Tuần hiện tại là tuần thứ mấy trong tháng':<55} | {(now.day - 1) // 7 + 1}")
    print(f"{'Ngày hiện tại là ngày thứ mấy trong năm':<55} | {now.strftime('%j').lstrip('0')}")
    print(f"{'Ngày dương lịch hiện tại là ngày':<55} | {now.day}")
    print(f"{'Thứ của ngày hiện tại':<55} | {now.strftime('%A')}")
    print(f"{'Giờ phút giây hiện tại':<55} | {now.strftime('%H:%M:%S')}")

def bai_ii():
    print("\n--- BÀI ii ---")
    str_date1 = input("Ngày thứ nhất (dd/mm/yyyy): ")
    str_date2 = input("Ngày thứ hai (dd/mm/yyyy): ")
    try:
        date1 = datetime.strptime(str_date1, "%d/%m/%Y")
        date2 = datetime.strptime(str_date2, "%d/%m/%Y")
        print(f"=> Hai ngày này cách nhau: {abs((date2 - date1).days)} ngày.")
    except ValueError:
        print("Lỗi: Sai định dạng dd/mm/yyyy!")

def bai_iii():
    print("\n--- BÀI iii ---")
    S = input("Nhập chuỗi S (VD: Sep 18 2019 2:43PM): ")
    if not S:
        S = 'Sep 18 2019 2:43PM'
    try:
        print(f"Dữ liệu datetime: {datetime.strptime(S, '%b %d %Y %I:%M%p')}")
    except ValueError:
        print("Lỗi: Chuỗi không đúng định dạng!")

def bai_iv():
    print("\n--- BÀI iv ---")
    now = datetime.now()
    print(f"Thời gian lúc này: {now.strftime('%H:%M:%S')}")
    print(f"Sau khi buff 5s:   {(now + timedelta(seconds=5)).strftime('%H:%M:%S')}")

# Gọi hàm
bai_i()
bai_ii()
bai_iii()
bai_iv()