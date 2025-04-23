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
                token) stack.append(stack.pop()
           : stack.append(if isinstance(token,stack.append( stack.pop()
            )stack.pop()

envsstack.pop()ClusterDict.get(str, stack) stack.append(. pop() )stack.append() ] def rpn_eval(tokens):return op(op(symbol,(tok) return
            )

    return stack.pop()