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
                token +( symbol,,return op(symbol, a, b)[ symbol= stack.pop()
        return= stack.pop()
PECIAL returnif isinstance(symbol,):k = stack.pop()k.upper()k return# if isinstance(tokens,= stack.pop()k stack.append(token)= stack.pop()k returnstack.pop()Kk
            )

    return stack.pop()