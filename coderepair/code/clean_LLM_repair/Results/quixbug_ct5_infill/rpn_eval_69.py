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
                token ) stack.append(isinstance(token,= stack.pop()
VfsFile= stack.pop()
VfsFilestack.append( b)= stack.pop()
VfsFile stack.append(.append( Token_eval(tokens)= stack.pop()stack.append( Token_eval(tokens))for tokenstoken., 'rpn' ))stack.pop
            )

    return stack.pop()