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
                a + bstack.pop()

ology stack.append( astack.pop()
           )if isinstance(a, float):stack.append(a)stack.append(a)
ology stack.append(if isinstance(token,stack.append(b)
ology stack.append( b)if isinstance(token,returnstack.pop()
ology stack.append(stack.pop
            )

    return stack.pop()