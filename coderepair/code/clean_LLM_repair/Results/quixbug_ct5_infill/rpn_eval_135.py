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
                op(symbol, a, b)returnif isinstance(token,stack.pop()
envs= stack.pop()
envs if isinstance(token,stack.pop()
envsstack.append(]= stack.pop()
envs ifstack.append(stack.pop()
envs stack.append(stack.append( op(symbol, a,= stack.pop()
envs ifstack
            )

    return stack.pop()