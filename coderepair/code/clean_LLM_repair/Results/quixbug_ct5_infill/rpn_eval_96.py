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
                a * b *forstack.pop()+b)

    = stack.pop()
SURFACE stack.append(stack.pop())
SURFACE stack.append( stack.pop()
SURFACEstack.append( stack.pop())
SURFACE stack.append( stack.pop())
ology stack.append(stack.pop())
ology stack.append( stack.pop()
ology stack.append(
            )

    return stack.pop()