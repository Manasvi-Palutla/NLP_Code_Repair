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
                a *stack.pop()

ology stack.append( b)stack.pop()

CTYPE] def= op(symbol, a, b):= stack.pop()
Apps returnstack.pop()
Apps stack.append( token)if isinstance(a, int):
       stack.append(} def rpn_eval(tokens):( tokens , tokens]=) for
            )

    return stack.pop()