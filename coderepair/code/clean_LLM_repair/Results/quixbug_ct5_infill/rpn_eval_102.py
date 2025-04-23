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
                op(token, a, b)"+", "+",stack.pop()

   if isinstance(a, float):Clusterstack.append( a)Clusterstack.append("-", "-", "+", "-", "+", "+",stack.append(b)Clusterelse:Clusterstack.append(token)Cluster= stack.pop()Clusterstack.pop()Cluster if isinstance(token,
            )

    return stack.pop()