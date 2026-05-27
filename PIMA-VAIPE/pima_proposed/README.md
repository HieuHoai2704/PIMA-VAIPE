# PIMA_NEW: Advanced Multi-Modal Pill-Prescription Matching (Custom Architecture)

This repository (`PIMA_NEW`) represents a **massive architectural evolution** over the baseline PIMA method. It replaces almost every component of the original system with State-of-the-Art (SOTA) Deep Learning techniques, transforming it from a simple graph-contrastive model into a highly advanced **Transformer-based Multi-Modal Cross-Attention Framework**. 

This is a custom-built solution heavily optimized for the VAIPE dataset.

---

## 🌟 The Dual-Vision Architecture (2 Models in 1)

This repository supports **two distinct visual pipelines**, depending on whether you want to use clean, pre-cropped images or a true end-to-end detection system. You can switch between them using the `--vision-model` argument.

### Model 1: Vision Transformer (ViT-B/16) - *The "Perfect Crop" Approach*
- **How it works:** Assumes the pill has already been cropped from the image and its background has been removed (using an external tool like `rembg`). The isolated pill image is passed to a `ViT-B/16` transformer.
- **Pros:** Because the ViT only "sees" the clean pill without any background noise, it is incredibly accurate at capturing morphological features.
- **Cons:** Requires a separate pre-processing pipeline. It cannot automatically find the pill inside a raw, full-sized prescription photo.
- **Command:** `--vision-model vit`
- **Current Accuracy:** `82.46%`

### Model 2: Faster R-CNN - *The "End-to-End" Approach*
- **How it works:** Takes the **full, raw prescription/pill photo** directly without any manual cropping or background removal. It uses a ResNet50 backbone to scan the image and applies **RoI Align** (Region of Interest Align) to extract features directly from the bounding box coordinates.
- **Pros:** A true End-to-End system. Ready to be deployed in a real-world application where users just upload a photo.
- **Cons:** The extracted features will inevitably contain some background noise around the pill, making the matching task slightly harder compared to the ViT approach.
- **Command:** `--vision-model faster_rcnn`
- **Current Accuracy:** `68.43%`

---

## 🧠 Shared Core Innovations

Regardless of which Vision Model you choose, both pipelines share these groundbreaking modules:

### 1. Language & OCR Branch: MiniLM + PP-OCRv3
- **Replaced standard BERT with `all-MiniLM-L6-v2`.** This provides much faster and highly accurate sentence embeddings.
- **End-to-End OCR Integration:** Built-in support for `PaddleOCR` (PP-OCRv3) allows the model to extract text and bounding boxes directly from raw prescription images dynamically.

### 2. Graph Branch: Relational Graph Attention (R-GAT)
- **Replaced `GraphSAGE` with `RGATConv`.**
- Unlike standard GCNs, R-GAT can understand *directional relations* (e.g., left, right, top, bottom) between text boxes on the prescription paper.
- **Pseudo-Classifier:** The graph branch includes an auxiliary binary classifier that predicts the probability of a text box actually containing a pill name, acting as an attention gate.

### 3. Fusion: Multi-Modal Cross-Attention
- **Replaced basic Cosine Similarity with a powerful `MultiModalCrossAttention` module.**
- Visual Features act as **Queries**, while the GNN-enriched Text Features act as **Keys/Values**. This allows the visual appearance of the pill to dynamically "search" for its textual match across the prescription graph.

### 4. Advanced Objective: InfoNCE Loss
- **Replaced standard Contrastive Loss with `InfoNCE Loss`.**
- Uses a temperature-scaled cross-entropy optimization over the entire batch, pulling positive Multi-Modal pairs closer while aggressively pushing all negative pairs apart simultaneously.

---

## ⚙️ Engineering & Infrastructure Upgrades

- **High-Performance Multi-GPU Training (DDP):** The `train.py` loop supports PyTorch Distributed Data Parallel (`torchrun`), allowing the model to train across 4+ GPUs efficiently.
- **Unified Pipeline:** Both the ViT and Faster R-CNN models are trained using the exact same contrastive loss and text graphs, ensuring fair comparison.

---

## 🚀 How to Run

### 1. Train Model 1 (ViT)
*(Ensure you have run `preprocess_pills.py` to create `pill_crops/` first)*
```bash
nohup python train.py --vision-model vit --save-name model_best_vit.pth > lap_vit.log 2>&1 & disown
```

### 2. Train Model 2 (Faster R-CNN)
*(Reads raw images directly, no pre-processing required)*
```bash
nohup python train.py --vision-model faster_rcnn --save-name model_best_faster_rcnn.pth > lap_faster_rcnn.log 2>&1 & disown
```

### 3. Evaluate the Models
Run the standalone evaluation script to test Top-1 Matching Accuracy:

**Evaluate ViT:**
```bash
python eval.py --vision-model vit --weights model_best_vit.pth
```

**Evaluate Faster R-CNN:**
```bash
python eval.py --vision-model faster_rcnn --weights model_best_faster_rcnn.pth
```
