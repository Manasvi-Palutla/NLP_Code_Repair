def rpn_eval(tokens):
    def op(symbol, a, b):
        return {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }[symbol](a, b)

    stack = []

    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(
                a + b,if isinstance(tokens[0], int):stack.append(if isinstance(tokens[0], float):
= stack.pop()

stack.append(] elif isinstance(tokens[1], int):stack.append(token)

envs = stack.pop()] ) returntokens [ 0 ]= stack.pop().pop()

envs = stack.pop()
            )

    return stack.pop()