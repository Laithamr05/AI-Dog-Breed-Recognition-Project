# 🐶 AI Dog Breed Recognition Project  

This project uses **pre-trained Convolutional Neural Networks (CNNs)** (ResNet, AlexNet, VGG16) from **PyTorch** to classify pet images and identify whether they are dogs (and if so, their breed).  

It was developed as part of an **Image Classification Udacity Nanodegree project**, and it compares model performance on different datasets.

---

## 📂 Project Structure  

```
.
├── adjust_results4_isadog.py        # Adds 'is-a-dog' flags to results
├── calculates_results_stats.py      # Calculates summary statistics
├── check_images.py                  # Main program to run classification
├── check_images.txt                 # Example Q&A on uploaded image classification
├── classify_images.py               # Uses chosen CNN model to classify images
├── classifier.py                    # Wrapper for pretrained PyTorch models
├── dognames.txt                     # Text file of valid dog breed names
├── get_input_args.py                # Handles command line arguments
├── get_pet_labels.py                # Extracts pet labels from filenames
├── imagenet1000_clsid_to_human.txt  # ImageNet labels (1000 classes)
├── print_functions_for_lab_checks.py# Helper functions for debugging checks
├── print_results.py                 # Prints results and statistics
├── run_models_batch.sh              # Runs models on `pet_images/` dataset
├── run_models_batch_uploaded.sh     # Runs models on `uploaded_images/`
├── test_classifier.py               # Test script for single image classification
└── pet_images/                      # (or uploaded_images/) directory of images
```

---

## ⚙️ Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/AI-Dog-Recognition-Project.git
   cd AI-Dog-Recognition-Project
   ```

2. Install dependencies:  
   ```bash
   pip install torch torchvision pillow
   ```

---

## 🚀 Usage  

### Run on your own dataset (default: `pet_images/`)  

```bash
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

**Arguments:**  
- `--dir` : Path to images directory (default: `pet_images/`)  
- `--arch` : CNN model architecture (`resnet`, `alexnet`, `vgg`)  
- `--dogfile` : File containing valid dog breed names (default: `dognames.txt`)  

---

### Batch Run (all 3 models)  

On `pet_images/`:  
```bash
sh run_models_batch.sh
```

On `uploaded_images/`:  
```bash
sh run_models_batch_uploaded.sh
```

Each run generates result text files (`resnet_pet-images.txt`, etc.).

---

### Test Classifier on One Image  

```bash
python test_classifier.py
```

This runs classification on a sample image and prints the predicted label.

---

## 📊 Output Example  

For each model, you’ll get:  
- Number of total images, dog images, not-dog images  
- % correctly classified dogs, breeds, and not-dogs  
- Optionally: list of misclassified dogs/breeds  

