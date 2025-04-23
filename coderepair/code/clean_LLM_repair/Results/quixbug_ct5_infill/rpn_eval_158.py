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
                token)
        = op(a, b,if isinstance(token,stack.append(stack.append(stack.pop()
Episodestack.append(token)
Episode stack.append(a). append(token)KDCO_I_I_I_I_I_I_I_I_I_I_I_I_I_I_I_I_I_I_
            )

    return stack.pop()