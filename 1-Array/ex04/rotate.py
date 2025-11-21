import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from load_image import ft_load


def custom_print_array(arr: np.ndarray) -> str:
    """3 premières et 3 dernières valeurs"""
    np.set_printoptions(threshold=3)
    string = f"[{arr[0].__str__()}\n  ... \n {arr[-1].__str__()}]"
    return string


def zoom_image(image: np.ndarray, start_x=100,
               start_y=450, x=400, y=400) -> np.ndarray:
    """
    Effectue un zoom sur une zone spécifique de l'image
    et la convertit en niveaux de gris.

    Args:
        image (np.ndarray): L'image sous forme de tableau NumPy.
        start_x (int): Coordonnée x de départ pour le zoom.
        start_y (int): Coordonnée y de départ pour le zoom.
        x (int): Largeur de la zone à zoomer.
        y (int): Hauteur de la zone à zoomer.

    Returns:
        np.ndarray: L'image zoomée et en niveaux de gris.

    Raises:
        ValueError: Si la zone de zoom est invalide.
    """
    try:
        # Vérifier que la zone de zoom est valide
        if (
            start_x < 0
            or start_y < 0
            or x <= 0
            or y <= 0
            or start_x + x > image.shape[0]
            or start_y + y > image.shape[1]
        ):
            raise ValueError("Zone de zoom invalide.")
        end_x = start_x + x
        end_y = start_y + y
        # Zoom sur la zone spécifiée
        zoomed_image = image[start_x:end_x, start_y:end_y]

        # Afficher la nouvelle forme de l'image
        or_shape = zoomed_image.reshape(zoomed_image.shape[0],
                                        zoomed_image.shape[1], 1)
        print(f"The shape of image is:{or_shape.shape} or{zoomed_image.shape}")
        print(zoomed_image.reshape(1, zoomed_image.shape[0]
                                   * zoomed_image.shape[1], 1))

        # Application de la Transposition avec array.T
        zoomed_image = zoomed_image.T
        print(f"New shape after Transpose: {zoomed_image.shape}")

        print(custom_print_array(zoomed_image))
        return zoomed_image
        # return zoomed_image
    except Exception as e:
        raise e


def display_image(image: np.ndarray, title: str):
    """
    Affiche l'image avec un titre.

    Args:
        image (np.ndarray): L'image à afficher.
        title (str): Le titre de l'image.
    """
    try:
        plt.imshow(image, cmap="gray", vmin=0, vmax=255)
        # Afficher en niveaux de gris
        # plt.title(title)
        # plt.xlabel("X axis")
        # plt.ylabel("Y axis")
        plt.show()
    except KeyboardInterrupt:
        plt.close("all")
    except Exception as e:
        raise e


def main():
    """
    Fonction principale pour charger l'image,
    zoomer sur une zone spécifique et l'afficher.
    """
    try:
        # Charger l'image
        image = ft_load("animal.jpeg")

        if image is None:
            raise ValueError("Failed to load image.")

        # Définir la zone à zoomer (par exemple, un carré au centre de l'image)
        height, width, _ = image.shape

        # Effectuer le zoom

        gray_array = np.array(Image.fromarray(image).convert("L"))

        zoomed_image = zoom_image(gray_array, 150, 450, 400, 400)
        # Afficher l'image zoomée
        display_image(zoomed_image, "Zoomed Image")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        plt.close("all")


if __name__ == "__main__":
    main()
