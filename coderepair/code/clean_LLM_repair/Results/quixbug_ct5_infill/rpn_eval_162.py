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
        = op(a,b,stack.pop()
SURFACE= stack.pop()
envs= stack.pop()
envsstack.append(= stack.pop()
envs stack.append(stack.append( a)= stack.pop()
envs stack.append( bstack.pop()
envs stack.append(stack.pop()
envs stack.append(stack.
            )

    return stack.pop()