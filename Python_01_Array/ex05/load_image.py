import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt


def ft_load(path: str) -> np.ndarray:
    """
        Load an image from the specified file path into a NumPy array.

        Args:
            path (str): The file path to the image to be loaded.

        Returns:
            np.array: A NumPy array representing the loaded image pixels.
            If the loading fails an empty NumPy array is returned.

        Raises:
            TypeError: If the provided path is not a string.
    """
    try:
        if not isinstance(path, str):
            raise TypeError('the path is not a string.')
        img = mpimg.imread(path)
        img_shape = img.shape
        print(f'The shape of image is: {img_shape}')

        plt.subplot(3, 2, 1)
        plt.imshow(img)
        plt.xlabel('Figure 1: Original')

        return img
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')
        return np.array([])
