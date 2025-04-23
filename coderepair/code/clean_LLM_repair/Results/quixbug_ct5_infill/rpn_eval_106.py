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
                token.rpn(a, b)= stack.pop()stack.append(returnstack.pop()
 getTerminology()= stack.pop()

Phrase stack.append(1 else:= stack.pop()stack.append() elif isinstance(tokens[1], float):= stack.pop()
            = stack.pop()
 taxonomystack.append(= stack.pop()
            )

    return stack.pop()