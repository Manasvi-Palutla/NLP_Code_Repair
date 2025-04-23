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
                op(Symbol, a, b)for token in[a, b]b]stack.append(( stack.pop())stack.append(op(Symbol, a,None:None=, b =stack.pop()=stack.pop()
ology =stack.append(Op(Symbol, a, b,if isinstance(token, float):= stack.pop()

            )

    return stack.pop()