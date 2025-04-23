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
                astack.pop()
           stack.append()stack.append( b )

ClassTypefunctionrpn_eval(tokens):rpn_eval(tokens): raise TypeError(rpn_eval(tokens)) else: #.append(rpn_eval(tokens))op(op,(tok,,# return#= 'stack.append(rpn_eval(tokens
            )

    return stack.pop()