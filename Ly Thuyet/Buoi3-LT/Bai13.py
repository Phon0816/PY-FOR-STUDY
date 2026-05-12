def bai_13():
    print("Nhập bài thơ của bạn (Nhấn Enter 2 lần để kết thúc việc nhập):")
    lines = []


    while True:
        line = input()
        if not line:
            break
        lines.append(line)

    print("\n--- KẾT QUẢ CHUỖI HOÀN CHỈNH ---")
    for line in lines:

        chuoi_chuan = " ".join(line.split())

        chuoi_chuan = chuoi_chuan.replace(" .", ".")
        chuoi_chuan = chuoi_chuan.replace(" ,", ",")


        if chuoi_chuan:
            print(chuoi_chuan)


# Gọi hàm để chạy
bai_13()