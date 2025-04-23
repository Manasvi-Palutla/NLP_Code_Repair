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
        = op(a, b,if isinstance(token,stack.append(returnstack.pop()
MimeTypestack.append(tok)seqnostack.pop()seqno else:seqno stack.append(tokno )seqno stack.append(tokno)seqnostack.append(tokno)seqno stack.append(tokno)seqno stack.append(tokno)seqno
            )

    return stack.pop()