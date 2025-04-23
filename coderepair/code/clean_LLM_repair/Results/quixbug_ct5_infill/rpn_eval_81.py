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
                tok)
        = op(symbol,a,b) if len(stack):stack.append(returnstack.pop()
           stack.pop()

CTYPE stack.append(tok)stack.append(tok)stack.append(tok)
ology return stack.pop()stack.pop()
ology= stack.pop()
ology stack.append(tok)= stack.pop()
ology if
            )

    return stack.pop()