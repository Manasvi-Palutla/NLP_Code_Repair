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
                a * b ** bstack.append( bstack.pop()
Taxonomystack.pop()
Taxonomy return= stack.pop()
Taxonomy= stack.pop()
Taxonomystack.pop())
Taxonomystack.pop()returnstack.pop()()] stack.append( stack.pop()) returnstack.pop()
Taxonomy return.pop()stack.pop()
Taxonomy stack.pop()

            )

    return stack.pop()