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
                "%.4f" %if isinstance(a, float):
       isinstance(b, float):
       stack.append( "%.4f" %if isinstance(a, float):
ologystack.append( a)
ology stack.append( b). pop()stack.pop()
ology stack.append( "+ "+ "+ "+ "+ "++a)stack.append( "+ "+ "+ "+ "+
            )

    return stack.pop()