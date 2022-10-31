"""Significant Figure Counter Function"""


def get_significant_figure(number: str | float | int) -> int:
    """
    Returns the number of significant figures in a number.

    :param number: The number to count the significant figures of.
    :return: The number of significant figures in the number.
    """
    try:
        float(number)
    except ValueError:
        raise ValueError("Number must be a valid rational number")
    number = str(number)
    if "." in number:
        before_decimal, after_decimal = number.split(".")
        count = len(str(int(before_decimal)))
        if after_decimal != "":
            count += len(after_decimal)
        return count
    else:
        return len(number.rstrip("0").lstrip("0"))


if __name__ == "__main__":
    print(get_significant_figure(1230), "\n")
    print(get_significant_figure(1230.0), "\n")
    print(get_significant_figure("0000"), "\n")
    print(get_significant_figure("00456"), "\n")
    print(get_significant_figure("0045600"), "\n")
    print(get_significant_figure("456"), "\n")
    print(get_significant_figure("456."), "\n")
    print(get_significant_figure("456.0"), "\n")
