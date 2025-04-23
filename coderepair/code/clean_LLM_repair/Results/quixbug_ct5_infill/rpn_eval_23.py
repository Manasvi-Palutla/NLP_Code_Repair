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
                a + b) stack.append( belse:returnreturn= stack.pop()return stack.pop()

   a, b=stack.pop()

 taxonomy =stack.pop()
 taxonomy = stack.pop()stack.append( z. pop()]= z.pop()z.pop()) #.a = stack.pop()
stack.append( z.pop()
            )

    return stack.pop()