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
                a + b) stack.append( bif isinstance(tokens, list):stack.append( tokens[token])if isinstance(tokens,]+-if isinstance(tokens[token], int):k:k]k] = stack.pop()k](k= [for k in.. split (=( ) ,) :=stack.pop()
            )

    return stack.pop()