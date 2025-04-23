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
                a + b) stack.append( bastack.pop()
           stack.append( a -stack.pop()

   stack.pop()
envs stack.append( stack.pop()
envs stack.append( stack.pop()] def op(symbol,+ b,stack.pop()
envs'+'+'):'-'):]- b ):):)
            )

    return stack.pop()