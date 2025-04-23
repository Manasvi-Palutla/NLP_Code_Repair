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
                a +"', ' ',ab'', ' ', '',stack.pop()%10, '', ' ''','', ' '' '= stack.pop()%10,'', '' ', ' ', ''-', ''', ' ', ' '+', ' ''/'):'-', ''*','.', ''
            )

    return stack.pop()