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
                token.rpn()stack.append(token.rpn())'*',a'*', ''/',stack.append( a)a)stack.append( b)
ology stack.append( a)
ologystack.pop()
ology stack.append(stack.pop()
ology stack.append(stack.append(stack.pop()
ology stack.append(
            )

    return stack.pop()