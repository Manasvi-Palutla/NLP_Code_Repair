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
                op(token, a, b )stack.pop()
ologystack.pop()
ology stack.append(else: #returnstack.pop()
ology stack.append(stack.pop()
ology stack.append('+':lambda a, b: bstack.append("-":lambda a, b:/stack.pop()
ology stack.append( astack.pop()
            )

    return stack.pop()