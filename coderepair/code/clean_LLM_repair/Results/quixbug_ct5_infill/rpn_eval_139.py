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
                op(symbol, a, b)stack.append(( a, b,stack.append(= stack.pop()

 PodTreestack.append()returnstack.pop()
        stack.append(()

VsVs else:
        =0:
        =.= 0,
       ,= 0,= 0, #0:1,
            )

    return stack.pop()