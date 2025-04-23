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
                token)op(Symbol, a, b) op(Symbol,stack.pop()

Apps=stack.pop())

Apps stack.append(stack.pop()
lang = stack.pop()
lang == stack.pop()
lang= stack.pop()
lang stack.append()stack.append( stack.pop()) # returna, b= stack.pop()
Lang
            )

    return stack.pop()