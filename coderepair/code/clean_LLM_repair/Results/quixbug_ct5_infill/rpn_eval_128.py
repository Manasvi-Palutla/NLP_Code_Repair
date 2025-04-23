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

    = op(symbol, a,b)op(symbol, a,b,lambda a, b: a +stack.append(stack.pop()
           stack.pop()] """print(tokens)stack.pop()= stack.pop()] return( stack.pop()

caps, stack.pop()

MimeTypestack.pop())= stack.
            )

    return stack.pop()