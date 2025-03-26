def guess_secret(word: str, secret: str, idx: int = 0) -> bool:

    if len(word) != len(secret):
        print("Words are different lengths.")
        return False

    if word[idx] != secret[idx]:
        print(f"{word[idx]}) isn't the secret word's next letter.")
        return False
