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
ology = op(a, b,= stack.pop()
ology stack.append(stack.append( stack.pop()
ology )( stack.pop()
ologya, b):
ology stack.append(stack.pop()
ologystack.pop()
ologystack.pop()
ology stack.append()_match(stack,op(op(op, a, b)):
            )

    return stack.pop()