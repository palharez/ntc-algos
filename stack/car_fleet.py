def fleet(target, position, speed):
    pairs = [[p, s] for p, s in zip(position, speed)]

    stack = []
    for p, s in sorted(pairs)[::-1]:
        stack.append((target - p) / s)

        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


if __name__ == "__main__":
    assert fleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]) == 3
