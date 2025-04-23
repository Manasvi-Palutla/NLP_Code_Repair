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
                token) stack.append(return None,None, None, None[,returnlen(tokens)):return len(tokens) - 1][0] if isinstance(token, int):
][0]=(a, b)]),]. append ( token )] =return len(tokens) returnn[ i( a ,stack
            )

    return stack.pop()