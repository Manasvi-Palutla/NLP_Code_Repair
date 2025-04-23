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
                op(a, b)for token in tokens:a + b: stack.append( token)stack.append( tokenstack.append(stack.pop()
        return.[ a) , a= stack.pop()stack.pop()

    stack.append( stack.pop()
           )()a, b)= stack.pop()

    stack.
            )

    return stack.pop()