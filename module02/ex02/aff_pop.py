import matplotlib
import matplotlib.pyplot as plt
from load_csv import load

matplotlib.use("Qt5Agg")


def convert_to_float(value):
    """
    Description: This function convert a string to float.

    Args:
        - value: (str) value to convert

    Returns:
        - value: (float) value converted or None
    """
    if value is None:
        return None
    elif value[-1] == 'k':
        return float(value[:-1]) * 1000
    elif value[-1] == 'M':
        return float(value[:-1]) * 1000000
    else:
        return None


def main():
    """
    Description: This program plot the life expectancy in France.
    """
    data = load("population_total.csv")
    try:
        pltdata = data[data["country"] == "France"][:1]
        pltdata2 = data[data["country"] == "Belgium"][:1]
    except KeyError:
        print("KeyError: 'country'")
        return 1
    pltdata = pltdata.dropna(axis=1)
    pltdata2 = pltdata2.dropna(axis=1)
    france_y = pltdata.values[0][1:]
    belgium_y = pltdata2.values[0][1:]
    xaxis = pltdata.columns[1:].astype(int)
    xaxis_filtered = xaxis[xaxis <= 2050]
    france_filtered = france_y[:len(xaxis_filtered)]
    france_filtered = [convert_to_float(value) for value in france_filtered]
    belgium_filtered = belgium_y[:len(xaxis_filtered)]
    belgium_filtered = [convert_to_float(value) for value in belgium_filtered]
    plt.plot(xaxis_filtered, belgium_filtered)
    plt.plot(xaxis_filtered, france_filtered)
    plt.xlabel("Year", fontsize=10)
    plt.ylabel("Population", fontsize=10)
    max_v = int(
        max(france_filtered) > max(belgium_filtered) and max(france_filtered)
        or max(belgium_filtered))
    yticks = [0 + i * 10000000 for i in range(0, int(max_v / 10000000) + 2)]
    ytick_labels = [f"{int(ytick / 1000000)}M" for ytick in yticks]
    plt.yticks(yticks, ytick_labels)
    plt.xticks(range(xaxis_filtered[0], xaxis_filtered[-1], 40))
    plt.suptitle("Population Projections")
    plt.legend(["Belgium", "France"])
    plt.show()
    return 0


if __name__ == "__main__":
    main()
