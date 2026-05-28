# Kết Quả Đánh Giá Mô Hình (Evaluation Results)

Tài liệu này tổng hợp các thông số và kết quả cuối cùng sau quá trình huấn luyện và đánh giá hai mô hình thị giác trong hệ thống **PIMA_NEW**.

Quá trình đánh giá được thực hiện trên tập dữ liệu kiểm thử (test set) nhằm đo lường khả năng khớp (matching) chính xác hình ảnh viên thuốc thực tế với tên thuốc dạng văn bản được ghi trên đơn thuốc. 

---

## 📊 Bảng Tóm Tắt Kết Quả

| Mô Hình | Phương Pháp | Tổng Số Lượt Đánh Giá | Khớp Chính Xác (Top-1) | Độ Chính Xác (Accuracy) |
| :--- | :--- | :---: | :---: | :---: |
| **Vision Transformer (ViT-B/16)** | *Cắt Gọn Hoàn Hảo* | 3,627 | 2,991 | **82.46%** |
| **Faster R-CNN (ResNet50_FPN)** | *End-to-End* | 7,058 | 4,830 | **68.43%** |

---

## 🔍 Chi Tiết Kết Quả Đánh Giá

### 1. Mô Hình Vision Transformer (ViT-B/16)
Mô hình này yêu cầu đầu vào là hình ảnh viên thuốc đã được cắt (crop) sạch nền. 
- **Tổng số viên thuốc được đánh giá (có nhãn khớp):** 3,627
- **Số viên thuốc được khớp chính xác (Top-1):** 2,991
- **Độ chính xác khớp Top-1 (Top-1 Matching Accuracy):** **82.46%**

**Kết quả huấn luyện (Early stopping at Epoch 45):**
- **Average Loss:** 0.2075

> **Nhận xét:** Việc loại bỏ được nhiễu từ nền xung quanh giúp mạng lưới Transformer tập trung hoàn toàn vào việc bắt giữ các đặc trưng hình thái của viên thuốc, đem lại độ chính xác rất cao.

### 2. Mô Hình Faster R-CNN (ResNet50_FPN)
Mô hình này hoạt động end-to-end trên ảnh gốc nguyên bản của đơn thuốc và viên thuốc mà không cần bước tiền xử lý cắt ảnh thủ công.
- **Tổng số cặp được đánh giá:** 7,058
- **Số cặp được khớp chính xác (Top-1):** 4,830
- **Độ chính xác (Accuracy):** **68.43%**

**Kết quả huấn luyện tốt nhất (Best Epoch 40/50):**
- **Total Loss:** 0.5810
- **Match Loss:** 0.5338
- **Det Loss:** 0.0459
- **Cls Loss:** 0.0013

> **Nhận xét:** Bài toán trở nên khó khăn hơn do các đặc trưng được trích xuất trực tiếp thông qua RoI Align sẽ chứa những yếu tố nhiễu của nền ảnh thực tế. Dù độ chính xác thấp hơn so với ViT, mô hình này vẫn duy trì khả năng hoạt động tốt và cực kỳ tiện lợi cho các ứng dụng thực tế.

---
*Lưu ý: Kết quả trên được trích xuất từ các file log sinh ra sau khi chạy quá trình đánh giá (evaluation).*
