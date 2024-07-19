def is_palindrome(string):
    l, r = 0, len(string) - 1

    while l < r:
        l, r = l + 1, r - 1

        while l < r and not is_alpha_numeric(string[l]):
            l += 1

        while r > l and not is_alpha_numeric(string[r]):
            r -= 1

        if string[l].lower() != string[r].lower():
            return False

        l, r = l + 1, r - 1

    return True


def is_alpha_numeric(character):
    return (
        ord("A") <= ord(character) <= ord("Z")
        or ord("a") <= ord(character) <= ord("z")
        or ord("0") <= ord(character) <= ord("9")
    )


if __name__ == "__main__":
    assert is_palindrome("mam, mam") == True
