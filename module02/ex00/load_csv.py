import pandas as pd
import sys


def load(path: str) -> pd:
    """
    Description: This function load a csv file.

    Args:
        - path: (str) path to load the file

    Returns:
        - dataset: (pd) dataset loaded
    """
    try:
        dataset = pd.read_csv(path)
        if dataset.empty:
            print("File .csv is empty")
            sys.exit(1)
    except Exception:
        print("File is invalid")
        sys.exit(1)
    print("Loading dataset of dimensions ", dataset.shape)
    return dataset


def main():
    return 0


if __name__ == "__main__":
    main()
