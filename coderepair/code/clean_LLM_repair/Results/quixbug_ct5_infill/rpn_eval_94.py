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

ology stack.append(for token in tokens:stack.append(=stack.pop()
            stack.append(stack.append() else:seqn)#seqn== stack.pop() seqn == stack.pop()seqnstack.append(stack.append()):( stack. pop (),
            )

    return stack.pop()