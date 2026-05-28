# Kết Quả Đánh Giá Mô Hình Cắt Tỉa (PIMA Ablation Study)

Tài liệu này tổng hợp các thông số và kết quả chi tiết sau quá trình huấn luyện và đánh giá mô hình trong hệ thống **PIMA_ablation**.

Mục đích của việc đánh giá này là đo lường hiệu năng của mạng khi thay đổi các hàm Loss hoặc lược bỏ một số thành phần trong kiến trúc GraphSAGE kết hợp với ResNet50.

---

## 📊 Bảng Tóm Tắt Kết Quả

| Mô Hình | Epoch Dừng Sớm | Loss Huấn Luyện | Độ Chính Xác (Val Accuracy) | Khớp Chính Xác (Top-1 Matching) |
| :--- | :---: | :---: | :---: | :---: |
| **Mô hình Ablation** | Epoch 9 | 0.862 | 50.52% | **26.23%** |

---

## 🔍 Chi Tiết Quá Trình Huấn Luyện (Training Metrics)

Dưới đây là các thông số chi tiết được ghi nhận lại trong quá trình huấn luyện mô hình Ablation:

- **File log ghi nhận huấn luyện:** `ablation.log`
- **File log ghi nhận đánh giá (Evaluation):** `log_eval.log`
- **Số Epoch huấn luyện đạt được:** 9 (Mô hình hội tụ khá nhanh và kích hoạt Early Stopping ở epoch 9)
- **Train Loss (Total Loss):** 0.862
- **Validation Accuracy (trong lúc train):** 50.52%
- **Top-1 Matching Accuracy (trên tập Test):** 26.23%

---

## 📝 Nhận Xét Tổng Quan

- **Về Train Loss:** Mức loss đạt được là `0.862`, cho thấy quá trình huấn luyện của kiến trúc mạng bị cắt tỉa gặp khó khăn nhất định so với phiên bản PIMA gốc. 
- **Về Độ Chính Xác:** Mặc dù **Validation Accuracy** trên tập xác thực trong quá trình train đạt mức khá tốt (trên 50%), nhưng khi thực hiện ghép cặp thực tế trên tập kiểm thử (Test set), **Top-1 Matching Accuracy** lại bị giảm sâu, chỉ dừng lại ở **26.23%**. Sự chênh lệch này cho thấy mô hình dễ bị quá khớp (overfitting) hoặc gặp khó khăn khi tổng quát hóa lên dữ liệu ghép cặp thực tế.
- **Kết luận từ Ablation Study:** Việc thay đổi cấu trúc đồ thị hoặc hàm loss trong thử nghiệm Ablation không đem lại hiệu năng lý tưởng như kỳ vọng. Kết quả này là bằng chứng thực nghiệm quan trọng, giúp phát hiện điểm yếu cốt lõi trong quy trình trích xuất và kết hợp đặc trưng. Nhờ đó, chúng ta có đủ căn cứ để nâng cấp toàn diện sang một kiến trúc ưu việt hơn (chính là phiên bản `PIMA_NEW`).

*(Lưu ý: Kết quả trên được tổng hợp trực tiếp từ các file log sinh ra sau khi chạy quá trình train và eval: `ablation.log` và `log_eval.log`)*
