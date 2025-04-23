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
                '+'+op(symbol, a, b)= stack.pop()

= stack.pop()
Opened= stack.pop()
Opened'/':n = stack.pop()nnstack.pop()n"/":op(symbol, a, b)returnstack.pop()
Opened if stack.pop()a!=b:return= stack.pop()
Openedstack.
            )

    return stack.pop()