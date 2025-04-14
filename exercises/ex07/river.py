"""File to define River class."""

__author__ = "730478433"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """River class to simulate an ecosystem with bears and fish."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes fish & bears once they reach a certain age."""
        new_fish = []
        for fish in self.fish:
            if fish.age > 3:
                continue
            new_fish.append(fish)
        self.fish = new_fish
        new_bears = []
        for bear in self.bears:
            if bear.age > 5:
                continue
            new_bears.append(bear)
        self.bears = new_bears
        return None

    def remove_fish(self, amount: int):
        """Removes fish from population when bears eat them."""
        for _ in range(amount):
            if len(self.fish) > 0:
                self.fish.pop(0)
        return None

    def bears_eating(self):
        """Removes fish from population when bears eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self):
        """Removes bears from population if hunger score is below 0."""
        new_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                continue
            new_bears.append(bear)
        self.bears = new_bears
        return None

    def repopulate_fish(self):
        """Adds fish to the population."""
        baby_fish = (len(self.fish) // 2) * 4
        for i in range(baby_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Adds bears to the population."""
        baby_bears = len(self.bears) // 2
        for _ in range(baby_bears):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Prints the fish and bear population in the river."""
        num_fish = len(self.fish)
        num_bears = len(self.bears)
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {num_fish}")
        print(f"Bear population: {num_bears}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates one week of life in the river."""
        for i in range(7):
            self.one_river_day()
        return None
