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
                tok.upper()+token).replace(a,b) stack.append( tok.lower()+token.upper()+token.lower()+token.upper()+token.upper()+token.lower()+token.upper()+token.lower()+token.upper()+token.upper()+token.to_s()+"+"+"+"+"+stack.pop()+"+"+stack.pop()a = stack.pop()
            )

    return stack.pop()