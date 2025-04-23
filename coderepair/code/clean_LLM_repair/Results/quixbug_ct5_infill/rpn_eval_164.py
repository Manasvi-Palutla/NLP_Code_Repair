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
                token)Op(op, a, b,stack.pop()

azystack.append( None)
       =]None:stack.append(stack.pop()'-')

CTYPE stack.append()'/'):= stack.pop()
            stack.append( bstack.append( b)
VfsResource= stack.pop()
VfsResourcestack.pop
            )

    return stack.pop()