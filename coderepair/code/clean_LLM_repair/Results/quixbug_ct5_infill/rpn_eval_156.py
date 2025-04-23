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
envs = op(op, a, b,: return None==if isinstance(token, float):if isinstance(token,None:return= stack.pop()return None= stack.pop()return None= stack.pop()return None=None if isinstance(token, float):a1:return= stack.pop()return Noneif isinstance(token, float):b=
            )

    return stack.pop()