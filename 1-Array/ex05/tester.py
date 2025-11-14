
import matplotlib.pyplot as plt
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

array = ft_load("landscape.jpg")
if array is not None:
	print(f"The shape of image is: {array.shape}")
	print(array.reshape(1, array.shape[0] * array.shape[1], array.shape[2]))
	print()

	filters = [
		(ft_invert, "Inverted"),
		(ft_red, "Red filter"),
		(ft_green, "Green filter"),
		(ft_blue, "Blue filter"),
		(ft_grey, "Grey filter")
	]
	for func, title in filters:
		img = func(array)
		plt.imshow(img)
		plt.title(title)
		plt.axis('off')
		plt.show()

	print(ft_invert.__doc__)
else:
	print("Image not loaded.")