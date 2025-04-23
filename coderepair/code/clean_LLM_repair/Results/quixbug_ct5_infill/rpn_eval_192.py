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

    = op(token,a,b) stack.append(a=stack.pop()

    stack.append( b)1.0 /stack.pop()
ology = stack.pop()
ology if isinstance(stack.pop(),= stack.pop()
ology stack.append(stack.pop()
ologystack.pop()
ology=else:stack.append(
            )

    return stack.pop()