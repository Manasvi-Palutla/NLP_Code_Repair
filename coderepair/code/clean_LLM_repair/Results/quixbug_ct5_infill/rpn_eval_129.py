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
                b -= stack.pop()
ology+= op(symbol, a, b):)
ology if isinstance(token,stack.append(= stack.pop()
ology stack.append(= stack.pop()
ology stack.append(stack.pop()
ology stack.append(= stack.pop()
ology stack.append(stack.append(stack.pop())
ologystack.append
            )

    return stack.pop()