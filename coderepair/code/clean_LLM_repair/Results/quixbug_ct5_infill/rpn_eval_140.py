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
                token + b+ aop(tok, a, b)op(tok, a, b)stack.append(tok)if isinstance(tok, float):

= stack.pop()

op(tok,stack.pop()

 getTerminals()) :stack.append(tok)return} stack.append(tok)token):stack.pop()
ology elif isinstance(tok, float
            )

    return stack.pop()