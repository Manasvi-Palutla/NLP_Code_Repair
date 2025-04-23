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
                token ) stack.append(else:==stack.pop()

   stack.append(if isinstance(token, int):

stack.append(( a, b)stack.append(stack.pop()

   stack.append( b)
Vfs       (a,= stack.pop()
Vfs        stack.append( a.get(symbol))stack.pop
            )

    return stack.pop()