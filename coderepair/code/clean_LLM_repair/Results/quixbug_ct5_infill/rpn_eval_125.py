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
                token +a, b) return0,stackstack.append( a)stack.pop()
 copyOflen(tokens):i,a,b):
ology,a,b,i,k,o,l,r,u,l,r,u,t,l,l,l,l,l,r,l,l,l,l,l,l,m,s,h,m
            )

    return stack.pop()