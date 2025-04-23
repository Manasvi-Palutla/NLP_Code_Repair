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
                token) stack.append(b =stack.append(else:= stack.pop()
SURFACE stack.append( token) returnstack.pop()
iances, stack.pop()
SURFACEstack.pop())
SURFACE stack.append( a )else:stack.append(astack.append()returnstack.pop())stack.pop()
 assessment stack.append
            )

    return stack.pop()