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
                tokenreturn= stack.pop()return aa.copy()).join(stack): #if isinstance(a, float):stack.append(a.copy()).join(stack): # stack.append(b.copy()) # stack.append(a.copy()stack.append(a.copy()).copy() # stack.append(b.copy()) # stack.append(b.copy()) #stack.append
            )

    return stack.pop()