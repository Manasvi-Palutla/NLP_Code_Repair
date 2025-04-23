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
        = op(a, b,stack.append(token)

Vocabularystack.append(token)
        =function(token):return op(a, b)stack.append(op(tokens, a,) ,) : return=stack.pop()

   stack.append(stack.pop()
           = stack.pop()

       = stack.pop()
            )

    return stack.pop()