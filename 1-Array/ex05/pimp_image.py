import numpy as np


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received"""
    return 255 - array


def ft_red(array) -> np.ndarray:
    """Keep only the red channel, set green and blue to 0"""
    result = array.copy()
    result[..., 1] = 0
    result[:, :, 2] = 0
    return result


def ft_green(array) -> np.ndarray:
    """Keep only the green channel, set red and blue to 0"""
    result = array.copy()
    result[..., 0] = 0
    result[..., 2] = 0
    return result


def ft_blue(array) -> np.ndarray:
    """Keep only the blue channel, set red and green to 0"""
    result = array.copy()
    result[..., 0] = 0
    result[..., 1] = 0
    return result


def ft_grey(array) -> np.ndarray:
    """Convert image to greyscale (average of channels)"""
    grey = (array[..., 0] / 3 + array[..., 1] / 3 +
            array[..., 2] / 3).astype(np.uint8)
    result = np.stack((grey, grey, grey), axis=-1)
    return result.copy()
