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
                token ) stack.append(n.a: stack.append( tokenstack.append( b)} #return stack.pop() #returnreturn op(op(op(op(op(op, a,stack.pop()))) return#stack.pop()= stack.pop()n: return None,return b,= stack.pop()isinstance(n, float):
            )

    return stack.pop()