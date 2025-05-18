import cv2
import numpy as np
import os

# Load image
def load_image(path):
    """
    Loads an image from the given path.

    Args:
        path (str): The path to the image file.

    Returns:
        numpy.ndarray: The loaded image as a NumPy array.

    Raises:
        ValueError: If the image cannot be loaded.
    """
    image = cv2.imread(path)
    if image is None:
        raise ValueError("Could not load image. Check the path.")
    return image

# Analyze brightness and color saturation
def analyze_image(image):
    """
    Analyzes the brightness and average color saturation of an image.

    Args:
        image (numpy.ndarray): The input image.

    Returns:
        tuple: A tuple containing the average brightness and average saturation.
               Brightness is the mean of the grayscale image, and saturation is the
               mean of the saturation channel in the HSV representation.
    """
    image = cv2.resize(image, (200, 200))  # Resize for faster processing
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    brightness = np.mean(gray)  # Calculate average brightness

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # Convert to HSV color space
    saturation = hsv[..., 1]  # Extract the saturation channel
    avg_saturation = np.mean(saturation)  # Calculate average saturation

    return brightness, avg_saturation

# Assign conveyor belt
def assign_conveyor(brightness, saturation):
    """
    Assigns a conveyor belt based on the image's brightness and saturation.

    Args:
        brightness (float): The average brightness of the image.
        saturation (float): The average saturation of the image.

    Returns:
        str: The assigned conveyor belt ("A", "B", or "C") with a descriptive string.
    """
    if brightness > 180 and saturation < 30:
        return "Transparent → Conveyor B"  # High brightness, low saturation: Transparent
    elif brightness < 80 and saturation < 50:
        return "Black → Conveyor A"  # Low brightness, low-mid saturation: Black
    else:
        return "Colorful → Conveyor C"  # Mid-High saturation: Colorful

# Main classification function
def classify_image(path):
    """
    Classifies an image and assigns it to a conveyor belt.

    Args:
        path (str): The path to the image file.
    """
    image = load_image(path)  # Load the image
    brightness, saturation = analyze_image(image)  # Analyze brightness and saturation
    result = assign_conveyor(brightness, saturation)  # Assign conveyor belt

    print(f"Result: {result}")  # Print the result
    print(f"Brightness: {brightness:.2f}, Saturation: {saturation:.2f}")  # Print analysis values

    cv2.imshow("Input Image", image)  # Display the image
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close all windows


if __name__ == "__main__":
    #  Run the classifier on all images in the test_images folder
    test_images_dir = "test_images"  # Directory containing test images
    if os.path.exists(test_images_dir) and os.path.isdir(test_images_dir):
        for filename in os.listdir(test_images_dir):
            image_path = os.path.join(test_images_dir, filename)
            if os.path.isfile(image_path) and image_path.lower().endswith(('.png', '.jpg', '.jpeg')): # Check if it's a file and an image
                print(f"\nProcessing image: {image_path}")
                classify_image(image_path)
    else:
        print(f"Error: Directory '{test_images_dir}' not found or is not a directory.")
