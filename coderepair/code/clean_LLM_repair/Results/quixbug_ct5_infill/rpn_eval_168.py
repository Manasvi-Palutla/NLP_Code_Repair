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

    = op(op, a,b)((stack.pop()
           if isinstance(tokens, tuple):=stack.append(stack.pop()
Apps( stack.pop()
Appsstack.append(stack.pop()
Apps]. append (+ a)[ ]stack.append( stack.pop()
Apps ). append ()stack
            )

    return stack.pop()