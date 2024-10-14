from load_image import ft_load
import pimp_image as pmp_img
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))

array = ft_load('landscape.jpg')
pmp_img.ft_invert(array)
pmp_img.ft_red(array)
pmp_img.ft_green(array)
pmp_img.ft_blue(array)
pmp_img.ft_grey(array)

print(array)

print(pmp_img.ft_invert.__doc__)

plt.tight_layout()
plt.show()
