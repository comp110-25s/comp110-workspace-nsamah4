"""File to define Fish class."""


class Fish:
    """Fish class for ecosystem."""

    age: int

    def __init__(self):
        """Initializing our age with value of 0"""
        self.age = 0
        return None

    def one_day(self):
        """Day to day population of fish."""
        self.age += 1
        return None
