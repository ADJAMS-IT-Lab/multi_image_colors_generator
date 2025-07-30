# Background Color Tint Generator

Generate multiple color-tinted versions of an input image automatically using Python and Pillow.

---

## Features

- Creates 64 tinted images with different colors and intensities
- Supports output to a dedicated folder
- Saves original source image as prefix for all output images
- Easily customizable color tints and output folder

---

## Requirements

- Python 3.7+
- Pillow

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

------------
2. Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

------------
3. Install dependencies:

    pip install -r requirements.txt

------------
Usage

1.    Place your input images in the input_images/ folder.

2.    Run the script:

python adj_get_different_background.py

3.    Check your generated tinted images in the output_samples/ folder.



License

This project is licensed under the MIT License - see the LICENSE file for details.


---

### 4. **requirements.txt**

Your project depends on Pillow only, so create `requirements.txt`:

Pillow>=9.0.0


---

### 5. **Adjust Your Script**

Update your script to use **input_images/** as the source folder and **output_samples/** as the output folder:

```python
import os
from PIL import Image, ImageEnhance, ImageOps

# === Setup Paths ===
script_dir = os.path.dirname(os.path.abspath(__file__))

input_dir = os.path.join(script_dir, "input_images")
output_dir = os.path.join(script_dir, "output_samples")

os.makedirs(output_dir, exist_ok=True)

# Pick your source image (make sure it exists in input_images)
image_filename = "example.jpg"
image_path = os.path.join(input_dir, image_filename)

try:
    original = Image.open(image_path).convert("RGB")
except FileNotFoundError:
    print(f"Image file not found: {image_path}")
    exit(1)

# (Your tint functions and processing below...)

# Save original copy to output folder with prefix
original.save(os.path.join(output_dir, f"{os.path.splitext(image_filename)[0]}_original.png"))

# Continue generating tinted images with naming pattern
# ...

6. Add Sample Input and Output

    Place at least one sample input image in input_images/ (e.g. example.jpg)

    Run the script to generate outputs in output_samples/

    Commit those outputs for demonstration on GitHub

7. Git Ignore

Create a .gitignore if you want to ignore any files/folders (like virtual environments):

venv/
__pycache__/
*.pyc