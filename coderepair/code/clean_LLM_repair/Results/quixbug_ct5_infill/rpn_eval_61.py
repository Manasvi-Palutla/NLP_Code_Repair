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

CTYPE stack.append()(a, b)= stack.pop()
            stack.append( a)stack.append()isinstance(token, float):
            =stack.pop()
            stack.append( b)):stack.append(token)

CTYPE stack.append()stack.pop())

azy stack.append()=
            )

    return stack.pop()