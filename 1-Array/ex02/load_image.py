import numpy as np
import numpy.typing as npt
from PIL import Image

def ft_load(path: str) -> npt.NDArray | None:
    """
    Cette fonction charge une image à partir du chemin donné,
    affiche son format (dimensions) et retourne les pixels en RGB.

    """
    try:
        # Charger l'image avec PIL pour obtenir le format
        with Image.open(path) as pil_img:
            img_format = pil_img.format
            print(f"Image format: {img_format}")
            
            # Si l'image est en niveaux de gris, la convertir en RGB
            """if len(img.shape) == 2:
                img = np.stack((img,)*3, axis=-1)
            elif img.shape[2] == 4:
                img = img[:, :, :3]"""
            # S'assurer que l'image est bien en RGB
            if pil_img.mode != 'RGB':
                pil_img = pil_img.convert('RGB')
            img = np.array(pil_img)
            #print(img)

            print(f"The shape of image is: {img.shape}")
            # Afficher un aperçu des pixels (3 premières et 3 dernières lignes)
            #np.set_printoptions(threshold=3, edgeitems=2)
            ret = img.reshape(1, pil_img.size[0] * pil_img.size[1], 3)
            print(ret.shape)
            return ret
    
    except FileNotFoundError:
        print(f"Erreur : Le fichier {path} n'a pas été trouvé.")
        return
    except Exception as e:
        print(f"Erreur : {e}")
        return

