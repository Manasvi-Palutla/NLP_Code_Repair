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
                a *= stack.pop()Stack: stack.append(stack.pop()
envsstack.append(stack.append( b *)stack.append( b= stack.pop()
envsstack.pop()
envs stack.append(stack.pop())stack.pop()
envs stack.append(stack.pop()
envsstack.pop()
envs stack.append()
            )

    return stack.pop()