import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray as array
def on_key(event):
    plt.close(event.canvas.figure)


def _collect_and_show(img, name, original=None):
    # Attributs fonction pour stocker le cycle sans global
    if not hasattr(_collect_and_show, "images"):
        _collect_and_show.images = []
        _collect_and_show.titles = []
        _collect_and_show.original_added = False
    # Ajoute l'original au début
    if not _collect_and_show.original_added and original is not None:
        _collect_and_show.images.append(original)
        _collect_and_show.titles.append("Figure VIII.1: Original")
        _collect_and_show.original_added = True
    _collect_and_show.images.append(img)
    _collect_and_show.titles.append(name)
    # Affiche quand on a 6 images
    if len(_collect_and_show.images) == 6:
        fig, axes = plt.subplots(3, 2, figsize=(14, 8))
        for i, (im, title) in enumerate(zip(_collect_and_show.images, _collect_and_show.titles)):
            ax = axes[i // 2, i % 2]
            ax.imshow(im)
            ax.set_title(title, y=-0.15, fontsize=18)
            ax.axis("off")
        fig.canvas.manager.set_window_title("Pimped Images")
        plt.tight_layout()
        fig.canvas.mpl_connect('key_press_event', on_key)
        plt.show()
        # Réinitialiser pour un nouveau cycle éventuel
        _collect_and_show.images.clear()
        _collect_and_show.titles.clear()
        _collect_and_show.original_added = False

def ft_invert(array) -> array:
    if array is not None:
        res = 255 - array
        _collect_and_show(res, "Figure VIII.2: Invert", original=array)
        return res

def ft_red(array) -> array:
    if array is not None:
        result = array.copy()
        result[..., 1] = 0
        result[..., 2] = 0
        _collect_and_show(result, "Figure VIII.3: Red")
        return result

def ft_green(array) -> array:
    if array is not None:
        result = array.copy()
        result[..., 0] = 0
        result[..., 2] = 0
        _collect_and_show(result, "Figure VIII.4: Green")
        return result

def ft_blue(array) -> array:
    if array is not None:
        result = array.copy()
        result[..., 0] = 0
        result[..., 1] = 0
        _collect_and_show(result, "Figure VIII.5: Blue")
        return result

def ft_grey(array) -> array:
    if array is not None:
        # Calcul de la moyenne sur les 3 canaux (axe 2) avec np.mean (addition interne)
        grey_array = np.mean(array, axis=2).astype(np.uint8)
        
        # Création d'une image en niveaux de gris en dupliquant le canal unique sur 3 canaux
        grey_image = np.zeros_like(array)
        grey_image[:, :, 0] = grey_array
        grey_image[:, :, 1] = grey_array
        grey_image[:, :, 2] = grey_array
        
        # Affichage automatique des résultats avec fonction utilitaire interne
        _collect_and_show(grey_image, "Figure VIII.5: Gray")
        
        return grey_image
