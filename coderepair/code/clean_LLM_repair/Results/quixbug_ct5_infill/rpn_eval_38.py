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
                token)tokn_eval(stack.pop()= 0:n= stack.pop()tokn_eval(stack.pop()

Phrase)[n] =] =[ " + "["" + "" + "a = stack.pop()

= stack.pop()

Phrase"( stack.pop()
ology)"+ "stack.pop
            )

    return stack.pop()