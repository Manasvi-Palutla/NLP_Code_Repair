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
        = op(symbol, a,b)stack.pop()
MimeTypereturn= stack.pop()
MimeType stack.append(stack.pop()
MimeType stack.append() #stack.append( b). pop() #stack.append( b)) ###stack.append( a)
MimeTypeif isinstance(a, float):= stack.pop()
            )

    return stack.pop()