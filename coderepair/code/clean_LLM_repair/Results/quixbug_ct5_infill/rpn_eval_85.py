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

Apps = op(a,b) stack.append(=():
Images = stack.pop()
Images.pop()[:-1]=stack.pop()] if len(tokens) >: k =[]= [ ]token in kstack.extend( [ kk ] )[ k=]( k , k ,] =
            )

    return stack.pop()