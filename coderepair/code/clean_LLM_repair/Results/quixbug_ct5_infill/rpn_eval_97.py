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
        = op(a, b,for token in tokens= stack.pop()
envs(stack.append( a ))stack.append(stack.append(+) return)stack.pop()
        = stack.pop()
envsstack.pop()
envsstack.pop()stack.pop())stack.pop()
envs stack.append(stack.
            )

    return stack.pop()