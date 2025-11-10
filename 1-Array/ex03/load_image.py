import numpy as np
import numpy.typing as npt
from PIL import Image

def ft_load(path: str) -> npt.NDArray | None:
    """
    Cette fonction charge une image à partir du chemin donné,
    affiche son format (dimensions) et retourne les pixels en RGB.

    """
    try:
        with Image.open(path) as pil_img:
            img_format = pil_img.format
            print(f"Image format: {img_format}")
            if pil_img.mode != 'RGB':
                pil_img = pil_img.convert('RGB')
            img = np.array(pil_img)
            print(f"The shape of image is: {img.shape}")
            # Aperçu des pixels : 3 premières et 3 dernières lignes
            print(img[:3])
            print("...")
            print(img[-3:])
            return img
    except FileNotFoundError:
        print(f"Erreur : Le fichier {path} n'a pas été trouvé.")
        return None
    except Exception as e:
        print(f"Erreur : {e}")
        return None

