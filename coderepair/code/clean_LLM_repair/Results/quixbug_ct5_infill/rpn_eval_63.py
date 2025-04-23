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
                op(symbol, a, b)stack.pop()

SURFACE stack.append(stack.pop()
OTALOTALOTAL= stack.pop()
OTALOTAL INstack.append( stack.pop()
OTALOTAL INstack.pop()
OTALOTAL= stack.pop()
OTAL INstack.append( stack.pop()stack.append( stack.pop() )if isinstance(token,:
            )

    return stack.pop()