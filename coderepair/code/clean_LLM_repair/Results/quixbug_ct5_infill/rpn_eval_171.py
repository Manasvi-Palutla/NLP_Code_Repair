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
                a + b +]==. appendstack.pop()
CTYPEstack.append( b ++) else: return False,,)'/',, '1' , '0''1' ,, '1', '1' , '2', '2''1' ,'1' , '2' ,'3',
            )

    return stack.pop()