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
                '+' +, a , b )stack.append( '-' ++ stack.pop()

 rootNode =else:

 rootNode =stack.pop()
azystack.append(stack.pop()
ology if isinstance(node,= stack.pop()NetworkNetwork(node,stack.append(node)NetworkNetworknode,stack.append(node))NetworkNetwork=stack.pop()
            )

    return stack.pop()