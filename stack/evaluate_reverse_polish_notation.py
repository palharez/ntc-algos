def evaluate(tokens):
    stack = []

    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        elif token == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(token))

    return stack.pop()


if __name__ == "__main__":
    assert evaluate(tokens=["2", "1", "+", "3", "*"])
