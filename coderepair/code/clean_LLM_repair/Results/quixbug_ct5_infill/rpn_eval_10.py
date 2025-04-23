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
                op(token, a, b)1.0/np.nan).exp() )stack.append( 1.0a, b) if isinstance(tokens, list):.. pop()] return tuple(stack'-'b ) elif isinstance(tokens,'/'stack.pop()stack.pop()() ] ) for)stack( stack.pop():
            )

    return stack.pop()