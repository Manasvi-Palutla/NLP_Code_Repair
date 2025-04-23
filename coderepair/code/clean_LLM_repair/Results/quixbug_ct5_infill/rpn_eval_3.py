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
                a * bstack.append( b)

envs =else:
Taxonomy =a:
Taxonomystack.append(a):
Taxonomystack.append(b)
Taxonomy return= stack.pop()
Taxonomy stack.append(a)seqnStack.append(seqnStack.pop())seqnStack.append(seqnStack.pop()seqnStack.pop()seqnStack.pop()seqnStack
            )

    return stack.pop()