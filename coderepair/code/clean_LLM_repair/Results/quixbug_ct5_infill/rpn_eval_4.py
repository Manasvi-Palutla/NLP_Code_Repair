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
                a += stack.pop()
Vfs= stack.pop()
Vfsstack.append(stack.pop()
Vfsstack.append( b)
Vfsstack.append()stack.append(stack.pop()
Vfs stack.append(stack.pop()
Vfsstack.append(stack.pop()
Vfsstack.pop())return stack.pop()
Vfsstack.
            )

    return stack.pop()