from collections import Counter


def main():
    # Nhập 2 chuỗi S1 và S2
    s1 = input("Nhập chuỗi S1: ")
    s2 = input("Nhập chuỗi S2: ")

    # --- Câu a: In ra những ký tự xuất hiện trong cả 2 chuỗi ---
    counter1 = Counter(s1)
    counter2 = Counter(s2)

    common_chars = counter1 & counter2  # Lấy các phần tử chung với số lượng tối thiểu
    print(f"\na) Các ký tự xuất hiện trong cả 2 chuỗi: {list(common_chars.keys())}")

    # --- Câu b & c: Ký tự có trong chuỗi này nhưng không có trong chuỗi kia ---
    dict1 = Counter(s1)
    dict2 = Counter(s2)

    # Tìm ký tự trong S1 nhưng không có trong S2
    only_in_s1 = [char for char in dict1 if char not in dict2]

    # Tìm ký tự trong S2 nhưng không có trong S1
    only_in_s2 = [char for char in dict2 if char not in dict1]

    # Kết quả câu b: Đếm số lượng
    print(f"\nb) Số lượng ký tự trong S1 nhưng không có trong S2: {len(only_in_s1)}")
    print(f"   Số lượng ký tự trong S2 nhưng không có trong S1: {len(only_in_s2)}")

    # Kết quả câu c: In ra các ký tự đó
    print(f"\nc) Ký tự có trong S1 nhưng không có trong S2: {only_in_s1}")
    print(f"   Ký tự có trong S2 nhưng không có trong S1: {only_in_s2}")


if __name__ == "__main__":
    main()