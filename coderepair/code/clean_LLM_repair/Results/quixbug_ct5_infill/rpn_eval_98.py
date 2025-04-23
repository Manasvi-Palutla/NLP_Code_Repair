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
                op(token, a, b)stack.append(stack.pop()
        if isinstance(token,if isinstance(token, float):stack.append(= stack.pop()
           stack.append( a)
       stack.append(stack.append(stack.pop()
            stack.append( bstack.append( b)b)
Taxonomystack.pop()
VfsResource
            )

    return stack.pop()