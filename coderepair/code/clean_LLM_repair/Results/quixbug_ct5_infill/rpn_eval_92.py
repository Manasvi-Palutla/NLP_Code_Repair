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
                tok)
        = op(token, a,b,stack.append(tok)stack.append(tok)if isinstance(tok, int):

else:

Taxonomyelse:. pop(),stack.pop()

Taxonomystack.pop()
Taxonomy else:op(tok, a,= stack.pop()
Taxonomy stack.append(tok)
Taxonomy= stack.pop()

            )

    return stack.pop()