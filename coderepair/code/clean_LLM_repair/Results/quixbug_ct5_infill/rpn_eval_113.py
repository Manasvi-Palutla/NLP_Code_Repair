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
                tokenfor token in= stack.pop()
 xsd= stack.pop()
 xsdstack.append('+':lambda a, b:a*b+a*(a-b)= stack.pop()
 xsd stack.append()stack.append(= stack.pop()
 xsd stack.append(stack.append( a )stack.pop()
 xsd stack.append()
            )

    return stack.pop()