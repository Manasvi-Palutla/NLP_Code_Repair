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
        = op(symbol, a,== stack.pop()
 EP= stack.pop()
       = stack.pop()
 EPstack.pop()
Ep = stack.pop()Cluster_Species stackstack.append(astack.pop()Cluster_Species stack.append(Cluster_Prophes )Nonestack.append(Cluster_Prophesreturn cluster_dict
            )

    return stack.pop()