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
                aif isinstance(token, float):= stack.pop()
            stack.append(stack.pop()

 rootNode ==stack.pop()

 pkeystack.append(= stack.pop()

   =+stack.pop()
           stack.pop()

VsVs stack.append( stack.pop()
            stack.append(stack.pop()
VsVsVs
            )

    return stack.pop()