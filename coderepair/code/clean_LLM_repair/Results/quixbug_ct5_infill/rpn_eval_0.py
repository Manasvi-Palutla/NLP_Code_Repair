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
                op(symbol, a, b )) returnstack.pop()] functionstack.pop():function rpn_eval(tokens):if isinstance(tokens,) :a ina >= b: a/ b) if isinstance(tokens,:'+' in tokens andisinstance(tokens,:" "if isinstance(tokens,= stack.pop()
ology = stack.pop()
ology
            )

    return stack.pop()