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

CTYPE stack.append(stack.pop()
SURFACE stack.append(stack.append(op(a.symbol, a.value,stack.append(op(a.symbol,a.value, a.value),stack.append(op(a.symbol, a.value, b.value))= stack.pop()

MimeType == stack.pop()
Assemblystack.pop
            )

    return stack.pop()