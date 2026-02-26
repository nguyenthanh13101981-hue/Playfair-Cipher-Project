# Thuật toán Playfair Cipher (Python)

Dự án này cài đặt thuật toán mã hóa cổ điển Playfair Cipher bằng hai ngôn ngữ lập trình là Python và C++. Đây là bài tập thực hành mật mã học với các quy tắc chuẩn của Playfair.

## 📌 Các quy tắc áp dụng
- Sử dụng ma trận khóa kích thước **5x5**.
- Bảng chữ cái tiếng Anh gồm 25 ký tự (chữ `J` được gộp chung với chữ `I`).
- Xử lý bản rõ (Plaintext):
  - Loại bỏ toàn bộ khoảng trắng và ký tự đặc biệt.
  - Tách thành các cặp 2 ký tự.
  - Chèn ký tự `X` nếu hai ký tự trong một cặp trùng nhau.
  - Chèn ký tự `X` vào cuối nếu tổng số ký tự của chuỗi bị lẻ.

## 📁 Cấu trúc thư mục
- `playfair.py`: Cài đặt thuật toán bằng Python.

## 🚀 Ví dụ kiểm thử (Test Case)
Chương trình đã được thiết lập sẵn ví dụ kiểm thử với các thông số sau:
- **Từ khóa (Key):** `CRYPTO`
- **Bản rõ (Plaintext):** `DO YOU LIKE TO STUDY A CRYPTOGRAPHY COURSE`

**Kết quả đầu ra dự kiến:**
- Quá trình mã hóa (Encryption) sẽ tạo ra một chuỗi Ciphertext dựa trên ma trận khóa sinh ra từ chữ `CRYPTO`.
- Quá trình giải mã (Decryption) sẽ dịch ngược lại và so sánh với chuỗi ban đầu để kiểm tra tính chính xác (Hiển thị `PASS` nếu khớp).

## 💻 Cách chạy chương trình
**Với Python:**
Mở terminal và chạy lệnh:
```bash
python playfair.py
