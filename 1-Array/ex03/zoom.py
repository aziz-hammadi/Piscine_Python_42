# zoom.py

import sys
import numpy as np
from matplotlib import pyplot as plt
from load_image import ft_load


def zoom_image(image: np.ndarray, zoom_area: tuple) -> np.ndarray:
    """
    Zoom on a specific area of the image and convert it to grayscale.

    Args:
        image (np.ndarray): The image as a NumPy array.
        zoom_area (tuple): The area to zoom (start_x, start_y, end_x, end_y).

    Returns:
        np.ndarray: The zoomed and grayscale image.

    Raises:
        ValueError: If the zoom area is invalid.
    """
    try:
        start_x, start_y, end_x, end_y = zoom_area

        # Vérifier que la zone de zoom est valide
        if (
            start_x < 0
            or start_y < 0
            or end_x > image.shape[1]
            or end_y > image.shape[0]
            or start_x >= end_x
            or start_y >= end_y
        ):
            raise ValueError("Invalid zoom area.")

        # Zoom sur la zone spécifiée
        zoomed_image = image[start_y:end_y, start_x:end_x]

        # Convertir l'image zoomée en niveaux de gris (1 canal)
        zoomed_gray = np.mean(zoomed_image, axis=2, keepdims=True).astype(
            np.uint8
        )

        # Afficher la nouvelle forme de l'image
        or_shape = (zoomed_image.shape[0], zoomed_gray.shape[1])
        print(f"New shape after slicing: {zoomed_gray.shape} or {or_shape}")
        print(zoomed_gray)

        return zoomed_gray
        # return zoomed_image
    except Exception as e:
        sys.tracebacklimit = 0
        raise ValueError(f"ValueError: {e}")


def display_image(image: np.ndarray, title: str):
    """
    Display the image with a title.

    Args:
        image (np.ndarray): The image to display.
        title (str): The title of the image.
    """
    plt.imshow(image, cmap="gray")  # Afficher en niveaux de gris
    plt.title(title)
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.show()


def main():
    """
    Main function to load the image, zoom on a specific area, and display it.
    """
    try:
        # Charger l'image
        image = ft_load("animal.jpeg")

        # Définir la zone à zoomer (par exemple, un carré au centre de l'image)
        height, width, _ = image.shape
        start_x = width // 4
        start_y = height // 4
        end_x = start_x + 400
        end_y = start_y + 400
        zoom_area = (start_x, start_y, end_x, end_y)

        # Effectuer le zoom
        zoomed_image = zoom_image(image, zoom_area)

        # Afficher l'image zoomée
        display_image(zoomed_image, "Zoomed Image")
    except Exception as e:
        sys.tracebacklimit = 0
        print(f"Error: {e}")


if __name__ == "__main__":
    main()