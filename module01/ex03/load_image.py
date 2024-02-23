import numpy as np
import os
import matplotlib.image as mpimg
import PIL


def ft_load(path: str) -> np.array:
    """
    Description:
            - This function takes a path to an image and returns a 3D numpy
            array from the image.
    Args:
            - path: str
    Returns:
            - numpy.ndarray: 3D array
    """
    if not path.endswith((".jpg", '.jpeg')):
        print("Error: The file should be a jpg or jpeg.")
        return None
    if not os.path.exists(path):
        print("Error: The file does not exist.")
        return None
    try:
        img = np.array(mpimg.imread(path))
    except PIL.UnidentifiedImageError:
        print("Error: The file should be a valid image.")
        return None
    if len(img.shape) != 3:
        print("Error: The file should be a 3D array.")
        return None
    print(f"The shape of image is: {img.shape}")
    return img


def main():
    return 0


if __name__ == "__main__":
    main()
