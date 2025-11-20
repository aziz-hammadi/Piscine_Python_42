import numpy as np
import numpy.typing as npt
from PIL import Image


def ft_load(path: str) -> npt.NDArray | None:
    """
    Charge une image à partir du chemin donné,
    affiche son format et dimensions, puis retourne un array RGB.
    """
    try:
        with Image.open(path) as pil_img:
            img_format = pil_img.format
            print(f"Image format: {img_format}")
            if pil_img.mode != "RGB":
                pil_img = pil_img.convert("RGB")
            img = np.array(pil_img).copy()
            print(f"The shape of image is: {img.shape}")
            print(img.reshape(1, img.shape[0] * img.shape[1], img.shape[2]))
            # _collect_and_show(img, "Original")
            return img
    except FileNotFoundError:
        print(f"Erreur : Le fichier {path} n'a pas été trouvé.")
    except Exception as e:
        print(f"Erreur : {e}")
    return None
