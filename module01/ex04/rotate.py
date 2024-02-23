import matplotlib
import matplotlib.pyplot as plt
from load_image import ft_load
import numpy as np

matplotlib.use("Qt5Agg")


def main():
    """
    Description:
        Program to slice an image and display the grayscale version of the
        sliced image.
    """
    image = ft_load("animal.jpeg")
    if image is None:
        return 1
    img_crop = image[200:600, 400:800, :1]
    transp = np.zeros((img_crop.shape[1], img_crop.shape[0]))
    for i in range(img_crop.shape[0]):
        for j in range(img_crop.shape[1]):
            transp[j, i] = img_crop[i, j, 0]
    print("The shape of image is :", img_crop.shape)
    print(img_crop)
    print("New shape after Transpose: ", transp.shape)
    print(transp)
    plt.imshow(transp, cmap="gray")
    plt.show()
    return 0


if __name__ == "__main__":
    main()
