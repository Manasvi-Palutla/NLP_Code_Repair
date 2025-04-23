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
                a+b)

    = stack.append(0] =1 ]2]= stack.pop()

SURFACE returnstack.pop()] =stack.pop()]stack: k =for k in: k, stackk ] =. append, b= stack.pop()]stack.pop()k] = stack.pop()k(stack
            )

    return stack.pop()