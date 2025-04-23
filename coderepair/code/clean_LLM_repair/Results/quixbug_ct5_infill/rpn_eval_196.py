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
                a * b*stack.append(stack.pop())
        =stack.pop()

 penaltystack.append(.pop())stack.append(b)

SURFACE stack.append().= stack.pop()
SURFACE stack.append()


 penaltystack.pop()
 LayoutParams stack.append(isinstance(tok, int):
        ==
            )

    return stack.pop()