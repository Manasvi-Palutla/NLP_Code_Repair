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
                '%.2f' % ( a, b): for token in tokensreturn= stack.pop()

stack.append((]= stack.pop()stack.append(. appendreturn a return,), stack.pop()

   == stack.pop()

Taxonomystack.append() if isinstance( token,= stack.pop()
            )

    return stack.pop()