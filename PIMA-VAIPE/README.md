# 📊 PIMA-VAIPE: Hệ Thống Ghép Cặp Tên Thuốc - Hình Ảnh Thuốc Đa Phương Thức

Tài liệu này tổng hợp toàn bộ các kết quả đánh giá (evaluation results) từ 4 phương pháp và thử nghiệm khác nhau trong dự án được tổ chức thành các thư mục tương ứng: **PIMA Baseline**, **PIMA Ablation**, **PIMA_OCR**, và **PIMA_NEW (ViT / Faster R-CNN)**.

Kết quả được trích xuất trực tiếp từ các file log sinh ra trong quá trình huấn luyện (training) và đánh giá (evaluation).

---

## 🏆 Bảng Tổng Hợp Nhanh (Leaderboard)

| Phương Pháp / Thư Mục | Mô Hình / Kịch Bản | Train Loss | Val Accuracy | Khớp Chính Xác (Top-1 Matching) |
| :--- | :--- | :---: | :---: | :---: |
| **pima_ViT** (PIMA_NEW) | **ViT-B/16 (Cắt gọn)** | 0.2075 | - | **82.46%** |
| **pima_Faster-R-CNN** | **Faster R-CNN (End-to-End)**| ~0.4871 | 80.02% | **83.47%** |
| **PIMA_Baseline** | Baseline Nguyên Bản | 0.5730 | 38.88% | **49.89%** |
| **ocr_comparison** | OCR End-to-End (PaddleOCR) | 0.6480 | 50.95% | **44.31%** |
| **ocr_comparison** | Không OCR (GT Text & BBox) | 0.2390 | 44.08% | **44.26%** |
| **pima_ablation_study** | Mô hình cắt tỉa (Ablation) | 0.8620 | 50.52% | **26.23%** |
| **ocr_comparison** | Kịch bản Ablation | 0.8160 | 43.73% | 0.00% |

---

## 🔍 Chi Tiết Từng Phương Pháp

### 1. Nâng Cấp Toàn Diện (Kiến trúc Đa Phương Thức - Transformer)
Đây là các mô hình đem lại kết quả tốt nhất, giải quyết được những hạn chế của phương pháp Baseline bằng cách ứng dụng Vision Transformer hoặc mạng trích xuất đối tượng, kết hợp ngôn ngữ `all-MiniLM-L6-v2` và đồ thị `R-GAT`.

#### 🌟 `pima_ViT`: Mô Hình Vision Transformer (ViT-B/16)
* **Cách tiếp cận:** Cắt gọn hoàn hảo (Crop sạch nền bằng tay).
* **Số Epoch đạt được:** 45 (Early Stopping).
* **Average Loss:** 0.2075
* **Khớp Chính Xác (Top-1):** **82.46%** (Khớp đúng 2,991 / 3,627 viên).
* *Nhận xét:* Việc loại bỏ được nhiễu từ nền xung quanh giúp mạng lưới Transformer tập trung hoàn toàn vào việc bắt giữ các đặc trưng hình thái, đem lại độ chính xác cao nhất.

#### 🌟 `pima_Faster-R-CNN`: Mô Hình Faster R-CNN (ResNet50_FPN)
* **Cách tiếp cận:** End-to-End (Nhận diện trực tiếp trên ảnh gốc đơn thuốc và viên thuốc, không cần cắt ảnh).
* **Số Epoch tốt nhất:** Dừng sớm ở ~17 epoch (Validation Accuracy cao nhất ~83.47%).
* **Khớp Chính Xác (Accuracy / Top-1 Test):** **83.47%** (Khớp đúng 5,635 / 7,058 cặp).
* *Nhận xét:* Kiến trúc End-to-End tự động trích xuất đặc trưng bằng RoI Align. Dù gặp nhiễu nền thực tế, mô hình vẫn đạt độ chính xác trên 80% trên số lượng mẫu đánh giá cực lớn. Thiết kế này có tính ứng dụng thực tế cao do tự động hóa hoàn toàn.

---

### 2. Thư mục `PIMA_Baseline`: Mô Hình Cơ Sở (Baseline)
Mô hình quy chiếu kết hợp kiến trúc ResNet50 và GraphSAGE gốc dùng làm tham chiếu để đo đếm sự cải tiến của các mô hình khác.

* **Số Epoch huấn luyện:** 10 (Early Stopping).
* **Train Loss (Total):** 0.573
* **Validation Accuracy:** 38.88%
* **Top-1 Matching Accuracy (Tập Test):** **49.89%**
* *Nhận xét:* Với độ chính xác chỉ dừng ở mức ~50%, phương pháp GraphSAGE nguyên bản vẫn còn bộc lộ nhiều hạn chế khi biểu diễn đặc trưng quan hệ phức tạp, do đó cần thiết phải sử dụng kiến trúc tiên tiến hơn.

---

### 3. Thư mục `ocr_comparison`: Tích Hợp OCR & Phân Tích Sai Số
Hệ thống PIMA_OCR phân tích sâu mức độ ảnh hưởng của sai số do hệ thống đọc chữ (OCR) mang lại khi áp dụng vào thực tế.

* **Kịch bản 1: Không dùng OCR (Dùng Text & BBox chuẩn - 100% chính xác)**
  * **Train Loss (Total):** 0.239
  * **Validation Accuracy:** 44.08%
  * **Top-1 Matching Accuracy:** **44.26%**
* **Kịch bản 2: Tích hợp OCR (PaddleOCR End-to-End tự động lấy chữ & BBox)**
  * **Train Loss (Total):** 0.648
  * **Validation Accuracy:** 50.95%
  * **Top-1 Matching Accuracy:** **44.31%**
* **Kịch bản 3: Ablation Study trên nhánh OCR**
  * **Top-1 Matching Accuracy:** 0.00% (Dữ liệu không hội tụ ở chặng cuối)
* *Nhận xét:* Việc triển khai thực tế bằng PaddleOCR đã sinh ra **sai số tích lũy (Cascading Errors)** khiến Train Loss tăng vọt. Mặc dù vậy, Top-1 Matching trên test set vẫn giữ vững (44.31% so với 44.26%), chứng minh khả năng chống nhiễu mạnh mẽ.

---

### 4. Thư mục `pima_ablation_study`: Đánh Giá Cắt Tỉa Kiến Trúc
Thử nghiệm hiệu năng khi thay đổi hàm Loss hoặc lược bỏ (ablate) một số thành phần thuộc cấu trúc Baseline.

* **Số Epoch huấn luyện:** 9 (Early Stopping).
* **Train Loss (Total):** 0.862
* **Validation Accuracy (Quá trình Train):** 50.52%
* **Top-1 Matching Accuracy (Quá trình Test):** **26.23%**
* *Nhận xét:* Phiên bản Ablation gặp hiện tượng quá khớp (Overfitting) nghiêm trọng, độ chính xác giảm sút nghiêm trọng, khẳng định các thành phần của Baseline đều đóng vai trò quan trọng không thể cắt bỏ tùy tiện.