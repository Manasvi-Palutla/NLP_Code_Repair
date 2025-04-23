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
                a+b)

 taxonomy = op(token,a,b) stack.append(for token instack.pop()

= stack.pop()

stack.append(( a,stack.append( b)

       if isinstance(token, int):stack.append(= stack.pop()
           stack.append()stack.pop()
            stack.append(
            )

    return stack.pop()