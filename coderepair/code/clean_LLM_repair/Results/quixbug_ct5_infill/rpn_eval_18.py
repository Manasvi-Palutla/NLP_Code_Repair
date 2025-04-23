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
                op(token, a, b )== stack.pop()
 xsd =) if isinstance(token,stack.append( token)= stack.pop()

stack.append(return##,stack.pop()

stack.append()return None if isinstance(token,stack.pop()None:
SURFACE stack.append( token)
MimeTypestack
            )

    return stack.pop()