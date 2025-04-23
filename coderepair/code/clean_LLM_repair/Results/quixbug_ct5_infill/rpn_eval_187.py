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
                a + b ) stack.append(( stack)
        stack.append(else:

    = stack.pop()
Episodestack.append( areturnstack= stack.pop()
Episode stack.append()= stack.pop()
Episodestack.append(return a= stack.pop())
Episode stack.append(stack.pop()
Episode
            )

    return stack.pop()