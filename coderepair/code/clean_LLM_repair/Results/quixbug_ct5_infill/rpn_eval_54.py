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
                token +stack.pop()
CTYPE stack.append(stack.append(b)

CTYPEstack.pop()
CTYPE stack.append(stack.pop()
Taxonomy stack.append( stack.pop()
Taint stack.append(stack.append(stack.pop()
 taxonomy stack.append( stack.pop())stack.append( stack.pop()
Taxonomy stack.append( stack.pop()

            )

    return stack.pop()