import matplotlib
import matplotlib.pyplot as plt
from load_csv import load

matplotlib.use("Qt5Agg")


def main():
    """
    Description: This function plot a scatter plot of life expectancy
    and gross domestic product in 1900.
    """
    data1 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    data2 = load("life_expectancy_years.csv")

    feature1 = data1["1900"]
    feature2 = data2["1900"]
    print(f"Life expectancy in 1900\n{feature2}")
    print(f"Gross domestic product in 1900\n{feature1}")
    plt.scatter(feature1, feature2)
    plt.title("1900")
    plt.ylabel("Life expectancy")
    plt.xlabel("Gross domestic product")
    plt.xscale("log")
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.legend(["1900"], loc="lower right")
    plt.show()
    return 0


if __name__ == "__main__":
    main()
