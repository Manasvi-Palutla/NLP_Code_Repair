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
                token#'+':lambda a, b: a'-':lambda a, b: a -: stack.append()stack.pop()
isis stack.append( b)stack.pop()

azy stack.append( a)stack.pop()

 neighbourstack.append( a)stack.pop()

 penalty stack.append(if isinstance( tokens)= stack.
            )

    return stack.pop()