# NumPix
_An Interactive Image Manipulation Toolkit via NumPy_

**NumPix** is a Python-based command-line application designed for interactive image processing and manipulation using NumPy and PIL. Featuring a menu-driven interface, users can load images, apply transformations (flip, crop, blur, sharpen, etc.), and save results — all through educational, step-by-step implementations of core image processing techniques.

The primary purpose of **NumPix** is to provide a hands-on, educational toolkit for learning image manipulation with NumPy arrays. It serves as both a practical utility and a teaching tool for students, developers, and data scientists exploring computer vision fundamentals.

## FEATURES
✅ **Interactive CLI Menu** – Navigate transformations via numbered options with real-time feedback.  
✅ **NumPy-Powered Processing** – All operations use explicit NumPy array manipulation for clarity and learning.  
✅ **Educational Implementations** – Manual convolution, edge detection, normalization, and more — no black-box filters.  
✅ **Image I/O Support** – Load from local paths or URLs; save processed images and `.npy` matrices.  

## FUTURE IMPLEMENTATIONS
Advanced Filtering – Implement Gaussian blur, median filtering, and custom kernel support.  
Batch Processing – Support processing multiple images from a directory.  
Visualization Tools – Integrate matplotlib previews during operations.  
GUI Version – Build a simple Tkinter or web-based interface.  
Performance Mode – Add optimized versions using `scipy.ndimage` for comparison.

## UPDATES
Initial CLI with menu system and core transformations implemented.  
Manual convolution loops for blur/sharpen/edge detection (educational focus).  
Ongoing enhancements to error handling, input validation, and user experience.

## PROJECT DETAILS
Author: [Your Name/GitHub Handle]  
Started: November 2025  
Finished:  

## TECH STACK
Language: Python 3.8+  
Framework: Standard Library + External Libraries  
Libraries: NumPy, Pillow (PIL), custom UI modules (`clear_screen`, `display_format`, etc.)

## INSTALLATION
### Prerequisites
- Python 3.8 or higher
- `pip` package manager

### Install Dependencies
Clone the repository and install required packages:
```bash
git clone https://github.com/yourusername/numpix.git
cd numpix
pip install numpy pillow