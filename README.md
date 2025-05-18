# Kursi Object Sorter

Overview

This project implements a rule-based system using Python and OpenCV to classify objects (black, transparent, or colorful) in images and assign them to specific conveyor belts (A, B, or C) for recycling at Kursi's facility.

Requirements

* Python 3.x
* OpenCV (`cv2`)
* NumPy

Installation

1.  **Install Python:** If you don't have Python installed, download it from (https://www.python.org/downloads/).
2.  **Install Libraries:** Open your terminal or command prompt and install the necessary libraries using pip:

    bash
    pip install opencv-python numpy
    

Dataset

The dataset for this project consists of a collection of images for each category of plastic object: black, transparent, and colorful. The images are organized within the `test_images/` folder.

* `test_images`: Contains images of black, transparent and colorful objects or sceneries.

Usage

1.  Clone the Repository: If you haven't already, clone this repository to your local machine:

    ```bash
    git clone <your_repository_url>
    cd Kursi-Plastic-Sorter  # Or whatever you named your repository
    ```

2.  Place Images: Ensure your image files are organized into the `test_images' folder

3.  Run the Script: Execute the `classify.py` script from the command line:

    bash
    python classify.py
   

    The script will process each image in the `test_images/` folder and print the classification result (assigned conveyor belt, brightness, and saturation) for each image. It will also display each image in a separate window. Press any key in the image window to close it and move to the next image.

Code Description

The `classify.py` script contains the following main functions:

 `load_image(path)`: Loads an image from the specified file path.
 `analyze_image(image)`: Takes an image as input, resizes it, converts it to grayscale to calculate average brightness, and converts it to HSV to calculate average saturation. It returns the calculated brightness and saturation values.
 `assign_conveyor(brightness, saturation)`: Takes the brightness and saturation values as input and applies a set of rules to determine the appropriate conveyor belt:
    * If brightness is high and saturation is low, the object is classified as transparent and assigned to Conveyor B.
    * If brightness is low and saturation is relatively low, the object is classified as black and assigned to Conveyor A.
    * Otherwise, the object is classified as colorful and assigned to Conveyor C.
 `classify_image(path)`: Loads an image, analyzes its brightness and saturation, assigns a conveyor belt based on the analysis, prints the results, and displays the image.
 The `if __name__ == "__main__":` block iterates through all image files within the `test_images` folder and its subfolders, calling `classify_image()` for each one.

File Structure

Kursi/
├── classify.py
└── test_images


Author
Muneeb Ansari and Ammar Beg
