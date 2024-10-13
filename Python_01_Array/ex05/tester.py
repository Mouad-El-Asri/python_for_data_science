from load_image import ft_load
import pimp_image as pmp_img

array = ft_load('landscape.jpg')
pmp_img.ft_invert(array)
pmp_img.ft_red(array)
pmp_img.ft_green(array)
pmp_img.ft_blue(array)
pmp_img.ft_grey(array)

print(pmp_img.ft_invert.__doc__)
