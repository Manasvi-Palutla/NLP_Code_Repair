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
                op(token, a, b): returnif isinstance(token, str):
ology = stack.pop()stack.append(op(tok, a,(= stack.pop())
ologystack.append(tok)stack.pop()
ology = stack.pop()
ologystack.append(tok): returnstack.pop()
ologystack.append(tok)return tokens[token]
            )

    return stack.pop()