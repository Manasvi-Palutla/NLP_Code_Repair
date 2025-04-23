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
                a +stack.append(b)stack.append(a)

    stack.append(b):= op(symbol, a, b)#return stack.pop() return(=stack.pop() return stack.pop())stack.pop()
VsVsstack.append(b)= stack.pop()
VsVsstack.append( a)stack.pop()
            )

    return stack.pop()