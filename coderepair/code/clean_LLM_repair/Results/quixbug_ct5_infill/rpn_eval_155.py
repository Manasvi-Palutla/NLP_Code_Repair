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

    = op(a, b,) #if isinstance(token,stack.append(token) #else: #== stack.pop()
NP= stack.pop()] #stack.append(token) returnelse: #= stack.pop()
NP= stack.pop()
NPstack.append(token)stack.pop()
NP). append (
            )

    return stack.pop()