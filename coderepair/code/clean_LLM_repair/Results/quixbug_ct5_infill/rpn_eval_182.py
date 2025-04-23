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

        = op(token, a,b)(a,b)()stack.pop()
OTALOTALOTALOTALstack.pop()
OTALOTALStack(stack.pop()
OTALOTAL_SURFACE stack.append( stack.pop()
OTALOTAL_SURFACEstack.pop()returnstack.pop()ZKS_TO_RPN_COMPLEX_LIST stack.pop()Z
            )

    return stack.pop()