import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray as array


def on_key(event):
    plt.close(event.canvas.figure)


def _collect_and_show(img, name, original=None):
    # Fonction pour stocker les images
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
        for i, (im, title) in enumerate(
            zip(_collect_and_show.images, _collect_and_show.titles)
        ):
            ax = axes[i // 2, i % 2]
            ax.imshow(im)
            ax.set_title(title, y=-0.15, fontsize=18)
            ax.axis("off")
        fig.canvas.manager.set_window_title("Pimped Images")
        plt.tight_layout()
        fig.canvas.mpl_connect("key_press_event", on_key)
        plt.show()
        # Réinitialiser la liste qui stocke les images
        _collect_and_show.images.clear()
        _collect_and_show.titles.clear()
        _collect_and_show.original_added = False
        print(ft_invert.__doc__)
        print(ft_red.__doc__)
        print(ft_green.__doc__)
        print(ft_blue.__doc__)
        print(ft_grey.__doc__)

def ft_invert(array) -> array:
    """Inverts the color of the image received"""
    if array is not None:
        res = 255 - array
        _collect_and_show(res, "Figure VIII.2: Invert", original=array)
        return res


def ft_red(array) -> array:
    """Keep only the red channel, set green and blue to 0"""
    if array is not None:
        result = array.copy()
        result[..., 1] = 0
        result[..., 2] = 0
        _collect_and_show(result, "Figure VIII.3: Red")
        return result


def ft_green(array) -> array:
    """Keep only the green channel, set red and blue to 0"""
    if array is not None:
        result = array.copy()
        result[..., 0] = 0
        result[..., 2] = 0
        _collect_and_show(result, "Figure VIII.4: Green")
        return result


def ft_blue(array) -> array:
    """Keep only the blue channel, set red and green to 0"""
    if array is not None:
        result = array.copy()
        result[..., 0] = 0
        result[..., 1] = 0
        _collect_and_show(result, "Figure VIII.5: Blue")
        return result


def ft_grey(array, correction_index: int = 0) -> array:
    """Convert image to greyscale with correction factor"""
    correction = [1 / 0.5000, 1 / 0.80, 1 / 0.001]

    rgb = array.copy()

    r = rgb[:, :, 0:1]
    g = rgb[:, :, 1:2]
    b = rgb[:, :, 2:3]

    r[:, :, :] = r / correction[0]
    g[:, :, :] = g / correction[1]
    b[:, :, :] = b / correction[2]

    r[:, :, :] = np.where(r > g, r, g)
    r[:, :, :] = np.where(r > b, r, b)

    b[:, :, :] = np.where(b > r, b, r)
    b[:, :, :] = np.where(b > g, b, g)

    g[:, :, :] = np.where(g > r, g, r)
    g[:, :, :] = np.where(g > b, g, b)
    _collect_and_show(rgb, "Figure VIII.5:Grey")
    return rgb
