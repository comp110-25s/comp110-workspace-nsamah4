"""My version of wordle :)"""

__author__ = "730478433"


def contains_char(search_string: str, character: str) -> bool:
    """Checks if a character is present in the guess."""
    assert len(character) == 1
    position: bool = False
    index: int = 0
    while position is False and index < len(search_string):
        if search_string[index] == character:
            position = True
        else:
            position = False
        index = index + 1
    return position


def emojified(guess: str, secret: str) -> str:
    """displays the colored emoji boxes"""
    assert len(guess) == len(secret)

    i: int = 0
    emoji: str = ""

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while i < len(secret):
        if guess[i] == secret[i]:
            emoji = emoji + GREEN_BOX
        else:
            if contains_char(secret, guess[i]):
                emoji = emoji + YELLOW_BOX
            else:
                emoji = emoji + WHITE_BOX
        i = i + 1
    return emoji


def input_guess(length: int) -> str:
    guess: str = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    won: bool = False
    while turns < 7 and won is False:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            won = True
        else:
            turns = turns + 1
    if won is True:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
