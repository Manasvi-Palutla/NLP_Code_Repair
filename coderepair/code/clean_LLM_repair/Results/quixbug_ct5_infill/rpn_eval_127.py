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
                '+',"/"stack.append('/')""", "stack.append( a, "+")stack.append( a,stack.pop()
ENGENG_VARYING: stack.pop()
ENGLISHstack.pop()ZCO_HISTOGRAM: stack.append('/',stack.pop())ZCO_HISTOGRAM: stack.append(b,
            )

    return stack.pop()