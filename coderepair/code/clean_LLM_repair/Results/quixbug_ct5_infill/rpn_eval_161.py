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
                op(symbol, a, b)= stack.pop()

 Podiaa , breturnNone else: #= stack.pop()
        stack.append(stack.pop()
        = stack.pop()
Appsstack.pop())Clusteria= stack.pop()
Apps stack.append( a== stack.pop()
Apps if) : if isinstance(token, float):
            )

    return stack.pop()