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
                token) stack.append(} return op(op, a,astack.pop()
Taxonomy,stack.pop()
Taxonomy,stack.pop()
Taxonomy) return= stack.pop() return Nonestack.pop()stack.pop()
Taxonomy= stack.pop()
Taxonomy stack.append(stack.pop()
Taxonomy"= stack.pop()
Taxonomy stack.append(stack
            )

    return stack.pop()