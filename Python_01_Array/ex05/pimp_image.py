import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
        Inverts the color of the image received.

        Args:
            array (np.ndarray): A 3D NumPy array representing an image.

        Returns:
            np.ndarray: A 3D NumPy array,
            representing the color-inverted image.
    """
    invert_img = array.copy()
    invert_img[:, :, :3] = 255 - invert_img[:, :, :3]

    plt.subplot(3, 2, 2)
    plt.imshow(invert_img)
    plt.xlabel('Figure 2: Invert')

    return invert_img


def ft_red(array: np.ndarray) -> np.ndarray:
    """
        Retains only the red channel of the input image.

        Args:
            array (np.ndarray): A 3D NumPy array representing an image.

        Returns:
            np.ndarray: A 3D NumPy array, with only the red
            channel retained and green and blue channels set to zero.
    """
    red_img = array.copy()
    red_img[:, :, 1:] *= 0

    plt.subplot(3, 2, 3)
    plt.imshow(red_img)
    plt.xlabel('Figure 3: Red')

    return red_img


def ft_green(array: np.ndarray) -> np.ndarray:
    """
        Retains only the green channel of the input image.

        Args:
            array (np.ndarray): A 3D NumPy array representing an image.

        Returns:
            np.ndarray: A 3D NumPy array, with only the green
            channel retained and red and blue channels set to zero.
    """
    green_img = array.copy()
    green_img[:, :, 0] -= green_img[:, :, 0]
    green_img[:, :, 2] -= green_img[:, :, 2]

    plt.subplot(3, 2, 4)
    plt.imshow(green_img)
    plt.xlabel('Figure 4: Green')

    return green_img


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
        Retains only the blue channel of the input image.

        Args:
            array (np.ndarray): A 3D NumPy array representing an image.

        Returns:
            np.ndarray: A 3D NumPy array, with only the blue
            channel retained and red and green channels set to zero.
    """
    blue_img = array.copy()
    blue_img[:, :, :2] = 0

    plt.subplot(3, 2, 5)
    plt.imshow(blue_img)
    plt.xlabel('Figure 5: Blue')

    return blue_img


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
        Converts the input image to grayscale.

        Args:
            array (np.ndarray): A 3D NumPy array representing an image.

        Returns:
            np.ndarray: A 3D NumPy array, where each pixel
            is represented by its grayscale value.
    """
    grayscale_img = np.array([[int(sum(el[:3]) / 3) for el in row]
                              for row in array.tolist()])

    plt.subplot(3, 2, 6)
    plt.imshow(grayscale_img, cmap='gray')
    plt.xlabel('Figure 6: Grey')

    return grayscale_img
