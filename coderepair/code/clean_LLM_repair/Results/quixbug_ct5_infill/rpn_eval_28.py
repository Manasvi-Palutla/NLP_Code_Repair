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
                a +ifstack.pop())
OTALS stack.append( b ): stack.append(stack.pop()
 EP= stack.pop()stack.pop()
OTALS stack.append(stack.pop()
           if isinstance(a,stack.pop()
OTALS stack.append(stack.pop()astack.pop()
OTALS stack.append(stack.pop()
            )

    return stack.pop()