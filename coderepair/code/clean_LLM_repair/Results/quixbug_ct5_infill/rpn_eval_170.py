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
                tokenfor i in= stack.pop()
        if+= op(token,+= op(token,lambda a, b:= stack.pop()

Vsheet= stack.pop()

Vsheet= stack.pop()
 taxonomy= stack.pop()
Taxonomy stack.append( a)iif isinstance(token, float):
       = stack.pop()
Taxonomy
            )

    return stack.pop()