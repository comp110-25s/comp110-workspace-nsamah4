"""My version of wordle :)"""

__author__ = "730478433"


def contains_char(search_string: str, character: str, idx: int = 0) -> bool:
    """Checks if a character is present in the provided search string."""
    assert len(character) == 1, f"len('{character}') is not 1"
    if idx < len(search_string):
        if search_string[idx] != character[idx]:
            print("False")
            return False
        else:
            print("True")
            return contains_char(
                search_string=search_string, character=character, idx=idx + 1
            )
    return True
