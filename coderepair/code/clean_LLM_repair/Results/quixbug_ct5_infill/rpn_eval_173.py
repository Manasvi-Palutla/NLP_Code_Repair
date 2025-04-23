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
        = op(Symbol, a,if isinstance(token,stack.append(== stack.pop()

   ==stack.pop()

TTstack.append(stack.append()

TT stack.append(= stack.pop()
TT stack.append(stack.append(= stack.pop()
TTstack.pop()
TT stack
            )

    return stack.pop()