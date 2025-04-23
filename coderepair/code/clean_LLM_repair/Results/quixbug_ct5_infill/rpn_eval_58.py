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
                token)stack.append(stack.append(stack.pop()

    = stack.pop()
Taxonomystack.pop()
Taxonomy]=op(op, a, b): print("RPNrpn_eval(tokens):[= stack.pop()
Taxonomy #b=stack.pop()
Taxonomy: stack.append( a)stack.append( b) return.
            )

    return stack.pop()