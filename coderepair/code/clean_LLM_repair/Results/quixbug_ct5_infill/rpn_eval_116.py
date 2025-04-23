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
                (a+b)/(2-len(tokens))) stack.append(lambda token,.stack.append( (a*tok,tok,: returnreturn len(tokens)): returnstack.pop()
Auxiliaryreturnstack.pop())stack.pop()
Auxiliary function=( token)if isinstance(tok, int):return len(tok) ifreturnstack.pop
            )

    return stack.pop()