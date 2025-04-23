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
                a * b /stack.pop()

CTYPEstack.append(stack.pop()

SURFACE stack.append( stack.pop())stack.pop()
NP= stack.pop()
NPstack.append())[= stack.pop())stack.pop()
NPstack.pop()]) return stack.pop()
NP[]( )
            )

    return stack.pop()