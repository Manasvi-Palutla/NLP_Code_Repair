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
                op(token, a, b)for token inif= stack.pop()
Episodestack.append(op(symbol, a, b)#if isinstance(token, int):
Taxonomy#else: #if isinstance(token, str):"-")"-")"_" )"_" )"_""_""_""_" )"_" )"_" )
            )

    return stack.pop()