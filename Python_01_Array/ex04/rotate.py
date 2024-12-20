from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_rotate(img: np.ndarray) -> np.ndarray:
    """
        Rotate an image 90 degrees.

        Args:
            img (np.ndarray): Input image as a 3D array.

        Returns:
            np.ndarray: Rotated grayscale image as a 2D array (width, height).
    """
    height, width, channels = img.shape
    grayscale_img = img.reshape(height, width)

    rotated_img = [[0] * height for el in range(width)]

    for i in range(height):
        for j in range(width):
            rotated_img[width - 1 - j][i] = grayscale_img[i][j]

    rotated_img = np.array(rotated_img)
    print(f'New shape after Transpose: {rotated_img.shape}')
    return rotated_img


def ft_zoom(rgb_img: np.ndarray) -> np.ndarray:
    """
        Convert an RGB image to grayscale and zoom in on a region.

        Args:
            rgb_img (np.ndarray): A numpy 3D array representing the RGB image.

        Returns:
            np.ndarray: A numpy 3D array of the zoomed grayscale image.
    """
    if len(rgb_img.shape) != 2 and rgb_img.shape[2] != 1:
        grayscale_img = np.array([[[sum(int(el / 3) for el in col)]
                                   for col in row] for row in rgb_img])

    y_min, y_max, x_min, x_max = 100, 500, 450, 850
    zoomed_img = grayscale_img[y_min:y_max, x_min:x_max]

    zoomed_img_shape = zoomed_img.shape

    print(f'The shape of image is: {zoomed_img_shape} '
          'or {zoomed_img_shape[:2]}')

    return zoomed_img


def display_img(img: np.ndarray) -> None:
    """
        Display an image.

        Args:
            img (np.ndarray): A numpy 3D array representing the image.

        Returns:
            None: This function displays the image without returning a value.
    """
    plt.imshow(img, cmap='gray')
    plt.show()


def main():
    img_path = 'animal.jpeg'

    original_img = ft_load(img_path)
    zoomed_img = ft_zoom(original_img)
    print(zoomed_img)

    rotated_img = ft_rotate(zoomed_img)
    print(rotated_img)

    display_img(rotated_img)


if __name__ == '__main__':
    main()
