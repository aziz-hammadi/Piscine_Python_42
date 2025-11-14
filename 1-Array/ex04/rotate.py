import numpy as np
from PIL import Image
from load_image import load_and_crop_image


def manual_transpose(arr):
    """
    Manually transposes a 2D numpy array.
    Args:
        arr (np.ndarray): 2D array to transpose.
    Returns:
        np.ndarray: Transposed array.
    """
    rows, cols = arr.shape
    transposed = np.zeros((cols, rows), dtype=arr.dtype)
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = arr[i][j]
    return transposed


def display_image(arr):
    """
    Displays a numpy array as an image.
    Args:
        arr (np.ndarray): Array to display.
    """
    img = Image.fromarray(arr)
    img.show()


def main():
    try:
        arr = load_and_crop_image("animal.jpeg", 400)
        print("The shape of image is:", arr.shape)
        print(arr)
        arr_t = manual_transpose(arr)
        print("New shape after Transpose:", arr_t.shape)
        print(arr_t)
        display_image(arr_t)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
