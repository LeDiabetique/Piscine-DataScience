from time import sleep
from tqdm import tqdm


def ft_tqdm(lst: range) -> None:
    """
    Description:
    Function that takes a range and returns an iterator that will display a
    progress bar with the percentage of completion and the number of iterations
    completed over the total number of iterations.

    Args:
    lst: range - range of numbers to iterate over

    Returns:
    None
    """
    for i in lst:
        j = i + 1
        prct = (j / len(lst)) * 100
        update = f"{j}/{len(lst)}"
        bar = (
            f"[{'='*int((j/len(lst))*50)}>{' '*(50-int((j/len(lst))*50))}]"
        )
        print(f"\r{prct:.0f}%{bar} {update}", flush=True, end="")
        yield i


def main():
    """
    Description:
    Main function that will display the progress of the iteration using the
    ft_tqdm function and the tqdm function to compare the implementation
    of the ft_tqdm function.
    """
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()
    for elem in tqdm(range(333)):
        sleep(0.005)
    print()
    # Afficher une autre progression sans flush=True

    return


if __name__ == "__main__":
    main()
