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
                op(symbol, a, b)else:
SURFACE stack.append(tok)"%s" %= stack.pop()
SURFACEstack.append(tok)
SURFACE stack.append(tok)
SURFACEstack.pop()
SURFACE stack.append(tok) return=stack.pop()return.pop()

SURFACE stack.pop() returnstack.pop()
SUR
            )

    return stack.pop()