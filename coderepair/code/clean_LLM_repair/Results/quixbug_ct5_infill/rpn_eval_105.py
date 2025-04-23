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
                token ) stack.append(= stack.pop()
 taxonomystack.append(if isinstance(a, float):
stack.append()= stack.pop()
ology stack.append(stack.append( b)if isinstance(b,stack.append( b)= stack.pop()
Taxonomystack.pop()
Taxonomy stack.append()
Taxonomy stack.append()
            )

    return stack.pop()