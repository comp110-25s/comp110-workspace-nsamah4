"""File to define Bear class."""


class Bear:
    """Bears living by the river."""

    def __init__(self):
        """Initializing age and hunger_score."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Simulate day in the life of a bear."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish):
        """Determines the number if fish the bear eats"""
        self.hunger_score += num_fish
