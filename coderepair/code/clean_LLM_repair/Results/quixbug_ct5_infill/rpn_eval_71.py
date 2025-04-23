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
        = op(Symbol, a,b,return==( stack.pop()
MimeType)stack.append(token)
MimeType == stack.pop()
MimeType stack.append(token)AmbMimeType= stack.pop()
MimeTypestack.append()stack.append(stack.pop()
MimeType stack.append(stack.pop()
MimeType )
MimeTypestack
            )

    return stack.pop()