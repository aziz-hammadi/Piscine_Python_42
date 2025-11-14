import matplotlib.pyplot as plt
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


def main():
    array = ft_load("landscape.jpg")
    if array is not None:
        print(f"The shape of image is: {array.shape}")
        print(array.reshape(1, array.shape[0]
                            * array.shape[1], array.shape[2]))
        print()

        imgs = [
            array,
            ft_invert(array),
            ft_red(array),
            ft_green(array),
            ft_blue(array),
            ft_grey(array),
        ]
        titles = ["Original", "Inverted", "Red", "Green", "Blue", "Grey"]
        fig, axes = plt.subplots(3, 2, figsize=(12, 8))
        for i, ax in enumerate(axes.flat):
            ax.imshow(imgs[i])
            ax.set_title(f"Figure VIII.{i+1}: {titles[i]}",
                         y=-0.25, fontsize=18)
            ax.axis("off")
        if fig.canvas.manager is not None:
            fig.canvas.manager.set_window_title("Pimped Images")
            plt.tight_layout()
            plt.show()

        print(ft_invert.__doc__)
        print(ft_red.__doc__)
        print(ft_green.__doc__)
    else:
        print("Image not loaded.")


if __name__ == "__main__":
    main()
