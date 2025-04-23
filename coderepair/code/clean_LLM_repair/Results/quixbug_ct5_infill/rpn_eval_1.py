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
                op(token, a, b)if isinstance(token,+ bstack.append( a)

stack.append( b)

CTYPE=stack.pop()
azystack.pop()

SURFACE stack.append( a=stack.pop()
        else:cvn =stack.pop()
 LayoutParamsstack.append()
            )

    return stack.pop()