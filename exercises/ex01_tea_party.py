"""This program will be used to calculate the cost of planning a tea party!"""

__author__ = "730478433"


def main_planner(guests: int) -> None:
    """Displays the total number tea bags, treats, and cost for the tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_count=guests * 2, treat_count=guests * 3)))
    return None


def tea_bags(people: int) -> int:
    """Calculates the number of tea bags needed for all of the guests"""
    return people * 2


def treats(people: int) -> int:
    """Calculates the number of treats needed for all of the guests drinking tea"""
    return int((tea_bags(people=people)) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost of tea bags & treats based on the number of guests"""
    return float(0.5 * tea_count + 0.75 * treat_count)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
