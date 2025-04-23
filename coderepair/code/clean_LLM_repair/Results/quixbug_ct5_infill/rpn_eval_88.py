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
                op(a, b)#stack.append( b)return'',= stack.pop()
OTALOTALOTALOTALa , b]= stack.pop()
OTALOTALOTAL= stack.pop()
OTALOTALAX stack.append( a).pop()
OTALAX stack.append( b),stack.append(returna) return)stack.pop()
OTAL
            )

    return stack.pop()