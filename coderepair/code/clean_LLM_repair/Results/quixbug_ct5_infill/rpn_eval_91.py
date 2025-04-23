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
                a + b)
        =op(symbol,a,bstack.append( b)

ology= stack.pop()
ology =stack.pop()
ology+ b)
ology stack.append(stack.pop())
ology stack.append(stack.append())
ology= stack.pop()
ologystack.append(b)= stack.pop()
ologystack
            )

    return stack.pop()