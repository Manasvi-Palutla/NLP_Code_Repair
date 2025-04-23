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
                token)

ClassType = op(token, a, b,if(a, b)stack.append( b)stack.pop()

ClassType= stack.pop()
TERMif isinstance(a,stack.append( a)if isinstance(a, float):( a)stack.append( b)else:


b):
        = stack.pop()
           
            )

    return stack.pop()