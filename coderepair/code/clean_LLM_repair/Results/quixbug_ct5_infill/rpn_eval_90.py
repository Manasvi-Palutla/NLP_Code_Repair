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
                tok) stack.append(stack.append(tok)returnif isinstance(token,stack.pop())

CTYPE stack.append(tok))seqN=stack.pop()seqN return (TokenList(stack,)seqNstack)seqNstack)seqNstack =tokenList = [tok, ] returntokList,,)seqNstack=tokList,tokList,, token
            )

    return stack.pop()