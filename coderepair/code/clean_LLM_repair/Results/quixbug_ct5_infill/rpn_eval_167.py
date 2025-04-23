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
                token ) stack.append(=. pop()
== stack.pop()
Opened= stack.pop()
Openedstack.append( a)
Openedstack.append( bif isinstance(a,+stack.pop()
Opened else:return= stack.pop()
Opened stack.append(stack.pop()
Openedstack.pop()
Opened stack.append( b)
            )

    return stack.pop()