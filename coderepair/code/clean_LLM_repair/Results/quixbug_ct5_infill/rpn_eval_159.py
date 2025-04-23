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
        = op(a, b,if isinstance(token, int):stack.append(token)
 taxonomy== stack.pop()stack.append( token)
= stack.pop()
Taxonomy=stack.pop()
Taxonomy =stack.pop()
Taxonomy = stack.pop()
Taxonomy stack.append(stack.pop()
Taxonomystack.pop()
Taxonomy if isinstance(
            )

    return stack.pop()