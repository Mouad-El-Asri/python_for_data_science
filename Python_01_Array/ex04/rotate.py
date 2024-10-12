from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_rotate(img: np.ndarray) -> np.ndarray:
    rotated_img = np.rot90(img)
    print(f'New shape after Transpose: {rotated_img.shape[:2]}')
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
        grayscale_img = np.dot(rgb_img[:, :, :3],
                               [[0.2989], [0.5870], [0.1140]]).astype(int)

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
