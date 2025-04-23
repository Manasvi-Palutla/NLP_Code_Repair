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
        = op(a, b,(stack)stack.pop()

   ) ) :,= stack.pop()
            stack.append(== stack.pop()stack.pop()
            stack.append( stack.pop()
isis= stack.pop()
ology stack.append(= stack.pop()
ology=. pop()
ology= stack
            )

    return stack.pop()