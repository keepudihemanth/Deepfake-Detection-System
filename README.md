#  Hybrid Deepfake Detection System
A hybrid deep learning framework for detecting manipulated facial images by combining **spatial (RGB) features** and **frequency-domain artifacts**. The project leverages an **EfficientNet-B0 backbone** together with a custom **Frequency CNN** to improve robustness against AI-generated face manipulations.
---
##  Project Overview

Deepfake technology has advanced rapidly, making manipulated images increasingly difficult to distinguish from authentic ones. This project proposes a hybrid architecture that simultaneously learns:
- **Spatial Features** from RGB images using EfficientNet-B0.
- **Frequency Features** using FFT, DCT, and Sobel edge representations.
- Feature fusion through an attention mechanism for final binary classification.

The objective is to accurately classify facial images as:
- ✅ Real
- ❌ Fake
---
#  Architecture
```
                   RGB Image
                       │
                EfficientNet-B0
                       │
                 RGB Feature Vector
                       │
                       │
Input Image ───────────┼──────────► Feature Fusion ► Attention ► Classifier
                       │
              Frequency Transform
            (FFT + DCT + Sobel)
                       │
                 Frequency CNN
                       │
             Frequency Feature Vector
```
---
#  Features

- Hybrid Deep Learning Architecture
- EfficientNet-B0 Spatial Feature Extraction
- Frequency Domain Analysis
- FFT (Fast Fourier Transform)
- DCT (Discrete Cosine Transform)
- Sobel Edge Features
- Attention-based Feature Fusion
- Resume Training using Checkpoints
- Mixed Precision Training (AMP)
- Automatic GPU/CPU Support
- Modular Project Structure
- Ready for Streamlit Deployment

---

#  Project Structure

```
DDS/

│
├── notebooks/
│      Notebook 7.ipynb          # Training
│      Notebook 8.ipynb          # Evaluation
│      Notebook 9.ipynb          # Inference
│
├── src/
│      model.py                  # Hybrid Architecture
│      dataset.py                # Dataset Loader
│      transforms.py             # Frequency Transform
│
├── models/
│      best_model.pth
│      latest_checkpoint.pth
│      final_model.pth
│
├── outputs/
│      evaluation_metrics.csv
│
├── data/
│      archive.zip
│
├── requirements.txt
│
└── README.md
```

---

#  Model Architecture
## RGB Branch

- EfficientNet-B0 Backbone
- Global Average Pooling
- Feature Projection Layer
---

## Frequency Branch

Frequency representation generated using:
- Fast Fourier Transform (FFT)
- Discrete Cosine Transform (DCT)
- Sobel Edge Detection

Processed using a custom CNN consisting of:

- Convolution Layers
- Batch Normalization
- ReLU
- Adaptive Average Pooling

---
## Fusion

The extracted spatial and frequency features are combined using:

- Attention Module
- Fully Connected Layers
- Dropout
- Binary Classifier
---

#  Dataset

Dataset Structure
```
Dataset/

Train/
Real
Fake

Validation/
Real
Fake

Test/
Real
Fake
```

Dataset Statistics

| Split | Real | Fake |
|--------|------|------|
| Train | 70,001 | 70,001 |
| Validation | 19,787 | 19,641 |
| Test | 5,413 | 5,492 |

---

#  Training Details

Backbone
- EfficientNet-B0
Optimizer
- AdamW
Loss
- CrossEntropy Loss
Scheduler
- ReduceLROnPlateau
Mixed Precision
- Automatic Mixed Precision (AMP)
Epochs
- 15
Checkpointing
- Resume Training Supported
---

#  Results

## Training Performance

| Metric | Value |
|---------|------:|
| Best Validation Accuracy (during training) | **91.39%** |

This represents the highest validation accuracy achieved during model training and was used to save the best model checkpoint.

---

## Official Validation Set Performance

| Metric | Value |
|---------|------:|
| Accuracy | **86.41%** |

The trained model was then evaluated on the official validation dataset, achieving an overall accuracy of **86.41%**, demonstrating good generalization beyond the training process.

---

## Official Test Set Performance

| Metric | Value |
|---------|------:|
| Accuracy | **72.31%** |
| Precision | **68.61%** |
| Recall | **82.96%** |
| F1 Score | **75.11%** |
| ROC-AUC | **79.88%** |

The test set was kept completely unseen during training and was used to evaluate the final performance of the model.---

#  Completed Milestones

✔ Dataset Preparation
✔ Data Preprocessing
✔ Frequency Domain Feature Extraction
✔ Hybrid CNN Model
✔ EfficientNet Integration
✔ Training Pipeline
✔ Resume Checkpoint Support
✔ Mixed Precision Training
✔ Evaluation Pipeline
✔ Confusion Matrix
✔ ROC Curve
✔ Classification Report
✔ Single Image Inference
✔ GPU & CPU Compatibility

---

#  Future Enhancements

The following improvements are planned for future versions:

## Deployment

- Streamlit Web Application
- Interactive User Interface
- Drag-and-Drop Image Upload
- Confidence Visualization
- Probability Charts

---

## Explainable AI

- Grad-CAM Visualization
- Attention Heatmaps
- Feature Map Visualization

---

#  Current Progress

| Phase | Status |
|--------|--------|
| Dataset Preparation | ✅ |
| Preprocessing | ✅ |
| Frequency Transform | ✅ |
| Hybrid Model | ✅ |
| Training | ✅ |
| Resume Training | ✅ |
| Evaluation | ✅ |
| Inference | ✅ |
| Streamlit Deployment | 🚧 In Progress |
| Explainability | 🚧 Planned |
| Final Deployment | 🚧 Planned |

---

#  Technologies Used

### Programming
- Python
### Deep Learning
- PyTorch
- Torchvision
- timm
### Computer Vision
- OpenCV
- Pillow
### Data Processing
- NumPy
- Pandas
### Visualization
- Matplotlib
### Deployment (Planned)
- Streamlit

---

#  Author
**Hemanth**

---

#  Repository Status

 Active Development

This project is currently under active development. Future updates will include deployment, explainable AI visualizations, model optimization, and support for real-time deepfake detection.
