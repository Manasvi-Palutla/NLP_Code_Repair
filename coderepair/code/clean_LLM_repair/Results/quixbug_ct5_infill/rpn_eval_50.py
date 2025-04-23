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
                op(a, b,stack.pop()
NUM_HETATM_VERSION_COEFFICIENTS,stack.append( stack.pop()
NUM_HETATM_VERSION_COEFFICIENTS,0]stack.pop():= stack.pop()(stack.pop())a,=]stack.append( a)#if isinstance
            )

    return stack.pop()