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
                a + belse:stack.append( astack.pop()

    stack.append(stack.pop()
ology stack.append( b )stack.append( stack.pop()
ology stack.pop()stack.pop()
ologystack.pop()
ologystack.pop()
ology stack.append(, a , bif isinstance(tokens, list):stack.append(stack
            )

    return stack.pop()