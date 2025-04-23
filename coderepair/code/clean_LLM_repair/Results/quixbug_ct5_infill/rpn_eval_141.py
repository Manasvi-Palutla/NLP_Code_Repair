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
                token)op(a, b,.== '0''/':
Taxonomy a.set_node_type(0)stack.pop()
Taxonomy b.set_node_type(1):
Taxonomy a.set_node_type(1) # stack.append(a.set_node_type(0)).'/', '+', '-',else:
Taxonomy1' '
            )

    return stack.pop()