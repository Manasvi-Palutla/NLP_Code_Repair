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
                token + bstack.append( ab = stack.pop()

   if isinstance(token,return"/",) returnstack.pop()] if isinstance(token, float):
ologystack.append(a) else:"/", a)"", " "].join(stack):astack.append(a)stack.append(b) returnstack.append(a
            )

    return stack.pop()