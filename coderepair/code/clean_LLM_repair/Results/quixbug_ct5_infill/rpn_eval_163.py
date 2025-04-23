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

envs stack.append(stack.pop()
           stack.pop())
            stack.append(== stack.pop()
MimeType=stack.pop()
MimeType stack.append( token)
MimeTypestack.append("n" stack.append("c" stack.append( c )"n"= stack.pop()
MimeType stack.append( c )stack
            )

    return stack.pop()