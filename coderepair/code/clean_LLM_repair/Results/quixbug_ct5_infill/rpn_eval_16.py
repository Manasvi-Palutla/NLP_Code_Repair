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
                token) stack.append(op(symbol, a,= stack.pop()
        = stack.pop()
for token in tokens:ifisinstance(token, int):
= stack.pop()
Taxonomystack.append(token)else:
Taxonomy==):1.0/stack.pop()
Taxonomy = stack.pop()
Taxonomystack.append(token)
Taxonomy
            )

    return stack.pop()