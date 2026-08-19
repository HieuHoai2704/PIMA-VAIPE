# A Transformer-Based Multimodal Cross-Attention Framework with Relational Graph Attention for Pill–Prescription Matching

[![Paper PDF](https://img.shields.io/badge/Paper-PDF-red.svg)](./CMC-86877-Manuscript-Clean-128484-1.pdf)
[![Acceptance Letter](https://img.shields.io/badge/Acceptance%20Letter-PDF-green.svg)](./CMC--ISSN_1546--2226_Acceptance_Letter_A%20Transformer--Based%20Multimodal%20Cross--Attention%20Framework%20wit.pdf)
[![Journal](https://img.shields.io/badge/Journal-Computers%2C%20Materials%20%26%20Continua%20%28CMC%29-blue.svg)](https://www.techscience.com/journal/cmc)
[![Dataset](https://img.shields.io/badge/Dataset-VAIPE-orange.svg)](https://www.kaggle.com/datasets/tommyngx/vaipepill2022)

Official repository for the paper **"A Transformer-Based Multimodal Cross-Attention Framework with Relational Graph Attention for Pill–Prescription Matching"**, published in **Computers, Materials & Continua (CMC)**.

This repository contains the official implementation of our multimodal framework for matching physical pills from mobile photos with prescribed drug names on medical prescriptions.

---

## 🎉 News & Publication Status

- **Status**: **Accepted & Published** in **Computers, Materials & Continua (CMC)** (ISSN: 1546-2226).
- **Manuscript**: [CMC-86877-Manuscript-Clean-128484-1.pdf](./CMC-86877-Manuscript-Clean-128484-1.pdf)
- **Acceptance Letter**: [CMC-ISSN_1546-2226_Acceptance_Letter.pdf](./CMC-ISSN_1546-2226_Acceptance_Letter_A%20Transformer-Based%20Multimodal%20Cross-Attention%20Framework%20wit.pdf)

---

## 📝 Abstract

Matching physical pills with drug names on a prescription is a safety-critical task for preventing medication errors. While the pioneering PIMA framework addressed this problem, its real-world deployment is hindered by reliance on manual ground-truth annotations, sensitivity to background clutter, and a simplistic fusion mechanism. 

In this work, we propose a redesigned, fully multimodal framework featuring five coordinated improvements:
1. **Interchangeable Visual Encoders**: A Vision Transformer (ViT-B/16) applied to background-removed crops, and an end-to-end Faster R-CNN/RoI-Align detector that learns directly from raw images.
2. **Lightweight Language Encoder**: `all-MiniLM-L6-v2` for efficient pill-name representation.
3. **Automated OCR**: An integrated PP-OCRv3 module that automates text and bounding box extraction.
4. **Relational Graph Attention (R-GAT)**: A spatial encoder with a pseudo-classifier gate to model directional spatial logic (e.g., left-to-right relations) and filter irrelevant non-drug text.
5. **Multimodal Cross-Attention Head**: Optimized via an InfoNCE objective for stable and dense gradient convergence.

Experiments on the real-world **VAIPE dataset** show substantial improvements: the ViT-B/16 variant reaches **82.46%** Top-1 matching accuracy, and the end-to-end Faster R-CNN variant achieves **83.47%**, significantly outperforming the baseline (49.89%).

---

## 🚀 Repository Structure

The codebase is organized into several directories corresponding to the different experimental setups and models discussed in the paper:

- `pima_Faster-R-CNN/`: Contains the best-performing **End-to-End Faster R-CNN** variant (**83.47%** accuracy). Operates directly on raw prescription and pill images without requiring a separate background removal step.
- `pima_ViT/`: Contains the **ViT-B/16** variant (**82.46%** accuracy). Utilizes clean-cropped pill images to extract highly detailed morphological features.
- `ocr_comparison/`: Code for evaluating the impact of automatic text extraction (PP-OCRv3) versus ground-truth manual annotations.
- `pima_ablation_study/`: Scripts for the ablation studies (removing R-GAT and InfoNCE loss) to validate the architectural contributions.
- `pima_baseline/`: The reproduced original PIMA baseline (ResNet50 + GraphSAGE) used for benchmarking.
- `CMC-86877-Manuscript-Clean-128484-1.pdf`: Official published manuscript.
- `CMC-ISSN_1546-2226_Acceptance_Letter_A Transformer-Based Multimodal Cross-Attention Framework wit.pdf`: Official acceptance notification.

---

## 📊 Leaderboard & Results

Performance comparison on the hold-out test set of the VAIPE dataset:

| Method / Configuration | Visual Backbone | Train Loss | Top-1 Accuracy (%) |
| :--- | :--- | :---: | :---: |
| **Proposed (Faster R-CNN)** | **Faster R-CNN + RoI-Align (End-to-End)** | **0.4871** | **83.47** |
| **Proposed (ViT-B/16)** | **ViT-B/16 (Clean crop)** | **0.2075** | **82.46** |
| Baseline PIMA (Reproduced)| ResNet50 + GraphSAGE | 0.5730 | 49.89 |
| OCR (PP-OCRv3, automatic) | ResNet50 + GraphSAGE | 0.6480 | 44.31 |
| No-OCR (GT text & boxes) | ResNet50 + GraphSAGE | 0.2390 | 44.26 |
| Ablation (Pruned model) | ResNet50 + GraphSAGE | 0.8620 | 26.23 |

---

## ⚙️ Getting Started

### 1. Prerequisites
- Python 3.8+
- PyTorch (with CUDA support for GPU acceleration)
- PP-OCRv3 (PaddleOCR)
- Transformers (Hugging Face)

Install dependencies for each specific module by navigating to the respective directory and running:
```bash
pip install -r requirements.txt
```

### 2. Dataset
The experiments use the [VAIPE dataset](https://www.kaggle.com/datasets/tommyngx/vaipepill2022). 
- Please download the dataset and place it inside the `data/` folder of the respective model directory (e.g., `pima_Faster-R-CNN/data/`).
- Note: Large dataset files and model weights (`*.pth`) are ignored via `.gitignore` to prevent repository bloat.

### 3. Training & Evaluation
Each sub-directory operates as a standalone module. To train and evaluate a specific model variant, navigate to its folder and execute the training script:

```bash
# Example for running the Faster R-CNN variant
cd pima_Faster-R-CNN
python train.py
python eval.py
```

---

## ✒️ Citation

If you find this code or research helpful in your work, please cite our paper:

```bibtex
@article{nguyen2026transformer,
  title={A Transformer-Based Multimodal Cross-Attention Framework with Relational Graph Attention for Pill–Prescription Matching},
  author={Linh Nguyen Thi My, Lap Thai Viet, Hoai Truong Hieu, Tham Vo and Vinh Truong Hoang},
  journal={Computers, Materials \& Continua},
  volume={--},
  number={--},
  pages={--},
  year={2026},
  publisher={Tech Science Press},
  doi={10.32604/cmc.2026.086877}
}
```

## 📄 License
This project is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
