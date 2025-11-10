import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def zoom_image(img: np.ndarray) -> np.ndarray:
    """
    Effectue un zoom sur la zone centrale de l'image (slicing).
    :param img: tableau NumPy de l'image.
    :return: tableau NumPy de la zone zoomée.
    """
    # Slicing central (exemple : 400x400 pixels, canal 1)
    h, w = img.shape[0], img.shape[1]
    start_x = w // 2 - 200
    start_y = h // 2 - 200
    zoom = img[start_y:start_y+400, start_x:start_x+400, 0:1]
    print(f"New shape after slicing: {zoom.shape}")
    print(zoom)
    return zoom

def display_image(img: np.ndarray, title: str = "Image"):
    """
    Affiche l'image avec les axes x et y.
    :param img: tableau NumPy de l'image.
    :param title: titre de la fenêtre.
    """
    plt.imshow(img.squeeze(), cmap='gray' if img.shape[-1] == 1 else None)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.colorbar()
    plt.show()

def main():
    """
    Fonction principale pour charger, zoomer et afficher l'image.
    """
    try:
        img = ft_load("animal.jpeg")
        if img is None:
            return
        print(f"Taille de l'image : {img.shape}")
        print(f"Nombre de canaux : {img.shape[2] if img.ndim == 3 else 1}")
        print("Contenu des pixels :")
        print(img[:3])
        print("...")
        print(img[-3:])
        zoom = zoom_image(img)
        print(f"New shape after slicing: {zoom.shape}")
        print(zoom[:3])
        print("...")
        print(zoom[-3:])
        display_image(zoom, title="Zoomed Image")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

if __name__ == "__main__":
    main()
