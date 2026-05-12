def bai_7():
    S = input("Nhập chuỗi S: ")
    idx_not = S.find('not')
    idx_poor = S.find('poor')


    if idx_not != -1 and idx_poor != -1 and idx_not < idx_poor:

        S = S[:idx_not] + 'good' + S[idx_poor + 4:]

    print(f"=> xuất ra {S}")

bai_7()