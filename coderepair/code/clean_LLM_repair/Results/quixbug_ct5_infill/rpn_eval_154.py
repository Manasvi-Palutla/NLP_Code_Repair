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
                (float(a) + b)returnreturn None= stack.pop()
 LayoutParams =. pop() , 'A/C/N/R'stack.append(stack.append( (float(a),stack.pop() )stack.append( (float(a)),stack.append(stack.pop()stack.append( (int(a), 'A'))= stack.pop
            )

    return stack.pop()