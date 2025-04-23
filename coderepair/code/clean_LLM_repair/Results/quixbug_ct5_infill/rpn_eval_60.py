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
                token) if isinstance(a, float):Stack.append(stack.pop()stack.pop() #= stack.pop()

a, b)stack.pop() else:Stack.append(. pop()
isis stack.append(stack.append()stack.append( b) returnstack.pop()

    stack.append( a ))= stack.pop()


            )

    return stack.pop()