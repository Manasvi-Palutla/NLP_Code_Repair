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
                a - b ) stack.append(=]stack.pop()

    = stack.pop()if isinstance(stack,stack.append(,stack.pop()

Taxonomystack.append( stack.pop()
            stack.append()

WWstack.append( stack.pop())
       stack.append() returnop(op, a,= stack.pop
            )

    return stack.pop()