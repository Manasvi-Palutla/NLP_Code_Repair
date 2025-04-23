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
                token) stack.append(:if isinstance(a, int):
 LayoutParams"["].join(stack):if isinstance(a, float):
returnstack.pop() #stack.append(+ 'stack.append( "stack.append( " + "+ "+ "+ "++"+"stack.append( "+ "+ "+ "+ "+ "+ "++"if a >=stack.pop()
 LayoutParams else+ "++"
            )

    return stack.pop()