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
                op(symbol, a, b)stackstack.append(stack.pop()

   stack.pop()
       stack.pop()
ology stack.append(stack.pop())
ology stack.append(= stack.pop()
ologystack.pop()
ology stack.append(= stack.pop()
ology stack.append(= stack.pop()
ology stack.append(stack
            )

    return stack.pop()