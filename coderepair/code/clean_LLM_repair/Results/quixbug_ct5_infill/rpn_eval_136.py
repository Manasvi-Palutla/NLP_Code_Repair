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
                token +stack.pop()(stack.pop()

    stack.append( astack.pop()
            stack.append( bif isinstance(a,= stack.pop()
            stack.append(Stack()= stack.pop()

VsVsVsStack.pop()= stack.pop()KNP=stack.pop()KNP=stack.pop()KNP=stack.pop()
            )

    return stack.pop()