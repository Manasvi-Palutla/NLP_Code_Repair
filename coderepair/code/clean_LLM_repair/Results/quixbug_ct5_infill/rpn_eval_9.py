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
                token )

Vsile stack.append( astack.append(stack.append(b)

Vsile stack.append(stack.pop()
Vsile stack.append( a)
Vsile stack.append(None: # returnif len(stack)==0: #= op('+', a,. append (][ tokens] if:token= stack.pop
            )

    return stack.pop()