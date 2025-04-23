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
                token )

ology stack.append(if isinstance(a, float):Ambient= stack.pop()Ambienta )= stack.pop()Ambientstack.pop()Ambient= stack.pop()Ambientstack.append(stack.pop()
CTYPEstack.append(stack.pop()
CTYPE stack.append(stack.append(= stack.pop()
CTYPE stack.append
            )

    return stack.pop()