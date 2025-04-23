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
                a / b +( )stack.append(stack.pop())

lang=stack.pop()
lang stack.append(stack.append(b)
lang stack.append( a)
langstack.append(b)
lang stack.append(stack.append( stack.pop()
lang stack.append(stack.pop()
lang stack.append(stack.pop()
lang stack
            )

    return stack.pop()