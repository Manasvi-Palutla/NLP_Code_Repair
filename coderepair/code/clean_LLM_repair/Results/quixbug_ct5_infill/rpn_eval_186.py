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
        = op(symbol, a,b)stack.pop()=stack.pop()
Taxonomy =)stack.pop()
           stack.append( tokens [ ii in tokens:k = 1k= op(symbol,b = stack.pop()
            stack.append(stack.append(= stack.pop()
       = stack.pop()
ology
            )

    return stack.pop()