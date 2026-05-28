# 📊 Tổng Hợp Kết Quả Thực Nghiệm VAIPE Pill-Prescription Matching

Tài liệu này tổng hợp toàn bộ các kết quả đánh giá (evaluation results) từ 4 phương pháp và thử nghiệm khác nhau trong dự án: **PIMA Baseline**, **PIMA Ablation**, **PIMA_OCR**, và **PIMA_NEW**.

Kết quả được trích xuất trực tiếp từ các file log sinh ra trong quá trình huấn luyện (training) và đánh giá (evaluation).

---

## 🏆 Bảng Tổng Hợp Nhanh (Leaderboard)

| Phương Pháp / Thư Mục | Mô Hình / Kịch Bản | Train Loss | Val Accuracy | Khớp Chính Xác (Top-1 Matching) |
| :--- | :--- | :---: | :---: | :---: |
| **PIMA_NEW** | **ViT-B/16 (Cắt gọn)** | 0.2075 | - | **82.46%** |
| **PIMA_NEW** | **Faster R-CNN (End-to-End)**| 0.5810 | - | **68.43%** |
| **PIMA** | Baseline Nguyên Bản | 0.5730 | 38.88% | **49.89%** |
| **PIMA_OCR** | OCR End-to-End (PaddleOCR) | 0.6480 | 50.95% | **44.31%** |
| **PIMA_OCR** | Không OCR (GT Text & BBox) | 0.2390 | 44.08% | **44.26%** |
| **PIMA_ablation** | Mô hình cắt tỉa (Ablation) | 0.8620 | 50.52% | **26.23%** |
| **PIMA_OCR** | Kịch bản Ablation | 0.8160 | 43.73% | 0.00% |

---

## 🔍 Chi Tiết Từng Phương Pháp

### 1. Thư mục `/PIMA_NEW`: Đề Xuất Kiến Trúc Mới (Hiệu Năng Tốt Nhất)
Đây là thư mục chứa các mô hình đem lại kết quả tốt nhất, giải quyết được những hạn chế của phương pháp Baseline. Quá trình đánh giá được thực hiện trên tập dữ liệu kiểm thử (test set) nhằm đo lường khả năng khớp (matching).

* **Mô hình 1: Vision Transformer (ViT-B/16)**
  * **Cách tiếp cận:** Cắt gọn hoàn hảo (Crop sạch nền bằng tay).
  * **Số Epoch đạt được:** 45 (Early Stopping).
  * **Average Loss:** 0.2075
  * **Khớp Chính Xác (Top-1):** **82.46%** (Khớp đúng 2,991 / 3,627 viên).
  * *Nhận xét:* Việc loại bỏ được nhiễu từ nền xung quanh giúp mạng lưới Transformer tập trung hoàn toàn vào việc bắt giữ các đặc trưng hình thái, đem lại độ chính xác cao nhất trong toàn bộ các thử nghiệm.

* **Mô hình 2: Faster R-CNN (ResNet50_FPN)**
  * **Cách tiếp cận:** End-to-End (Nhận diện trực tiếp trên ảnh gốc đơn thuốc và viên thuốc, không cần cắt ảnh).
  * **Số Epoch tốt nhất:** 40 / 50.
  * **Chi tiết Loss (Quá trình Train):**
    * **Total Loss:** 0.5810
    * **Match Loss (Đối sánh):** 0.5338
    * **Det Loss (Detection - Phát hiện bbox):** 0.0459
    * **Cls Loss (Classification - Phân loại):** 0.0013
  * **Khớp Chính Xác (Accuracy / Top-1):** **68.43%** (Khớp đúng 4,830 / 7,058 cặp).
  * *Nhận xét:* Kiến trúc End-to-End gặp khó khăn hơn do nhiễu nền (đặc trưng lấy qua RoI Align) nhưng mô hình vẫn duy trì khả năng hoạt động ở độ chính xác khá cao. Thiết kế này có tính ứng dụng thực tế mạnh mẽ do tự động hóa hoàn toàn.

---

### 2. Thư mục `/PIMA`: Mô Hình Cơ Sở (Baseline)
Mô hình quy chiếu kết hợp kiến trúc ResNet50 và GraphSAGE gốc dùng làm tham chiếu để đo đếm sự cải tiến của các mô hình khác.

* **Số Epoch huấn luyện:** 10 (Early Stopping).
* **Train Loss (Total):** 0.573
* **Validation Accuracy:** 38.88%
* **Top-1 Matching Accuracy (Tập Test):** **49.89%**
* *Nhận xét:* Với độ chính xác chỉ dừng ở mức ~50%, phương pháp GraphSAGE nguyên bản vẫn còn bộc lộ nhiều hạn chế khi biểu diễn đặc trưng quan hệ phức tạp, do đó cần thiết phải sử dụng kiến trúc như `PIMA_NEW`.

---

### 3. Thư mục `/PIMA_OCR`: Tích Hợp OCR & Phân Tích Sai Số
Hướng tới thực tế, thử nghiệm này phân tích sâu mức độ ảnh hưởng của sai số do hệ thống đọc chữ (OCR) mang lại.

* **Kịch bản 1: Không dùng OCR (Dùng Text & BBox chuẩn - 100% chính xác)**
  * **Số Epoch:** 10
  * **Train Loss (Total):** 0.239
  * **Validation Accuracy:** 44.08%
  * **Top-1 Matching Accuracy:** **44.26%**
* **Kịch bản 2: Tích hợp OCR (PaddleOCR End-to-End tự động lấy chữ & BBox)**
  * **Số Epoch:** 10
  * **Train Loss (Total):** 0.648
  * **Validation Accuracy:** 50.95%
  * **Top-1 Matching Accuracy:** **44.31%**
* **Kịch bản 3: Ablation Study trên nhánh OCR**
  * **Số Epoch:** 6
  * **Train Loss (Total):** 0.816
  * **Validation Accuracy:** 43.73%
  * **Top-1 Matching Accuracy:** 0.00% (Dữ liệu không hội tụ ở chặng cuối)
* *Nhận xét:* Việc triển khai thực tế bằng PaddleOCR đã sinh ra **sai số tích lũy (Cascading Errors)** khiến Train Loss tăng vọt (0.648 so với 0.239 ở dữ liệu sạch). Mặc dù vậy, Top-1 Matching trên test set vẫn giữ vững (44.31% so với 44.26%), chứng minh tính bền bỉ và khả năng chống nhiễu (robustness) của mạng.

---

### 4. Thư mục `/PIMA_ablation`: Đánh Giá Cắt Tỉa Kiến Trúc
Thử nghiệm hiệu năng khi thay đổi hàm Loss hoặc lược bỏ (ablate) một số thành phần thuộc cấu trúc Baseline.

* **Số Epoch huấn luyện:** 9 (Early Stopping).
* **Train Loss (Total):** 0.862
* **Validation Accuracy (Quá trình Train):** 50.52%
* **Top-1 Matching Accuracy (Quá trình Test):** **26.23%**
* *Nhận xét:* Phiên bản Ablation gặp hiện tượng quá khớp (Overfitting) rất nghiêm trọng. Mặc dù Valid Acc đạt đến 50.52%, nhưng khi đưa vào thực nghiệm ghép cặp Top-1 lại tụt dốc thê thảm (26.23%). Điều này khẳng định việc cắt tỉa kiến trúc gốc không phải là giải pháp tốt.

---
*Lưu ý: Báo cáo trên được tổng hợp trực tiếp từ các file `lap.log`, `log_eval.log`, `train_with_paddleocr.log`, `lap_faster_rcnn.log` cùng các file README trong 4 thư mục chính.*
