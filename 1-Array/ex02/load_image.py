import numpy as np

def ft_load(path: str) -> (np.ndarray | None):
    """
    Cette fonction charge une image à partir du chemin donné,
    affiche son format (dimensions) et retourne les pixels en RGB.

    :param path: chemin du fichier image (JPG ou JPEG).
    :return: un tableau NumPy des pixels de l'image au format RGB.
    :raises FileNotFoundError: si le fichier spécifié n'existe pas.
    :raises IOError: si le fichier n'est pas une image valide.
    """
    try:
        from PIL import Image
        # Charger l'image avec PIL pour obtenir le format
        with Image.open(path) as pil_img:
            img_format = pil_img.format
            print(f"Image format: {img_format}")
            img = np.array(pil_img)
            # Si l'image est en niveaux de gris, la convertir en RGB
            if len(img.shape) == 2:
                img = np.stack((img,)*3, axis=-1)
            elif img.shape[2] == 4:
                img = img[:, :, :3]
            # S'assurer que l'image est bien en RGB
            if pil_img.mode != 'RGB':
                pil_img = pil_img.convert('RGB')
                img = np.array(pil_img)

        print(f"The shape of image is: {img.shape}")
        # Afficher un aperçu des pixels (3 premières et 3 dernières lignes)
        preview = np.concatenate((img[:3], img[-3:]), axis=0)
        print(preview)
        return img
    except FileNotFoundError:
        print(f"Erreur : Le fichier {path} n'a pas été trouvé.")
        return
    except Exception as e:
        print(f"Erreur : {e}")
        return
