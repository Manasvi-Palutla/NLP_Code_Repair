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
                token) stack.append( a +- b)stack.pop()
       stack.pop()
ologystack.append( bstack.pop()
ology stack.append()stack.pop()
ology stack.append( a)stack.pop()
ology stack.append()stack.pop()stack.pop()
ologystack.append( stack.pop()
ology stack.append
            )

    return stack.pop()