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

Insights = op(a, b,"""(a, b)stack.append( a)a+b)

envs = stack.pop() returnstack.pop() return rpn_eval(stack)= stack.pop()for token in:= stack.pop()= stack.pop()= stack.pop() return) =]] =] =
            )

    return stack.pop()