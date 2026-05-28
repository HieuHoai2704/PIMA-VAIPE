# Kết Quả Đánh Giá Mô Hình Cơ Sở (PIMA Baseline)

Tài liệu này tổng hợp các thông số và kết quả chi tiết sau quá trình huấn luyện và đánh giá mô hình trong hệ thống **PIMA** nguyên bản.

Mục đích của việc đánh giá này là thiết lập một hệ quy chiếu (baseline) trên bộ dữ liệu VAIPE để từ đó so sánh với các phương pháp cải tiến (Ablation, OCR, PIMA_NEW).

---

## 📊 Bảng Tóm Tắt Kết Quả

| Mô Hình | Epoch Dừng Sớm | Loss Huấn Luyện | Độ Chính Xác (Val Accuracy) | Khớp Chính Xác (Top-1 Matching) |
| :--- | :---: | :---: | :---: | :---: |
| **PIMA Baseline** | Epoch 10 | 0.573 | 38.88% | **49.89%** |

---

## 🔍 Chi Tiết Quá Trình Huấn Luyện (Training Metrics)

Dưới đây là các thông số chi tiết được ghi nhận lại trong quá trình huấn luyện mô hình PIMA Baseline:

- **File log ghi nhận huấn luyện:** `lap.log`
- **File log ghi nhận đánh giá (Evaluation):** `log_eval.log`
- **Số Epoch huấn luyện đạt được:** 10 (Mô hình hội tụ và kích hoạt Early Stopping sau 10 epoch)
- **Train Loss (Total Loss):** 0.573
- **Validation Accuracy (trong lúc train):** 38.88%
- **Top-1 Matching Accuracy (trên tập Test):** 49.89%

---

## 📝 Nhận Xét Tổng Quan

- **Quá trình huấn luyện:** Mô hình hội tụ tương đối nhanh (chỉ sau khoảng 10 epoch với sự hỗ trợ của cơ chế Early Stopping). Mức Train Loss cuối cùng đạt `0.573`.
- **Hiệu năng ghép cặp (Matching Performance):** Trái ngược với mô hình Ablation (dễ bị quá khớp trên tập Test), phiên bản PIMA Baseline nguyên bản cho thấy khả năng tổng quát hóa tốt hơn. Dù độ chính xác Validation trong quá trình train chỉ ở mức `38.88%`, nhưng khi thực thi ghép cặp phân lớp thực tế trên tập Test, mô hình đạt **Top-1 Matching Accuracy là 49.89%**.
- **Vai trò Baseline:** Mức độ chính xác `~50%` này được sử dụng làm mốc chuẩn (benchmark) cho toàn bộ dự án. Kết quả này chứng minh rằng kiến trúc kết hợp ResNet50 và GraphSAGE nguyên bản vẫn còn nhiều hạn chế khi phải xử lý đặc trưng hình dáng phức tạp của các viên thuốc trong tập VAIPE, qua đó mở đường cho việc phát triển kiến trúc thay thế ưu việt hơn ở thư mục `PIMA_NEW`.

*(Lưu ý: Kết quả trên được tổng hợp trực tiếp từ các file log sinh ra sau khi chạy mô hình: `lap.log` và `log_eval.log`)*
