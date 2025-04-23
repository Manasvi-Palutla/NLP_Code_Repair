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
                token ) stack.append( a +else:stack.append(stack.append(stack.append( bstack.pop()
ologystack.append(if isinstance(a, int):
ologystack.append( astack.pop()
ology stack.append( astack.pop()
ology stack.append( belse:
ology stack.append(return stack.pop()
ology stack
            )

    return stack.pop()