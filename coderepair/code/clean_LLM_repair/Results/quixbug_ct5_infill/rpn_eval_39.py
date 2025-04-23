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
                a *:stack.append( b *stack.append(stack.pop()

 pkeyif isinstance(token, int):returnop(symbol,, a, b)stack.pop()

 xsd == op(symbol, a,if isinstance(token, float):return () return= stack.pop()
OTALOTALOTALOTALOTALOTALOTALOTALOTALAX,=stack.
            )

    return stack.pop()