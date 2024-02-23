import matplotlib
import matplotlib.pyplot as plt
from load_image import ft_load

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
    channel = 1
    img_cropped = image[200:600, 400:800, :]
    gray = img_cropped
    if image.ndim == 3:
        channel = image.shape[2]
        gray = (
            0.2989 * img_cropped[:, :, 0]
            + 0.5870 * img_cropped[:, :, 1]
            + 0.1140 * img_cropped[:, :, 2]
        )
    print(image)
    print("Number of channels :", channel)
    print("Width and height", image.shape[:2])
    print("New shape after slicing: ", gray.shape)
    print(gray)
    plt.imshow(gray, cmap="gray")
    plt.show()
    return 0


if __name__ == "__main__":
    main()
