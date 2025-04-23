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
        = op(a, b,= stack.pop()
ENGANDS= stack.pop()
LANGUAGE= stack.pop()
LANGUAGEstack.append(stack.append(rpn_eval(stack)) returnelse: #in= stack.pop()
LANGUAGE stack.append(rpn_eval(stack)) #stack.append(rpn_eval(stack))= stack.
            )

    return stack.pop()