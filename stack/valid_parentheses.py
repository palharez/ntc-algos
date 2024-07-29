MATCHES = {
    "}": "{",
    "]": "[",
    ")": "(",
}


def valid(s: str) -> bool:
    stack = []

    for c in s:
        if c not in MATCHES:
            stack.append(c)
            continue

        if not stack or stack[-1] != MATCHES[c]:
            return False

        stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    assert valid("()") == True
    assert valid("{[()]}") == True
    assert valid("{]") == False
