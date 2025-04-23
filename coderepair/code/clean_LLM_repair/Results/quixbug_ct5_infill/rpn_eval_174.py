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
        = op(token, a,b,= stack.pop()if len(tokens) > 1:stack.append( tokens[1]'.') if len(tokens) > 1:stack.append( tokens[1]stack.pop()stack.append(=stack.append( stack.pop()

stack.pop()K_1_1 stack.append( stack.pop
            )

    return stack.pop()