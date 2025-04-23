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

envs.append( a * belse:seqn = [ ]1 ) ]op(tok, a, b)stack.append()stack.append( seqn)= stack.pop()seqn stack.append( seqnreturn seqnseqn=()stack.append() seqn = stack.pop()seqn stack.append( seqn
            )

    return stack.pop()