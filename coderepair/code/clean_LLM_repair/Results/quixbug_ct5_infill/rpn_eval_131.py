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
        stack.append(- b):=stack.pop()
Ambient= stack.pop()
Assembly stack.append(stack.pop()
Assembly stack.append(stack.pop()KVCF= stack.pop()KVCF stack.append( KVCFstack.pop()KVCF stack.append( kVCF=b)KVCF stack.append( K
            )

    return stack.pop()