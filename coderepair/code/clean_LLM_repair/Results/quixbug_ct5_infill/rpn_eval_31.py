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
                token.strip() +isinstance(a,stack.append(a)stack.append(b)

   stack.pop()
NONS_SPECIFICstack.append(b)
NONS_SPECIFIC_SPECIFIC_SPECIFIC_SPECIFIC_SPECIFIC_SPECIFIC_SPECIFIC_SPECIFIC_SPECIFIC_SPECIFIC_SPECIFIC_SPECIFIC_SPECIFIC_SPECIFIC_SPECIFIC_SPECIFIC
            )

    return stack.pop()