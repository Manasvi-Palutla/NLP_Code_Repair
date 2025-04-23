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
                op(symbol, a, b)return= stack.pop()

    = stack.pop()None= stack.pop()

ology= stack.pop()
ology stack.append( b:= stack.pop()
ology stack.append(if isinstance(token, float):
ology stack.append(( token)
ology:
ology stack.append( a)
ology=
            )

    return stack.pop()