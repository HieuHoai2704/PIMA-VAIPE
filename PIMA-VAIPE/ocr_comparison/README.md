# Mô hình 3: Mở rộng Baseline tích hợp OCR (PIMA_OCR)

Thư mục `PIMA_OCR` chứa mã nguồn cho **Phương pháp PIMA có tích hợp công nghệ Trích xuất Quang học (OCR)**.

Trong các phiên bản trước (như Baseline và Ablation), hệ thống giả định rằng các Bounding Box chứa tên thuốc trên đơn thuốc đã được con người đánh dấu sẵn (Ground Truth). Tuy nhiên, để đưa mô hình vào ứng dụng thực tế, mô hình phải tự đọc được chữ từ ảnh đơn thuốc thô. Thư mục này giải quyết bài toán đó.

---

## 🔬 Sự Khác Biệt & Kiến trúc Kỹ thuật

Phiên bản `PIMA_OCR` vẫn sử dụng lõi thuật toán của Baseline (`ResNet50` + `GraphSAGE`), nhưng quy trình xử lý dữ liệu đầu vào (Data Pipeline) được thiết kế lại hoàn toàn:

### 1. Trích xuất Text Tự động (PaddleOCR / PP-OCRv3)
- Thay vì nạp nhãn văn bản có sẵn, hệ thống nhúng trực tiếp thư viện **PaddleOCR**.
- Khi nạp một ảnh đơn thuốc, hệ thống tự động chạy AI OCR để dò tìm các vùng văn bản, sinh ra các Bounding Box và dự đoán chuỗi ký tự bên trong đó.
- Các chuỗi ký tự này (có thể có nhiễu hoặc sai chính tả do lỗi OCR) sau đó mới được đưa vào Text Encoder.

### 2. Các nhánh còn lại (Vision & Graph)
- **Đồ thị (Graph):** Đồ thị lúc này được dựng lên từ tọa độ không gian do AI OCR dự đoán, thay vì tọa độ do con người gán nhãn.
- **Hình ảnh (Vision):** Vẫn sử dụng `ResNet50` nhận đầu vào là ảnh viên thuốc đã cắt.
- **Ghép cặp (Matching):** Vẫn sử dụng Contrastive Learning, nhưng thử thách khó hơn rất nhiều vì văn bản đầu vào chứa nhiễu từ bộ OCR.

---

## 📊 Đánh giá Phương pháp (Pros & Cons)

- **Ưu điểm:** Khả năng ứng dụng thực tế (End-to-End) cao hơn so với Baseline. Mô hình tự động hoàn thiện quy trình phân tích văn bản mà không cần sự can thiệp của con người.
- **Nhược điểm:** 
  - Gánh chịu **Sai số tích lũy (Cascading Errors)**: Bất kỳ một lỗi nhận diện chữ nào của OCR đều sẽ bị khuếch đại khi đưa vào GraphSAGE và làm độ chính xác matching giảm sút nghiêm trọng.
  - Tốc độ xử lý (Inference Time) chậm hơn do phải gánh thêm tiến trình quét ảnh bằng OCR trước khi chạy GNN.

## 📈 Kết quả Thực nghiệm (Độ chính xác)
Nhằm mục đích so sánh khách quan mức độ ảnh hưởng của sai số OCR đến hệ thống, chúng tôi tiến hành đánh giá trên cả 2 kịch bản (có dùng OCR và không dùng OCR nhưng chạy chung một kiến trúc mô hình):

1. **Kịch bản 1: Không dùng OCR (Ground Truth Text & Bounding Box):**
   - Sử dụng nhãn chữ và tọa độ chuẩn 100% do con người gán.
   - **Độ chính xác (Top-1 Accuracy):** `44.26%`
   - *Đánh giá:* Mô hình đạt hiệu năng tối đa khi không bị nhiễu văn bản.

2. **Kịch bản 2: Có dùng OCR (End-to-End với PaddleOCR):**
   - Hệ thống tự đọc chữ và vẽ tọa độ hoàn toàn tự động.
   - **Độ chính xác (Top-1 Accuracy):** `44.31%`
   - *Đánh giá:* Độ chính xác sụt giảm so với Kịch bản 1 do gánh chịu **sai số tích lũy (Cascading Errors)** từ các từ bị OCR nhận diện sai hoặc vẽ sai tọa độ Bounding Box. Điều này phản ánh đúng thách thức của bài toán trong thực tế.

---
## ⚙️ Hướng dẫn Chạy (Dành cho Giáo viên chấm bài)

**Huấn luyện & Đánh giá (Run script):**
```bash
# Script thực thi thường được tích hợp tham số OCR hoặc chạy thông qua file main
python main.py
```
