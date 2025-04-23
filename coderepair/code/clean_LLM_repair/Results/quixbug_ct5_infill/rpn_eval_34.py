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
                token)coeff = op(a, b,stack.append(coeff ) # return stack.pop()if len(tokens)stack.pop()]= stack.pop()
Aux= stack.pop()
Aux stack.append(stack.pop()
Aux stack.append(stack.pop()
Aux stack.append(stack.pop()
Aux stack.append(stack.pop()
Aux stack.pop()
Aux
            )

    return stack.pop()