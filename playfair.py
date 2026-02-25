import string

def create_matrix(key):
    """Tạo ma trận 5x5 từ từ khóa, bỏ qua ký tự trùng lặp và chữ J."""
    key = key.upper().replace("J", "I")
    seen = set()
    matrix_list = []

    # Thêm khóa và bảng chữ cái vào ma trận
    for char in key + string.ascii_uppercase:
        if char.isalpha() and char not in seen and char != 'J':
            seen.add(char)
            matrix_list.append(char)

    # Cắt danh sách 1 chiều thành ma trận 5x5
    return [matrix_list[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    """Tìm tọa độ (hàng, cột) của một ký tự trong ma trận."""
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def prepare_text(text):
    """Xử lý bản rõ: bỏ khoảng trắng, ghép cặp và chèn 'X' nếu cần."""
    text = text.upper().replace("J", "I")
    text = ''.join(filter(str.isalpha, text))

    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        # Nếu là ký tự cuối cùng bị lẻ, tự động mượn 'X' làm b
        b = text[i+1] if i+1 < len(text) else 'X'

        if a == b:
            # Hai ký tự trong cặp trùng nhau -> chèn 'X' vào giữa
            result += a + 'X'
            i += 1
        else:
            # Khác nhau -> ghép thành cặp bình thường
            result += a + b
            i += 2

    # Đảm bảo chuỗi luôn có độ dài chẵn (thực tế vòng lặp while đã cover)
    if len(result) % 2 == 1:
        result += 'X'

    return result

def encrypt(text, matrix):
    """Mã hóa bản rõ dựa trên luật của Playfair."""
    text = prepare_text(text)
    cipher = ""

    # Duyệt từng cặp 2 ký tự
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            # Cùng hàng: Dịch sang phải 1 vị trí
            cipher += matrix[r1][(c1+1) % 5]
            cipher += matrix[r2][(c2+1) % 5]
        elif c1 == c2:
            # Cùng cột: Dịch xuống dưới 1 vị trí
            cipher += matrix[(r1+1) % 5][c1]
            cipher += matrix[(r2+1) % 5][c2]
        else:
            # Khác hàng, khác cột: Đổi góc hình chữ nhật
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher

def decrypt(cipher, matrix):
    """Giải mã bản mã để lấy lại bản rõ (đã kèm ký tự đệm X)."""
    plain = ""

    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            # Cùng hàng: Dịch sang trái 1 vị trí
            plain += matrix[r1][(c1-1) % 5]
            plain += matrix[r2][(c2-1) % 5]
        elif c1 == c2:
            # Cùng cột: Dịch lên trên 1 vị trí
            plain += matrix[(r1-1) % 5][c1]
            plain += matrix[(r2-1) % 5][c2]
        else:
            # Khác hàng, khác cột: Đổi góc hình chữ nhật (Giống mã hóa)
            plain += matrix[r1][c2]
            plain += matrix[r2][c1]

    return plain


if __name__ == "__main__":
    key = "CRYPTO"
    plaintext = "DO YOU LIKE TO STUDY A CRYPTOGRAPHY COURSE"

    matrix = create_matrix(key)

    print("--- PLAYFAIR MATRIX 5x5 ---")
    for row in matrix:
        # In ma trận có khoảng trắng để dễ nhìn hơn
        print("  " + " ".join(row))

    cipher = encrypt(plaintext, matrix)
    decrypted = decrypt(cipher, matrix)
    prepared = prepare_text(plaintext)

    print(f"\n[+] Plaintext ban đầu : {plaintext}")
    print(f"[+] Plaintext chia cặp: {prepared}")
    print(f"[+] Ciphertext (Mã hóa): {cipher}")
    print(f"[+] Decrypted (Giải mã): {decrypted}")

    print("\n--- KIỂM THỬ KẾT QUẢ ---")
    if decrypted == prepared:
        print("-> [PASS] Quá trình mã hóa và giải mã khớp nhau hoàn toàn!")
    else:
        print("-> [FAIL] Có lỗi xảy ra trong thuật toán.")