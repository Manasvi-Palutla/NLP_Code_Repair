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
        = op(a, b,if isinstance(stack.pop(), int):

stack.append(= stack.pop()

Taxonomystack.append( stack.pop())else:return=stack.pop()
SURFACE stack.append(: if isinstance(stack.pop(),'string'):=stack.pop()

 xsd = stack.pop()
Specimenstack
            )

    return stack.pop()