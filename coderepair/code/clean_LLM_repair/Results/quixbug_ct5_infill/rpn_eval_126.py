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
                op(token, a, b)lambda tokens: tokens[0]stack.pop()stack.pop()

    = stack.pop()

SURFACEstack.append(stack.pop())

Suggestion =stack.pop()
SURFACE stack.append( stack.pop()stack.pop()
SURFACE= stack.pop()seqnStackStack =stack.pop()seqnStackStack =
            )

    return stack.pop()