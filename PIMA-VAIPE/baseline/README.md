# Mô hình 1: Phương pháp PIMA Nguyên Bản (Baseline Model)

Đây là mã nguồn gốc của phương pháp **PIMA (Zero-shot Pill-prescription Matching with Graph Convolutional Network and Contrastive Learning)** - một phương pháp đã được công bố tại hội nghị PRICAI 2022 và tạp chí IEEE Access.

Trong khuôn khổ của báo cáo/luận văn này, phương pháp PIMA nguyên bản được sử dụng như một **Mô hình Cơ sở (Baseline Model)** để chạy thử nghiệm trên bộ dữ liệu **VAIPE (Vietnam AI for Precision mEdicine)**, từ đó làm hệ quy chiếu so sánh hiệu năng với các phương pháp cải tiến sau này.

---

## 🔬 Kiến trúc Kỹ thuật (Công nghệ Sử dụng)

Vì là phương pháp nguyên bản, kiến trúc của thư mục này giữ nguyên các công nghệ cũ như sau:

### 1. Trích xuất Đặc trưng Hình ảnh (Vision Encoder)
- Sử dụng các mạng CNN truyền thống như **`ResNet50`** hoặc **`MobileNetV3`**.
- Đầu vào bắt buộc là ảnh viên thuốc đã được cắt gọn gàng (cropped pills). Mạng CNN sẽ trích xuất ảnh thành một vector đặc trưng đa chiều.

### 2. Trích xuất Đặc trưng Văn bản (Text Encoder)
- Sử dụng mô hình `sentence-transformers/paraphrase-mpnet-base-v2`.
- Mô hình này nhận đầu vào là các **Bounding Box chứa chữ (Ground Truth Text)** có sẵn trong nhãn của tập dữ liệu VAIPE để chuyển đổi thành vector ngữ nghĩa.

### 3. Biểu diễn Đồ thị (Graph Contextualization)
- Sử dụng thuật toán GNN cơ bản: **`GraphSAGE`**.
- Xây dựng một đồ thị (Graph) trong đó mỗi viên thuốc là một node, các cạnh (edges) thể hiện sự tương quan về vị trí không gian của chữ trên đơn thuốc. GraphSAGE giúp cập nhật và làm giàu ngữ cảnh cho từng vector văn bản.

### 4. Cơ chế Ghép cặp (Contrastive Matching)
- Sử dụng **Contrastive Loss** kết hợp **DIoU Loss** (để tính toán khoảng cách không gian bounding box).
- Pha inference (dự đoán) sử dụng **Cosine Similarity** để tìm ra nhãn văn bản gần giống nhất với đặc trưng hình ảnh của viên thuốc.

---

## 📊 Đánh giá Phương pháp (Pros & Cons)

- **Ưu điểm:** Khai thác được cấu trúc đồ thị (GNN) để hiểu mối liên hệ không gian giữa các dòng chữ trên đơn thuốc thay vì chỉ đọc text thuần túy.
- **Nhược điểm đối với dữ liệu VAIPE:** 
  - Mạng `ResNet50` tỏ ra khá yếu trong việc trích xuất đặc trưng các viên thuốc có hình dạng giống hệt nhau (chỉ khác màu/chữ dập chìm) trong tập VAIPE.
  - Thuật toán `GraphSAGE` khá thô sơ, chưa có cơ chế Attention mạnh mẽ để học trọng số định hướng (trái/phải/trên/dưới).

## 📈 Kết quả Thực nghiệm (Độ chính xác)
- **Độ chính xác (Top-1 Accuracy) trên tập VAIPE:** `49.89%`

---
## ⚙️ Hướng dẫn Chạy (Dành cho Giáo viên chấm bài)

**Huấn luyện (Train):**
```bash
python run.py --config config/pima_vaipe.json --mode train
```

**Đánh giá (Evaluate):**
```bash
python run.py --config config/pima_vaipe.json --mode test
```