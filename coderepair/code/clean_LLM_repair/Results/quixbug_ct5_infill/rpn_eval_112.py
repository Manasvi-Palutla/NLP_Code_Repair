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
                token )

        = op(symbol,a,b)= stack.pop()seqn_eval()seqn_eval(tokens)seqn_eval(tokens)seqn_eval(tokens)seqn_eval(tokens)seqn_eval(tokens)seqn_eval(tokens)seqn_eval(tokens)return seqn_eval(tokens)seqn_eval(tokens)seqn_eval(tokens)seq
            )

    return stack.pop()