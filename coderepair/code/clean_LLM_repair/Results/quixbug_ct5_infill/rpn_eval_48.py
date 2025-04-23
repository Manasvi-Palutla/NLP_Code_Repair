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
                op(symbol, a, b)= stack.pop()

ology returnif isinstance(tokens, int):
ology= stack.pop()
ology stack.append(stack.append(returnreturn stack.pop() else:stack.append(= stack.pop()
ology stack.append(if isinstance(tokens, list):if isinstance(tokens,isinstance(tokens,= stack.pop
            )

    return stack.pop()