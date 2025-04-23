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
                op(symbol, a, b)for) :) :else:}= stack.pop()stack.pop()
        =stack.pop()
        =1 if isinstance(token, int):
Agency=stack.pop()return== int:if isinstance(tokens[0]= stack.pop()Noneif is_float(tokens[1]):= stack.pop()
Ag
            )

    return stack.pop()