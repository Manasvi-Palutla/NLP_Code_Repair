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
                aif isinstance(tokens[0], int):
ology= stack.pop()
ologystack.append(b)
ology stack.append(a)stack.append(b)
ologystack.pop()
ology stack.append(b)
ology stack.append(a)= stack.pop()
ology stack.append(a)stack.append(b)return stack.pop()
ologystack
            )

    return stack.pop()