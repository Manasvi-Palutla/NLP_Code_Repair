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
                token)op(op, a, bstack.pop()
            returnstack.pop())

Phrasestack.pop()
MimeType = stack.pop()
MimeType stack.append(stack.pop()
MimeType stack.append(stack.pop()
MimeType stack.append()
MimeType= stack.pop()
MimeType stack.append(stack.pop()
MimeType stack.append(stack.pop())
            )

    return stack.pop()