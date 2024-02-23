import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Qt5Agg")


def ft_blue(array):
    """
    Description:
        Function to display the blue channel of the image.
    Args:
        array: Image array.
    """
    final_arr = np.zeros((array.shape), dtype=np.uint8)
    final_arr[:, :, 2] = array[:, :, 2]
    plt.imshow(final_arr)
    plt.show()


def ft_green(array):
    """
    Description:
        Function to display the green channel of the image.
    Args:
        array: Image array.
    """
    final_arr = np.zeros((array.shape), dtype=np.uint8)
    final_arr[:, :, 1] = array[:, :, 1]
    plt.imshow(final_arr)
    plt.show()


def ft_red(array):
    """
    Description:
        Function to display the red channel of the image.
    Args:
        array: Image array.
    """
    final_arr = np.zeros((array.shape), dtype=np.uint8)
    final_arr[:, :, 0] = array[:, :, 0]
    plt.imshow(final_arr)
    plt.show()


def ft_grey(array):
    """
    Description:
        Function to display the grayscale version of the image.
    Args:
        array: Image array.
    """
    final_arr = np.zeros((array.shape), dtype=np.uint8)
    final_arr[:, :, 0] = np.mean(array, axis=2)
    final_arr[:, :, 1] = np.mean(array, axis=2)
    final_arr[:, :, 2] = np.mean(array, axis=2)
    plt.imshow(final_arr)
    plt.show()


def ft_invert(array):
    """
    Description:
        Function to display the inverted version of the image.
    Args:
        array: Image array.
    """
    final_arr = np.zeros((array.shape), dtype=np.uint8)
    final_arr[:, :, 0] = 255 - array[:, :, 0]
    final_arr[:, :, 1] = 255 - array[:, :, 1]
    final_arr[:, :, 2] = 255 - array[:, :, 2]
    plt.imshow(final_arr)
    plt.show()


def main():
    return 0


if __name__ == "__main__":
    main()
