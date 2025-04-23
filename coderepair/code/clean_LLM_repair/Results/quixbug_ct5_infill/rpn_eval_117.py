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
        = op(Symbol, a,b)stack.pop()
TERNstack.pop()
TERN stack.append(+stack.pop()
TERN stack.append(( )Stack( stack) returnstack.pop()KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
            )

    return stack.pop()