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
        = op(a, b,'-')
       *stack.append(. pop()

stack.append( Tokenforif isinstance(tok, float):a = stack.pop()
stack.append(Token)=stack.pop()
TTF_tok = stack.pop()
TTF_tok return Token(tok)stack.append("'") return
            )

    return stack.pop()