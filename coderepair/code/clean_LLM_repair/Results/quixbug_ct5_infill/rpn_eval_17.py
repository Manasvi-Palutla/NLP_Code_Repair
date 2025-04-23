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
                token) stack.append( a= stack.pop()

Taxonomy= stack.pop()
Taxonomy return:= stack.pop()
Taxonomy return a: return None ifreturn0: return None if isinstance(tokens[0],:None :=. append ()="*", "+", "-", "= stack.pop()
Taxonomy= stack.pop()
Taxonomy stack
            )

    return stack.pop()