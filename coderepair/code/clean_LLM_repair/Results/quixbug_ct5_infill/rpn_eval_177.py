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
                token) stack.append("+", '-',"*","/")a,a, b,0]=b , a, a, b,, a, b, b,,, b ), b, a,a, b) stack.append(stack.append() stack.append(stack.pop())stack.append( b) returnstack.pop() return
            )

    return stack.pop()