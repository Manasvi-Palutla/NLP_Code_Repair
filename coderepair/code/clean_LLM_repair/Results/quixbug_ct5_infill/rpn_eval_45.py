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
                token )
        = op(token,a,b)#end= stack.pop()
Taxonomystack.append(stack.pop())
Taxonomystack.append( stack.pop()
Taxonomystack.pop()
Taxonomy stack.append( stack.pop() )stack.append(stack.pop()
Taxonomy return None= stack.pop()
Taxonomystack.pop()
Taxonomystack.pop()
            )

    return stack.pop()