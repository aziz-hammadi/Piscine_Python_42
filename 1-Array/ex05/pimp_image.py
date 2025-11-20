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

def ft_grey(array, correction_index: int = 0) -> array:
    rgb_as_gimp = [1 / 0.3, 1 /0.59, 1 / 0.11]
    rgb_as_gimp2= [1 / .2127, 1/0.6780, 1/0.0593]
    rgb_CIE_1931  = [1/0.299,1/0.587,1/ 0.114]
    rgb_ITU_R_BT_2100 = [1 / .2127, 1/0.6780, 1/0.0593]
    rgb_ITU_R_BT_709 = [1 / .2126, 1/0.7152, 1/0.0722]
    rgb_custom= [1 / .5000, 1/0.80, 1/0.001]

    match correction_index:
        case 0:
            correction = rgb_as_gimp
        case 1:
            correction = rgb_as_gimp2
        case 2:
            correction = rgb_CIE_1931
        case 3:
            correction = rgb_ITU_R_BT_2100
        case 4:
            correction = rgb_ITU_R_BT_709
        case 5:
            correction = rgb_custom
        case _:
            correction = [1,1,1]


  
    rgb = array.copy()

    r = rgb[:,:,0:1] 
    g = rgb[:,:,1:2] 
    b = rgb[:,:,2:3]

 
    r[:,:,:]= r / correction[0]
    g[:,:,:]= g / correction[1]
    b[:,:,:]= b / correction[2]

    r[:,:,:]= np.where(r > g, r, g)
    r[:,:,:]= np.where(r > b, r, b)

    b[:,:,:]= np.where(b > r, b, r)
    b[:,:,:]= np.where(b > g, b, g)

    g[:,:,:]= np.where(g > r, g, r)
    g[:,:,:]= np.where(g > b, g, b)
    _collect_and_show(rgb, "Figure VIII.5:Grey")
    return  rgb