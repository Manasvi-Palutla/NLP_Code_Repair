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
                token)tokn = op(a, b,stack.pop()
       None:
       = stack.pop()tokntokenn = stack.pop()tokn == stack.pop()tokn= stack.pop()tokn,stack.pop()tokn= stack.pop()tokn returntokn[tokn][tokn]if) :stack.append(tokn
            )

    return stack.pop()