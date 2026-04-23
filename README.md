# Background_Eraser
A high-performance image processing utility for automated color-keying and background transparency. Leverages NumPy-based masking to identify and remove specific hex-color ranges from images, outputting professionally rendered RGBA files.

This script provides a clean, efficient solution for automated color keying—similar to a "green screen" effect—but for static images. It demonstrates your ability to use **NumPy** for high-performance matrix operations and **Pillow** for image manipulation.

### 📝 Project Description

For your GitHub **About** section:
> A high-precision image processing utility for automated color-keying and background transparency. Leverages NumPy-based masking to identify and remove specific hex-color ranges from images, outputting professionally rendered RGBA files.

# 🖼️ Chroma Key Image Processor

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.20+-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Pillow](https://img.shields.io/badge/Pillow-Latest-C1111D?logo=pythonist)](https://python-pillow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Chroma Key Image Processor** is a lightweight, high-performance Python utility designed to automate the removal of specific background colors from static images. By utilizing matrix-based masking rather than iterative loops, it ensures rapid processing even for high-resolution assets.

---

## ✨ Key Features

* **Targeted Color Removal:** Specifically tuned to identify and isolate custom hex codes (Default: `#29731d`).
* **Intelligent Masking:** Employs NumPy array slicing to evaluate the R, G, and B channels simultaneously for maximum accuracy.
* **Adjustable Tolerance:** Includes a configurable tolerance threshold to handle lighting variances and anti-aliased edges.
* **Alpha Channel Integration:** Converts target pixels to full transparency (`Alpha = 0`) while preserving the integrity of the foreground.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.8+
* An input image (Default expects `HA.png` in the root directory).

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Arjunren/Background_Eraser.git
   cd Background_Eraser
   ```

2. **Install dependencies:**
   ```bash
   pip install Pillow numpy
   ```

3. **Run the script:**
   ```bash
   python app.py
   ```

---

## ⚙️ Configuration

You can customize the color keying behavior directly within the source code:

| Parameter | Purpose | Location |
| :--- | :--- | :--- |
| `target_green` | The RGB values of the color you wish to remove. | Step 3 |
| `tolerance` | Determines how "close" a color must be to the target to be removed. | Step 3 |
| `image_path` | The filename of your source image. | Step 1 |

---

## 🧪 Technical Implementation

The script follows a 6-step professional image processing workflow:
1. **Normalization:** Converts the input image to a 4-channel `RGBA` format to ensure transparency support.
2. **Vectorization:** Transforms the image into a 3D NumPy array for efficient mathematical operations.
3. **Difference Calculation:** Computes the absolute difference between every pixel and the `target_green` array.
4. **Logical Masking:** Generates a boolean mask where the pixel differences fall within the `tolerance` range.
5. **Transparency Injection:** Sets the alpha channel of all masked pixels to `0`.
6. **Reconstruction:** Rebuilds the image from the modified array and exports the final `.png`.

### 💡 Pro-Tip for this script:
Currently, your `target_green` is hardcoded as `[41, 115, 29]`. To make this even more "PRO," you could add a small function to convert a **Hex Code** (like `#29731D`) to an **RGB array** automatically. It’s a small addition that makes the script much easier for designers to use!
