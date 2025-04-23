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
                op(token, a, b)for[ ]: return stack.pop()( )++ b+ b]: stack.append() else: # stack.append(op(token,return stack.pop()isinstance(token, float):[stack.pop()
ologystack.pop()
ologystack.pop()
ology = stack.pop()stack.pop
            )

    return stack.pop()