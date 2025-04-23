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
                token) stack.append(stack.pop()

 LangDomainstack.append("["else] for token in stack:returnb = stack.pop()
ologystack.append() :) else:return),"+"]b")"] stack.append( b)else:return "+", "+", "+", "+",","+","-","
            )

    return stack.pop()