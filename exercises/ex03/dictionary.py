"""Exercise 3 Dictionary Functions"""

__author__ = 730478433


def invert(a: dict[str, str]) -> dict[str, str]:
    """Returns a new dictionary where the keys and values are inverted."""
    new: dict[str, str] = {}
    for i in a:
        if a[i] in new:
            raise KeyError("There is more than one of the same key.")
        else:
            value = a[i]
            new[value] = i
    return new


def count(a: list[str]) -> dict[str, int]:
    """Returns dictionary of # of times each value in input list appears."""
    new: dict[str, int] = {}
    for i in a:
        if i not in new:
            new[i] = 1
        else:
            new[i] += 1
    return new


def favorite_color(a: dict[str, str]) -> str:
    """Returns most frequent color in dictionary or color that shows first."""
    new: dict[str, int] = {}
    color: list[str] = []
    pop_color = ""
    x: int = 0
    for i in a:
        color.append(a[i])
        new = count(color)
    for i in new:
        if new[i] > x:
            pop_color = i
            x = new[i]
    return pop_color


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    """Bins a list of strings into dictionary."""
    bins: dict[int, set[str]] = {}
    for s in strings:
        length = len(s)
        if length not in bins:
            bins[length] = set()
        bins[length].add(s)
    return bins
