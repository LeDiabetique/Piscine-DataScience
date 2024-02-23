import matplotlib
import matplotlib.pyplot as plt
from load_csv import load

matplotlib.use("Qt5Agg")


def main():
    """
    Description: This program plot the life expectancy in France.
    """
    data = load("life_expectancy_years.csv")
    pltdata = data[data["country"] == "France"]
    yaxis = pltdata.values[0][1:]
    xaxis = pltdata.columns[1:].astype(int)
    plt.plot(xaxis, yaxis)
    plt.xlabel("Year", fontsize=10)
    plt.suptitle("Life expectancy in France")
    plt.xticks(range(xaxis[0], xaxis[-1] + 1, 40))
    plt.ylabel("Life expectancy")
    plt.show()
    return 0


if __name__ == "__main__":
    main()
