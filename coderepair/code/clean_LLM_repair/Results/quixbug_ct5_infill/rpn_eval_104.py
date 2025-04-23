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
                a + bfor token in tokens:seqns'+', '-', '+','/', '+','/', '+','',if isinstance(token, float):seqns =stack.pop()seqns stack.append( a +)seqns stack.append( b'/','-'),stack.pop()seqns = stack.pop()seqnsstack.pop()seqns stack
            )

    return stack.pop()