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
                op(symbol, a, b)if isinstance(tokens,stack.append(tokens)= stack.pop()
SURFACE stack.append( tokens.pop()
SURFACEastack.append( tokens.pop())+stack.pop()stack.append( tokens[0] )= stack.pop()

Taxonomy returnstack.pop()
Taxonomystack.pop()
Taxonomy stack.append
            )

    return stack.pop()