import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main():
    numbers = []

    # Nhập dữ liệu
    while True:
        try:
            val = int(input("Nhập một số nguyên: "))
            numbers.append(val)
        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ!")
            continue

        choice = input("Bạn có muốn nhập tiếp không? (Y/N): ").strip().upper()
        if choice == 'N':
            break

    if not numbers:
        print("Danh sách trống.")
        return

    print("\n--- KẾT QUẢ ---")

    # a) In ra các số nguyên tố
    primes = [x for x in numbers if is_prime(x)]
    print(f"a) Các số nguyên tố trong list: {primes}")

    # b) Tính trung bình cộng số âm và số dương
    negatives = [x for x in numbers if x < 0]
    positives = [x for x in numbers if x > 0]

    avg_neg = sum(negatives) / len(negatives) if negatives else 0
    avg_pos = sum(positives) / len(positives) if positives else 0

    print(f"b) Trung bình cộng số âm: {avg_neg}")
    print(f"   Trung bình cộng số dương: {avg_pos}")

    # c) Số lớn nhất, số nhỏ nhất
    print(f"c) Số lớn nhất: {max(numbers)}")
    print(f"   Số nhỏ nhất: {min(numbers)}")

    # d) Kiểm tra sắp xếp tăng dần
    is_sorted = all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))
    if is_sorted:
        print("d) Các số trong list ĐÃ được sắp xếp tăng dần.")
    else:
        print("d) Các số trong list CHƯA được sắp xếp tăng dần.")


if __name__ == "__main__":
    main()


