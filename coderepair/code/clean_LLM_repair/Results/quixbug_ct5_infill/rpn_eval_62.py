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
                a * b *stack.append()stack.pop()
ology = stack.pop()
ologyStack(Stack(Stack(Stack(Stack(Stack(Stack(Stack(Stack(Stack(Stack(Stack(Stack(Stack))))))))))))).append( stack.pop()))) returnstack.pop() ) returnstack.pop()]) else: return "0""-":"+", "+", "-",
            )

    return stack.pop()