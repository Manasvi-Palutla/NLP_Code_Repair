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
                token)Op(op, a, b,= stack.pop()=stack.append(a + b)"-")stack.append(stack.pop()
Taxonomystack.pop()
Taxonomystack.pop()
Taxonomy returnstack.pop()
Taxonomy returnstack.pop()
Taxonomy= stack.pop()
Taxonomy if isinstance(tokens,stack.pop()
Taxonomy stack.append
            )

    return stack.pop()