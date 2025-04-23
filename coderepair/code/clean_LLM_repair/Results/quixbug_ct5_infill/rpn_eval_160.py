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
                op(token, a, b)if isinstance(tokens,stack.pop()else:
Datum=. pop())
Datum"/", "0.0":) return a ,stack.pop()stack.pop()
Taxonomystack.pop()
Taxonomy =stack.pop()
Taxonomy= stack.pop()
Taxonomy stack.append( "1."stack.append( "
            )

    return stack.pop()