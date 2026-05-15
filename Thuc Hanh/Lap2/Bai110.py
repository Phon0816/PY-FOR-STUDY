def decode_string(cipher_text):
    plain_text = ""
    i = 0
    n = len(cipher_text)

    while i < n:
        if cipher_text[i] == '#':
            count = int(cipher_text[i + 1])
            char_to_repeat = cipher_text[i + 2]
            plain_text += char_to_repeat * count
            i += 3
        else:
            plain_text += cipher_text[i]
            i += 1

    return plain_text


test_1 = "XY#6Z1#4023"
test_2 = "#39+1=1#30"

print(f"Ví dụ 1:\n  Cipher text: {test_1}\n  Plain text : {decode_string(test_1)}\n" + "-" * 40)
print(f"Ví dụ 2:\n  Cipher text: {test_2}\n  Plain text : {decode_string(test_2)}")