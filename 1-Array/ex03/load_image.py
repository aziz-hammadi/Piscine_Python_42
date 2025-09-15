import numpy as np
from PIL import Image

def ft_load(path: str) -> np.ndarray:
    """
    Charge une image à partir du chemin donné, affiche ses dimensions, le nombre de canaux et les pixels.
    :param path: chemin du fichier image (JPG ou JPEG).
    :return: un tableau NumPy des pixels de l'image au format RGB.
    """
    try:
        with Image.open(path) as pil_img:
            img_format = pil_img.format
            img = np.array(pil_img)
            print(f"the shape of image is: {img.shape}")
            print(img)
            return img
    except FileNotFoundError:
        print(f"Erreur : Le fichier {path} n'a pas été trouvé.")
        return None
    except Exception as e:
        print(f"Erreur : {e}")
        return None
