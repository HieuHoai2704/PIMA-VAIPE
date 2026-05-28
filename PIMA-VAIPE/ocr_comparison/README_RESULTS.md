# Kết Quả Đánh Giá Mô Hình Tích Hợp OCR (PIMA_OCR)

Tài liệu này tổng hợp các thông số và kết quả chi tiết (loss, accuracy, v.v.) sau quá trình huấn luyện và đánh giá mô hình trong hệ thống **PIMA_OCR**.

Quá trình đánh giá tập trung vào so sánh mức độ ảnh hưởng của sai số OCR đến hệ thống ghép cặp đơn thuốc - viên thuốc.

---

## 📊 Bảng Tóm Tắt Kết Quả

| Kịch Bản | Phương Pháp | Loss Huấn Luyện (Cuối) | Độ Chính Xác (Val Accuracy) | Top-1 Matching (Đánh giá) |
| :--- | :--- | :---: | :---: | :---: |
| **Kịch bản 1 (Không dùng OCR)** | *Ground Truth Text & BBox* | 0.239 (Epoch 10) | 44.08% | **44.26%** |
| **Kịch bản 2 (Có dùng OCR)** | *PaddleOCR End-to-End* | 0.648 (Epoch 10) | 50.95% | **44.31%** |
| **Kịch bản Ablation** | *Thử nghiệm cắt bỏ* | 0.816 (Epoch 6) | 43.73% | 0.00% |

---

## 🔍 Chi Tiết Quá Trình Huấn Luyện (Training Metrics)

### 1. Kịch bản 1: Không dùng OCR (Ground Truth Text & Bounding Box)
Kịch bản này sử dụng nhãn và tọa độ Bounding Box được gán chuẩn xác bởi con người (100% chính xác), không bị nhiễu văn bản.
- **File log ghi nhận:** `ocr.log`, `log_eval.log`
- **Số Epoch huấn luyện:** 10 (kích hoạt Early Stopping)
- **Train Loss (Total):** 0.239
- **Validation Accuracy:** 44.08%
- **Top-1 Matching Accuracy:** 44.26%

### 2. Kịch bản 2: Có dùng OCR (End-to-End với PaddleOCR)
Kịch bản này hệ thống tự động đọc văn bản và trích xuất Bounding Box bằng thư viện AI PaddleOCR. Dữ liệu văn bản sẽ chứa các sai số tự nhiên.
- **File log ghi nhận:** `train_with_paddleocr.log`, `log_eval.log`
- **Số Epoch huấn luyện:** 10 (kích hoạt Early Stopping)
- **Train Loss (Total):** 0.648
- **Validation Accuracy:** 50.95%
- **Top-1 Matching Accuracy:** 44.31%

### 3. Kịch bản Ablation
Thử nghiệm phân rã (Ablation study) trên tập dữ liệu của mô hình OCR.
- **File log ghi nhận:** `ocr_ablation.log`
- **Số Epoch huấn luyện:** 6 (kích hoạt Early Stopping)
- **Train Loss (Total):** 0.816
- **Validation Accuracy:** 43.73%

---

## 📝 Nhận Xét Tổng Quan
- **Sự khác biệt về Train Loss:** Ở kịch bản có dùng OCR, quá trình hội tụ trên tập huấn luyện khó khăn hơn (Loss `0.648` so với `0.239`) do mô hình phải đối mặt với **sai số tích lũy (Cascading Errors)** từ kết quả đọc OCR.
- **Độ chính xác tương đương:** Mặc dù chịu nhiễu từ OCR, Top-1 Matching Accuracy ở Kịch bản 2 (44.31%) vẫn gần tương đương với kịch bản dùng Ground Truth (44.26%). Điều này cho thấy khả năng chống chịu nhiễu tốt của nhánh Vision và Graph.
- **Hội tụ nhanh:** Cơ chế Early Stopping được kích hoạt trong hầu hết các kịch bản sau khoảng 5 đến 10 epochs. 

*(Lưu ý: Các kết quả trên được trích xuất chi tiết từ dữ liệu file log: `ocr.log`, `train_with_paddleocr.log`, `ocr_ablation.log` và `log_eval.log`.)*
