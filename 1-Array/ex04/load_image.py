from PIL import Image
import numpy as np

def load_and_crop_image(path, size):
    """
    Loads an image, converts it to grayscale, and crops a square of given size.
    Args:
        path (str): Path to the image file.
        size (int): Size of the square to crop.
    Returns:
        np.ndarray: Cropped grayscale image as a numpy array.
    Raises:
        FileNotFoundError: If the image file does not exist.
        ValueError: If the size is invalid.
    """
    img = Image.open(path).convert('L')
    width, height = img.size
    if size > width or size > height:
        raise ValueError("Crop size is larger than image dimensions.")
    left = (width - size) // 2
    top = (height - size) // 2
    img_cropped = img.crop((left, top, left + size, top + size))
    arr = np.array(img_cropped)
    return arr

def main():
    try:
        arr = load_and_crop_image("animal.jpeg", 400)
        print("The shape of image is:", arr.shape)
        print(arr)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
