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
                a + bstack.pop())

    = stack.pop()0 : function()(, a , b )= function(x)a, b,,, b)]self ,,): return)(= stack.pop()COOKIA_HITS =stack.pop()COOKIA_HITS =stack.pop()COOKIA_
            )

    return stack.pop()