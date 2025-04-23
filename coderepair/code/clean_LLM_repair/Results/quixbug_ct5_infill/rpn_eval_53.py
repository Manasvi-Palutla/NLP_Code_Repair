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
                token) stack.append(stack.append( stack.pop()
       astack.append( areturn op(symbol, a, b)op(symbol,+ b )stack.pop()

CTYPE stack.append( stack.pop()

 pkey= stack.pop()
OTAL) return
            )

    return stack.pop()