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

        = op(op(symbol, a,b)returnstack.pop()
SURFACE stack.append() else:

MimeTypestack.pop()
MimeType stack.append(op(symbol, a,)stack.append(token)if isinstance(tokens, list):stack.append(tokens)stack.append(tokens[0]stack.append(tokens[1] )
            )

    return stack.pop()