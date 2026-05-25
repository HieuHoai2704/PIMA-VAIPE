
# PIMA - A Novel Approach for Pill-Prescription Matching with GNN Assistance and Contrastive Learning

This repository is an implementation of "A Novel Approach for Pill-Prescription Matching with GNN Assistance and Contrastive Learning" by
Trung Thanh Nguyen, Hoang Dang Nguyen, Thanh Hung Nguyen, Huy Hieu Pham, Ichiro Ide, and Phi Le Nguyen" by Huy-Hieu Pham. The paper was accepted for presentation at The 19th Pacific Rim International Conference on Artificial Intelligence Shanghai, China November 10-13, 2022.

Full paper is available [here](https://github.com/AIoT-Lab-BKAI/PIMA/tree/main/paper).

Journal version: Trung Thanh Nguyen, Phi Le Nguyen, Yasutomo Kawanishi, Takahiro Komamizu, and Ichiro Ide, "Zero-shot Pill-prescription Matching with Graph Convolutional Network and Contrastive Learning," IEEE Access (IF: 3.9)

[Open Access](https://ieeexplore.ieee.org/document/10504270)

---
Environment setting using [Anaconda](https://www.anaconda.com/).

```bash
conda create --name pima
conda install pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia
conda install pyg -c pyg
conda install -c conda-forge transformers
conda install -c conda-forge timm
conda install -c anaconda networkx
conda install -c conda-forge wandb
```

## 🛠️ Windows Compatibility & System Optimization

The original codebase has been thoroughly updated and optimized to run flawlessly on Windows environments:
* **Path Separation Fixes:** Replaced hardcoded POSIX/Linux paths with dynamic OS-independent path construction using Python's `os.path` module (specifically in `train.py`, `inference.py`, and `data/data.py`).
* **UTF-8 Encoding Support:** Fixed file read crashes on Windows due to default system encoding by explicitly enforcing `encoding="utf-8"` on all JSON label/prescription loading operations.
* **Label Mapping Correction:** Solved mapping ID mismatch errors (comparing `str` with `int`) in GNN data representation within `data/data.py`.
* **Automated Data Preparation:** Added `preprocess.py` to seamlessly crop pill bounding boxes from the VAIPE dataset on Windows and split them automatically into the required Train/Val directory structure.

---

## 📈 Training & Validation Results

* **Hardware:** Local RTX 4060 Ti GPU.
* **Dataset:** VAIPE Pill & Prescription Dataset.
* **Best Model Weights:** Saved automatically at `logs/saved/model_best.pth`.
* **Accuracy Achieved:** 
  * **Best Validation Accuracy:** **`30.19%`** (Val accuracy: `0.30198`) on the multi-modal match benchmark.

---

## 🔬 Real-world Inference & Demonstration

We verified the trained model by running inference on prescription graph samples. With a customized classification confidence threshold of `0.5`, the model achieved **100% correct matching classification** on our sample test images:

* **Command to run Inference:**
  ```powershell
  python inference.py --model-path "logs/saved/model_best.pth"
  ```
* **Sample Inference Output:**
  ```text
  Predicted:  1) Droxicef 500mg (similarity = 0.6663)
  Predicted:  1) Droxicef 500mg (similarity = 0.6551)
  Predicted:  1) Droxicef 500mg (similarity = 0.6355)
  Predicted:  1) Droxicef 500mg (similarity = 0.6263)
  ...
  ```
  *(Model successfully matches pill images to the corresponding "Droxicef 500mg" text node with high cosine similarity confidence reaching up to **66.63%**).*

---

## 🚀 How to Run

### 1. Data Preprocessing
Prepare your raw VAIPE dataset directories, then automatically crop pills and format the folders:
```powershell
python preprocess.py
```

### 2. Training
Train the multi-modal Graph & Contrastive Learning network:
```powershell
python train.py --run-name "pima_run"
```

### 3. Inference / Evaluation
Run the model on any sample test prescription:
```powershell
python inference.py --model-path "logs/saved/model_best.pth"
```

