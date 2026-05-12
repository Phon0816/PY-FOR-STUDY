import zlib


def nen_file(input_file, compressed_file):
    with open(input_file, 'rb') as f:
        data = f.read()

    # Nén dữ liệu
    compressed_data = zlib.compress(data)

    with open(compressed_file, 'wb') as f:
        f.write(compressed_data)
    print(f"Đã nén file. Dung lượng mới: {len(compressed_data)} bytes")


def giai_nen_file(compressed_file, output_file):
    with open(compressed_file, 'rb') as f:
        compressed_data = f.read()

    # Giải nén dữ liệu
    original_data = zlib.decompress(compressed_data)

    with open(output_file, 'wb') as f:
        f.write(original_data)
    print("Đã giải nén và khôi phục định dạng ban đầu.")


# 1. Nén file gốc thành file mới giảm dung lượng
nen_file('fileName.txt', 'compressed.dat')

# 2. Đọc file đã nén và trả về định dạng ban đầu
giai_nen_file('compressed.dat', 'restored_fileName.txt')