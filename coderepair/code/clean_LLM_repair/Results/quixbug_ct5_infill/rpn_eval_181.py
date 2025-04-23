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
                token)
        = op(op(a, b)stack.pop()

SURFACEstack.pop()
        if isinstance(tokens,=stack.pop()

 Pod= stack.pop()Pod Pod= stack.pop()Pod Pod= stack.pop()Pod Podstack.append( Podstack.append( Pod.pop()Pod)= stack.pop()Pod]
            )

    return stack.pop()