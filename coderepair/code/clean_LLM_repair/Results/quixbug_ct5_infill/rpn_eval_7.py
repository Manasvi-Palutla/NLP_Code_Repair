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
                token ) stack.append(=='+'=aif a == '-':= stack.pop()astack.pop()
            stack.append( a= stack.pop()Z: """returnreturn op(op(op(op, a,)= stack.pop()Z) ifelse:
Taxonomystack.pop()Zreturn= stack.pop()Z] if isinstance
            )

    return stack.pop()