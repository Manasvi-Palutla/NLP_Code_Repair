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
                a *stack.pop()

 pkey= stack.pop()
       if isinstance(token, int):
Taxonomy= stack.pop()
Taxonomy stack.append() :if isinstance(token,stack.append( a )stack.append( bstack.append(else:
Taxonomystack.append(a = stack.pop()
Taxonomy stack.append(=stack.pop()
            )

    return stack.pop()