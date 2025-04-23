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
                a + b +return. appendstack.append( stack.pop())
ology(. pop()stack.append( stack.pop()
ology ):= stack.pop()returnstack.pop()
ologystack.append(stack.pop()
ologystack.append( stack.pop()
ology)stack.pop()
ology stack.append( stack.pop()
ology
            )

    return stack.pop()