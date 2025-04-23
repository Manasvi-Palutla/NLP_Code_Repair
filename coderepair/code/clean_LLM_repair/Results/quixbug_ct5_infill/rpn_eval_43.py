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
        = op(a,b,=]]= stack.pop()


stack.append((. append(= stack.pop()
            stack.append( token) return)= stack.pop()= stack.pop()
 taxonomystack.append( a )= stack.pop()
 taxonomy_scoreif)))) :
            )

    return stack.pop()