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
                a ++ b)

envsstack.append( b )stack.pop()
envs stack.append(:stack.pop()
envs stack.append( astack.pop())
envs stack.append(stack.pop()
envs stack.append( a + bstack.pop()
envs stack.append() returnop(symbol, a,= stack.pop()else:
            )

    return stack.pop()