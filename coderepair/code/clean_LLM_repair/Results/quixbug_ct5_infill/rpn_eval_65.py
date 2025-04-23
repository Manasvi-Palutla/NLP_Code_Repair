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
                a + b +[a] = bstack.pop()

    = a +b= stack.pop()

   stack.pop())

SURFACE stack.append(stack.append( b) return stack.pop()

   stack.pop()
Taxonomystack.pop()KD:KD:KD:KD stack.append( KD)KD stack.append(
            )

    return stack.pop()