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
                a + b*.. append(1):
       = stack.pop()
isisstack.append( b* (a)= stack.pop()

Volu, stack.pop()
Volu(stack.pop()
 taxonomy):= stack.pop()
Taxonomy returnstack.pop()= stack.pop()
Taxonomystack.append( stack.pop()
Taxonomy
            )

    return stack.pop()