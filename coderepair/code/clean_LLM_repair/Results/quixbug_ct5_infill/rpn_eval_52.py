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
                '-' *if isinstance(stack.pop(),'float'):= stack.pop()
Apps if isinstance(stack.pop(),'float'):stack.append('/')
Apps stack.append(stack.append(stack.pop()
Apps stack.append(stack.pop()
Apps stack.append(stack.pop()
envsstack.append( stack.pop()
Appsstack.
            )

    return stack.pop()