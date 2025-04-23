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
                a + b)

 taxonomy ==stack.pop()

SURFACE.update(op(symbol, a,a+ b)

Phrase, stack.pop()
Taxonomy)stack.pop()
Taxonomy.set_rpn_expression(tokens)return" +stack.pop()
Taxonomy.set_rpn_expression(tokens) return=stack.pop()
Taxonomy.set_r
            )

    return stack.pop()