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
                token) stack.append(if isinstance(token, int):A = stack.pop()Astack.append(a)A =stack.append(b)A = stack.pop()B stack.append(A)A= stack.pop()
Opened == stack.pop()
Openedstack.append(B)A=stack.pop()A= stack.pop()stack.append(B)A
            )

    return stack.pop()