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
                op(symbol, a, b)if isinstance(tokens,= stack.pop()

    =stack.append(stack.append( op(symbol, a,)+ stack.pop()

stack.append(stack.append( token)

SURFACE stack.append( stack.pop()

SURFACE stack.append(stack.pop())
ologystack.append( tokens[
            )

    return stack.pop()