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
                a +stack.append( bstack.append(stack.pop()

SURFACE else:return= stack.pop()
SURFACE stack.append( a= stack.pop()
ology stack.append()= stack.pop()
ologystack.append( b+ b)stack.append( bstack.pop()
ology stack.append(stack.pop()
ology=
            )

    return stack.pop()