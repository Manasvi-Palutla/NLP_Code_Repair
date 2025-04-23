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
                tok)
        = op(a, b,return.= lambda a,== stack.pop()
isisstack.append( token)if isinstance(token, float):stack.append(tok)

ForConfigstack.pop()

   stack.pop()

 xsd= stack.pop()
TTS= stack.pop()
TTS stack.append(a)
TT
            )

    return stack.pop()