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
                a( token,(= stack.pop()

if isinstance(token, int):
ology==stack.pop()
ology stack.append((= stack.pop()
ologystack.append( b)
ology,(stack.pop()
ology stack.append( a)
ologystack.append()stack.append(stack.append()
            )

    return stack.pop()