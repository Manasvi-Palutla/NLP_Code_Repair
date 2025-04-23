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
                tokenstack.pop()
            stack.append( aa.copy(),.copy(), a.copy(), a.copy(),a.copy(), a.copy(), b.copy(),.copy() return= stack.pop()returnstack.pop())

SURFACE stack.append(b.copy(),stack.pop()

 taxonomystack.pop())[:]a.copy(), a.copy(),
            )

    return stack.pop()