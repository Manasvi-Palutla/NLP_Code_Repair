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
                a + b"""stack.append(op(symbol, a,b, a, b) returnfunction(symbol, a, b):a , b( tokens ) ), stack.pop(),= stack.pop()
 69=lambda a,: b , a ,a, b):( tokens ) ) ))= stack.pop()
 69=lambda a,: a
            )

    return stack.pop()