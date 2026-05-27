# Mô hình 2: Thử nghiệm Cắt tỉa (PIMA Ablation Study)

Thư mục `PIMA_ablation` chứa mã nguồn phục vụ cho phương pháp **Ablation Study (Nghiên cứu Cắt tỉa/Thử nghiệm thành phần)**. 

Trong nghiên cứu Deep Learning, Ablation Study là một bước cực kỳ quan trọng để chứng minh tính hiệu quả của hệ thống. Chúng tôi tinh chỉnh, thay đổi hoặc loại bỏ một số module lõi của phương pháp PIMA gốc (ví dụ: đổi hàm Loss, thay đổi cách kết hợp đồ thị) để quan sát xem hiệu năng thay đổi như thế nào trên bộ dữ liệu **VAIPE**.

---

## 🔬 Các Kiến trúc được Thử nghiệm (Ablations)

Trong phiên bản này, các công nghệ nền tảng phần lớn vẫn giống với PIMA Baseline (`ResNet50` cho hình ảnh, `GraphSAGE` cho đồ thị văn bản). Tuy nhiên, có một số cấu hình đã được thay đổi để đo lường:

### 1. Thử nghiệm thay đổi Hàm mất mát (Loss Function Variations)
- Hệ thống thử nghiệm tinh chỉnh các trọng số của **Contrastive Loss** và **BCE Loss** để tìm ra điểm cân bằng tốt nhất giữa việc phân loại chữ (Text Node) và việc ghép cặp ảnh-chữ (Image-Text Matching).
- Thay vì dùng InfoNCE tiêu chuẩn, thử nghiệm tùy biến nhiệt độ (temperature scaling) trong hàm Loss để xem khả năng đẩy xa các mẫu âm tính (Negative samples).

### 2. Thử nghiệm cấu trúc Đồ thị (Graph Variations)
- Chặn/bỏ qua (bypass) thuật toán GraphSAGE để so sánh trực tiếp: Liệu việc ghép cặp thuần túy (Text thuần - Image thuần) có tốt hơn là dùng Đồ thị hay không? Qua đó chứng minh vai trò thiết yếu của GNN.

---

## 📊 Phân tích Thực nghiệm (Pros & Cons)

- **Vai trò trong nghiên cứu:** Bước đệm hoàn hảo để rút ra những điểm yếu cốt lõi của kiến trúc cũ. Nhờ Ablation Study, chúng tôi nhận ra rằng chỉ tinh chỉnh nhỏ (đổi Loss, đổi Data Augmentation) là **không đủ** để vượt qua các rào cản đặc thù của bộ dữ liệu VAIPE.
- **Tiền đề phát triển:** Kết quả hạn chế từ thư mục này chính là lý do và động lực bắt buộc phải đập đi xây lại toàn bộ kiến trúc (dẫn đến sự ra đời của phiên bản `PIMA_NEW` hoàn thiện nhất).

## 📈 Kết quả Thực nghiệm (Độ chính xác)
Kết quả của mô hình Ablation sau khi tinh chỉnh tốt nhất có sự cải thiện so với Baseline, nhưng vẫn chưa đạt mức lý tưởng:
- **Độ chính xác (Top-1 Accuracy) cao nhất:** `26.23%`

---
## ⚙️ Hướng dẫn Chạy (Dành cho Giáo viên chấm bài)

**Huấn luyện (Train):**
```bash
python train.py
```

**Đánh giá (Evaluate):**
```bash
python eval.py
```
