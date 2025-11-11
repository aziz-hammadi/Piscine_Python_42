# zoom.py


import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from load_image import ft_load


def zoom_image(image: np.ndarray,  start_x = 100, start_y = 450, x = 400, y = 400) -> np.ndarray:
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
        # Vérifier que la zone de zoom est valide
        if (
            start_x < 0
            or start_y < 0
            or x <= 0
            or y <= 0
            or start_x  + x > image.shape[0]
            or start_y  + y > image.shape[1]
        ):
            raise ValueError("Invalid zoom area.")
        end_x = start_x + x
        end_y = start_y + y
        # Zoom sur la zone spécifiée
        zoomed_image = image[start_x:end_x, start_y:end_y]
        zoomed_image = zoomed_image.reshape(zoomed_image.shape[0],zoomed_image.shape[1], 1)

        # Afficher la nouvelle forme de l'image
        or_shape = (zoomed_image.reshape(zoomed_image.shape[0], zoomed_image.shape[1]))
        print(f"New shape after slicing: {zoomed_image.shape} or {or_shape.shape}")
        print(zoomed_image.reshape(1, zoomed_image.shape[0] * zoomed_image.shape[1], 1))
        return zoomed_image
        # return zoomed_image
    except Exception as e:
        raise e


def display_image(image: np.ndarray, title: str):
    """
    Display the image with a title.

    Args:
        image (np.ndarray): The image to display.
        title (str): The title of the image.
    """
    try:
        plot = plt.imshow(image, cmap="gray", vmin=0, vmax=255)  # Afficher en niveaux de gris
        #plt.title(title)
        #plt.xlabel("X axis")
        #plt.ylabel("Y axis")
        plt.show()
    except KeyboardInterrupt:
        plt.close("all")
    except Exception as e:
        raise e


def main():
    """
    Main function to load the image, zoom on a specific area, and display it.
    """
    try:
        # Charger l'image
        image = ft_load("animal.jpeg")

        if image is None:
            raise ValueError("Failed to load image.")

        # Définir la zone à zoomer (par exemple, un carré au centre de l'image)
        height, width, _ = image.shape

        # Effectuer le zoom
        
        gray_array = np.array(Image.fromarray(image).convert('L'))
        
        zoomed_image = zoom_image(gray_array, 150, 450, 400, 400)
        # Afficher l'image zoomée
        plot = display_image(zoomed_image, "Zoomed Image")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        plt.close('all')




if __name__ == "__main__":
    main()