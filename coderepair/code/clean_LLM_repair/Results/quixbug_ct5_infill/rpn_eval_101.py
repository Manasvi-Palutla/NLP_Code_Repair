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
        = op(a, b,forif isinstance(tokens,)]for token inlen(tokens) :stack.append(a. pop()] , ") , "astack.pop()

 penalty= stack.pop()

 penalty= stack.pop()
ENGLISH, ""+", "-", "*", ""/",
            )

    return stack.pop()